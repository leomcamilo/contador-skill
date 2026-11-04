# Pessoa jurídica: MEI, Simples, Presumido, Real e retirada do sócio

Conferido em 2026-11-04. Confiança: **alta** = fonte oficial lida (Planalto, Perguntão do Simples, Receita); **média** = portal contábil, escritório ou imprensa, ou lei conhecida não relida; **baixa** = não confirmado ou fontes em conflito. A reforma do consumo (CBS/IBS) está em `reforma-tributaria.md`.

Calculadora: `scripts/calc.py regimes` reproduz a tabela de comparação do tópico 3 (os números batem com a conta independente da pesquisa) e acrescenta o IRPFM e o cenário de 2027 (`--ano 2027`).

**Empresa nova em 2026 e 2027.** A janela de opção pelo Simples para 2027 já fechou para empresas existentes, mas empresa inscrita no CNPJ entre o fim de outubro e 31/12/2026 opta na própria inscrição (Res. CGSN 186 e 194/2026, confiança média). Em 2027, empresa em início de atividade segue a regra da Res. CGSN 140, art. 6º: opção em até 30 dias da última inscrição (municipal ou estadual), limitada a 60 dias da abertura do CNPJ (confiança média, conferir no Perguntão antes de abrir).

## Resumo do que mudou em relação ao senso comum

1. O teto do MEI sobe: R$ 110 mil em 2027 e R$ 140 mil a partir de 2028 (LC 238/2026, sancionada em 21/10/2026). O de 2028 depende de a renúncia constar na LOA. Programador continua sem poder ser MEI.
2. Desde 01/01/2026, dividendo acima de R$ 50 mil por mês, de uma mesma PJ para uma mesma PF, tem IRRF de 10% sobre o total, inclusive quando a PJ é do Simples (posição oficial da Receita). Quem tem renda anual abaixo de R$ 600 mil recebe esse IRRF de volta na declaração. Acima de R$ 600 mil entra o IRPFM, de até 10%.
3. A LC 224/2025 subiu a presunção do Lucro Presumido em 10% (32% vira 35,2%), mas só sobre a receita acima de R$ 5 mi/ano (R$ 1,25 mi por trimestre). Também subiu o IRRF do JCP de 15% para 17,5%. O Simples ficou de fora do corte.
4. Para 2027, a opção pelo Simples foi antecipada para setembro/outubro de 2026, e já fechou. Quem optou pelo regime regular de IBS/CBS pode cancelar entre 03/11 e 20/12/2026. A próxima janela do regime regular é março de 2027, para o 2º semestre.
5. O Simples perde o regime de caixa em 2027 e passa a calcular RBT12 e Fator R com um mês de defasagem.
6. Em 2027 o PIS/Cofins acaba e entra a CBS. O TCU calculou 11,3% como alíquota de referência para 2027, e o Senado tem até 15/12/2026 para fixar o valor. Para o Lucro Presumido que vende a consumidor final ou a quem não credita, a carga sobe uns 7,6 pontos percentuais da receita. Para o Simples, nada muda na alíquota do DAS em 2027.
7. Para prestador de serviço com poucos insumos, optar pelo IBS/CBS "por fora" do Simples é quase neutro na conta do cliente B2B. O ganho real vem só dos créditos sobre as compras do próprio prestador. Isso contraria o conselho genérico "vende para empresa, então opta".

## 1. MEI em 2026

### Números

| Item | Regra | Vigência | Base legal | Confiança |
|---|---|---|---|---|
| Teto de faturamento 2026 | R$ 81.000/ano. Abertura no meio do ano: R$ 6.750 por mês de atividade | até 31/12/2026 | LC 123, art. 18-A, §§ 1º e 2º | alta |
| Teto 2027 | R$ 110.000/ano. Abertura em 2027: R$ 9.166,67 por mês | ano-calendário 2027 | LC 238/2026, art. 2º | alta |
| Teto 2028 em diante | R$ 140.000/ano (R$ 11.666,67 por mês). Condicionado à inclusão da renúncia nas LOAs de 2027 a 2029 | efeitos a partir de 01/01/2028 | LC 238/2026, arts. 1º, 3º e 10 | alta |
| Excesso de faturamento | Até 20% acima do teto: desenquadra a partir de 1º de janeiro seguinte e paga a diferença no DAS de janeiro, sem acréscimos. Acima de 20%: desenquadramento retroativo a 1º de janeiro do ano do excesso | vigente | LC 123, art. 18-A, §§ 7º, III, e 10 | alta |
| DAS-MEI 2026 | INSS 5% do salário mínimo (R$ 1.621) = R$ 81,05, mais R$ 1 de ICMS e/ou R$ 5 de ISS. Serviços: R$ 86,05. Comércio/indústria: R$ 82,05. Ambos: R$ 87,05 | 2026 | LC 123, art. 18-A, § 3º, V; Decreto 12.797/2025 (salário mínimo) | média |
| DAS-MEI 2027 com IBS/CBS | Continua valor fixo. Fontes falam em cerca de R$ 1 a mais (CBS R$ 0,994 e IBS R$ 0,006 pela Res. CGSN 190/2026) | 2027 | LC 214/2025; LC 227/2026, art. 168 (repartição do IBS do MEI) | baixa |
| Empregados | Até 2026: 1 empregado com salário mínimo ou piso da categoria. A partir de 2027: até 2 | 01/01/2027 | LC 123, art. 18-C, na redação da LC 238/2026 | alta |
| Custo do MEI que contrata | CPP de 3% sobre o salário, mais a retenção do INSS do empregado. FGTS de 8% (o percentual não está no art. 18-C) | vigente | LC 123, art. 18-C, § 1º | alta (3%); média (FGTS) |
| Atividades vedadas | MEI não pode exercer atividade tributada pelo Anexo V (serviços intelectuais), ter mais de um estabelecimento ou ser sócio de outra empresa | vigente | LC 123, art. 18-A, § 4º | alta |
| Programador | Desenvolvimento de software (6201-5/01, 6202-3/00, 6203-1/00) não consta no Anexo XI da Res. CGSN 140/2018. Há PLP 25/2026 propondo incluir, ainda sem aprovação | vigente | Res. CGSN 140/2018, Anexo XI | média |
| Ocupações de TI permitidas ao MEI | Instrutor de informática (8599-6/03) e técnico de manutenção de computador (9511-8/00), entre outras | vigente | Res. CGSN 140/2018, Anexo XI | média |
| Remissão de dívidas | Perdão integral dos débitos do MEI com a União até 13/10/2026, desde que fique em dia por 6 meses e desista de ações judiciais | 2026/2027 | LC 238/2026, arts. 5º e 6º | alta |
| Nota fiscal B2C | A DASN-SIMEI passa a valer como documento fiscal nas vendas a consumidor PF sem CNPJ | 01/01/2027 | Res. CGSN 195/2026 | média |
| Nanoempreendedor | Pessoa física (não MEI) com receita bruta abaixo de 50% do teto do MEI não é contribuinte de IBS/CBS. Com o teto de R$ 81 mil, o limite é R$ 40.500. Motorista e entregador de aplicativo contam 25% do bruto | a partir de 2027 (IBS/CBS) | LC 214, art. 26, IV e § 10 | alta |
| Nanoempreendedor com o teto novo | Se a regra dos 50% seguir o teto, daria R$ 55 mil em 2027 e R$ 70 mil em 2028. Nenhuma fonte confirma | 2027/2028 | inferência sobre LC 214, art. 26, e LC 238 | não confirmado |

### Jogada legal

Programador e consultor não podem ser MEI, e cadastrar CNAE de "manutenção de computador" para desenvolver software é enquadramento falso: dá exclusão retroativa e cobrança pelo Simples ou pela PF. O MEI só serve ao cliente típico para uma atividade paralela permitida e pequena, como aulas de informática. A partir de 2027, quem fatura pouco como pessoa física fica fora do IBS/CBS como nanoempreendedor. IRPF e INSS continuam devidos, e essa opção só compensa para renda paralela de serviço B2C. Para quem já tem MEI com débito antigo, a LC 238 perdoa tudo até 13/10/2026 se o MEI ficar em dia por seis meses.

