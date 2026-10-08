# Fase 02 — Biblioteca climática NOMOS

**Estado: candidato visual, não publicado nem testado no Amazfit Bip 6.**

29 estados meteorológicos do formato Zepp conforme [Watchface Specification](https://docs.zepp.com/docs/watchface/specification/), índice 0 a 28. Correspondência ainda pendente de conferência no Maker atual.

## Arte
- Geometria vetorial autoral desenhada para a NOMOS, não adaptada de GNOME/Adwaita/Tabler.
- Linguagem de fita arquitetônica, recortes secos, base branca/cinza e precipitação laranja.
- 29 SVGs sob `assets/weather/svg/`; renderizados automaticamente para PNG RGBA transparentes de 64x64.
- Conjuntos de dia e noite, nuvem, chuva/neve/granizo, névoa, vento/areia e tempestade.

## Estado de validação
- Símbolos gerados: **sim**.
- Conferência técnica dos PNGs: realizada no workflow.
- Aprovação final do design: **pendente**.
- Importação no Zepp Watchface Maker: **não testada**.
- Teste real no relógio: **não testado**.

### Importante
Este conjunto **não reutiliza** a biblioteca genérica rejeitada, retirada em `docs/INCIDENTE-CLIMA.md`. Não confundir renderização SVG com teste da watch face.
