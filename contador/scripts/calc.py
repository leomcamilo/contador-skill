#!/usr/bin/env python3
"""Calculadora do contador: IRPF, Simples, Presumido e comparação de regimes.

Todos os números legais vêm de parametros.json (mesma pasta). Cada bloco de lá
tem fonte e data de conferência; o script avisa quando o ano dos parâmetros
não é o ano corrente, porque tabela vencida dá conselho errado.

Uso:
  calc.py irpf-mensal --renda 12000 [--inss 0] [--dependentes 0] [--pensao 0]
  calc.py irpf-anual --tributaveis 180000 [--inss 0] [--dependentes 0]
                     [--saude 0] [--educacao 0] [--pgbl 0] [--pensao 0]
                     [--livro-caixa 0] [--retido 0]
  calc.py simples --rbt12 600000 --receita-mes 50000 --anexo III
                  [--exportacao 0]
  calc.py regimes --faturamento 30000 [--iss 0.05] [--exportacao-pct 0]
                  [--despesas 0] [--dependentes 0] [--tem-mei-atividade]
                  [--outras-rendas-anuais 0] [--ano 2026|2027]
  calc.py ganho-capital --venda 900000 --custo 400000
  calc.py irpfm --renda-total 900000 [--ir-pago 0]

Valores em reais. Alíquotas em fração (0.02 = 2%).
"""
import argparse
import datetime
import json
import math
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
P = json.loads((AQUI / "parametros.json").read_text())


def aviso_vigencia():
    ano = datetime.date.today().year
    if P["ano_vigencia"] != ano:
        print(f"ATENÇÃO: parametros.json é de {P['ano_vigencia']} e hoje é {ano}. "
              "Confira as tabelas antes de usar o resultado.\n", file=sys.stderr)


def brl(v):
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def pct(v):
    return f"{v * 100:.2f}%".replace(".", ",")


# ---------------------------------------------------------------- IRPF

def tabela(base, faixas):
    """Aplica tabela progressiva [{ate, aliquota, deduzir}] e devolve o imposto."""
    for f in faixas:
        if f["ate"] is None or base <= f["ate"]:
            return max(0.0, base * f["aliquota"] - f["deduzir"])
    return 0.0


def redutor(renda_bruta, r):
    """Redução da Lei 15.270/2025, calculada sobre o rendimento tributável bruto.

    Até o limite a redução tem teto (R$ 312,89/mês, R$ 2.694,15/ano): zera o
    imposto de quem usa o desconto simplificado, mas não o de quem usa a
    declaração completa com poucas deduções.
    """
    if renda_bruta <= r["limite"]:
        return r["maximo"]
    if renda_bruta <= r["transicao_ate"]:
        return max(0.0, r["constante"] - r["coeficiente"] * renda_bruta)
    return 0.0


def irpf_mensal(renda, inss=0.0, dependentes=0, pensao=0.0):
    m = P["irpf"]["mensal"]
    legais = inss + dependentes * m["dependente"] + pensao
    deducao = max(legais, m["desconto_simplificado"])
    base = max(0.0, renda - deducao)
    bruto = tabela(base, m["faixas"])
    red = redutor(renda, P["irpf"]["redutor_mensal"])
    return {"base": base, "deducao": deducao,
            "deducao_tipo": "simplificado" if deducao > legais else "legais",
            "imposto_tabela": bruto, "imposto": max(0.0, bruto - red)}


