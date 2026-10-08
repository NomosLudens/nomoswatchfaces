# Inventário de assets

| Recurso | Local | Estado |
| --- | --- | --- |
| Glifo HAR, silhueta vetorizada a partir da imagem fornecida | `assets/har/har.svg`, `assets/har/har_{64,128,256,390}.png` | SVG + quatro PNGs transparentes; ainda não testados no Maker |
| Mapeamento dos estados climáticos | `assets/weather/mapeamento.csv` | Registro preliminar; confirmar a ordem do Maker |
| PNGs climáticos 0–28 em 64×64 transparentes | `assets/weather/png_64/` | Gerados e versionados por `tools/build_weather.py`; workflow passou |
| Prévia dos estados climáticos | `assets/weather/preview.png` | Gerada e versionada |
| ZIP com ícones climáticos | `dist/nomos-weather-29.zip` | Gerado e versionado |
| Mockup conceitual aprovado na conversa | `assets/concepts/nomos-face-01-10-09-preview.webp` | Cópia reduzida/recomprimida em 390×450; apenas referência visual, não usar como fundo final |
| Set tipográfico 0–9 da hora | — | **PENDENTE**, desenho não fechado |
| Background final 390×450 | — | **PENDENTE** |
| AOD | — | **PENDENTE** |
| Pacote .zab | — | **NÃO EXISTE** |

## Regras
- Arquivos PNG climáticos gerados devem ter **64×64 px**, transparência verdadeira e nomes `0.png` a `28.png`.
- Gráfico do glifo HAR não deve ser substituído por interpretações diferentes.
- Imagens finais não contêm valores fictícios de sensores; valores devem vir dos componentes Zepp.
- Não declarar compatibilidade prática até concluir importação e teste em hardware.
- Guardar atribuição e informação de licença dos ícones de terceiros.

## Licenças e proveniência
Os ícones climáticos são derivados do projeto **GNOME Adwaita**, instalado via pacote `adwaita-icon-theme`. Consulte `docs/TERCEIROS.md` e o arquivo de copyright da distribuição. Não afirmar que são do conjunto MIT Makin-Things: **não são**.