### Fontes
- LC 238/2026: https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp238.htm
- LC 123/2006 (compilada): https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp123.htm
- LC 214/2025, art. 26: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
- Votação na Câmara (14/10/2026) e no Senado (15/10/2026), portais: https://www.dgabc.com.br/Noticia/4352780/por-461-a-4-camara-aprova-plp-que-amplia-teto-do-mei-e-perdoa-dividas-do-setor e https://www.congressoemfoco.com.br/noticia/123307/senado-aprova-aumento-do-teto-do-mei-para-r-140-mil-a-partir-de-2028
- DAS 2026 (portal): https://www.opovo.com.br/noticias/economia/2026/01/02/amp/contribuicao-mensal-do-mei-sobe-para-rs-8105-em-2026.html
- Res. CGSN 195/2026 (portal): https://netcpa.com.br/colunas/resolucao-cgsn-no-1952026-altera-a-resolucao-cgsn-no-14018-que-dispoe-sobre-o-regime-especial-unificado-de-arrecadacao-de-tributos-e-contribuicoes-sn/28572
- DAS-MEI 2027 (portal): https://guiatributario.net/2026/08/20/mei-pagara-ibs-e-cbs-a-partir-de-2027/
- Programador e MEI (portal): https://contabilidade.com/blog/programador-pode-ser-mei-descubra-como-abrir-empresa/

---

## 2. Simples Nacional em 2026

### Limites e regras gerais

| Item | Regra | Base legal | Confiança |
|---|---|---|---|
| Teto | R$ 4.800.000/ano no mercado interno, mais R$ 4.800.000/ano de exportação de mercadorias e serviços, contados separadamente | LC 123, art. 3º, II e § 14 | alta |
| Sublimite ISS/ICMS | R$ 3.600.000 (obrigatório no RJ). Acima disso, ISS e ICMS saem do DAS e seguem as regras normais do município/estado | LC 123, art. 19, § 4º | alta |
| Cálculo | Alíquota efetiva = (RBT12 × nominal − parcela a deduzir) / RBT12 | LC 123, art. 18, § 1º-A | alta |
| Mercado interno x exportação | Desde 2016 há duas alíquotas, com RBT12 interna e RBT12 externa separadas para achar a faixa. O Fator R usa as duas somadas | LC 123, art. 3º, § 15; Perguntão 5.24 | alta |
| CPP | Incluída no DAS nos Anexos III e V. No Anexo IV é paga à parte (20%) | Perguntão 5.12 | alta |
| Sistema S | Optante dispensado das demais contribuições da União (Sistema S etc.) | LC 123, art. 13, § 3º | alta |
| Regime de caixa | Permitido só até 31/12/2026. A partir de 2027, só competência | Perguntão 5.7 (reforma) | alta |
| RBT12 e Fator R a partir de 2027 | Passam a usar os 12 meses anteriores ao mês anterior ao do período de apuração (defasagem de um mês) | Perguntão 5.3.2 e 5.11 | alta |
| Opção para 2027 | Janela antecipada: 01/09 a 15/10/2026 (Res. CGSN 194/2026; a Res. 186 previa até 30/09). Empresas abertas de 16/10 a 31/12/2026 optam na inscrição do CNPJ | Res. CGSN 186/2026 e 194/2026 | média (o Perguntão de 09/10/2026 ainda cita 30/09) |
| Cancelamento da opção 2027 | 03/11 a 20/12/2026, irretratável | Res. CGSN 194/2026 | média |

### Anexo III (serviços sem Fator R e serviços com Fator R ≥ 28%)

| Faixa | RBT12 (R$) | Nominal | Parcela a deduzir (R$) | IRPJ | CSLL | Cofins | PIS | CPP | ISS |
|---|---|---|---|---|---|---|---|---|---|
| 1ª | até 180.000 | 6,00% | 0 | 4,00% | 3,50% | 12,82% | 2,78% | 43,40% | 33,50% |
| 2ª | 180.000,01 a 360.000 | 11,20% | 9.360 | 4,00% | 3,50% | 14,05% | 3,05% | 43,40% | 32,00% |
| 3ª | 360.000,01 a 720.000 | 13,50% | 17.640 | 4,00% | 3,50% | 13,64% | 2,96% | 43,40% | 32,50% |
| 4ª | 720.000,01 a 1.800.000 | 16,00% | 35.640 | 4,00% | 3,50% | 13,64% | 2,96% | 43,40% | 32,50% |
| 5ª | 1.800.000,01 a 3.600.000 | 21,00% | 125.640 | 4,00% | 3,50% | 12,82% | 2,78% | 43,40% | 33,50% (*) |
| 6ª | 3.600.000,01 a 4.800.000 | 33,00% | 648.000 | 35,00% | 15,00% | 16,03% | 3,47% | 30,50% | fora do DAS |

(*) ISS efetivo limitado a 5%. O excesso vai para os tributos federais.

### Anexo IV (construção, vigilância, limpeza, advocacia; CPP fora do DAS)

| Faixa | RBT12 (R$) | Nominal | Parcela a deduzir (R$) |
|---|---|---|---|
| 1ª | até 180.000 | 4,50% | 0 |
| 2ª | 180.000,01 a 360.000 | 9,00% | 8.100 |
| 3ª | 360.000,01 a 720.000 | 10,20% | 12.420 |
| 4ª | 720.000,01 a 1.800.000 | 14,00% | 39.780 |
| 5ª | 1.800.000,01 a 3.600.000 | 22,00% | 183.780 |
| 6ª | 3.600.000,01 a 4.800.000 | 33,00% | 828.000 |

### Anexo V (serviços com Fator R < 28%)

| Faixa | RBT12 (R$) | Nominal | Parcela a deduzir (R$) | IRPJ | CSLL | Cofins | PIS | CPP | ISS |
|---|---|---|---|---|---|---|---|---|---|
| 1ª | até 180.000 | 15,50% | 0 | 25,00% | 15,00% | 14,10% | 3,05% | 28,85% | 14,00% |
| 2ª | 180.000,01 a 360.000 | 18,00% | 4.500 | 23,00% | 15,00% | 14,10% | 3,05% | 27,85% | 17,00% |
| 3ª | 360.000,01 a 720.000 | 19,50% | 9.900 | 24,00% | 15,00% | 14,92% | 3,23% | 23,85% | 19,00% |
| 4ª | 720.000,01 a 1.800.000 | 20,50% | 17.100 | 21,00% | 15,00% | 15,74% | 3,41% | 23,85% | 21,00% |
| 5ª | 1.800.000,01 a 3.600.000 | 23,00% | 62.100 | 23,00% | 12,50% | 14,10% | 3,05% | 23,85% | 23,50% |
| 6ª | 3.600.000,01 a 4.800.000 | 30,50% | 540.000 | 35,00% | 15,50% | 16,44% | 3,56% | 29,50% | fora do DAS |

Confiança das três tabelas: alta (LC 155/2016, anexos com vigência desde 01/01/2018, no planalto).

Para 2027 e 2028, a LC 227/2026 trocou PIS e Cofins por CBS e IBS na repartição do Anexo III, sem mexer nas alíquotas nominais. Na 1ª faixa ficou IRPJ 4%, CSLL 3,5%, CBS 15,43%, CPP 43,4%, ISS 33,5%, IBS 0,17%. Na 2ª faixa, CBS 16,91% e IBS 0,19%. A partir de 2029 o IBS cresce dentro do DAS enquanto o teto do ISS cai: 4,5% em 2029, 4% em 2030, 3,5% em 2031, 3% em 2032. A repartição do Anexo V para 2027 não aparece no trecho da LC 227 que li (não confirmado). Confiança: alta para o Anexo III.

### Fator R

