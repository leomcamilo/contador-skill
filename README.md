# contador-skill

Uma skill de contador pessoal no formato Agent Skills, para Claude Code, Hermes e OpenClaw. Ela tem um objetivo: o cliente pagar o mínimo de imposto que a lei permite, sem se expor a autuação. Cuida da pessoa física e da empresa ao mesmo tempo, porque a conta que importa é o total que sai do bolso, e não a alíquota de um tributo isolado.

As regras são as federais vigentes em novembro de 2026, com o que já está aprovado para 2027, e as do Rio de Janeiro (estado e cidade). Cada número tem fonte, data de conferência e grau de confiança, e cada referência termina com uma lista do que ainda está em aberto.

## O que cobre

- Imposto de renda da pessoa física em 2026: redutor da Lei 15.270 (zero até R$ 5 mil por mês), imposto mínimo acima de R$ 600 mil por ano, retenção de 10% sobre dividendos acima de R$ 50 mil por mês, deduções, carnê-leão, investimentos, ganho de capital, INSS do autônomo, declaração completa x simplificada e conjunta x separada.
- Empresa: MEI, Simples Nacional com Fator R, Lucro Presumido (com a LC 224/2025), Lucro Real e Lei do Bem, pró-labore, distribuição de lucros, pejotização, obrigações e multas.
- Reforma do consumo: CBS e IBS a partir de 2027, regime de IBS/CBS por fora do Simples e quando compensa, cronograma até 2033.
- Rio de Janeiro: ISS carioca por tipo de serviço (2% para software sob encomenda, 5% para SaaS e consultoria), incentivos do Porto Maravilha e do Parque Tecnológico da UFRJ, Nota Carioca, ITCMD, ITBI, IPTU, IPVA, Taxa de Incêndio e abertura de empresa.
- Limites: o que separa planejamento de sonegação, multas, crimes, e um catálogo de jogadas com risco verde, amarelo ou vermelho. Vermelho a skill explica, mas não recomenda.

## O que tem aqui

```
contador/
  SKILL.md                     a skill
  references/
    pessoa-fisica.md           IRPF, INSS, investimentos, ganho de capital
    pessoa-juridica.md         MEI, Simples, Presumido, Real, retirada do sócio
    reforma-tributaria.md      CBS, IBS e o Simples na transição
    rio-de-janeiro.md          tributos do estado e da cidade do Rio
    estrategias.md             catálogo de jogadas legais com economia e risco
    limites-legais.md          elisão x evasão, multas, crimes, pejotização
    calendario.md              prazos e janelas de opção
    fontes.md                  onde conferir cada coisa
    perfil-modelo.md           formato do perfil do cliente
  scripts/
    calc.py                    calculadora (IRPF, Simples, Presumido, regimes, IRPFM)
    parametros.json            todos os números legais, com fonte e vigência
    testar.py                  testes contra exemplos oficiais
    atualizar.sh               git pull no começo de cada uso
    publicar.sh                publica uma correção (testes, PR e merge)
install.sh                     instala no Claude Code, no Hermes ou no OpenClaw
```

## Instalar

```bash
git clone https://github.com/leomcamilo/contador-skill ~/contador-skill
cd ~/contador-skill
./install.sh claude      # Claude Code: ~/.claude/skills/contador
./install.sh hermes      # Hermes: ~/.hermes/skills/contador
./install.sh openclaw    # OpenClaw: ~/.openclaw/skills/contador
```

O script cria um link para a pasta `contador/`. Se já houver uma skill `contador` no destino, ela vai antes para `~/.contador-skill-backup/`. Use `--copy` para copiar, mas aí a atualização automática não funciona.

## Atualização automática

A skill se mantém atualizada sozinha, nos dois sentidos:

- **Ao ser chamada**, ela roda `scripts/atualizar.sh`, que faz `git pull` do repositório. Sem rede, segue com a versão local. Se o próprio SKILL.md mudou, o agente relê antes de responder.
- **Quando uma conversa confirma em fonte oficial** que um número ou uma regra mudou, o agente corrige o arquivo e roda `scripts/publicar.sh "o que mudou (fonte: ...)"`. O script roda os testes, recusa diff com CPF, CNPJ ou e-mail, abre um PR e faz o merge. As outras instalações recebem na chamada seguinte.

Publicar exige `gh` logado com permissão de escrita aqui. Sem ela, a correção fica só na sua instalação; abra uma issue ou um PR pelo seu fork.

## Usar

Peça como pediria a um contador: "abro MEI ou ME?", "como pago menos imposto este ano?", "vou vender meu apartamento, quanto pago?", "vale a pena PGBL?", "quanto de ISS pago no Rio por SaaS?". Na primeira conversa a skill monta o seu perfil em `~/.contador/perfil.md` (a pasta muda com `CONTADOR_HOME`) e depois guarda as decisões e os prazos ali. Esse perfil nunca vai para o repositório.

A calculadora também roda sozinha:

```bash
python3 contador/scripts/calc.py regimes --faturamento 30000 --iss 0.05 --ano 2027
python3 contador/scripts/calc.py irpf-anual --tributaveis 120000 --saude 8000 --pgbl 14000 --inss 10000
python3 contador/scripts/calc.py simples --rbt12 600000 --receita-mes 50000 --anexo III --exportacao 20000
```

## Limites

É apoio à decisão, não serviço contábil. Abrir empresa, assinar declaração, escriturar e se defender numa fiscalização são tarefas de contador com CRC ou de advogado tributarista, e a skill diz quando chamar cada um. Os números foram conferidos em 04/11/2026. A alíquota da CBS de 2027 está provisória até a resolução do Senado (prazo de 15/12/2026).

Para conferir números com uma segunda fonte revisada por contador, as skills brasileiras do [OpenAccountants](https://github.com/openaccountants/openaccountants) são boas. Elas calculam e declaram, mas não fazem planejamento nem cobrem o Rio em detalhe.

## Licença

MIT.
