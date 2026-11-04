# Pessoa física: IRPF, INSS e investimentos

Conferido em 2026-11-04. Vale para o ano-calendário 2026 (DIRPF 2027). Confiança: **alta** = texto oficial lido; **média** = portal ou imprensa; **baixa** = não confirmado. "Cálculo próprio" = conta feita com as tabelas oficiais (o exemplo de R$ 6.000/mês bate com o da Receita).

Calculadora: `scripts/calc.py irpf-mensal`, `irpf-anual`, `ganho-capital`, `irpfm`.

## Normas-base desta pesquisa

| Norma | O que mudou | Link |
|---|---|---|
| Lei 15.270/2025 (26/11/2025) | Redução mensal e anual do IR, IRRF de 10% sobre dividendos acima de R$ 50 mil/mês, IRPFM, desconto simplificado anual de R$ 17.640 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm |
| Lei 9.250/1995 compilada | Deduções, dependentes, educação, doações, isenção de bolsas (art. 26) | https://www.planalto.gov.br/ccivil_03/leis/l9250.htm |
| Lei 11.482/2007 compilada (tabela dada pela Lei 15.191/2025) | Tabela progressiva mensal vigente desde maio/2025 | https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11482.htm |
| LC 224/2025 (26/12/2025) | Corte de 10% em benefícios de PJ; IRRF sobre JCP sobe para 17,5% a partir de 01/01/2026 | https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp224.htm |
| LC 222/2025 | Nova lei de incentivo ao esporte (PF até 7% do IR devido) | https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp222.htm |
| Lei 15.265/2025 | Rearp (atualização de bens a 4%), prazo encerrado em fev/2026 | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15265.htm |
| Lei 15.513/2026 (22/09/2026) | Prorroga Pronon e Pronas/PCD até 2031 **só para PJ** | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15513.htm |
| Receita, "Tributação de 2026" (atualizada em 27/04/2026) | Tabelas mensal e anual oficiais, inclusive a anual da DIRPF 2027 | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026 |
| Perguntão IRPF 2026 (v1.00, 23/04/2026, 745 perguntas) | Interpretação oficial da Receita para o ano-calendário 2025 | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf |
| P&R Receita "Tributação de Altas Rendas: lucros e dividendos" (19/12/2025) | Interpretação da Receita sobre IRRF de dividendos e transição | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirf/manual_padrao_rfb_per_tributacao_cotin_v-19-12-2025.pdf |

## O que mudou em relação ao que "todo mundo sabe"

1. A faixa de isenção da tabela continua em R$ 2.428,80/mês. O "isento até R$ 5 mil" vem de um redutor calculado à parte, sobre o rendimento **bruto**, e só zera o imposto se a pessoa usar o desconto simplificado (ou tiver deduções de pelo menos R$ 607,20/mês).
2. A faixa de transição (R$ 5.000,01 a R$ 7.350/mês) tem alíquota marginal efetiva de até 40,81%, mais alta que os 27,5% de quem ganha R$ 20 mil. No anual, entre R$ 60 mil e R$ 88,2 mil a marginal fica em 31,56% (com desconto simplificado).
3. Declaração conjunta ficou muito pior. Cada CPF tem seu próprio redutor anual de até R$ 60 mil. Casal com R$ 55 mil cada paga zero em separado e cerca de R$ 14,5 mil em conjunto (cálculo próprio).
4. Dividendos de Simples Nacional e de MEI também sofrem a retenção de 10% acima de R$ 50 mil/mês na visão da Receita, apesar da LC 123. Há liminares para os dois lados.
5. Doação ao Pronon e ao Pronas/PCD deixou de ser dedutível para pessoa física a partir do ano-calendário 2026. A prorrogação até 2031 (Lei 15.513/2026) vale só para PJ.
6. O Perguntão diz que a bolsa de estudos isenta "não justifica acréscimo patrimonial". Para um doutorando que poupa a bolsa e compra bens, isso é um risco de malha a gerenciar.
7. O IRRF sobre JCP subiu de 15% para 17,5% desde 01/01/2026 (LC 224/2025).
8. A MP 1.303/2025 caducou em 08/10/2025. LCI, LCA, CRI, CRA, FII e a isenção de R$ 35 mil/mês em cripto doméstica continuam como antes.

---

## 1. Tabela progressiva, redutor da Lei 15.270, desconto simplificado e dependentes

### Números

**Tabela progressiva mensal (vigente desde maio/2025, mantida em 2026)**

| Base de cálculo mensal (R$) | Alíquota | Parcela a deduzir (R$) |
|---|---|---|
| até 2.428,80 | 0% | 0 |
| 2.428,81 a 2.826,65 | 7,5% | 182,16 |
| 2.826,66 a 3.751,05 | 15% | 394,16 |
| 3.751,06 a 4.664,68 | 22,5% | 675,49 |
| acima de 4.664,68 | 27,5% | 908,73 |

**Redutor mensal (art. 3º-A da Lei 9.250, desde jan/2026)**

| Rendimento tributável mensal **bruto** | Redução do imposto |
|---|---|
| até R$ 5.000,00 | até R$ 312,89 (limitada ao imposto da tabela, de modo a zerar) |
| R$ 5.000,01 a R$ 7.350,00 | R$ 978,62 − (0,133145 × rendimento bruto) |
| acima de R$ 7.350,00 | zero |

Vale também para o IR exclusivo na fonte do 13º salário (art. 3º-A, § 3º) e para o carnê-leão (Perguntão, pergunta 266).

**Tabela progressiva anual da DIRPF 2027 (ano-calendário 2026), publicada pela Receita**

| Base de cálculo anual (R$) | Alíquota | Parcela a deduzir (R$) |
|---|---|---|
| até 29.145,60 | 0% | 0 |
| 29.145,61 a 33.919,80 | 7,5% | 2.185,92 |
| 33.919,81 a 45.012,60 | 15% | 4.729,91 |
| 45.012,61 a 55.976,16 | 22,5% | 8.105,85 |
| acima de 55.976,16 | 27,5% | 10.904,66 |

**Redutor anual (art. 11-A, a partir do exercício 2027)**

| Rendimento tributável anual bruto | Redução |
|---|---|
| até R$ 60.000,00 | até R$ 2.694,15 (zera o imposto) |
| R$ 60.000,01 a R$ 88.200,00 | R$ 8.429,73 − (0,095575 × rendimento anual) |
| acima de R$ 88.200,00 | zero |

**Outros valores de 2026**

| Item | Mensal | Anual |
|---|---|---|
| Desconto simplificado | R$ 607,20 (25% da faixa isenta) | 20% dos rendimentos tributáveis, teto R$ 17.640,00 (era R$ 16.754,34 até o ano-calendário 2025) |
| Dedução por dependente | R$ 189,59 | R$ 2.275,08 |
| Parcela isenta de aposentadoria para 65+ | R$ 1.903,98 | R$ 24.751,74 (13 × R$ 1.903,98, cálculo próprio) |

