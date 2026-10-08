# Diretrizes para Codex — NOMOS Watchfaces

Escopo: primeira face NOMOS FACE 01, **Zepp Watchface Maker no navegador**, não criar app próprio, SDK ou firmware sem decisão expressa.

- Produto funcionando > teste real > dados reais > rollback > código bonito.
- Este repositório contém um **estudo visual e gerador de assets**, não um mostrador operacional.
- Preserve exatamente a silhueta e três estruturas do glifo HAR (`assets/har/har.svg`); nunca invente um HAR substituto.
- Paleta apenas laranja, preto, branco e cinzas.
- Aproveite recursos já presentes, não desenhe manualmente dezenas de estados climáticos.
- Modificar o conjunto de clima apenas com justificativa e validar `0…28` contra o editor atual.
- NÃO tratar compilação de PNG/CI como prova da instalação da face.
- NÃO afirmar que relógio, sensores, clima, AOD ou appId foram testados sem evidência do Bip 6 físico.
- Evitar mocks, placeholders e dados hardcoded em assets finais. Valores de um *mockup de conceito* são apenas exemplos.
- Documentar qualquer etapa dependente de autenticação humana no Zepp Maker.
