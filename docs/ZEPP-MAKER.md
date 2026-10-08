# Fluxo — Zepp Console / Watchface Maker

Console: https://console.zepp.com/#/service/app/form/watchface
Maker: https://watchface.zepp.com/create

1. Design em **390 × 450**, formato Zepp OS, com seleção explícita do **Amazfit Bip 6**. Confirmar na interface a compatibilidade e o template em branco.
2. Verificar vínculo do Maker com o registro existente **NOMOS FACE 01 / 1130388**. Nunca assumir correspondência automática.
3. Aprovar o desenho dos algarismos 0–9, de mesmo tamanho por conjunto, antes de importar no componente Digital Time.
4. Aprovar **três amostras climáticas autorais** (céu limpo, nublado, chuva). Só então ampliar e revisar **cada mapeamento** oferecido pelo Maker. A faixa histórica 0–28 não prova que a versão atual usa exatamente essa sequência.
5. Integrar HAR sem descaracterizar o desenho original.
6. Vincular hora, data, bateria, passos e clima **aos componentes de dados reais do Zepp**. Nunca gravar valores fictícios na imagem final.
7. Criar versão AOD a partir da face aprovada.
8. Importar, instalar pelo Zepp e testar **no Bip 6 físico**: abertura, legibilidade, mudança de minutos/data, atualização das condições climáticas e sensores, AOD.
9. Publicação e aprovação são uma etapa posterior, não prova de que o produto funciona.

**Status:** nenhuma destas verificações físicas foi concluída. Não existe pacote de clima aceito. Os assets rejeitados estão registrados em `docs/INCIDENTE-CLIMA.md` e foram removidos da main.

Docs oficiais:
- https://docs.zepp.com/docs/guides/faq/watchface-maker/
- https://docs.zepp.com/docs/designs/customization/watchface/
- https://docs.zepp.com/docs/guides/tools/watchface/guides/time/
