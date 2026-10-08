# NOMOS Watchfaces

Identidade visual e assets para mostradores Amazfit, começando por **NOMOS FACE 01** (Amazfit Bip 6, 390 × 450 pixels).

**Estado: CONCEITO / NÃO INSTALADO.** O projeto ainda não foi importado e validado no [Zepp Watchface Maker](https://watchface.zepp.com/) nem no relógio físico.

## Direção visual

- Glifo **HAR** original do proprietário como assinatura da face; preservar suas três estruturas sem separar, redesenhar ou modificar os traços.
- Paleta estrita: laranja, preto, branco e escala de cinza.
- Tipografia geométrica autoral, composição brutalista/editorial assimétrica e muito espaço negativo.
- Hora protagonista; data, bateria, passos e clima discretos; evitar anéis de progresso e painéis genéricos.
- Tela de referência: **390 × 450 px**, cantos arredondados.
- Projeto criado no Zepp Console: **NOMOS FACE 01 — appId 1130388**. Vínculo com projeto do Maker ainda não confirmado.

## Status

Ainda não há pacote `.zab`, publicação aprovada ou prova de funcionamento no Bip 6. Os recursos gráficos são estudos, não dados reais nem interface operante.

## Referências oficiais

- [Watchface Maker](https://watchface.zepp.com/)
- [Watch Face Design](https://docs.zepp.com/docs/designs/customization/watchface/)
- [Watchface Maker FAQ](https://docs.zepp.com/docs/guides/faq/watchface-maker/)
- [Watch Face Specification](https://docs.zepp.com/docs/watchface/specification/)

## Materiais no repositório

- [Glifo HAR vetorial](assets/har/har.svg) e PNGs transparentes de 64, 128, 256 e 390 px (`assets/har/`).
- [Estudo visual 10:09 de 390×450](assets/concepts/nomos-face-01-10-09-preview.webp) — **prévia comprimida** para referência, não fundo final da face.
- [Conjunto climático 0–28](assets/weather/png_64/) — 29 ícones PNG RGBA 64×64.
- [Prancha climática](assets/weather/preview.png) e [ZIP para download](dist/nomos-weather-29.zip).
- [Conceito](docs/CONCEITO.md), [inventário](docs/ASSETS.md), [procedimento Zepp Maker](docs/ZEPP-MAKER.md), [atribuições](docs/TERCEIROS.md) e [orientações Codex](AGENTS.md).
- Geradores automatizados em `tools/`, executados e publicados por GitHub Actions.

**Estado do produto:** os dois pipelines de assets passaram, mas o mostrador ainda **não existe como watch face instalada**, não foi importado pelo Maker e não possui `.zab` validado. Os números do mockup são ilustrativos. A sequência climática deve ser confrontada com a interface Zepp atual antes do upload.
