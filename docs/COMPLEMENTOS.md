# Complementos — NOMOS FACE 01

**Estado:** assets gráficos preliminares, sem importação ou teste no Zepp Maker/Bip 6.

## Glifo RAAR
Já existe em `assets/raar/raar.svg` e quatro tamanhos PNG; não criamos ou redesenhamos outro glifo.

## Separador
`colon_64.png`, `colon_96.png`, `colon_128.png` têm dois pontos **separados** em laranja, com canvas vertical 1:2 e transparência real. Houve correção de um protótipo local com apenas um ponto. **Não reutilizar aquele arquivo defeituoso.**

## Bateria
Duas combinações de moldura/preenchimento em PNG transparente (`67×240` e `89×320`). O preenchimento foi desenhado a 100% para fornecer geometria; **não é um indicador dinâmico**. Importar apenas se o Maker permitir ligação do progresso ao dado real. Se não permitir, preferir componente nativo sem simulações ou texto estático de carga.

## Data
Sete abreviações de dia da semana (`MON..SUN`) e doze meses (`JAN..DEC`) em inglês, com o mesmo canvas 220×72 dentro de cada família. São **candidatos gráficos**, não tipografia aprovada. Para valores de dia do mês e ano, preferir o componente dinâmico do Zepp. O conteúdo não deve ficar fixo como imagem de background.

## Verificação
A rotina `tools/render_support_assets.py` verifica a existência de **26 PNGs RGBA transparentes**, ambos os pontos do separador, contagens dos dias e meses, e integridade ZIP. Isto prova apenas a geração de recursos, **não** o funcionamento de sensores ou montagem no Maker.

## Dois idiomas de data
- Inglês mantido nos caminhos anteriores (`date/weekdays`, `date/months`).
- Português do Brasil adicional em `date/pt-BR/weekdays` e `date/pt-BR/months` — sem sobrescrever o inglês.
- Dias: SEG, TER, QUA, QUI, SEX, SÁB, DOM (arquivo `SAB.png`); meses: JAN, FEV, MAR, ABR, MAI, JUN, JUL, AGO, SET, OUT, NOV, DEZ.
- Todos os rótulos com canvas `220x72`, transparência e a mesma tipografia da versão inglesa.
- ZIPs separados para as duas versões. O Zepp Maker precisa ser verificado antes de afirmar troca de idioma automática; por ora são dois conjuntos independentes.