| Item | Regra | Base legal | Confiança |
|---|---|---|---|
| Fórmula | r = FS12 / RBT12. Se r ≥ 0,28, Anexo III. Se r < 0,28, Anexo V | LC 123, art. 18, §§ 5º-J e 5º-M | alta |
| O que entra na FS12 | Salários, pró-labore, pagamentos a autônomos, 13º, CPP efetivamente recolhida (o Perguntão diz "inclusive a recolhida dentro do Simples") e FGTS | Res. CGSN 140, art. 26; Perguntão 5.11 | alta |
| O que não entra | Distribuição de lucros, aluguel, bolsa de estagiário, pagamento a MEI | Perguntão 5.11 | alta |
| Pró-labore mínimo para 28% (sócio único, sem empregados) | 0,28 × receita mensal. Exemplos: R$ 2.800 para R$ 10 mil/mês, R$ 8.400 para R$ 30 mil/mês, R$ 28.000 para R$ 100 mil/mês | cálculo próprio | alta (a conta) |
| Atividades sujeitas ao Fator R | Elaboração de programas, inclusive jogos, feita no estabelecimento da optante; licenciamento ou cessão de uso de software; criação e manutenção de sites; engenharia, pesquisa, design; consultoria, gestão, auditoria; intermediação de negócios; outros serviços intelectuais | Res. CGSN 140, art. 25, § 1º, V; Perguntão 5.2 | alta |
| Serviços no Anexo III sem Fator R | Cursos gerenciais e escolas livres; instalação, reparo e manutenção em geral; outros serviços não intelectuais | Res. CGSN 140, art. 25, § 1º, III; Perguntão 5.2 | alta |

### CNAEs típicos de TI

A lei não manda pelo CNAE, e sim pela descrição da atividade (art. 25 da Res. CGSN 140). A tabela abaixo é o enquadramento usual.

| CNAE | Descrição | Anexo usual | Confiança |
|---|---|---|---|
| 6201-5/01 | Desenvolvimento de programas sob encomenda | III ou V (Fator R) | alta (Perguntão: elaboração de programas) |
| 6202-3/00 | Desenvolvimento e licenciamento de programas customizáveis | III ou V (Fator R) | alta (licenciamento está na lista) |
| 6203-1/00 | Desenvolvimento e licenciamento de programas não customizáveis | III ou V (Fator R) | alta |
| 6204-0/00 | Consultoria em TI | III ou V (Fator R), por ser consultoria | média |
| 6209-1/00 | Suporte técnico, manutenção e outros serviços em TI | Divergente: portais dizem Fator R; instalação e manutenção pura iria para o Anexo III sem Fator R | baixa |
| 6311-9/00 | Tratamento de dados, provedores de aplicação e hospedagem | Anexo III sem Fator R (serviço não intelectual) na leitura mais comum | média |
| 7020-4/00 | Consultoria em gestão empresarial | III ou V (Fator R) | alta (Perguntão: consultoria, gestão) |
| 8599-6/04 | Treinamento em desenvolvimento profissional e gerencial | Anexo III sem Fator R (cursos gerenciais) | alta (Perguntão) |
| 7490-1/04 | Intermediação e agenciamento de serviços e negócios | III ou V (Fator R) | alta (Perguntão: intermediação) |

SaaS: entre "licenciamento ou cessão de uso" (Fator R) e "provedor de aplicação" (6311-9/00, Anexo III direto) não achei posição oficial recente para o Simples. Ver pontos em aberto.

### Exportação de serviços no Simples

| Item | Regra | Base legal | Confiança |
|---|---|---|---|
| O que é exportação | Serviço a PF ou PJ residente no exterior, com ingresso de divisas (ou recursos mantidos lá na forma da Lei 11.371/2006). Não conta como exportação o serviço desenvolvido no Brasil cujo resultado aqui se verifique | Res. CGSN 140, art. 25, §§ 4º e 4º-A; Perguntão 2.19 | alta |
| Efeito no DAS | Receita segregada como exportação no PGDAS-D. Saem as parcelas de Cofins, PIS, ISS (e ICMS/IPI, quando houver). Ficam IRPJ, CSLL e CPP | LC 123, art. 18, §§ 4º-A, IV, e 14 | alta |
| Exemplo Anexo III, 1ª faixa | 6% × (1 − 12,82% − 2,78% − 33,5%) = 3,05% da receita exportada | cálculo próprio | alta |
| Exemplo Anexo V, 1ª faixa | 15,5% × (1 − 14,10% − 3,05% − 14%) = 10,67% | cálculo próprio | alta |
| Exemplo Anexo III, 4ª faixa | 13,03% × (1 − 13,64% − 2,96% − 32,5%) = 6,63% | cálculo próprio | alta |
| A partir de 2027 | Exportação é imune a IBS e CBS (EC 132). Não li a redação nova do art. 18, § 14, com CBS/IBS no lugar de PIS/Cofins | EC 132; LC 214, art. 80 | média |

### Jogada legal

O Fator R é a principal alavanca de quem presta serviço intelectual no Simples. Até uns R$ 60 mil por mês de receita (RBT12 perto de R$ 720 mil), pagar pró-labore de 28% e cair no Anexo III custa menos, somando DAS, INSS e IRRF do pró-labore, do que ficar no Anexo V com pró-labore de um salário mínimo. Acima disso o Anexo V empata ou ganha, a não ser que o sócio passe de R$ 600 mil de renda no ano e pague IRPFM. Nesse caso o IR do pró-labore abate o IRPFM e o Anexo III volta a ganhar (ver tópico 3). Empregados reais também entram na folha e ajudam a bater os 28%.

Exportação precisa ser segregada no PGDAS-D todo mês. Muita gente paga PIS, Cofins e ISS sobre receita do exterior por erro de declaração, e isso tem restituição dentro de 5 anos. O limite e as faixas da exportação são separados dos do mercado interno, então uma empresa pode faturar R$ 4,8 mi aqui e mais R$ 4,8 mi lá fora sem sair do Simples. Para o ISS, o cuidado é com o "resultado verificado no Brasil": software desenvolvido aqui para cliente estrangeiro que o usa lá fora é exportação. Serviço cujo benefício fica no Brasil não é.

### Fontes
- Perguntão do Simples, atualizado parcialmente em 09/10/2026: https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf
- LC 155/2016 (anexos): https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp155.htm
- LC 123/2006: https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp123.htm
- LC 227/2026, texto atualizado da Câmara (arts. 168, 169 e anexos XX e XXI): https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-227-13-janeiro-2026-798657-normaatualizada-pl.pdf
- Res. CGSN 186/2026 (texto em portal): https://www.normaslegais.com.br/legislacao/resolucao-cgsn-186-2026.htm
- Res. CGSN 194/2026 (portal): https://netcpa.com.br/colunas/resolucao-cgsn-no-1942026-altera-a-resolucao-cgsn-no-18626-que-dispoe-sobre-os-prazos-e-condicoes-para-o-exercicio-de-opcao-pelo-simples-nacional/28455

---

## 3. Lucro Presumido em 2026 e comparação de carga

### Números

