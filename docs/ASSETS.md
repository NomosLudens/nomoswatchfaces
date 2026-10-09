# Inventário de assets

| Recurso | Arquivos | Estado |
|---|---|---|
| Numerais brutalistas 0 a 9 | `assets/numerals/png_320x420/0.png` a `9.png` | **Aprovados visualmente** pelo proprietário; recortados da última prancha aceita; 320×420 PNG RGBA transparente |
| Prévia dos numerais | `assets/numerals/preview.webp` | Prancha de conferência, não importar como dígito |
| Glifo RAAR | `assets/raar/raar.svg`, PNGs de 64, 128, 256 e 390 px | Preparado; não testado no Maker |
| Conceito anterior de watch face | `assets/concepts/nomos-face-01-10-09-preview.webp` | Estudo visual, não tela final |
| Ícones climáticos originais da fase 02 | `assets/weather/svg/0.svg` a `28.svg` e `assets/weather/png_64/0.png` a `28.png` | Em avaliação; mapeamento não confirmado no Maker |
| AOD e fundo final | — | Pendentes |
| Pacote `.zab` | — | Inexistente |

**Não chamar o conjunto de numerais de funcional no Zepp antes de importar e testar.** Os dez arquivos têm tamanho uniforme e transparência verdadeira, mas o editor e o relógio ainda não foram verificados.

## Localização de datas
- **EN (preservado):** `assets/date/weekdays/` (7) e `assets/date/months/` (12).
- **pt-BR (novo):** `assets/date/pt-BR/weekdays/` (7) e `assets/date/pt-BR/months/` (12); `SAB.png` exibe **SÁB**.
- ZIPs de cada idioma em `dist/NOMOS_FACE_01_DATA_EN.zip` e `dist/NOMOS_FACE_01_DATA_PT_BR.zip`.
- Aprovação visual e teste de importação, idioma e data dinâmica ainda pendentes.