**Exemplos (cálculo próprio, com desconto simplificado)**

| Bruto mensal | IR mensal | Bruto anual | IR anual |
|---|---|---|---|
| R$ 5.000 | R$ 0,00 | R$ 60.000 | R$ 0,00 |
| R$ 6.000 | R$ 394,54 (igual ao exemplo oficial) | R$ 70.000 | R$ 2.755,86 |
| R$ 7.350 | R$ 945,54 | R$ 88.200 | R$ 8.499,33 |
| R$ 10.000 | R$ 1.674,29 | R$ 110.000 | R$ 14.494,34 |

Alíquota marginal efetiva (cálculo próprio): 35,81% entre R$ 5.000 e R$ 5.271,88/mês; 40,81% entre R$ 5.271,88 e R$ 7.350/mês; 27,5% acima. No anual: 31,56% entre R$ 60 mil e R$ 88,2 mil com desconto simplificado (37,06% na completa com deduções fixas).

### Jogada legal

O redutor é calculado sobre o rendimento bruto, e o imposto da tabela sobre a base depois das deduções. Duas consequências práticas. Primeiro, quem fica até R$ 5.000/mês ou R$ 60.000/ano zera o imposto com o desconto simplificado, sem precisar guardar recibo nenhum; o teto do redutor (R$ 312,89 e R$ 2.694,15) foi desenhado exatamente para o caso do simplificado. Com a declaração completa e poucas deduções, o imposto **não** zera: R$ 60 mil de bruto com só R$ 6 mil de INSS deixa R$ 1.350 a pagar. Segundo, na faixa de transição cada real a mais custa 35% a 41%, então vale mexer no timing: antecipar ou adiar receita de autônomo, distribuir aluguel entre cônjuges, fixar pró-labore em R$ 5.000. Deduções como PGBL continuam economizando à alíquota da tabela (27,5%) porque não mexem no redutor. Quem tem duas fontes pagadoras abaixo de R$ 5 mil cada não sofre retenção, mas paga a diferença no ajuste anual (orientação da Receita), e o cliente precisa saber disso para não ser pego de surpresa.

### Fontes

- Lei 15.270/2025, arts. 2º (arts. 3º-A, 10, 11-A da Lei 9.250) e 8º: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm
- Lei 11.482/2007, art. 1º, XII (tabela mensal) e parágrafo único (anual = soma das mensais): https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11482.htm
- Lei 9.250/1995, art. 4º, III, "i" e § 2º; art. 8º, II, "b" e "c": https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
- Receita, Tributação de 2026: https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026
- Receita, Exemplos de aplicação da Lei 15.270 (redutor sobre o bruto): https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/exemplos-de-aplicacao-da-lei-15-270-2025
- Receita, orientação a fontes pagadoras (dez/2025): https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2025/dezembro/receita-federal-orienta-fontes-pagadoras-e-contribuintes-a-calcular-a-reducao-do-imposto-de-renda-a-partir-de-1o-de-janeiro-de-2026

**Confiança: alta.**

---

## 2. IRPFM (tributação mínima para altas rendas)

### Números

| Item | Regra |
|---|---|
| Quem entra | PF cuja soma de todos os rendimentos do ano supere R$ 600.000 (art. 16-A, caput) |
| Alíquota | 0% até R$ 600 mil; entre R$ 600 mil e R$ 1,2 mi: alíquota % = (REND / 60.000) − 10; 10% a partir de R$ 1,2 mi |
| Exemplos de alíquota (cálculo próprio) | R$ 750 mil: 2,5% (R$ 18.750); R$ 900 mil: 5% (R$ 45.000); R$ 1,2 mi: 10% (R$ 120.000) |
| Entram na base | Tudo, inclusive rendimentos isentos, tributados exclusivamente na fonte e de alíquota zero, e o resultado da atividade rural |
| Ficam fora da base (lista fechada, § 1º) | Ganho de capital (exceto bolsa e balcão organizado tributados pelo ganho líquido); RRA tributado exclusivamente na fonte; doação em adiantamento de legítima e herança; poupança; LH, LCI, CRI, LIG, LCD; debêntures e fundos da Lei 12.431; FIP-IE (Lei 11.478); rendimentos de FII e Fiagro negociados exclusivamente em bolsa com pelo menos 100 cotistas; CDA, WA, CDCA, LCA, CRA; CPR financeira; parcela isenta da atividade rural; indenizações por acidente de trabalho e danos materiais e morais (exceto lucros cessantes); moléstia grave (art. 6º, XIV e XXI, Lei 7.713); outros títulos isentos ou de alíquota zero, exceto ações e participações; lucros e dividendos de resultados até 2025 aprovados até 31/12/2025 e pagos em 2026, 2027 e 2028 conforme o ato de aprovação |
| Não estão na lista de exclusão (portanto entram) | Dividendos de 2026 em diante, JCP, juros de CDB e Tesouro, aluguéis, salários, bolsas isentas, parcela isenta de 65+ |
| Abatimentos do IRPFM | IR do ajuste anual; IR retido exclusivamente na fonte sobre rendimentos da base; IR da Lei 14.754 (exterior); IR definitivo pago; redutor do art. 16-B. Se der negativo, vira zero. Depois abate o IRRF de 10% dos dividendos (art. 6º-A) |
| Redutor por tributação da PJ (art. 16-B) | Se alíquota efetiva IRPJ+CSLL da empresa + alíquota efetiva do IRPFM superar 34% (regra geral), 40% (seguradoras, capitalização e várias financeiras da LC 105) ou 45% (bancos, inciso I da LC 105), devolve o excesso sobre os dividendos daquela empresa. Exige demonstrações financeiras; empresa fora do lucro real pode usar lucro contábil simplificado (faturamento menos folha, CMV, matéria-prima, aluguel, juros e depreciação) |
| Quando | Primeira apuração na DIRPF 2027 (ano-calendário 2026). Vai somado ao saldo do ajuste anual (art. 16-A, § 6º; art. 13), que pode ser parcelado em até 8 quotas (art. 14 da Lei 9.250) |
| Cartórios | Repasses obrigatórios sobre emolumentos saem da base (§ 7º) |

### Jogada legal

A alíquota é calculada sobre o REND depois das exclusões do § 1º. Quem tem R$ 2 milhões de rendimento, dos quais R$ 1,5 milhão em LCI, LCA, FII e ganho de capital, tem REND de R$ 500 mil e alíquota zero. A jogada clássica é deslocar a carteira para ativos fora da base (LCI, LCA, CRI, CRA, debêntures incentivadas, FII com 100+ cotistas) e preferir ganho de capital a renda recorrente. Para o sócio de empresa, o redutor do 16-B devolve tudo o que passar de 34% somando PJ e PF; empresa no lucro real com carga efetiva perto de 34% praticamente zera o IRPFM sobre os dividendos dela, desde que tenha demonstrações financeiras em ordem. Empresa do Presumido com margem alta tem carga efetiva baixa e o sócio paga o mínimo cheio, o que muda a conta Presumido x Real (assunto do relatório de PJ). Por fim, quem fica pouco acima de R$ 600 mil paga alíquotas pequenas: R$ 660 mil dá 1%.