| Item | Regra | Vigência | Base legal | Confiança |
|---|---|---|---|---|
| Presunção de serviços (IRPJ) | 32% da receita bruta | vigente | Lei 9.249, art. 15, § 1º, III, "a" | alta |
| Presunção de serviços (CSLL) | 32% | vigente | Lei 9.249, art. 20, I | alta |
| IRPJ | 15% da base, mais adicional de 10% sobre o que passar de R$ 20 mil por mês (R$ 60 mil por trimestre) | vigente | Lei 9.249, art. 3º, § 1º | alta |
| CSLL | 9% da base | vigente | Lei 7.689/1988 | média |
| PIS/Cofins cumulativos | 0,65% + 3% = 3,65% da receita (até 31/12/2026) | extintos em 2027 | Lei 9.718/1998; EC 132, ADCT art. 126 | média (alíquotas); alta (extinção) |
| Carga federal sem adicional | 4,8% + 2,88% + 3,65% = 11,33% da receita | 2026 | soma das linhas acima | alta (a conta) |
| Prestador pequeno | Presunção de 16% só para o IRPJ, para prestadora de serviços com receita anual de até R$ 120 mil, exceto profissão regulamentada | vigente | Lei 9.250/1995, art. 40 | média |
| Teto do regime | R$ 78 milhões/ano | vigente | Lei 9.718, art. 13 | média |
| LC 224/2025: presunção | Acréscimo de 10% nos percentuais (32% vira 35,2%; 8% vira 8,8%) só sobre a parcela da receita acima de R$ 5 mi/ano, apurada por trimestre (R$ 1,25 mi por trimestre), com ajuste nos períodos seguintes. Receita financeira e ganho de capital não entram na conta do limite | IRPJ desde 01/01/2026; CSLL desde 01/04/2026 (limite de R$ 3,75 mi para a CSLL em 2026) | LC 224, art. 4º, §§ 4º, VII, e 5º; P&R Receita v5 (30/07/2026), perguntas 11 a 14 | alta |
| LC 224/2025: JCP | IRRF sobre JCP de 15% para 17,5% | 01/01/2026 | LC 224, art. 8º (Lei 9.249, art. 9º, § 2º) | alta |
| LC 224/2025: quem fica fora | Simples Nacional, ZFM, Prouni, MCMV, CPRB, política de TIC e semicondutores e outras exceções | 2026 | LC 224, art. 4º, § 8º | alta |
| LC 224/2025: CSLL financeira | Instituições de pagamento: 12% até 2027 e 15% a partir de 2028 | 2026 a 2028 | LC 224, art. 7º | alta |
| Disputa judicial do acréscimo | Liminares concedidas (1ª Vara Federal de Resende, 27/01/2026, e TRFs). Status atual não confirmado | 2026 | ações individuais | baixa |
| Retenções na fonte quando o cliente é PJ | IRRF 1,5% e CSRF 4,65% em serviços profissionais. São antecipação, não custo extra | vigente | Lei 10.833, art. 30; RIR | média |

O acréscimo da LC 224 só pega quem fatura mais de R$ 416.667 por mês. Nenhum cenário da tabela abaixo chega lá.

### Comparação de carga: premissas

- Um sócio, sem empregados, serviço de TI sujeito ao Fator R, receita mensal constante (RBT12 = 12 × receita), só mercado interno, sem outras despesas.
- **Simples Anexo III**: pró-labore de 28% da receita (o mínimo para o Fator R). Custos: DAS, INSS de 11% do sócio (limitado ao teto de R$ 8.475,55, ou seja, no máximo R$ 932,31) e IRRF do pró-labore pela tabela mensal 2026 com a redução da Lei 15.270. A CPP está dentro do DAS.
- **Simples Anexo V**: pró-labore de 1 salário mínimo (R$ 1.621). INSS do sócio de R$ 178,31, sem IR.
- **Presumido**: pró-labore de 1 salário mínimo. INSS do sócio de R$ 178,31 mais 20% patronal (R$ 324,20), sem IR. Tributos: IRPJ, adicional, CSLL, PIS, Cofins e ISS de 2% ou 5%.
- No Simples, o ISS sai da repartição do anexo, não da alíquota do município. Por isso o ISS de 2% ou 5% só muda o Presumido.
- IRRF mensal: base = pró-labore − max(INSS, desconto simplificado de R$ 607,20). Tabela: até R$ 2.428,80 isento; 7,5% (−182,16); 15% (−394,16); 22,5% (−675,49); 27,5% (−908,73). Redução da Lei 15.270: zera até R$ 5.000; entre R$ 5.000,01 e R$ 7.350 abate R$ 978,62 − 0,133145 × rendimento.

### A conta, exemplo com R$ 30 mil por mês

**Simples Anexo III.** RBT12 = R$ 360.000, 2ª faixa. Alíquota efetiva = (360.000 × 11,2% − 9.360) / 360.000 = 8,60%. DAS = R$ 2.580. Pró-labore = 28% × 30.000 = R$ 8.400. INSS = 11% × 8.400 = R$ 924. Base do IR = 8.400 − 924 = 7.476. IR = 7.476 × 27,5% − 908,73 = R$ 1.147 (sem redução, porque o rendimento passa de R$ 7.350). Total = 2.580 + 924 + 1.147 = R$ 4.651, ou 15,50%.

**Simples Anexo V.** Efetiva = (360.000 × 18% − 4.500) / 360.000 = 16,75%. DAS = R$ 5.025. INSS sobre o salário mínimo = R$ 178. Total = R$ 5.203, ou 17,34%.

**Presumido, ISS 2%.** Base = 32% × 30.000 = 9.600. IRPJ = 15% × 9.600 = 1.440 (sem adicional, base abaixo de R$ 20 mil). CSLL = 9% × 9.600 = 864. PIS = 195. Cofins = 900. ISS = 600. Tributos da PJ = R$ 3.999. INSS sócio + patronal sobre o salário mínimo = R$ 503. Total = R$ 4.502, ou 15,01%.

### Tabela de comparação (2026)

| Receita/mês | Regime | Alíq. efetiva PJ | Tributos PJ/mês | Pró-labore | INSS (sócio + patronal) | IRRF pró-labore | Total/mês | Carga |
|---|---|---|---|---|---|---|---|---|
| 10.000 | Simples Anexo III (faixa 1) | 6,00% | 600 | 2.800 | 308 | 0 | 908 | **9,08%** |
| 10.000 | Simples Anexo V (faixa 1) | 15,50% | 1.550 | 1.621 | 178 | 0 | 1.728 | 17,28% |
| 10.000 | Presumido, ISS 2% | 13,33% | 1.333 | 1.621 | 503 | 0 | 1.836 | 18,36% |
| 10.000 | Presumido, ISS 5% | 16,33% | 1.633 | 1.621 | 503 | 0 | 2.136 | 21,36% |
| 30.000 | Simples Anexo III (faixa 2) | 8,60% | 2.580 | 8.400 | 924 | 1.147 | 4.651 | 15,50% |
| 30.000 | Simples Anexo V (faixa 2) | 16,75% | 5.025 | 1.621 | 178 | 0 | 5.203 | 17,34% |
| 30.000 | Presumido, ISS 2% | 13,33% | 3.999 | 1.621 | 503 | 0 | 4.502 | **15,01%** |
| 30.000 | Presumido, ISS 5% | 16,33% | 4.899 | 1.621 | 503 | 0 | 5.402 | 18,01% |
| 60.000 | Simples Anexo III (faixa 3) | 11,05% | 6.630 | 16.800 | 932 | 3.455 | 11.017 | 18,36% |
| 60.000 | Simples Anexo V (faixa 3) | 18,13% | 10.875 | 1.621 | 178 | 0 | 11.053 | 18,42% |
| 60.000 | Presumido, ISS 2% | 13,33% | 7.998 | 1.621 | 503 | 0 | 8.501 | **14,17%** |
| 60.000 | Presumido, ISS 5% | 16,33% | 9.798 | 1.621 | 503 | 0 | 10.301 | 17,17% |
| 100.000 | Simples Anexo III (faixa 4) | 13,03% | 13.030 | 28.000 | 932 | 6.535 | 20.497 | 20,50% |
| 100.000 | Simples Anexo V (faixa 4) | 19,08% | 19.075 | 1.621 | 178 | 0 | 19.253 | 19,25% |
| 100.000 | Presumido, ISS 2% | 14,53% | 14.530 | 1.621 | 503 | 0 | 15.033 | **15,03%** |
| 100.000 | Presumido, ISS 5% | 17,53% | 17.530 | 1.621 | 503 | 0 | 18.033 | 18,03% |
| 200.000 | Simples Anexo III (faixa 5) | 15,77% | 31.530 | 56.000 | 932 | 14.235 | 46.697 | 23,35% |
| 200.000 | Simples Anexo V (faixa 5) | 20,41% | 40.825 | 1.621 | 178 | 0 | 41.003 | 20,50% |
| 200.000 | Presumido, ISS 2% | 15,53% | 31.060 | 1.621 | 503 | 0 | 31.563 | **15,78%** |
| 200.000 | Presumido, ISS 5% | 18,53% | 37.060 | 1.621 | 503 | 0 | 37.563 | 18,78% |

