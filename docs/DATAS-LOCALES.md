# NOMOS FACE 01 — Dados da data em EN e pt-BR

A mesma watch face pode ser produzida com **dois conjuntos gráficos** de dias e meses. Eles não alternam automaticamente entre si sem vinculação e suporte comprovados no Zepp Maker. A estratégia de lançamento são duas variantes se o editor não fornecer localização nativa.

| Índice ISO (referência, **não** validado no Zepp) | Inglês | pt-BR (texto PNG / nome de arquivo) |
|---|---|---|
| 1 segunda | MON | SEG / SEG.png |
| 2 terça | TUE | TER / TER.png |
| 3 quarta | WED | QUA / QUA.png |
| 4 quinta | THU | QUI / QUI.png |
| 5 sexta | FRI | SEX / SEX.png |
| 6 sábado | SAT | SÁB / SAB.png |
| 7 domingo | SUN | DOM / DOM.png |

| Mês | English | Português |
|---|---|---|
| Janeiro | JAN | JAN |
| Fevereiro | FEB | FEV |
| Março | MAR | MAR |
| Abril | APR | ABR |
| Maio | MAY | MAI |
| Junho | JUN | JUN |
| Julho | JUL | JUL |
| Agosto | AUG | AGO |
| Setembro | SEP | SET |
| Outubro | OCT | OUT |
| Novembro | NOV | NOV |
| Dezembro | DEC | DEZ |

**Arquivos:** EN permanece em `assets/date/{weekdays,months}/`; pt-BR novo em `assets/date/pt-BR/{weekdays,months}/`. Todos os PNGs usam `220 × 72 px`, fundo transparente e a mesma tipografia.

**Não representar os dados de dia do mês nem ano com valores fixos.** Vincular ao componente de data real do relógio. Conferir o índice efetivamente esperado para dias/meses no Maker, sobretudo se ele usar domingo como primeiro dia.

**Gate:** geração de PNG = etapa de assets, **não** comprova que a watch face funciona.