### Fontes

- Lei 15.270/2025, art. 2º (arts. 13, 16-A e 16-B da Lei 9.250): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm
- P&R Receita sobre altas rendas, perguntas 3, 4 e 12: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirf/manual_padrao_rfb_per_tributacao_cotin_v-19-12-2025.pdf

**Confiança: alta** para o texto legal. **Média** para a leitura de que o gatilho de R$ 600 mil conta rendimentos isentos (ver pontos em aberto).

---

## 3. Dividendos

### Números

| Item | Regra |
|---|---|
| IRRF mensal (art. 6º-A) | 10% sobre o **total** pago por uma mesma PJ a uma mesma PF residente quando o total do mês for **superior** a R$ 50.000. Sem deduções. Vários pagamentos no mês são somados |
| Efeito degrau | R$ 50.000,00 no mês: zero de IRRF. R$ 50.000,01: R$ 5.000,00 de IRRF (cálculo próprio). A OAB ajuizou ação no STF contra o degrau em abr/2026; não achei decisão |
| Natureza do IRRF | Antecipação. Se o total anual da PF não passar de R$ 600 mil, o IRRF volta como restituição na DIRPF (P&R Receita, pergunta 4) |
| No ajuste anual comum | Dividendos seguem isentos (art. 10 da Lei 9.249 mantido); só entram no IRPFM |
| Capitalização de lucros | Conta como "emprego" e sofre IRRF e IRPFM (P&R, pergunta 12) |
| Simples Nacional e MEI | Receita entende que a retenção se aplica (P&R, pergunta 10). Liminar contra em fev/2026; TRF-1 a favor da retenção em out/2026; Justiça Federal de SP afastou a regra em set/2026 |
| Transição (lucros até 2025) | Não sofrem IRRF nem entram no IRPFM se: (i) resultado apurado até 2025; (ii) distribuição aprovada até 31/12/2025 pelo órgão competente; (iii) exigíveis e pagos nos termos originais do ato de aprovação, em 2026, 2027 ou 2028 |
| Como a Receita aceitou aprovar lucro de 2025 em 2025 | Balanço intermediário ou balancete de jan a nov/2025, aprovado até 31/12/2025; se o balanço final vier menor, a isenção fica limitada ao lucro efetivo (P&R, pergunta 9) |
| Prorrogação | Liminar do min. Nunes Marques (ADIs 7.912 e 7.914, 26/12/2025) estendeu o prazo de aprovação para 31/01/2026. Referendo virtual interrompido por destaque do min. Fachin em 18/02/2026; não achei julgamento posterior até nov/2026. O PL 5.473/2025 (prazo até 30/04/2026) não virou lei |
| Remessa ao exterior | 10% de IRRF em qualquer valor, desde jan/2026 (art. 10, § 4º, Lei 9.249). Isentos: lucros de até 2025 nas mesmas condições, governos estrangeiros com reciprocidade, fundos soberanos, fundos de pensão estrangeiros. Crédito opcional ao não residente quando carga da PJ + 10 p.p. passar de 34/40/45% (art. 10-A), pedido em até 360 dias |
| JCP | IRRF de 17,5% desde 01/01/2026 (LC 224/2025, art. 8º); entra no IRPFM |
| Prazo de recolhimento pela PJ | Até o último dia útil do 2º decêndio do mês seguinte, DARF 1841 |

### Jogada legal

Para quem fica abaixo de R$ 600 mil no ano, o IRRF de 10% é só um empréstimo ao governo que volta na restituição. Mesmo assim vale evitá-lo: programar a distribuição em parcelas de até R$ 50.000,00 por mês e por empresa (exatamente R$ 50 mil, nunca R$ 50.000,01) elimina a retenção e o problema de caixa. Nunca pagar entre R$ 50.000,01 e uns R$ 55.556 no mês: o líquido fica menor que o de R$ 50 mil. Quem aprovou lucros de 2025 até 31/12/2025 precisa pagar no cronograma do ato de aprovação e até 2028; atraso ou mudança do cronograma pode derrubar a isenção. JCP a 17,5% perdeu atratividade para o sócio pessoa física pequeno, que recebe dividendo a zero. Para quem passa de R$ 600 mil, a conta é o redutor do art. 16-B (tópico 2).

### Fontes

- Lei 15.270/2025, arts. 2º (art. 6º-A) e 3º (arts. 10 e 10-A da Lei 9.249): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm
- P&R Receita altas rendas (perguntas 4 a 14, 22): https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirf/manual_padrao_rfb_per_tributacao_cotin_v-19-12-2025.pdf
- LC 224/2025, arts. 8º e 14 (JCP 17,5%): https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp224.htm
- STF, liminar até 31/01/2026 (Poder360): https://www.poder360.com.br/poder-justica/stf-prorroga-prazo-para-aprovacao-de-lucros-e-dividendos-ate-31-de-janeiro/
- STF, destaque de Fachin (Conjur, 19/02/2026): https://conjur.com.br/2026-fev-19/stf-interrompe-analise-sobre-prorrogacao-do-prazo-para-aprovacao-de-dividendos-2/
- Linha do tempo judicial 2026 (Rota da Jurisprudência): https://rotadajurisprudencia.com.br/tag/lucros-e-dividendos/

**Confiança: alta** para lei, P&R e JCP. **Média** para o andamento das ações judiciais (só imprensa e portais).

---

## 4. Deduções

### Números