Nos cenários de R$ 100 mil e R$ 200 mil, o Presumido paga adicional de IRPJ: 10% × (32.000 − 20.000) = R$ 1.200 e 10% × (64.000 − 20.000) = R$ 4.400 por mês. No Simples de R$ 200 mil, o ISS do Anexo III bate no teto de 5% e o excesso vai para os federais, sem mudar o total.

### O mesmo comparativo com o IRPFM (renda anual do sócio acima de R$ 600 mil)

Premissas extras: o sócio não tem outra renda, todo o lucro é distribuído, e a alíquota efetiva da PJ para o redutor é (IRPJ + CSLL) / lucro contábil simplificado (receita − folha), que é o método do art. 16-B, § 6º, para quem não está no Lucro Real. É uma estimativa.

| Receita/mês | Regime | Dividendos/ano | IRPFM após redutor/ano | Carga total com IRPFM |
|---|---|---|---|---|
| 60.000 | Simples Anexo III | 438.840 | 0 | 18,36% |
| 60.000 | Simples Anexo V | 570.048 | 0 | 18,42% |
| 60.000 | Presumido, ISS 2% | 600.682 | 2.081 | 14,46% |
| 60.000 | Presumido, ISS 5% | 579.082 | 0 | 17,17% |
| 100.000 | Simples Anexo III | 707.640 | 0 | **20,50%** |
| 100.000 | Simples Anexo V | 951.648 | 60.063 | 24,26% |
| 100.000 | Presumido, ISS 2% | 1.002.298 | 71.820 | 21,02% |
| 100.000 | Presumido, ISS 5% | 966.298 | 63.375 | 23,31% |
| 200.000 | Simples Anexo III | 1.349.640 | 31.345 | 24,65% |
| 200.000 | Simples Anexo V | 1.890.648 | 191.010 | 28,46% |
| 200.000 | Presumido, ISS 2% | 2.003.938 | 202.339 | **24,21%** |
| 200.000 | Presumido, ISS 5% | 1.931.938 | 195.139 | 26,91% |

No Anexo III, o pró-labore alto já paga IR pela tabela progressiva, e esse IR abate o IRPFM. Por isso o Anexo III empata ou ganha do Presumido quando a renda passa de R$ 1 milhão por ano. O redutor quase nunca aparece: a carga da PJ de serviço fica em torno de 9% do lucro, longe dos 34%.

### Projeção 2027 (CBS no lugar de PIS/Cofins)

Premissas: CBS de 11,2% (os 11,3% do TCU menos 0,1 p.p. do ADCT, art. 127; o Senado ainda não fixou), IBS de 0,1%, prestador sem insumos creditáveis, ISS mantido, nominais do Simples iguais. Fração de CBS/IBS no DAS: Anexo III pela tabela da LC 227. No Anexo V, assumi igual à antiga fração de PIS+Cofins (não confirmado).

| Receita/mês | Regime | Carga para cliente consumidor final (B2C) | Custo não recuperável quando o cliente credita (B2B) |
|---|---|---|---|
| 30.000 | Simples Anexo III (no DAS) | 15,50% | 14,03% |
| 30.000 | Simples Anexo V (no DAS) | 17,34% | 14,47% |
| 30.000 | Presumido, ISS 2% | 22,66% | 11,36% |
| 30.000 | Presumido, ISS 5% | 25,66% | 14,36% |
| 100.000 | Simples Anexo III (no DAS) | 20,50% | 18,33% |
| 100.000 | Simples Anexo V (no DAS) | 19,25% | 15,60% |
| 100.000 | Presumido, ISS 2% | 22,68% | 11,38% |
| 100.000 | Presumido, ISS 5% | 25,68% | 14,38% |

### Jogada legal

Em 2026, com ISS de 2%, o Presumido ganha do Simples a partir de uns R$ 30 mil por mês. Com ISS de 5%, só ganha a partir de uns R$ 100 mil. Abaixo disso, o Simples Anexo III com Fator R é o mais barato. A conta não inclui o custo maior de contabilidade e de obrigações do Presumido (ECD, ECF, EFD-Contribuições, DCTFWeb), que pesa mais no faturamento baixo.

Em 2027 a conta se divide pelo tipo de cliente. Quem vende a consumidor final, ou a empresa do Simples que não credita, perde muito no Presumido, porque a CBS de cerca de 11% substitui os 3,65% de PIS/Cofins. Para esse cliente, o Simples passa a ser a escolha natural em quase todas as faixas. Quem vende a empresas do regime regular repassa a CBS como crédito, e o Presumido segue competitivo. A decisão de regime para 2027 precisa partir da carteira de clientes, não só do faturamento.

Acima de R$ 600 mil de renda anual do sócio, o IRPFM entra na conta. O que importa então é o total PJ + PF, e o pró-labore alto do Anexo III deixa de ser custo puro.

### Fontes
- Lei 9.249/1995 (arts. 3º, 9º, 10, 15, 20): https://www.planalto.gov.br/ccivil_03/leis/l9249.htm
- LC 224/2025: https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp224.htm
- Receita, P&R Redução dos incentivos e benefícios tributários v5, 30/07/2026: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/beneficios-fiscais/perguntas-e-respostas-reducao-dos-incentivos-e-beneficios-tributarios-v5-final.pdf
- Liminares contra a LC 224 (portal): https://www.barbieriadvogados.com/lucro-presumido-liminar-2/
- Lei 15.270/2025 (IRPFM, art. 16-B): https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm
- Teto INSS 2026, Portaria Interministerial MPS/MF 13/2026 (portal): https://www.barbieriadvogados.com/teto-do-inss-2026-valor-tabela-historica/
- Tabela IRRF 2026 e redução (portal): https://www.coad.com.br/home/noticias-detalhe/135216/receita-federal-orienta-fontes-pagadoras-e-contribuintes-a-calcular-a-reducao-do-imposto-de-renda-a-partir-de-janeiro2026

---

## 4. Lucro Real, Lei do Bem e JCP

### Números

| Item | Regra | Base legal | Confiança |
|---|---|---|---|
| IRPJ e CSLL | 15% + adicional de 10% (acima de R$ 20 mil/mês) e 9% sobre o lucro real ajustado | Lei 9.249, art. 3º | alta |
| Ponto de equilíbrio do IR (serviços) | Presumido cobra 32% × 24% = 7,68% da receita (sem adicional). O Real cobra 24% do lucro. Empate com margem tributável de 32%. Com adicional nos dois lados, o empate continua perto de 32% | cálculo próprio | alta (a conta) |
| PIS/Cofins não cumulativos (2026) | 1,65% + 7,6% = 9,25%, com créditos sobre insumos. Folha não gera crédito | Leis 10.637/2002 e 10.833/2003 | média |
| Ponto de equilíbrio do PIS/Cofins (2026) | O Real só empata com o Presumido (3,65%) se os insumos creditáveis passarem de 60,5% da receita: (9,25 − 3,65) / 9,25 | cálculo próprio | alta (a conta) |
| Prejuízo fiscal | Compensação limitada a 30% do lucro de cada período | Lei 9.065/1995, art. 15 | média |
| Lei do Bem: exclusão adicional | Até 60% dos dispêndios com P&D na base do IRPJ e da CSLL. Até 80% conforme o aumento de pesquisadores contratados (70% com aumento de até 5%, 80% acima de 5%). Mais até 20% para P&D com patente concedida ou cultivar registrado | Lei 11.196, art. 19, caput e §§ 1º e 3º | alta |
| Lei do Bem: limite | A exclusão fica limitada ao lucro real e à base da CSLL antes dela. O excesso não passa para os anos seguintes | Lei 11.196, art. 19, § 5º | alta |
| Lei do Bem: outros incentivos | Depreciação integral de equipamentos novos de P&D no ano da compra, amortização acelerada de intangíveis de P&D, redução de 50% do IPI desses equipamentos | Lei 11.196, art. 17 | alta |
| Lei do Bem: regime | Só para o Lucro Real. Exige prestação de contas anual ao MCTI (FORMP&D, aberto em 17/06/2026) | Lei 11.196; MCTI | alta (regime); média (prazo) |
| Lei do Bem e LC 224 | Divergência. Um portal diz que caiu 10% (60% vira 54%; 80% vira 72%). Outros dizem que o anexo da IN RFB 2.305/2025 (substituído pela IN 2.307/2026) preservou a Lei do Bem | IN RFB 2.305/2025 e 2.307/2026 | baixa |
| JCP: limite | Variação pro rata dia da TJLP sobre as contas do PL (capital integralizado, reservas de capital, reservas de lucros exceto incentivo fiscal, ações em tesouraria, lucros/prejuízos acumulados, com os ajustes da Lei 14.789/2023). O pagamento exige lucro do período ou lucros acumulados e reservas de pelo menos duas vezes o valor dos juros | Lei 9.249, art. 9º, caput, §§ 1º e 8º | alta |
| JCP: IRRF | 17,5% desde 01/01/2026 | Lei 9.249, art. 9º, § 2º (redação da LC 224) | alta |
| JCP: dedutível | Só no Lucro Real, contra IRPJ e CSLL (até 34%) | Lei 9.249, art. 9º | alta |
| TJLP do 4º trimestre de 2026 | não confirmado | Banco Central | não confirmado |