def irpf_anual(tributaveis, inss=0.0, dependentes=0, saude=0.0, educacao=0.0,
               pgbl=0.0, pensao=0.0, livro_caixa=0.0, retido=0.0, n_educ=None):
    a = P["irpf"]["anual"]
    n_educ = dependentes + 1 if n_educ is None else n_educ
    pgbl_ok = min(pgbl, a["pgbl_limite"] * tributaveis)
    educ_ok = min(educacao, a["educacao_por_pessoa"] * n_educ)
    completas = (inss + dependentes * a["dependente"] + saude + educ_ok
                 + pgbl_ok + pensao + livro_caixa)
    simpl = min(a["simplificado_pct"] * tributaveis, a["simplificado_teto"])
    red = redutor(tributaveis, P["irpf"]["redutor_anual"])
    res = {}
    for nome, ded in (("completa", completas), ("simplificada", simpl)):
        base = max(0.0, tributaveis - ded)
        imposto = max(0.0, tabela(base, a["faixas"]) - red)
        res[nome] = {"deducoes": ded, "base": base, "imposto": imposto,
                     "a_pagar_ou_restituir": imposto - retido}
    res["melhor"] = min(("completa", "simplificada"), key=lambda k: res[k]["imposto"])
    res["pgbl_considerado"] = pgbl_ok
    res["pgbl_espaco_restante"] = max(0.0, a["pgbl_limite"] * tributaveis - pgbl)
    return res


def inss_socio(prolabore):
    i = P["inss"]
    return min(prolabore, i["teto"]) * i["socio_contribuinte_individual"]


# ---------------------------------------------------------------- Simples

def simples(rbt12, receita_mes, anexo, exportacao=0.0):
    """DAS do mês. Receita de exportação de serviço tira ISS, PIS e Cofins da partilha."""
    s = P["simples"]
    if rbt12 > s["teto"]:
        raise ValueError("RBT12 acima do teto do Simples")
    faixas = s["anexos"][anexo]
    rbt = max(rbt12, 0.01)
    for i, f in enumerate(faixas):
        if f["ate"] is None or rbt <= f["ate"]:
            break
    ef = (rbt * f["aliquota"] - f["deduzir"]) / rbt
    partilha = s["partilha"][anexo][i]
    tira = sum(partilha.get(k, 0.0) for k in ("ISS", "PIS", "COFINS"))
    ef_exp = ef * (1 - tira)
    interna = receita_mes - exportacao
    das = interna * ef + exportacao * ef_exp
    return {"faixa": i + 1, "aliquota_efetiva": ef, "aliquota_exportacao": ef_exp,
            "das": das, "iss_no_das": interna * ef * partilha.get("ISS", 0.0),
            "cpp_fora_do_das": anexo == "IV"}


# ---------------------------------------------------------------- Presumido

def presumido(receita_mes, iss, exportacao=0.0, ano=2026):
    p = P["presumido"]
    anual = receita_mes * 12
    pres = p["presuncao_servicos"]
    excesso = max(0.0, anual - p["lc224_limite_anual"])
    base_anual = pres * (anual - excesso) + pres * (1 + p["lc224_acrescimo"]) * excesso
    base = base_anual / 12
    # Lei 9.250 art. 40: presunção de 16% só no IRPJ para prestadora com receita
    # anual até R$ 120 mil, exceto profissão regulamentada (TI não é).
    pres_irpj = p["presuncao_irpj_pequeno"] if anual <= p["pequeno_limite_anual"] else None
    base_irpj = receita_mes * pres_irpj if pres_irpj else base
    irpj = base_irpj * p["irpj"] + max(0.0, base_irpj - p["adicional_limite_mensal"]) * p["irpj_adicional"]
    csll = base * p["csll_aliquota"]
    interna = receita_mes - exportacao
    if ano >= 2027:  # CBS/IBS no lugar de PIS/Cofins; exportação é imune
        r = P["reforma_2027"]
        pis, cofins = 0.0, interna * (r["cbs"] + r["ibs"])
    else:
        pis = interna * p["pis"]
        cofins = interna * p["cofins"]
    iss_v = interna * iss
    return {"irpj": irpj, "csll": csll, "pis": pis, "cofins": cofins, "iss": iss_v,
            "total": irpj + csll + pis + cofins + iss_v}


# ---------------------------------------------------------------- dividendos

