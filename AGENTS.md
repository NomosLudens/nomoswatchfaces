# AGENTS.md — NOMOS Watchfaces

Objetivo: face original Amazfit Bip 6 no **Zepp Watchface Maker**, sem SDK ou infraestrutura nova não solicitada.

- Preserve rigorosamente o glifo HAR com as três estruturas originais.
- Use apenas laranja e escala de cinza. Direção: MONOLITH + EDITORIAL CHAOS.
- Os recursos `assets/weather/svg/0.svg..28.svg` são **NOVOS ícones autorais da Fase 02, ainda em avaliação**; não são derivados do GNOME Adwaita.
- Os ícones genéricos Adwaita anteriores foram rejeitados: **NÃO restaurar nem reutilizar** (ver `docs/INCIDENTE-CLIMA.md`).
- Alterar os desenhos da Fase 02 somente conforme avaliação da prancha; mudanças pequenas e reversíveis.
- Mapeamento climático segue especificação Zepp 0–28, mas **confirmar no Maker atual** antes de enviar.
- SVG/PNG e CI verde não significam que o relógio funcione; declarar PASS só após upload, sensores reais e teste físico do Bip 6.
- Não usar mocks, dados fictícios, bibliotecas de ícones genéricos ou substituições de arte não aprovadas.