### Jogada legal

Para empresa de TI com folha alta e poucos insumos, o Lucro Real perde em 2026 por causa do PIS/Cofins não cumulativo. Ele só compensa em três casos: margem tributável bem abaixo de 32% (empresa em crescimento queimando caixa ou com prejuízo), projeto de P&D que use a Lei do Bem, ou JCP relevante. O JCP economiza até 34% na PJ e paga 17,5% de IRRF, um ganho líquido de até 16,5 pontos sobre o valor pago, limitado pela TJLP sobre o patrimônio líquido. Só funciona com PL grande.

Em 2027 o PIS/Cofins acaba e a CBS é a mesma no Real e no Presumido. Sobra apenas a comparação de IRPJ e CSLL, e o Real fica mais atraente para quem tem margem abaixo de 32% ou gasta com P&D. Startups de IA com prejuízo nos primeiros anos devem refazer essa conta para 2027. A Lei do Bem não aproveita prejuízo: a exclusão morre se não houver lucro no ano.

### Fontes
- Lei 11.196/2005: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11196.htm
- Lei 9.249/1995: https://www.planalto.gov.br/ccivil_03/leis/l9249.htm
- Lei do Bem preservada pela IN 2.305 (portal): https://tagdlaw.com.br/desafios-trazidos-pela-lc-224-e-a-lei-do-bem-como-alternativa-para-frear-aumento-da-carga-tributaria/
- Alerta EY sobre IN 2.305 e Lei do Bem: https://www.ey.com/content/dam/ey-unified-site/ey-com/pt-br/campaigns/tax/documents/ey-brasil-alert-decreto-12808-in-rfb2305-01-06-2026.pdf
- IN 2.307/2026 substituiu o anexo (portal): https://www.contabeis.com.br/noticias/75251/rfb-atualiza-quais-beneficios-nao-serao-atingidos-por-reducao-linear-de-incentivos/
- FORMP&D 2026 (portal): https://tagdlaw.com.br/mcti-abre-prazo-para-preenchimento-do-formpd-2026-por-beneficiarias-da-lei-do-bem/

---

## 5. Retirada de dinheiro da empresa em 2026

### Números

| Item | Regra | Vigência | Base legal | Confiança |
|---|---|---|---|---|
| INSS do sócio sobre pró-labore | 11% retido pela empresa, até o teto de R$ 8.475,55 (máximo R$ 932,31/mês) | 2026 | Lei 8.212/1991; Lei 10.666/2003, art. 4º | média |
| INSS patronal sobre pró-labore | 20% fora do Simples (Presumido e Real). No Simples Anexos III e V, a CPP está dentro do DAS e não há 20% extra. No Anexo IV paga à parte | vigente | Lei 8.212, art. 22, III; Perguntão 5.12 | alta (Simples); média (20%) |
| IRRF do pró-labore | Tabela progressiva mensal com a redução da Lei 15.270 (zera até R$ 5 mil; redução decrescente até R$ 7.350) | desde 01/2026 | Lei 15.270, art. 3º-A | alta |
| Dividendos isentos (regra geral) | Isentos na declaração de ajuste, sem IRRF até R$ 50 mil por mês por PJ por PF | 2026 | Lei 9.249, art. 10 (redação da Lei 15.270) | alta |
| IRRF sobre dividendos | 10% sobre o total pago no mês (não só sobre o excedente) quando uma mesma PJ paga mais de R$ 50 mil a uma mesma PF residente. Sem deduções. Pagamentos múltiplos no mês são somados. DARF código 1841 | desde 01/01/2026 | Lei 9.250, art. 6º-A; P&R Receita (19/12/2025), perguntas 4 a 11 | alta |
| Simples Nacional | A Receita entende que a retenção também vale para dividendos de empresa do Simples, e que a isenção do art. 14 da LC 123 cede à Lei 15.270. Tributaristas contestam (a matéria seria de lei complementar) | 2026 | P&R Receita, pergunta 10 | alta (posição da Receita); baixa (desfecho) |
| Restituição | Se a renda anual total for menor que R$ 600 mil, o IRRF de 10% sobre dividendos pode ser restituído na declaração | ano-calendário 2026 | P&R Receita, pergunta 4 | alta |
| IRPFM | Renda anual total acima de R$ 600 mil: alíquota de (renda/60.000 − 10)%, chegando a 10% em R$ 1,2 milhão. Entra tudo, inclusive dividendos e rendimentos isentos, com exclusões como poupança, LCI/LCA, FII com 100 cotistas e ganho de capital fora de bolsa. Abate IR já pago e IRRF | ano-calendário 2026 (declaração de 2027) | Lei 9.250, art. 16-A | alta |
| Redutor do IRPFM | Se carga efetiva da PJ + carga efetiva do IRPFM passar de 34% (regra geral), devolve o excesso. Quem não está no Lucro Real pode calcular o lucro contábil de forma simplificada (receita menos folha, CMV, aluguéis, juros e depreciação) | ano-calendário 2026 | Lei 9.250, art. 16-B, §§ 1º a 6º | alta |
| Transição de lucros até 2025 | Sem IRRF e fora do IRPFM se apurados até 2025, com distribuição aprovada até 31/12/2025 e pagos conforme o ato de aprovação até 2028. O STF (liminar do min. Nunes Marques) estendeu a aprovação até 31/01/2026. Referendo do plenário não confirmado | prazo encerrado | Lei 15.270; STF, ADIs 7.912, 7.914 e 7.917 | alta (lei); média (STF) |
| Capitalização de lucros | Incorporar lucro ao capital conta como "emprego" e sofre IRRF de 10% se passar de R$ 50 mil no mês | 2026 | P&R Receita, perguntas 12 a 14 | alta |
| Limite isento sem contabilidade (Simples) | Presunção do art. 15 da Lei 9.249 (32% para serviços) sobre a receita, menos o DAS do período. Sem limite se a empresa mantém escrituração contábil que mostre lucro maior | vigente | LC 123, art. 14, §§ 1º e 2º | alta |
| Limite isento sem contabilidade (Presumido) | Base presumida menos IRPJ, CSLL, PIS e Cofins. Sem limite com escrituração contábil | vigente | IN RFB 1.700/2017, art. 238 | média |
| Distribuição desproporcional | Permitida em sociedade limitada se o contrato social prever | vigente | Código Civil, art. 1.007 | média |
| Dividendos ao exterior | IRRF de 10% (sócio não residente) | desde 01/01/2026 | Lei 9.249, art. 10, § 4º | alta |
| Informação na EFD-Reinf | Dividendos pagos, mesmo isentos, vão no evento R-4010 (natureza 12001; código de isenção 12 criado pela NT 02/2026, com efeito retroativo a 01/01/2026) | 2026 | NT EFD-Reinf 02/2026 | média |

