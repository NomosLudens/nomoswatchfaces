# Fluxo de trabalho — Zepp Console e Watchface Maker

1. Console: https://console.zepp.com/#/service/app/form/watchface
2. Maker: https://watchface.zepp.com/create
3. Usar formato Zepp OS e resolução **390×450**. Confirmar que **Amazfit Bip 6** consta nos dispositivos suportados.
4. Verificar se o Maker usa o cadastro existente **NOMOS FACE 01 / appId 1130388**. Não publicar com App ID divergente.
5. Preferir template em branco. Criar base 390×450 e importar glifo HAR sem alterar proporções.
6. Usar componente **Time → Digital Time** e as **10 artes (0–9)** de tamanho idêntico para a hora/minuto, se a tipografia autoral for aprovada.
7. Para clima, usar os PNGs 0–28 da pasta `assets/weather/png_64`. Confirmar **ordem exata de mapeamento na versão atual do Maker** antes do upload.
8. Inserir dados reais pelos componentes Zepp: tempo, data, passos, bateria e clima.
9. AOD deve minimizar conteúdo e contraste; implementar após a face principal funcionar.
10. Testar no relógio: abertura, atualização do horário e data, ícones com condições reais, sensores e AOD.

**Estado atual:** só planejamento e preparação de assets. Nenhum teste de importação, preview, pacote ou execução real foi confirmado.

## Docs oficiais
- https://docs.zepp.com/docs/guides/faq/watchface-maker/
- https://docs.zepp.com/docs/designs/customization/watchface/
- https://docs.zepp.com/docs/watchface/specification/
- https://docs.zepp.com/docs/guides/tools/watchface/guides/time/
- https://docs.zepp.com/docs/guides/tools/watchface/guides/editable-component/