| Dedução | Limite 2026 | Regras que mais importam |
|---|---|---|
| Saúde | Sem teto | Médicos, dentistas, psicólogos, fisioterapeutas, fonoaudiólogos, terapeutas ocupacionais, hospitais, exames, radiologia, aparelhos e próteses ortopédicas e dentárias (com receita e nota), plano de saúde, cirurgia plástica com finalidade de saúde, despesa médica no exterior comprovada, instrução de pessoa com deficiência em entidade especializada. **Não entram**: remédios e vacinas (salvo na conta do hospital), acompanhante, DNA de paternidade, células-tronco de cordão, enfermeiro e massagista fora de internação, despesa reembolsada. Pilates só com fisioterapeuta. Só do próprio contribuinte, dependentes e alimentandos judiciais. Receita Saúde é prova hábil, mas não obrigatória para deduzir |
| Educação | R$ 3.561,50 por pessoa por ano | Infantil, fundamental, médio, superior (graduação, mestrado, doutorado, especialização), técnico. Excesso de um dependente não compensa outro. Uniforme, material, transporte, curso de idiomas e computador não entram |
| PGBL e Fapi | 12% dos rendimentos tributáveis da declaração | Só na completa. Exige contribuição ao RGPS ou RPPS "observada a contribuição mínima" (dispensa para aposentado). VGBL não deduz. Funpresp e similares até a alíquota do patrocinador ficam fora dos 12% |
| Dependente | R$ 2.275,08/ano | Filhos até 21 (24 se universitários), cônjuge, companheiro com filho ou 5+ anos, pais e avós com rendimentos até o limite de isenção anual (R$ 28.467,20 em 2025) |
| Pensão alimentícia | Sem teto | Só judicial, acordo homologado ou escritura pública. Quem paga não pode deduzir o filho como dependente (salvo no ano da separação). Quem recebe não paga IR (ADI 5.422) |
| INSS (previdência oficial) | Sem teto | Inclusive contribuinte individual e facultativo, regime de caixa (atrasados pagos no ano entram, sem multa e juros) |
| Livro-caixa (autônomo) | Até a receita do mês; excesso vai para os meses seguintes até dezembro, não passa de ano | Salário de empregado e encargos, emolumentos, custeio necessário (aluguel, água, luz, telefone, material de consumo). **Não entram**: depreciação, leasing, locomoção (salvo representante comercial). Serve para receita de PF e de PJ |
| Doações incentivadas (abatem do imposto) | ECA + Idoso + cultura + audiovisual: 6% do IR devido. Com reciclagem: 6%. Com esporte: 7% | Só na completa. ECA e Idoso também direto na DIRPF: até 3% cada, dentro do limite global, só na declaração entregue no prazo e com DARF pago até o último dia do prazo (códigos 3351 ECA e 9090 Idoso). Esporte agora pela LC 222/2025 (7% conjunto com ECA, Idoso, cultura e audiovisual). Reciclagem até o ano-calendário 2027 |
| Pronon e Pronas/PCD | **Extinta para PF a partir do ano-calendário 2026** | Lei 15.513/2026 prorrogou até 2031 só para PJ. Na DIRPF 2026 ainda valeu (1% cada) |
| Empregada doméstica | **Extinta** | INSS patronal doméstico só foi dedutível até o exercício 2019 (ano-calendário 2018) |
| Doação a ONG, universidade, filantropia | Não dedutível | Sem previsão legal (Perguntão, pergunta 454) |

### Jogada legal

Saúde é a única dedução grande sem teto. Concentrar despesas médicas do casal em quem está na alíquota de 27,5% e na declaração completa, e pagar plano de saúde em nome desse titular, rende mais do que qualquer outra coisa. PGBL até 12% faz sentido para quem está em 27,5% e pretende ficar 10 anos: deduz agora a 27,5% e paga 10% no resgate pela tabela regressiva (tópico 8); a escolha do regime pode ser feita até o primeiro resgate (Lei 14.803/2024). Atenção ao detalhe do INSS: sem contribuição ao RGPS no ano, o PGBL não deduz. ECA e Idoso direto na declaração são dinheiro que iria para a Receita de qualquer jeito; se o cliente vai ter imposto a pagar ou restituição menor, destinar até 3% para cada fundo custa zero. Para o autônomo, aluguel de sala, telefone, internet e material de consumo no livro-caixa reduzem a base do carnê-leão mês a mês.

### Fontes

- Lei 9.250/1995, arts. 4º, 8º, 10 e 12: https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
- Perguntão IRPF 2026, perguntas 335, 340, 367 a 403, 427 a 429, 454 a 456: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- LC 222/2025, arts. 9º e 22 (esporte 7%, reciclagem 6%): https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp222.htm
- Lei 12.715/2012 compilada, art. 4º (Pronon/Pronas só para PJ): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12715.htm
- Lei 15.513/2026: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15513.htm
- Lei 11.053/2004, art. 1º, § 6º (opção de regime até o 1º resgate): https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11053.htm

**Confiança: alta.** Exceção: o limite de pais dependentes para 2026 (provavelmente R$ 29.145,60, igual à faixa isenta anual) é **baixa**, porque a Receita só publica isso no Perguntão 2027.

---

## 5. Carnê-leão em 2026

### Números

| Item | Regra |
|---|---|
| Quem é obrigado | Residente que recebe de pessoa física sem retenção (aluguel, trabalho autônomo, arrendamento), de fonte no exterior (salário, serviços, aluguel), emolumentos de cartório, de embaixadas e organismos internacionais, transporte de carga (10% tributável) e de passageiros (60% tributável) |
| Cálculo | Tabela progressiva mensal sobre o total do mês, com o redutor da Lei 15.270 desde jan/2026 |
| Deduções no mês | Pensão judicial, R$ 189,59 por dependente, INSS, previdência complementar, livro-caixa; ou desconto simplificado mensal de R$ 607,20 |
| Aluguel | Tributa o valor recebido menos IPTU e taxas, condomínio, aluguel de imóvel sublocado e despesas de cobrança (taxa da imobiliária), quando o ônus for do locador. Aluguel pago por PJ tem retenção na fonte, não vai ao carnê-leão |
| Exterior | Converte pela cotação de compra do dólar do último dia útil da 1ª quinzena do mês anterior. Imposto pago lá compensa no mês e no ajuste, se houver tratado ou reciprocidade |
| Prazo e DARF | Até o último dia útil do mês seguinte ao recebimento, código 0190 |
| Ajuste | Tudo vai ao ajuste anual; o carnê-leão é antecipação |
| Profissionais de saúde, advogados, psicólogos, corretores | Devem informar CPF do pagador e do beneficiário na DIRPF |

### Jogada legal

Com o redutor, quem recebe até R$ 5.000/mês de PF ou do exterior (somando tudo no mês) e usa o desconto simplificado paga zero no carnê-leão. Isso favorece quebrar receitas irregulares em meses diferentes, quando o contrato permitir, e dividir aluguel de imóvel do casal: em bens comuns, cada cônjuge pode declarar 50% do aluguel (Perguntão, pergunta 77), o que coloca dois CPFs abaixo de R$ 5 mil em vez de um acima. Aluguel de R$ 9.000/mês declarado por um só paga R$ 1.399,29 de IR mensal (cálculo próprio com simplificado); dividido em dois de R$ 4.500, paga zero. IPTU, condomínio e taxa da administradora, quando pagos pelo locador, saem da base. Cuidado com a armadilha da pergunta 89: no condomínio entre não cônjuges, só quem consta no DARF compensa o imposto.

### Fontes

- Perguntão IRPF 2026, perguntas 77, 89, 214, 266, 267: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- Lei 9.250/1995, art. 4º: https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
- Lei 15.270/2025 (redutor mensal): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm

**Confiança: alta.**

---

## 6. Rendimentos isentos ou com tributação favorecida

### Números