def ir_dividendos_mes(distribuido_mes):
    d = P["dividendos"]
    if distribuido_mes <= d["isento_ate_mes_por_fonte"]:
        return 0.0
    return distribuido_mes * d["irrf_aliquota"]  # incide sobre o total do mês


# ---------------------------------------------------------------- cenários

def retirada(fat, imposto_empresa, prolabore, despesas, dependentes, cpp_patronal,
             outras_rendas_anuais=0.0):
    """Custo total de tirar o dinheiro da empresa, por mês.

    Os 10% retidos sobre dividendos acima de R$ 50 mil/mês são antecipação: o
    custo definitivo é o IRPFM anual (que abate o IR já pago no pró-labore).
    A retenção aparece à parte como efeito de caixa. O redutor de 34% do
    art. 16-B não entra (quase nunca se aplica a PJ de serviço pequena).
    """
    inss = inss_socio(prolabore)
    ir_pl = irpf_mensal(prolabore, inss=inss, dependentes=dependentes)["imposto"]
    cpp = prolabore * P["inss"]["patronal"] if cpp_patronal else 0.0
    lucro = max(0.0, fat - imposto_empresa - prolabore - cpp - despesas)
    retido = ir_dividendos_mes(lucro)
    renda_anual = 12 * (prolabore + lucro) + outras_rendas_anuais
    minimo = irpfm(renda_anual)["minimo"]
    irpfm_mes = max(0.0, minimo - 12 * ir_pl) / 12
    total = imposto_empresa + inss + ir_pl + cpp + irpfm_mes
    return {"imposto_empresa": imposto_empresa, "prolabore": prolabore,
            "inss_socio": inss, "irpf_prolabore": ir_pl, "cpp_patronal": cpp,
            "lucro_distribuido": lucro, "ir_dividendos": irpfm_mes,
            "irrf_div_retido_mes": retido,
            "total": total, "carga": total / fat if fat else 0.0,
            "no_bolso": fat - despesas - total}


def cenarios(fat, iss, exp_pct, despesas, dependentes, mei_atividade, outras=0.0, ano=2026):
    exp = fat * exp_pct
    rbt12 = fat * 12
    sm = P["salario_minimo"]
    out = []

    mei = P["mei"]
    if mei_atividade and rbt12 <= mei["teto_anual"]:
        out.append(("MEI", retirada(fat, mei["das_servicos"], 0.0, despesas, dependentes, False, outras),
                    "só se a atividade constar da lista do MEI"))

    if rbt12 <= P["simples"]["teto"]:
        pl_r = max(sm, math.ceil(fat * P["simples"]["fator_r_minimo"]))
        das3 = simples(rbt12, fat, "III", exp)["das"]
        out.append(("Simples III (Fator R)", retirada(fat, das3, pl_r, despesas, dependentes, False, outras),
                    f"pró-labore de {brl(pl_r)} = 28% do faturamento"))
        das5 = simples(rbt12, fat, "V", exp)["das"]
        out.append(("Simples V (pró-labore mínimo)", retirada(fat, das5, sm, despesas, dependentes, False, outras),
                    "pró-labore de 1 salário mínimo"))

    pres = presumido(fat, iss, exp, ano)["total"]
    out.append(("Lucro Presumido", retirada(fat, pres, sm, despesas, dependentes, True, outras),
                "pró-labore de 1 salário mínimo, lucro distribuído com escrituração contábil"))

    # autônomo pessoa física prestando para PJ: INSS 11% retido e IR pela tabela
    inss_aut = inss_socio(fat)
    base_aut = fat - despesas  # livro-caixa
    ir_aut = irpf_mensal(base_aut, inss=inss_aut, dependentes=dependentes)["imposto"]
    tot = inss_aut + ir_aut
    out.append(("Autônomo PF (carnê-leão/IRRF)",
                {"imposto_empresa": 0.0, "prolabore": 0.0, "inss_socio": inss_aut,
                 "irpf_prolabore": ir_aut, "cpp_patronal": 0.0, "lucro_distribuido": 0.0,
                 "ir_dividendos": 0.0, "irrf_div_retido_mes": 0.0, "total": tot, "carga": tot / fat if fat else 0.0,
                 "no_bolso": fat - despesas - tot},
                "cliente PJ ainda paga 20% de INSS patronal por fora"))
    return out