### Exemplo do limite sem contabilidade, R$ 30 mil/mês

| Regime | Limite isento sem contabilidade | Lucro que sobra para distribuir |
|---|---|---|
| Simples Anexo III | 9.600 − 2.580 = R$ 7.020 | 30.000 − 2.580 − 8.400 = R$ 19.020 |
| Simples Anexo V | 9.600 − 5.025 = R$ 4.575 | 30.000 − 5.025 − 1.621 = R$ 23.354 |
| Presumido, ISS 2% | 9.600 − (1.440 + 864 + 195 + 900) = R$ 6.201 | 30.000 − 3.999 − 1.621 − 324 = R$ 24.056 |

### Jogada legal

O limite de R$ 50 mil é por mês, por PJ e por PF. Distribuir até R$ 50 mil por mês, em vez de um valor grande de uma vez, evita o IRRF de 10%. Para quem fica abaixo de R$ 600 mil de renda no ano, a retenção só adianta caixa e volta na restituição, mas mesmo assim vale escalonar. Acima de R$ 600 mil o IRPFM pega no ajuste anual, e escalonar só muda o momento do pagamento.

Dois sócios de verdade (por exemplo, o casal, com participação real e contrato social prevendo a divisão) dividem a renda entre duas pessoas físicas. Cada uma pode ficar abaixo de R$ 600 mil e escapar do IRPFM. A participação precisa ser real: sócio de fachada ou empresa criada só para fatiar pagamentos abaixo de R$ 50 mil é planejamento abusivo e a Receita desconsidera.

Sem escrituração contábil, quase nenhuma empresa de serviço consegue distribuir todo o lucro isento, porque o limite presumido fica bem abaixo do lucro real (ver tabela acima). O excedente vira rendimento tributável do sócio. Manter contabilidade completa com ECD é o que libera a distribuição integral.

Pró-labore de zero com tudo em dividendos dá margem para a Receita requalificar parte dos dividendos como remuneração e cobrar INSS. Não achei norma recente da Receita sobre isso nesta pesquisa. O mínimo prudente é um salário mínimo, e no Anexo III o pró-labore de 28% já resolve.

### Fontes
- Lei 15.270/2025: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm
- Receita, P&R Tributação de altas rendas, 19/12/2025: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirf/manual_padrao_rfb_per_tributacao_cotin_v-19-12-2025.pdf
- LC 123, art. 14: https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp123.htm
- STF, prorrogação até 31/01/2026: https://noticias.stf.jus.br/postsnoticias/stf-prorroga-prazo-para-aprovacao-de-lucros-e-dividendos-ate-janeiro-de-2026/
- NT EFD-Reinf 02/2026 (portal): https://documentacao.senior.com.br/exigenciaslegais/noticias/federal/2026/2026-05-11-sped-efd-reinf-nota-tecnica-no-02-2026-registro-de-lucros-e-dividendos-na-efd-reinf/

---

## 6. Pejotização e PJ x CLT

### Estado das decisões

| Item | Situação | Confiança |
|---|---|---|
| ADPF 324 e RE 958.252 (Tema 725), 2018 | Tese: é lícita a terceirização ou qualquer outra forma de divisão do trabalho entre pessoas jurídicas distintas, independentemente do objeto social, mantida a responsabilidade subsidiária da contratante | média |
| ADC 66, dez/2020 | STF (8 a 2, rel. Cármen Lúcia) declarou constitucional o art. 129 da Lei 11.196/2005: serviço intelectual, científico, artístico ou cultural prestado por PJ segue só a legislação da PJ para fins fiscais e previdenciários. Não protege fraude ou abuso | média |
| Tema 1389 (ARE 1.532.603) | Repercussão geral reconhecida em abril de 2025. Discute validade do contrato civil/comercial (franquia, PJ etc.), competência da Justiça do Trabalho e ônus da prova da fraude. Gilmar Mendes suspendeu os processos em abril de 2025 e liberou a tramitação até o 2º grau em 18/06/2026. Uma fonte diz que o mérito começou no fim de 2025 com pedido de vista de Cármen Lúcia. Não achei tese fixada até 04/11/2026 | média (suspensão e liberação); baixa (andamento do mérito) |
| Lei 6.019/1974, arts. 5º-C e 5º-D | Quarentena de 18 meses: ex-empregado não pode voltar como sócio de PJ contratada nem como empregado da prestadora antes de 18 meses (exceto aposentado) | média |

### O que torna a estrutura defensável

- Ausência de subordinação: entrega por escopo ou resultado, sem controle de jornada, sem chefe direto da contratante dando ordens do dia a dia.
- Mais de um cliente ao longo do tempo, ou pelo menos liberdade contratual para ter outros.
- Contrato B2B com objeto, prazo, preço por entrega e multa civil, e não "salário" mensal fixo com férias e 13º disfarçados.
- Possibilidade de se fazer substituir ou subcontratar quando o contrato permitir.
- Ferramentas, equipamento e custos próprios.
- Respeito à quarentena de 18 meses para quem era CLT da mesma empresa.
- Nota fiscal por serviço, empresa com CNAE e anexo coerentes com a atividade.

### Jogada legal

O risco trabalhista é maior para quem contrata do que para quem presta. Para o prestador, o risco fiscal é a Receita desconsiderar a PJ e tributar como salário (até 27,5% de IRPF mais INSS). O art. 129 da Lei 11.196, validado na ADC 66, protege quem presta serviço intelectual por PJ de verdade. O que derruba a estrutura é subordinação comprovada ou simulação. Enquanto o Tema 1389 não tiver tese, a skill deve recomendar contratos com cara de B2B real e evitar a passagem direta de CLT para PJ na mesma empresa sem respeitar os 18 meses.

### Fontes
- Liberação dos processos em 18/06/2026 (portal): https://acritica.net/politica/gilmar-mendes-libera-processos-pejotizacao-stf/
- Gilmar Mendes retira suspensão (imprensa): https://www.poder360.com.br/poder-justica/gilmar-mendes-retira-suspensao-dos-processos-sobre-pejotizacao/
- Status do Tema 1389 até junho de 2026 (portal): https://www.marraclt.com.br/salario/pejotizacao-stf-tema-1389-o-que-muda
- ADC 66, acórdão (cópia no TRT3): https://portal.trt3.jus.br/internet/jurisprudencia/repercussao-geral-e-controle-concentrado-adi-adc-e-adpf-stf/downloads/controle-concentrado-adc/copy_of_Acordao_ADC_66.pdf
- Lei 6.019/1974: https://www.planalto.gov.br/ccivil_03/leis/l6019.htm

---

## 7. Obrigações e multas da pequena empresa de serviço