| Rendimento | Tratamento em 2026 | Fonte |
|---|---|---|
| LCI, LCA, CRI, CRA, LH, CDA, WA, CDCA, CPR financeira | Isentos na fonte e no ajuste para PF; fora do IRPFM | Lei 11.033, art. 3º, II, IV e V |
| Debêntures incentivadas, CRI e fundos da Lei 12.431 | Alíquota zero para PF; fora do IRPFM | Lei 12.431, arts. 2º e 3º; Perguntão 738 |
| LIG | Isenta | Lei 13.097, art. 90 |
| FII e Fiagro (rendimentos distribuídos) | Isentos se cotas negociadas só em bolsa ou balcão, fundo com 100+ cotistas, cotista com menos de 10% das cotas e grupo familiar ligado com menos de 30%. Venda de cotas: 20% sobre o ganho | Lei 11.033, art. 3º, III e § 1º (red. Lei 14.754); Lei 8.668, art. 18 |
| Poupança | Isenta; fora do IRPFM | Lei 8.981, art. 68 |
| MP 1.303/2025 | Caducou em 08/10/2025 (retirada de pauta por 251 x 193). Nada dela sobre LCI, LCA, FII ou cripto virou lei. JCP 17,5% e alguns itens de PJ foram reaproveitados na LC 224/2025 | InfoMoney; LC 224/2025 |
| Bolsas de estudo e pesquisa | Isentas se caracterizadas como doação, recebidas só para estudar ou pesquisar, sem contraprestação de serviços e sem vantagem para o doador (art. 26, Lei 9.250). Também isentas as de médico-residente e as de estímulo à inovação (Lei 10.973, art. 9º, § 4º) | Lei 9.250, art. 26; Perguntão 181, 182, 287 |
| Bolsa CAPES, CNPq ou FAPERJ de doutorado | Enquadra-se no art. 26 quando não há contraprestação. Bolsa paga por fundação de apoio em projeto com entrega ao financiador costuma ser tributada (SC Cosit 140/2021) | Ver confiança |
| Ações à vista | Ganho isento se as vendas do mês somarem até R$ 20.000 (ouro ativo financeiro tem limite separado de R$ 20.000). Não vale para day trade, ETF, fundos de ações, opções | Lei 11.033, art. 3º, I; Perguntão 707 |
| Lucros de MEI | Isentos até a receita bruta × percentual de presunção do IRPJ (8% comércio, 32% serviços etc.), ou mais com escrituração contábil. Pró-labore, aluguel e serviços são tributáveis. A partir de 2026, sujeitos ao art. 6º-A e ao IRPFM segundo a Receita | Perguntão 184 |
| Lucros de sócio do Simples | Isentos até receita × presunção − IRPJ do Simples, ou o lucro contábil se houver escrituração. Mesma ressalva de 2026 | Perguntão 183; P&R altas rendas, pergunta 10 |
| Indenizações | Danos morais isentos (Ato Declaratório PGFN 9/2011); PDV isento; acidente de trabalho isento. Lucros cessantes são tributáveis e entram no IRPFM | Perguntão 228, 288; Lei 15.270 |
| Moléstia grave | Isentos só os proventos de aposentadoria, reforma e pensão (inclusive complementação e, segundo a PGFN, resgate de previdência complementar). Laudo de serviço médico público. Salário e aluguel continuam tributáveis | Lei 7.713, art. 6º, XIV e XXI; Perguntão 236, 237 |
| Aposentadoria de 65+ | Parcela isenta adicional de R$ 1.903,98/mês, sem prejuízo da faixa isenta da tabela. Entra no IRPFM | Lei 9.250, art. 4º, VI; Perguntão 277 |
| Pensão alimentícia recebida | Não tributável (ADI 5.422) | Perguntão 266 |

### Jogada legal (bolsista de pós-graduação)

A bolsa de doutorado da CAPES, do CNPq ou da FAPERJ é isenta e não conta para o limite de R$ 60 mil do redutor anual nem para a faixa da tabela. Isso abre espaço para o doutorando ter outra renda tributável (aulas, consultoria como autônomo, aluguel) até R$ 5.000/mês ou R$ 60.000/ano sem pagar IR, desde que use o desconto simplificado. A Portaria CAPES 133/2023 passou a permitir que o doutorando acumule a bolsa com trabalho remunerado, com autorização do orientador e registro na Sucupira (a regra do programa pode ser mais restritiva). Três cuidados. Primeiro, a bolsa é declarada como rendimento isento, e acima de R$ 200 mil/ano em isentos a DIRPF fica obrigatória. Segundo, o Perguntão (pergunta 287, apoiado na IN RFB 1.500, art. 11, § 5º) diz que a bolsa isenta "não justifica acréscimo patrimonial"; quem compra um carro ou investe a sobra da bolsa deve guardar extratos mostrando de onde veio cada real, porque essa é uma posição da Receita que pode gerar malha. Terceiro, bolsa ligada a projeto em que o bolsista entrega resultado ao financiador perde a isenção. Na carteira, LCI, LCA, CRI, CRA, debêntures incentivadas e FII seguem isentos para PF. A comparação com CDB e Tesouro deve ser feita pela taxa líquida: uma LCI a 90% do CDI equivale a um CDB a 105,9% do CDI no prazo de 15% de IR (cálculo próprio: 0,90 / 0,85).

### Fontes

- Lei 11.033/2004 compilada, art. 3º: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11033.htm
- Lei 9.250/1995, art. 26: https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
- Perguntão IRPF 2026, perguntas 181 a 184, 228, 236, 237, 266, 277, 287, 707, 738: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- MP 1.303 caducou (InfoMoney): https://www.infomoney.com.br/minhas-financas/mp-1-303-cai-no-congresso-veja-como-fica-a-tributacao-dos-investimentos-agora/
- SC Cosit 229/2023 (bolsa da Lei de Inovação é isenta, via Okai): https://okai.com.br/documento/2023-10-16/solucao-de-consulta-cosit-nº-229-de-16-de-outubro-de-2023
- Portaria CAPES 133/2023, resumo do IPEA: https://ipea.gov.br/cts/pt/central-de-conteudo/artigos/artigos/378-os-desafios-do-emprego-durante-o-doutorado-e-o-acumulo-com-bolsas-de-pesquisa

**Confiança: alta** para a lei e o Perguntão. **Média** para a aplicação direta às bolsas CAPES, CNPq e FAPERJ de doutorado (não achei página oficial da CAPES ou da Receita que nomeie essas bolsas; a prática e as Soluções de Consulta apontam isenção) e para a Portaria CAPES 133/2023 (li só resumos). **Média** para o fim da MP 1.303 (imprensa; não há "texto oficial" de caducidade além do ato do Congresso, que não consultei).

---

## 7. Ganho de capital

### Números

