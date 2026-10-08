# AGENTS.md — NOMOS Watchfaces

Objetivo: uma **watch face original** para Amazfit Bip 6, montada **no Zepp Watchface Maker**, sem criar SDK, app próprio ou infraestrutura desnecessária.

**Gates de produto:** conceito aprovado → três testes visuais originais de clima → validação do mapeamento Zepp → conjunto completo → importação → relógio físico.

Regras:
- Mantenha **HAR** fiel às três estruturas fornecidas pelo proprietário; não alterar suas formas.
- Use somente **laranja e escala de cinza**.
- O estudo MONOLITH + EDITORIAL CHAOS é referência de composição, não a arte final.
- **Não reutilize nem regenere** os 29 ícones genéricos Adwaita removidos por rejeição estética; veja `docs/INCIDENTE-CLIMA.md`.
- **Não** criar 29 ícones antes de aprovação de três símbolos distintos e **originais**.
- Não atribuir condições Zepp a índices com base em suposição; confirmar a sequência no Maker.
- Não declarar PASS com base apenas em gerar PNG, passar build/CI, produzir mockup ou atualizar GitHub.
- Não fingir funcionamento com valores, temporizadores, mockups ou APIs imaginárias.
- Alterações pequenas, reversíveis, isoladas. Preservar os arquivos e a identidade já aprovados.