# ---------------------------------------------------------------- outros

def ganho_capital(venda, custo):
    g = max(0.0, venda - custo)
    imposto, resto, piso = 0.0, g, 0.0
    for f in P["ganho_capital"]["faixas"]:
        teto = f["ate"] if f["ate"] is not None else math.inf
        fatia = min(resto, teto - piso)
        if fatia <= 0:
            break
        imposto += fatia * f["aliquota"]
        resto -= fatia
        piso = teto
    return {"ganho": g, "imposto": imposto}


def irpfm(renda_total, ir_pago=0.0):
    m = P["irpfm"]
    if renda_total <= m["inicio"]:
        return {"aliquota": 0.0, "minimo": 0.0, "devido": 0.0}
    aliq = min(m["aliquota_max"], (renda_total / m["inicio"] - 1) * m["aliquota_max"]
               * m["inicio"] / (m["teto"] - m["inicio"]))
    minimo = renda_total * aliq
    return {"aliquota": aliq, "minimo": minimo, "devido": max(0.0, minimo - ir_pago)}


# ---------------------------------------------------------------- CLI

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("irpf-mensal")
    s.add_argument("--renda", type=float, required=True)
    s.add_argument("--inss", type=float, default=0)
    s.add_argument("--dependentes", type=int, default=0)
    s.add_argument("--pensao", type=float, default=0)

    s = sub.add_parser("irpf-anual")
    s.add_argument("--tributaveis", type=float, required=True)
    for k in ("inss", "saude", "educacao", "pgbl", "pensao", "livro-caixa", "retido"):
        s.add_argument(f"--{k}", type=float, default=0)
    s.add_argument("--dependentes", type=int, default=0)

    s = sub.add_parser("simples")
    s.add_argument("--rbt12", type=float, required=True)
    s.add_argument("--receita-mes", type=float, required=True)
    s.add_argument("--anexo", choices=["III", "IV", "V"], required=True)
    s.add_argument("--exportacao", type=float, default=0)

    s = sub.add_parser("regimes")
    s.add_argument("--faturamento", type=float, required=True, help="faturamento mensal")
    s.add_argument("--iss", type=float, default=P["rio"]["iss_padrao_ti"])
    s.add_argument("--exportacao-pct", type=float, default=0)
    s.add_argument("--despesas", type=float, default=0, help="despesas mensais da empresa")
    s.add_argument("--dependentes", type=int, default=0)
    s.add_argument("--tem-mei-atividade", action="store_true")
    s.add_argument("--ano", type=int, default=2026, choices=[2026, 2027],
                   help="2027 troca PIS/Cofins do Presumido por CBS/IBS (cliente que não credita)")
    s.add_argument("--outras-rendas-anuais", type=float, default=0,
                   help="outras rendas do sócio no ano (salário, bolsa, aluguel), para o IRPFM")

    s = sub.add_parser("ganho-capital")
    s.add_argument("--venda", type=float, required=True)
    s.add_argument("--custo", type=float, required=True)

    s = sub.add_parser("irpfm")
    s.add_argument("--renda-total", type=float, required=True)
    s.add_argument("--ir-pago", type=float, default=0)

    a = ap.parse_args()
    aviso_vigencia()

    if a.cmd == "irpf-mensal":
        r = irpf_mensal(a.renda, a.inss, a.dependentes, a.pensao)
        print(f"Dedução usada: {brl(r['deducao'])} ({r['deducao_tipo']})")
        print(f"Base: {brl(r['base'])}  Tabela: {brl(r['imposto_tabela'])}  "
              f"IR após redutor Lei 15.270: {brl(r['imposto'])}")
    elif a.cmd == "irpf-anual":
        r = irpf_anual(a.tributaveis, a.inss, a.dependentes, a.saude, a.educacao,
                       a.pgbl, a.pensao, a.livro_caixa, a.retido)
        for k in ("completa", "simplificada"):
            x = r[k]
            print(f"{k:<13} deduções {brl(x['deducoes']):>16}  base {brl(x['base']):>16}  "
                  f"imposto {brl(x['imposto']):>14}  saldo {brl(x['a_pagar_ou_restituir']):>14}")
        print(f"Melhor: {r['melhor']}. Espaço de PGBL ainda dedutível: {brl(r['pgbl_espaco_restante'])}")
    elif a.cmd == "simples":
        r = simples(a.rbt12, a.receita_mes, a.anexo, a.exportacao)
        print(f"Anexo {a.anexo}, faixa {r['faixa']}: alíquota efetiva {pct(r['aliquota_efetiva'])}, "
              f"exportação {pct(r['aliquota_exportacao'])}. DAS do mês {brl(r['das'])}")
        if r["cpp_fora_do_das"]:
            print("Anexo IV: o INSS patronal de 20% sobre a folha é pago fora do DAS.")
    elif a.cmd == "regimes":
        linhas = cenarios(a.faturamento, a.iss, a.exportacao_pct, a.despesas,
                          a.dependentes, a.tem_mei_atividade, a.outras_rendas_anuais, a.ano)
        cab = f"{'Cenário':<32}{'Empresa':>12}{'INSS':>10}{'IR pl':>10}{'CPP':>10}{'IRPFM':>10}{'Total':>12}{'Carga':>8}{'No bolso':>13}"
        print(f"Ano {a.ano}. Faturamento {brl(a.faturamento)}/mês, ISS {pct(a.iss)}, exportação {pct(a.exportacao_pct)}\n")
        if a.ano >= 2027:
            r = P["reforma_2027"]
            print(f"2027: Presumido com CBS+IBS de {pct(r['cbs'] + r['ibs'])} sobre a receita interna, como custo "
                  "(cliente pessoa física, empresa do Simples ou que não credita). Cliente do regime regular "
                  "credita esse valor e o Presumido fica bem mais barato. O DAS do Simples não muda em 2027.\n")
        print(cab)
        print("-" * len(cab))
        for nome, r, _ in sorted(linhas, key=lambda x: x[1]["total"]):
            print(f"{nome:<32}{r['imposto_empresa']:>12.2f}{r['inss_socio']:>10.2f}{r['irpf_prolabore']:>10.2f}"
                  f"{r['cpp_patronal']:>10.2f}{r['ir_dividendos']:>10.2f}{r['total']:>12.2f}"
                  f"{pct(r['carga']):>8}{r['no_bolso']:>13.2f}")
        print()
        for nome, r, nota in linhas:
            extra = (f" Retenção de 10% sobre dividendos: {brl(r['irrf_div_retido_mes'])}/mês, "
                     "volta no ajuste se a renda anual não passar de R$ 600 mil."
                     if r["irrf_div_retido_mes"] else "")
            print(f"- {nome}: {nota}.{extra}")
        print("\nIRPFM = imposto mínimo anual rateado por mês (renda do sócio acima de R$ 600 mil). "
              "Não inclui custo de contador nem o redutor de 34% do art. 16-B.")
    elif a.cmd == "ganho-capital":
        r = ganho_capital(a.venda, a.custo)
        print(f"Ganho {brl(r['ganho'])}, imposto {brl(r['imposto'])} (antes de isenções e fatores de redução)")
    elif a.cmd == "irpfm":
        r = irpfm(a.renda_total, a.ir_pago)
        print(f"Alíquota mínima {pct(r['aliquota'])}, imposto mínimo {brl(r['minimo'])}, "
              f"a complementar {brl(r['devido'])} (sem o redutor da tributação da PJ)")


if __name__ == "__main__":
    main()
