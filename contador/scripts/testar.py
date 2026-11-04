#!/usr/bin/env python3
"""Testes da calculadora contra exemplos oficiais e contas já conferidas.

Roda antes de cada publicação (publicar.sh). Ao trocar parametros.json de ano,
troque também os casos abaixo por exemplos oficiais do ano novo: um teste
vermelho depois de mudar um número quer dizer que o caso precisa de fonte
nova, não que o teste deve ser apagado.
"""
import json
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import calc  # noqa: E402

CASOS = [
    # (descrição, valor calculado, esperado, fonte)
    ("IR mensal de R$ 6.000 com simplificado", lambda: calc.irpf_mensal(6000)["imposto"], 394.54,
     "Receita, exemplos da Lei 15.270/2025"),
    ("IR mensal de R$ 5.000 zera", lambda: calc.irpf_mensal(5000)["imposto"], 0.0, "Lei 15.270/2025"),
    ("IR anual de R$ 70 mil, simplificada", lambda: calc.irpf_anual(70000)["simplificada"]["imposto"], 2755.86,
     "tabela anual 2026 da Receita + redutor"),
    ("IR anual de R$ 60 mil, completa com INSS de R$ 6 mil",
     lambda: calc.irpf_anual(60000, inss=6000)["completa"]["imposto"], 1350.00, "redutor tem teto de R$ 2.694,15"),
    ("IR anual de R$ 110 mil, simplificada", lambda: calc.irpf_anual(110000)["simplificada"]["imposto"], 14494.34,
     "tabela anual 2026"),
    ("DAS Anexo III, RBT12 R$ 360 mil", lambda: calc.simples(360000, 30000, "III")["das"], 2580.00, "LC 123 Anexo III"),
    ("Exportação Anexo III, 1ª faixa", lambda: round(calc.simples(120000, 10000, "III", 10000)["aliquota_exportacao"], 4),
     0.0305, "partilha da LC 155/2016"),
    ("Presumido R$ 30 mil, ISS 2%, carga total",
     lambda: dict((n, r["total"]) for n, r, _ in calc.cenarios(30000, 0.02, 0, 0, 0, False))["Lucro Presumido"],
     4501.51, "conta independente da pesquisa de PJ"),
    ("Simples III R$ 30 mil, carga total",
     lambda: dict((n, r["total"]) for n, r, _ in calc.cenarios(30000, 0.02, 0, 0, 0, False))["Simples III (Fator R)"],
     4651.17, "conta independente da pesquisa de PJ"),
    ("Presumido 2027 R$ 30 mil, ISS 5%, tributos da empresa",
     lambda: calc.presumido(30000, 0.05, ano=2027)["total"], 7194.00, "CBS 11,2% + IBS 0,1% (provisório)"),
    ("IRPFM com renda de R$ 900 mil", lambda: calc.irpfm(900000)["aliquota"], 0.05, "Lei 9.250 art. 16-A"),
]


def main():
    falhas = 0
    for desc, f, esperado, fonte in CASOS:
        valor = f()
        ok = abs(valor - esperado) <= 0.01
        falhas += not ok
        print(f"{'ok   ' if ok else 'FALHA'} {desc}: {valor:.4f} (esperado {esperado}, {fonte})")

    p = json.loads((AQUI / "parametros.json").read_text())
    for chave in ("ano_vigencia", "conferido_em", "irpf", "simples", "presumido", "inss", "rio"):
        if chave not in p:
            print(f"FALHA parametros.json sem a chave {chave}")
            falhas += 1

    refs = AQUI.parent / "references"
    for nome in ("pessoa-fisica", "pessoa-juridica", "reforma-tributaria", "rio-de-janeiro",
                 "estrategias", "limites-legais", "calendario"):
        texto = (refs / f"{nome}.md").read_text()
        if "Conferido em" not in texto:
            print(f"FALHA references/{nome}.md sem a linha 'Conferido em'")
            falhas += 1

    print(f"\n{len(CASOS)} casos de cálculo, {falhas} falha(s) no total")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