| Item | Regra |
|---|---|
| Alíquotas (desde 2017) | 15% até R$ 5 mi de ganho; 17,5% de R$ 5 mi a R$ 10 mi; 20% de R$ 10 mi a R$ 30 mi; 22,5% acima de R$ 30 mi. Venda em partes até o fim do ano seguinte soma os ganhos para definir a faixa |
| Exceções de alíquota | FII: 20%. FIP, FIC-FIP, FIEE: 15%. Diferença de valor de mercado em herança, doação em adiantamento e separação: 15% |
| Único imóvel | Isento se valor de venda até R$ 440.000, único imóvel do titular e nenhuma outra venda de imóvel nos últimos 5 anos (Lei 9.250, art. 23) |
| Reinvestimento em 180 dias | Isento o ganho na venda de imóvel residencial se o dinheiro comprar outro residencial no Brasil em até 180 dias contados do contrato (dia do contrato incluído). Uso a cada 5 anos. Aplicação parcial isenta proporcionalmente. Vale para imóvel na planta e para quitar financiamento de residencial já possuído. Não vale para construir, reformar, terreno ou só vaga de garagem. Corretagem não conta como produto da venda (Lei 11.196, art. 39) |
| Fatores de redução | Imóvel até 1969: 100%; de 1970 a 1988: 95% a 5% (Lei 7.713, art. 18). FR1 = 1/1,0060^m1 (meses de jan/1996 ou da compra até nov/2005) e FR2 = 1/1,0035^m2 (meses de dez/2005 ou da compra até a venda), aplicados em sequência (Lei 11.196, art. 40) |
| Bens de pequeno valor | Isento se o total de vendas no mês de bens da mesma natureza for até R$ 35.000 (R$ 20.000 para ações em balcão não organizado). Cripto custodiada no Brasil entra aqui. Aplicações no exterior não têm essa isenção desde 2024 |
| Atualização de imóveis da Lei 14.973/2024 (4%) | Prazo encerrado em dez/2024 |
| Rearp (Lei 15.265/2025) | Atualização de imóveis e veículos adquiridos até 31/12/2024 pagando 4% sobre a diferença. Adesão de 02/01 a 19/02/2026, pagamento até 27/02/2026. **Encerrado**; não achei reabertura. Quem aderiu perde o benefício se vender o imóvel em menos de 5 anos (2 anos para veículo); nova data de aquisição para FR1 e FR2 é a da opção |
| Prazo e DARF | Último dia útil do mês seguinte à venda, código 4600 |
| IRPFM | Ganho de capital fica fora da base (exceto bolsa) |

### Jogada legal

O ganho de capital tem alíquota de 15% e fica fora do IRPFM, o que o torna a forma mais barata de realizar riqueza depois do dividendo isento. Para imóveis, a ordem de ataque é: (1) se for o único imóvel e a venda for até R$ 440 mil, isento; (2) se residencial, reinvestir em 180 dias, inclusive para quitar o financiamento do imóvel onde mora; (3) imóvel antigo, aplicar FR1 e FR2, que corroem boa parte do ganho de imóveis comprados antes de 2005; (4) inflar o custo de aquisição com tudo o que a Receita aceita (Perguntão, pergunta 671): reformas e ampliações com projeto aprovado, pequenas obras como pintura e pisos, ITBI, escritura e registro, corretagem da compra paga pelo comprador, contribuição de melhoria e, o item mais esquecido, **os juros do financiamento imobiliário**. A condição é ter documento e ter lançado cada gasto na DIRPF do ano em que foi feito, então a skill deve lembrar o cliente todo ano de atualizar o custo do imóvel na ficha de bens. Para bens móveis e cripto doméstica, vender até R$ 35 mil por mês por natureza de bem zera o imposto; quem tem posição grande parcela as vendas ao longo dos meses. Doação a filhos pelo valor de declaração não gera ganho para o doador (o ITCMD é estadual, fora deste relatório).

### Fontes

- Perguntão IRPF 2026, perguntas 574 a 583, 640, 641, 656, 671, 679: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- Lei 9.250/1995, arts. 22 e 23: https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
- Lei 15.265/2025, arts. 3º, 7º e 10 (Rearp): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15265.htm
- Prazo do Rearp até 19/02/2026 (reformatributaria.com, citando nota da Receita): https://www.reformatributaria.com/economia/contribuintes-tem-ate-19-de-fevereiro-para-aderir-ao-rearp-atualizacao/

**Confiança: alta** para regras do Perguntão e das leis. **Média** para as datas exatas de adesão e pagamento do Rearp (lidas em imprensa que cita a Receita).

---

## 8. Investimentos

### Números

| Investimento | Regra 2026 |
|---|---|
| Renda fixa e fundos de longo prazo (tabela regressiva) | 22,5% até 180 dias; 20% de 181 a 360; 17,5% de 361 a 720; 15% acima de 720 |
| Fundos de curto prazo | 22,5% até 180 dias; 20% acima |
| Come-cotas | Último dia útil de maio e de novembro: 15% (longo prazo) ou 20% (curto prazo), com complemento no resgate. Vale para fundos abertos e fechados desde 2024 (Lei 14.754, art. 17). FIA, FIP, ETF de ações e FIDC entidade de investimento não têm come-cotas: 15% no resgate ou distribuição |
| Fundos de ações | 15% no resgate |
| Ações, opções, futuros (ganho líquido mensal) | 15% operações comuns; 20% day trade. IRRF de 0,005% (comum) como antecipação. Prejuízo compensa ganhos futuros sem prazo, separado entre comum e day trade. Despesas de corretagem entram no custo |
| Previdência PGBL e VGBL, regime regressivo | 35% até 2 anos; 30% de 2 a 4; 25% de 4 a 6; 20% de 6 a 8; 15% de 8 a 10; 10% acima de 10 anos. Opção até o 1º resgate ou benefício (Lei 14.803/2024). PGBL tributa o total; VGBL só o rendimento |
| Aplicações no exterior (Lei 14.754/2023) | 15% no ajuste anual, sem deduções, sobre rendimento efetivamente percebido (juros, dividendos, ganho na venda, inclusive variação cambial). Sem isenção de R$ 35 mil. Perdas compensam ganhos do mesmo ano e de anos seguintes, uma vez só. Imposto pago lá abate se houver tratado ou reciprocidade |
| Conta corrente no exterior | Variação cambial de depósito não remunerado em banco autorizado: isenta. Moeda em espécie: isenta até US$ 5.000 de venda no ano |
| Offshore controlada (mais de 50% ou poder de controle) | Lucro tributado a 15% em 31/12 de cada ano, haja ou não distribuição (art. 5º). Opção pelo regime de transparência (art. 8º), irrevogável, declarando os ativos como se fossem da PF |
| Cripto em exchange no Brasil | Ganho de capital de 15% a 22,5%; isento se vendas do mês somarem até R$ 35.000 (conjunto de todas as criptos). Permuta cripto por cripto é alienação. DARF 4600 até o último dia útil do mês seguinte |
| Cripto em exchange no exterior ou autocustódia de ativo emitido lá | Tratada como aplicação no exterior: 15% no ajuste anual, sem isenção mensal |
| Obrigação acessória cripto | DeCripto (IN RFB 2.291/2025) substitui a IN 1.888 a partir de jul/2026. Segundo resumo da Mattos Filho, o limite mensal de reporte da PF que opera fora de exchange brasileira subiu de R$ 30 mil para R$ 35 mil |

### Jogada legal

