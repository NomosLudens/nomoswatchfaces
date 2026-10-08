# NOMOS FACE 01 — conceito aprovado e limites

## Objetivo criativo
Não produzir uma watch face de catálogo. Direção aprovada: **MONOLITH + EDITORIAL CHAOS**, proposta brutalista/editorial com números geométricos autorais e assimetria controlada, de leitura imediata.

- Priorizar **hora e minuto**: números próprios, construídos como família coerente de dez glifos 0–9.
- Fundo AMOLED preto com laranja reservado para interferências gráficas. Branco e cinza para os números.
- Não usar anéis de progresso genéricos, molduras gaming, neon, gradientes futuristas ou três widgets circulares.
- Informações secundárias (data, passos, bateria, clima) são discretas e **dinâmicas**, não números gravados na imagem final.
- Integrar **o glifo HAR** como assinatura, preservando exatamente suas três estruturas. A origem foi o arquivo de imagem fornecido pelo proprietário; `assets/har/har.svg` é uma vetorização da silhueta, não um redesign.
- Referência de estudo visual aprovada nesta conversa: layout 10 sobre 09, grande, recortes arquitetônicos, detalhes laterais e pequenos elementos laranja. O conteúdo desse estudo (hora, dia, data, passos, clima, bateria) é apenas demonstrativo.

## Modelo de dados e componentes
- Tela: **390 × 450 px** (Amazfit Bip 6).
- Hora com conjunto de **10 imagens 0.png…9.png de dimensões idênticas** + separador, se escolhermos o módulo de dígitos do Maker. Não criar dezenas de combinações de hora pré-renderizadas.
- Alternativa menos autoral: texto dinâmico por tags; só usar se o resultado visual for aprovado.
- Indicadores e clima devem ler recursos nativos do Zepp; jamais simular dados.
- Clima: recursos de **29 estados (0–28)** conforme a referência histórica do Zepp; confirmar correspondência no Maker **atual** antes de importar.
- Modo AOD simplificado ainda por desenhar e testar.

## Decisões pendentes
1. Posição e escala do glifo HAR no layout final.
2. Grade e tamanho definitivo do conjunto numérico (proposta depende da validação no Maker).
3. Confirmação do vínculo entre registro Console appId **1130388** e projeto criado no Maker.
4. Sequência de clima exigida no editor atual.
5. Teste físico no Bip 6.

**Nenhuma tela mockada é prova de que a watch face funciona.**