| Obrigação | Quem | Prazo | Multa por atraso | Base legal | Confiança |
|---|---|---|---|---|---|
| PGDAS-D (apuração mensal do Simples) | Todo optante, inclusive sem receita (informa zero) | Dia 20 do mês seguinte (mesmo dia do DAS) | 2% ao mês sobre os tributos declarados, mesmo pagos, até 20%; mínimo de R$ 50 por mês de referência; R$ 20 por grupo de 10 informações erradas. Desde 01/01/2026 conta a partir do dia seguinte ao prazo. Metade se entregar antes de procedimento de ofício; 75% se entregar no prazo da intimação | LC 123, art. 38-A; Perguntão 6.4 e 6.5 | alta |
| DEFIS | Optante do Simples, inclusive inativo | 31 de março do ano seguinte (sem prorrogação em fim de semana) | Agora existe multa: 2% ao mês sobre os tributos informados, mínimo de R$ 200, R$ 100 por grupo de 10 informações erradas. Não é lançada automaticamente (chega pela Caixa Postal). Sem a DEFIS, o PGDAS-D de março em diante fica bloqueado | LC 123, art. 38, § 3º; Res. CGSN 183/2025; Res. 140, art. 97-A; Perguntão 6.10 a 6.12 | alta (prazo e bloqueio); média (valores) |
| DASN-SIMEI | MEI | 31 de maio | Mínimo de R$ 50 | LC 123, art. 38, § 6º | média |
| DCTFWeb | Toda empresa com pró-labore, folha ou retenções previdenciárias | Último dia útil do mês seguinte (IN RFB 2.237/2024). O INSS vence no dia 20 | MAED automática: 2% ao mês sobre as contribuições informadas, até 20%; mínimo de R$ 200 (sem fato gerador) ou R$ 500. Redução de 50% para ME/EPP do Simples e 90% para MEI; de 50% se pagar em 30 dias. A partir de 2027, a redução de multas fixas/mínimas para ME/EPP do Simples sobe para 60% | Lei 8.212, art. 32-A; LC 123, art. 38-B, II (LC 227, efeito em 2027) | média (MAED); alta (60% em 2027) |
| eSocial | Toda empresa que paga pró-labore ou salário | Eventos mensais (S-1200, S-1210 etc.) até o dia 15 | Multas trabalhistas variadas (não levantadas) | IN RFB 2.043/2021 | média |
| EFD-Reinf | Quem retém tributos, paga serviços com retenção, ou distribui lucros (R-4010) | Dia 15 do mês seguinte | Mínimo de R$ 200 ou R$ 500 (não confirmado nesta pesquisa) | IN RFB 2.043/2021, art. 6º | alta (prazo); não confirmado (multa) |
| DIRF | Extinta | Fatos geradores desde 01/01/2025 vão para eSocial (S-1210, S-2501) e EFD-Reinf (R-4010, R-4020) | não se aplica | IN RFB 2.181/2024; Receita | alta |
| ECD e ECF | Presumido (ECD se distribuir lucro acima do presumido sem pagar IR; ECF sempre) e Real | ECD: último dia útil de maio; ECF: último dia útil de julho | não levantadas | IN RFB 2.003/2021 e 2.004/2021 | média |
| EFD-Contribuições | Presumido e Real até 2026 (PIS/Cofins) | 10º dia útil do 2º mês seguinte | não levantadas | IN RFB 1.252/2012 | média |
| Notas fiscais com IBS/CBS | Real e Presumido em 2026; Simples e MEI a partir de 2027 | a cada operação | Cura de 60 dias para autos de 2026 | Ato Conjunto 1/2025; LC 214, art. 348 | média |

### Jogada legal

As multas que mais pegam a empresa pequena de serviço são as automáticas: PGDAS-D sem movimento esquecido (R$ 50 por mês), DEFIS atrasada (agora com multa e bloqueio do PGDAS-D) e DCTFWeb do pró-labore (mínimo de R$ 200 a R$ 500 antes das reduções). A skill deve lembrar que empresa parada também declara, e que distribuir lucro em 2026 gera R-4010 na EFD-Reinf mesmo quando isento. Entregar antes da intimação reduz a multa à metade.

### Fontes
- Perguntão do Simples, capítulo 6: https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf
- Multas de PGDAS-D e DEFIS a partir de 2026 (portal Fenacon): https://fenacon.org.br/reforma-tributaria/novas-regras-para-multas-por-atraso-na-entrega-das-declaracoes-do-simples-nacional/
- MAED da DCTFWeb (portal Fenacon): https://fenacon.org.br/noticias/multas-por-atraso-da-dctfweb-passarao-a-ser-emitidas-automaticamente/
- Prazo da DCTFWeb pela IN 2.237/2024 (portal): https://documentacao.senior.com.br/exigenciaslegais/noticias/trabalhista-previdenciaria/2025/2025-02-12-contribuintes-ganham-mais-tempo-para-entregar-a-dctfweb
- Fim da DIRF (Receita): https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2025/julho/a-declaracao-do-imposto-sobre-a-renda-retido-na-fonte-dirf-nao-sera-mais-utilizada
- Fim da DIRF (eSocial): https://www.gov.br/esocial/pt-br/noticias/substituicao-da-dirf-pgd-por-eventos-do-esocial-comeca-no-periodo-de-apuracao-01-2025
- LC 227/2026 (art. 38-B da LC 123): https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-227-13-janeiro-2026-798657-normaatualizada-pl.pdf

---

## Em aberto (conferir antes de afirmar)

1. **Teto do MEI em 2028.** Os R$ 140 mil dependem de a renúncia constar nas LOAs de 2027 a 2029 (LC 238, art. 3º). Se não constar, o que vale em 2028 não está confirmado.
2. **Nanoempreendedor com o teto novo.** A LC 214 fala em 50% do "limite para adesão ao MEI". O art. 2º da LC 238 fixa R$ 110 mil para 2027 fora do texto do art. 18-A, que só muda em 2028. Não sei se em 2027 o limite do nano é R$ 40.500 ou R$ 55.000.
3. **Prazo de opção pelo Simples para 2027.** O Perguntão (09/10/2026) diz 01 a 30/09/2026. A Res. CGSN 194/2026, segundo portal, estendeu até 15/10/2026 (e o regime regular até 30/10). Não li a Res. 194 no DOU. Também não sei se a janela de janeiro volta a existir para 2028.
4. **CBS de 2027.** Os 11,3% do TCU ainda dependem do Senado (prazo 15/12/2026). Não confirmei se o número já desconta o 0,1 p.p. do ADCT, art. 127. Também não sei se a alíquota cheia vale para o cálculo por fora de quem sai do Simples.
5. **Lei do Bem e LC 224.** Um portal diz corte de 10% (60% vira 54%). Outro diz preservação total pelo anexo da IN 2.305 (depois IN 2.307). Precisa ler o anexo da IN 2.307/2026 no DOU.
6. **IRRF de dividendos no Simples.** A Receita aplica os 10% (P&R, pergunta 10). Tributaristas dizem que a isenção do art. 14 da LC 123 só cai por lei complementar. Há ações judiciais. Desfecho não confirmado.
7. **Acréscimo de 10% no Presumido (LC 224).** Há liminares (Resende, TRFs). Não achei decisão de tribunal superior.
8. **Tema 1389.** Não achei tese nem data de julgamento até 04/11/2026. Fontes divergem sobre se o mérito já começou (vista de Cármen Lúcia).
9. **SaaS no Simples.** Não achei posição oficial recente sobre SaaS ser licenciamento (Fator R) ou provimento de aplicação (Anexo III direto). Vale procurar Soluções de Consulta Cosit.
10. **CNAE 6209-1/00.** Portais divergem entre Fator R e Anexo III direto.
11. **Repartição do Anexo V em 2027.** Não li a tabela nova. A projeção de 2027 assumiu que a fração de CBS/IBS é igual à antiga de PIS+Cofins.
12. **Redução de 30% para o Simples por fora.** O art. 127 não diz se o optante do Simples no regime regular pode usar.
13. **Valores de IBS/CBS no DAS-MEI de 2027.** Portais falam em cerca de R$ 1, mas não li a Res. CGSN 190/2026.
14. **Multa da DEFIS.** O Perguntão diz que a multa vale "a partir do ano-calendário 2026". A Fenacon diz que a DEFIS do ano-calendário 2025, entregue depois de 31/03/2026, já sofre multa. Teto de 20% não confirmado para a DEFIS.
15. **Exportação de serviços no Simples a partir de 2027.** A imunidade de IBS/CBS está na Constituição, mas não li a redação nova do art. 18, § 14, da LC 123.
16. **Dividendos sem pró-labore.** Não achei norma ou solução de consulta recente da Receita sobre requalificar dividendos como remuneração.
17. **TJLP do 4º trimestre de 2026.** Não confirmado no site do Banco Central.
18. **Alíquotas de IRRF de JCP.** O compilado do planalto menciona redações anteriores de "15% e 18%". Não verifiquei de onde vêm os 18%. A alíquota vigente de 17,5% está confirmada.
19. **FS12 com CPP do DAS.** O Perguntão diz que a CPP "inclusive a recolhida dentro do Simples" entra na folha do Fator R. Na prática os contadores não somam a CPP do DAS. A tabela do tópico 3 usou a leitura conservadora (pró-labore de 28% sem CPP).