Para o investidor PF comum, a sequência é: primeiro LCI, LCA, CRI, CRA, debêntures incentivadas e FII (isentos e fora do IRPFM); depois Tesouro e CDB acima de 720 dias (15%); evitar fundos com come-cotas para posições de longo prazo, porque a antecipação semestral tira dinheiro dos juros compostos. Na bolsa, vender até R$ 20 mil por mês em ações dá isenção total; quem tem prejuízo acumulado deve registrá-lo mês a mês no demonstrativo da DIRPF, porque ele não caduca. Em dezembro, realizar prejuízo para compensar ganhos tributáveis do ano é legítimo. No exterior, a Lei 14.754 tributa só no recebimento: preferir ETFs de acumulação (que não distribuem dividendos) adia o imposto até a venda, e vender ativos com prejuízo no mesmo ano dos ganhos reduz a base. Para cripto, quem opera em exchange brasileira mantém a isenção de R$ 35 mil/mês, o que é muito melhor que os 15% sem isenção da exchange estrangeira; trazer a custódia para o Brasil é planejamento lícito.

### Fontes

- Receita, Tributação de 2026 (tabela regressiva e fundos): https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026
- Lei 14.754/2023, arts. 2º a 9º, 17 a 24: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm
- Lei 11.053/2004, art. 1º: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11053.htm
- Perguntão IRPF 2026, perguntas 653, 706 a 711: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- DeCripto (Mattos Filho): https://www.mattosfilho.com.br/unico/decripto-receita-federal-ocde/

**Confiança: alta**, exceto o limite de reporte da DeCripto e sua data de início (**média**).

---

## 9. INSS do contribuinte individual e do facultativo

### Números

| Item | Valor 2026 |
|---|---|
| Salário mínimo | R$ 1.621,00 (Decreto 12.797/2025) |
| Teto do salário de contribuição e dos benefícios | R$ 8.475,55 (Portaria Interministerial MPS/MF 13/2026) |
| Contribuinte individual, plano normal (20%) | De R$ 324,20 (sobre o mínimo) a R$ 1.695,11 (sobre o teto) |
| Plano simplificado (11% sobre o mínimo) | R$ 178,31. Só para CI que trabalha por conta própria **sem relação de trabalho com empresa** e para facultativo. Exclui aposentadoria por tempo de contribuição e contagem recíproca para RPPS, salvo complementação de 9% com juros (Decreto 3.048, art. 199-A) |
| MEI | 5% do mínimo: R$ 81,05 (mais ISS e/ou ICMS fixos) |
| Facultativo baixa renda (5%) | R$ 81,05, só para quem não tem renda própria, se dedica ao trabalho doméstico na própria casa e tem família no CadÚnico com renda até 2 mínimos |
| Bolsista de pós-graduação | Pode ser segurado facultativo se não tiver outro regime (Decreto 3.048, art. 11, § 1º, VIII) |
| Empregado (referência) | 7,5% / 9% / 12% / 14% progressivos até o teto |
| Dedução no IR | Toda contribuição ao INSS deduz na base (mensal e anual) |

### Jogada legal

Para manter cobertura (auxílio por incapacidade, salário-maternidade, pensão por morte, aposentadoria por idade, qualidade de segurado) pagando o mínimo, o plano simplificado de 11% sobre o salário mínimo (R$ 178,31/mês) é a opção para o autônomo que atende pessoa física e para o facultativo. Depois da EC 103/2019, a aposentadoria por tempo de contribuição só existe nas regras de transição, então abrir mão dela custa pouco para quem é jovem; quem tem cargo público em vista (RPPS) precisa da contagem recíproca e deve pagar 20% ou complementar depois. O doutorando bolsista não é segurado obrigatório: pode contribuir como facultativo a 11% para não perder carência e qualidade de segurado durante os anos de doutorado, e essa contribuição também é o que destrava a dedução do PGBL se ele tiver renda tributável. Quem é MEI paga 5% e já está coberto pela aposentadoria por idade. Pagar acima do mínimo só faz sentido como decisão de aposentadoria, porque o benefício é calculado pela média de todas as contribuições desde julho/1994.

### Fontes

- INSS, tabela de contribuição 2026 (atualizada em 13/01/2026): https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal
- INSS, teto de R$ 8.475,55: https://www.gov.br/inss/pt-br/assuntos/com-reajuste-de-3-9-teto-do-inss-chega-a-r-8-475-55-em-2026
- Decreto 12.797/2025 (salário mínimo): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12797.htm
- Decreto 3.048/1999, arts. 11, § 1º, VIII e 199-A: https://www.planalto.gov.br/ccivil_03/decreto/d3048.htm
- Perguntão IRPF 2026, pergunta 335 (PGBL exige contribuição ao RGPS): https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf

**Confiança: alta.** **Média** para a leitura de que o plano simplificado de 11% satisfaz a "contribuição mínima" exigida para deduzir o PGBL (a Receita não detalha).

---

## 10. DIRPF 2027: obrigatoriedade, prazos, completa x simplificada, conjunta x separada

### Números

| Item | Situação |
|---|---|
| Regras da DIRPF 2027 | **Não publicadas.** A IN costuma sair em março (a da DIRPF 2026 foi a IN RFB 2.312, de 13/03/2026) |
| Referência: obrigatoriedade na DIRPF 2026 | Rendimentos tributáveis acima de R$ 35.584,00; isentos e exclusivos acima de R$ 200.000; ganho de capital tributável; vendas em bolsa acima de R$ 40.000 ou com ganho tributável; receita rural acima de R$ 177.920; bens acima de R$ 800.000 em 31/12; quem passou a residente; quem usou a isenção dos 180 dias; quem tem aplicações, offshore ou trust no exterior com rendimentos, ganhos ou perdas a compensar |
| Projeção para DIRPF 2027 | Pelo critério histórico (1,25 × faixa isenta anual), o limite de rendimentos tributáveis iria para R$ 36.432,00 (cálculo próprio). **Não confirmado**: a Receita pode mudar o critério por causa do redutor de R$ 60 mil |
| Prazo DIRPF 2026 (referência) | 23/03 a 29/05/2026. Multa por atraso: 1% ao mês sobre o imposto devido, mínimo R$ 165,74, máximo 20% |
| Prazo DIRPF 2027 | **Não confirmado** |
| Novidades certas na DIRPF 2027 | Redutor anual (art. 11-A); desconto simplificado de R$ 17.640; apuração do IRPFM com abatimento do IRRF de dividendos; redutor do art. 16-B, que a Receita pode calcular na pré-preenchida |
| Simplificada | 20% dos rendimentos tributáveis, teto R$ 17.640. O teto é atingido em R$ 88.200 de rendimento, o mesmo ponto em que o redutor zera. O desconto é "rendimento consumido" e não justifica acréscimo patrimonial. Substitui todas as deduções, inclusive doações incentivadas |
| Completa | Vale quando deduções (INSS, saúde, educação, dependentes, PGBL, pensão, livro-caixa) superarem 20% dos rendimentos ou R$ 17.640 |
| Separada (casal) | Cada um declara seus rendimentos e 50% dos rendimentos de bens comuns (ou um declara 100% dos comuns). Dependente comum só em uma das declarações |
| Conjunta | Um titular declara todos os rendimentos do casal; o outro vira dependente (R$ 2.275,08) |

