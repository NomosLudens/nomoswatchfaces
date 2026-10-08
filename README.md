# NOMOS Watchfaces

Projeto autoral de mostradores Amazfit. Primeiro alvo: **NOMOS FACE 01 — Amazfit Bip 6 (390 × 450 px)**.

**Estado: CONCEITO + ÍCONES FASE 02 EM AVALIAÇÃO.** Nenhum projeto foi importado e validado no Zepp Maker, não existe pacote `.zab` ou teste no relógio físico.

## Identidade
- Glifo **HAR** original do proprietário, três estruturas preservadas.
- Exclusivamente laranja e escala de cinza.
- Direção MONOLITH + EDITORIAL CHAOS: tipografia geométrica autoral, assimetria controlada, espaço negativo. Sem dashboard genérico.
- Hora protagonista; demais indicadores dinâmicos devem usar dados reais do Zepp.

## Conteúdo
- [HAR SVG/PNG](assets/har/)
- [Estudo visual da watch face](assets/concepts/nomos-face-01-10-09-preview.webp)
- [Fase 02 — 29 ícones SVG climáticos autorais](assets/weather/svg/)
- [Prancha climática](assets/weather/prancha-fase-02.png) (gerada pelo workflow)
- [29 PNGs transparentes 64×64](assets/weather/png_64/) (gerados pelo workflow)
- [ZIP clima](dist/NOMOS_FASE_02_CLIMA_29_ORIGINAIS.zip) (gerado pelo workflow)
- [Correspondência 0–28](assets/weather/mapeamento.csv) (baseada na especificação publicada pela Zepp; verificar Maker atual)
- [Desenho e status da Fase 02](docs/CLIMA-FASE-02.md)
- [Fluxo de montagem no Zepp Maker](docs/ZEPP-MAKER.md)
- [Inventário](docs/ASSETS.md) · [Conceito](docs/CONCEITO.md) · [Codex](AGENTS.md)

## Histórico e status real
Os ícones genéricos Adwaita da primeira tentativa foram **rejeitados e retirados** da main; ver [incidente](docs/INCIDENTE-CLIMA.md). A Fase 02 introduz desenhos vetoriais novos, **não** recriação dos assets rejeitados.

Ainda pendente: aprovação visual do novo conjunto, confirmação da ordem do clima no Maker, criação das dez artes numéricas, composição final, importação, AOD e teste físico.

Zepp Console: NOMOS FACE 01, **App ID 1130388** (vínculo com projeto Maker não confirmado).
