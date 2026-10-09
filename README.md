# NOMOS Watchfaces

Projeto de mostradores personalizados para Amazfit. Primeiro alvo: **NOMOS FACE 01 — Bip 6, 390 × 450 px**.

**Estado do produto: ASSETS + CONCEITO.** Ainda não foi montado ou testado no Zepp Watchface Maker e não existe `.zab` validado no relógio físico.

## Identidade
- Glifo HAR fornecido pelo proprietário, preservando três estruturas originais.
- Laranja e escala de cinza, sem outras cores.
- MONOLITH + EDITORIAL CHAOS: números brutalistas originais, formas contínuas (sem traços misturados/interrompidos), escala de cinza harmonizada.
- Hora protagonista; outros indicadores com dados reais do Zepp.

## Materiais
- **[NUMERAIS APROVADOS — dez PNGs 0–9, 320×420 com transparência](assets/numerals/png_320x420/)**
- **[Prévia dos numerais aprovados](assets/numerals/preview.webp)**
- [Ficha de produção dos numerais](assets/numerals/README.md)
- [HAR SVG/PNG](assets/har/) — já versionado; nenhuma cópia duplicada.
- [Mockup conceitual anterior](assets/concepts/nomos-face-01-10-09-preview.webp)
- [29 SVG climáticos da Fase 02](assets/weather/svg/)
- [29 PNG climáticos](assets/weather/png_64/) / [mapeamento](assets/weather/mapeamento.csv)
- [Zepp Maker](docs/ZEPP-MAKER.md) · [Inventário](docs/ASSETS.md) · [Codex](AGENTS.md)

Os 29 ícones climáticos da Fase 02 ainda exigem aceite visual e teste no Zepp Maker. O primeiro lote genérico, rejeitado, foi retirado da main ([incidente](docs/INCIDENTE-CLIMA.md)).

**App ID do cadastro no Zepp Console: 1130388.** Vínculo com projeto do Maker não confirmado. Nenhuma validação de funcionamento no Bip 6 foi executada.

## Complementos — assets de apoio
- [Separadores](assets/separators/) — três PNGs de dois pontos em laranja, com fundo transparente.
- [Bateria](assets/battery/) — molduras e preenchimentos gráficos em duas resoluções; **não são leitura dinâmica do nível de carga por si só**.
- [Data](assets/date/) — 7 abreviações inglesas de dias e 12 de meses, imagens candidatas, ainda sem aprovação visual específica. Número do dia deve vir de componente nativo do Zepp.
- [Prévia dos complementos](assets/support/preview.png) e [ZIP para importação](dist/NOMOS_FACE_01_COMPLEMENTOS.zip).
- [Gerador reproduzível](tools/render_support_assets.py), executado por GitHub Actions.

**Atenção:** os PNGs são apenas recursos gráficos. Ainda falta vinculá-los aos dados reais e verificar a instalação no Bip 6. A formatação da data no Maker e o preenchimento dinâmico de bateria permanecem pendentes de confirmação na interface.