**Comparação conjunta x separada (cálculo próprio, ano-calendário 2026, desconto simplificado)**

| Casal | Separadas | Conjunta |
|---|---|---|
| R$ 55 mil + R$ 55 mil | R$ 0 | R$ 14.494,34 |
| R$ 80 mil + R$ 40 mil | R$ 5.911,61 | R$ 17.244,34 |

### Jogada legal

Abaixo de R$ 60 mil de rendimento tributável anual o imposto é zero com o desconto simplificado, então a escolha entre completa e simplificada só importa acima disso. Entre R$ 60 mil e R$ 88,2 mil, o redutor ignora as deduções, e a completa só ganha se as deduções passarem de 20% da renda. Acima de R$ 88,2 mil volta a regra antiga: completa quando as deduções superarem R$ 17.640. O programa da Receita compara as duas, mas o planejamento precisa acontecer durante o ano (PGBL em dezembro, concentrar despesas médicas num titular, doações ECA e Idoso só na completa). Sobre o casal: com o redutor por CPF, a declaração conjunta passou a ser quase sempre um erro quando os dois têm renda. Só compensa se um dos cônjuges não tem renda tributável nenhuma e o outro usa a completa, porque aí o cônjuge entra como dependente com suas despesas médicas e de educação. Mesmo nesse caso vale testar, já que o cônjuge sem renda tributável pode simplesmente constar como dependente na declaração separada do outro. Rendimentos de bens comuns (aluguel, aplicações) devem ser repartidos 50/50 para aproveitar dois redutores e duas faixas baixas da tabela. Entregar no prazo é condição para a doação direta na declaração e evita a multa mínima de R$ 165,74 mesmo para quem não tem imposto a pagar.

### Fontes

- Perguntão IRPF 2026, perguntas 001, 012 a 014, 021, 024, 077, 087, 088, 340: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf
- Lei 9.250/1995, arts. 10, 11-A, 13, 14 e 16-A: https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
- Receita, Tributação de 2026 (tabela anual do exercício 2027): https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026

**Confiança: alta** para as regras de 2026 e para a lei aplicável em 2027. **Baixa** para limites e prazos da DIRPF 2027, que ainda não existem.

---

## Nota fora do IR, mas federal e com data em 2027

A partir de 2027 a CBS substitui PIS e Cofins. Pessoa física vira contribuinte do IBS e da CBS no regime regular se, no ano anterior, teve receita de locação acima de R$ 240.000 **e** mais de 3 imóveis alugados; ou vendeu mais de 3 imóveis (com menos de 5 anos de posse); ou vendeu mais de 1 imóvel construído por ela nos últimos 5 anos (LC 214/2025, art. 251, § 1º). Locação tem redução de 70% nas alíquotas e redutor social de R$ 600 por imóvel residencial. Quem tem muitos imóveis alugados na PF precisa olhar isso junto com o relatório de PJ e o de consumo. Fonte: https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp214.htm. **Confiança: alta** para os limites do art. 251; não verifiquei o calendário de transição neste relatório.

---

## Em aberto (conferir antes de afirmar)

1. **Prazo para aprovar lucros de 2025.** A lei diz 31/12/2025. A liminar do STF (ADIs 7.912 e 7.914) estendeu para 31/01/2026, mas o referendo foi interrompido por destaque em 18/02/2026 e não achei julgamento até novembro de 2026. Aprovações feitas entre 01/01 e 31/01/2026 dependem dessa liminar. A Conjur chegou a mencionar "31/12/2026" num texto, que me parece erro; todas as outras fontes dizem 31/01/2026.
2. **Retenção de 10% em dividendos do Simples e do MEI.** Receita diz que vale (P&R, pergunta 10); há decisões judiciais conflitantes em 2026 (liminar contra em fev/2026, SP contra em set/2026, TRF-1 a favor em out/2026, TRF-6 negando liminares). Questão aberta.
3. **Efeito degrau dos R$ 50 mil.** Ação da OAB no STF (abr/2026) sem decisão encontrada. Uma decisão noticiada pela Apet afastou os 10% lineares entre R$ 50 mil e R$ 100 mil para um contribuinte. Só imprensa.
4. **Gatilho do IRPFM.** A lei fala em "soma de todos os rendimentos" acima de R$ 600 mil, mas a alíquota usa o REND já depurado das exclusões. Na prática, quem tem REND abaixo de R$ 600 mil fica com alíquota zero mesmo se disparar o gatilho, mas pode ter obrigação de preencher a apuração. A Receita ainda não publicou a IN da DIRPF 2027 que vai detalhar isso.
5. **Bolsa isenta "não justifica acréscimo patrimonial".** Está no Perguntão (pergunta 287) com base na IN RFB 1.500, art. 11, § 5º, que não consegui abrir (o site normas.receita.fazenda.gov.br é uma aplicação JavaScript que não carregou). A base legal dessa restrição me parece frágil, mas é a posição oficial.
6. **Bolsas CAPES, CNPq e FAPERJ.** Não achei texto oficial que as nomeie como isentas; a conclusão vem do art. 26 e de Soluções de Consulta lidas em portais. Bolsas pagas por fundação de apoio com contrapartida têm sido tratadas como tributáveis (SC Cosit 140/2021, citada em portal).
7. **Limite de renda de pais e avós dependentes em 2026.** Em 2025 foi R$ 28.467,20 (faixa isenta anual daquele ano). Para 2026 deve ser R$ 29.145,60, mas só sai no Perguntão 2027.
8. **Regras da DIRPF 2027** (limite de obrigatoriedade, prazo de entrega, calendário de restituição): não publicadas.
9. **Audiovisual.** Aparece no Perguntão 2026 como incentivo vigente em 2025; não confirmei o prazo final para pessoa física em 2026.
10. **LCD (Letra de Crédito do Desenvolvimento).** Está na lista de exclusões do IRPFM, mas não confirmei se o rendimento é isento ou de alíquota zero para PF (não aparece na lista do Perguntão, pergunta 738).
11. **DeCripto.** Início em jul/2026 e limite de R$ 35 mil/mês para reporte vêm de resumo de escritório (Mattos Filho); não li a IN 2.291/2025.
12. **Projeto de correção anual das tabelas.** O art. 6º da Lei 15.270 mandou o Executivo enviar projeto em 1 ano (até nov/2026). Não achei envio. Existe o PL 5.397/2026 (sen. Esperidião Amin, correção pelo IPCA a partir de 2027), aguardando comissões no Senado em set/2026. Nada aprovado para 2027.
13. **Contribuição máxima do empregado ao INSS.** Fontes secundárias citam R$ 988,07 e R$ 988,09; a página do INSS não traz o valor. Um portal citou teto de R$ 8.537,55, divergente do oficial R$ 8.475,55 (usei o oficial).
