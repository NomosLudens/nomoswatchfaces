# NOMOS Watchfaces

Projeto autoral de mostradores Amazfit. Primeiro alvo: **NOMOS FACE 01 — Amazfit Bip 6 (390 × 450 px)**.

**Estado: CONCEITO.** Nenhum projeto do Zepp Maker foi validado, nenhum pacote `.zab` existe e nenhum fluxo foi testado no Bip 6 físico.

## Identidade aprovada
- Glifo **HAR** fornecido pelo proprietário, composto por três estruturas; não redesenhar nem descaracterizar.
- Exclusivamente **laranja e escala de cinza**.
- Direção **MONOLITH + EDITORIAL CHAOS**: tipografia geométrica autoral, hierarquia clara, assimetria controlada, espaço negativo. Nada de dashboard genérico.
- Horário como protagonista. Data, bateria, passos e clima pequenos, sempre vinculados a dados reais.

## Recursos existentes
- [HAR — SVG e PNGs transparentes](assets/har/) (original entregue pelo proprietário; vetorização e exportação, ainda sem teste no Maker).
- [Mockup conceitual](assets/concepts/nomos-face-01-10-09-preview.webp) (apenas referência visual, não tela final).
- [Conceito e decisões](docs/CONCEITO.md).
- [Inventário real de assets](docs/ASSETS.md).
- [Fluxo Zepp Maker](docs/ZEPP-MAKER.md).
- [Plano dos ícones climáticos autorais](docs/CLIMA-IDENTIDADE.md).
- [Orientações para Codex](AGENTS.md).

## Incidente da biblioteca de clima

O primeiro pacote climático continha 29 **derivações de ícones genéricos Adwaita**, sem identidade visual aprovada e sem importação/validação no Zepp Maker. Foi **rejeitado e retirado da branch `main`**. Não deve ser utilizado. Consulte [o registro do incidente](docs/INCIDENTE-CLIMA.md). O histórico de commits permanece para recuperação/auditoria, sem que esses assets façam parte da versão atual.

**Próximo gate:** apresentar apenas **três estudos originais** (sol, nublado, chuva) no mesmo grid; obter aprovação visual antes de desenhar a família completa. O código/gerador só deve existir se reduzir trabalho real, sem substituir a etapa artística.

Zepp Developer Console: NOMOS FACE 01, **App ID 1130388**. O vínculo com um projeto Maker continua **não confirmado**.
