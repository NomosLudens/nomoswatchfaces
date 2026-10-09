# Complementos — NOMOS FACE 01

**Estado:** assets gráficos preliminares, sem importação ou teste no Zepp Maker/Bip 6.

## Glifo HAR
Já existe em `assets/har/har.svg` e quatro tamanhos PNG; não criamos ou redesenhamos outro glifo.

## Separador
`colon_64.png`, `colon_96.png`, `colon_128.png` têm dois pontos **separados** em laranja, com canvas vertical 1:2 e transparência real. Houve correção de um protótipo local com apenas um ponto. **Não reutilizar aquele arquivo defeituoso.**

## Bateria
Duas combinações de moldura/preenchimento em PNG transparente (`67×240` e `89×320`). O preenchimento foi desenhado a 100% para fornecer geometria; **não é um indicador dinâmico**. Importar apenas se o Maker permitir ligação do progresso ao dado real. Se não permitir, preferir componente nativo sem simulações ou texto estático de carga.

## Data
Sete abreviações de dia da semana (`MON..SUN`) e doze meses (`JAN..DEC`) em inglês, com o mesmo canvas 220×72 dentro de cada família. São **candidatos gráficos**, não tipografia aprovada. Para valores de dia do mês e ano, preferir o componente dinâmico do Zepp. O conteúdo não deve ficar fixo como imagem de background.

## Verificação
A rotina `tools/render_support_assets.py` verifica a existência de **26 PNGs RGBA transparentes**, ambos os pontos do separador, contagens dos dias e meses, e integridade ZIP. Isto prova apenas a geração de recursos, **não** o funcionamento de sensores ou montagem no Maker.
