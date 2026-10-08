# INCIDENTE — Ícones climáticos genéricos rejeitados

**Situação: material rejeitado pelo proprietário.**

### Causa
Foram criados 29 PNGs por recoloração/adaptação de símbolos climáticos do GNOME Adwaita, apresentados como entrega pronta mesmo sem aprovação estética, sem conferência do mapeamento real no Zepp Watchface Maker e sem teste no Bip 6.

Um gerador/CI funcional de PNGs **não substitui** a criação artística aprovada. A entrega não atendia ao requisito central: identidade autoral, reconhecível e diferente de watch faces genéricas.

### Contenção aplicada
- Removidos da branch `main`: `assets/weather/`, `dist/nomos-weather-29.zip`, `tools/build_weather.py`, workflow de clima e atribuição do Adwaita (que não é mais utilizado).
- Preservados: glifo HAR, sua vetorização/exportações e estudo visual, que são itens de outro escopo.
- Histórico Git mantido para auditoria e rollback; **não** recuperar ícones genéricos para a nova face.

### Correção de processo
1. Desenhar **três símbolos originais** como família: céu limpo, nublado, chuva.
2. Usar as mesmas regras gráficas inspiradas no caráter estrutural do HAR, **sem reproduzir o próprio glifo em cada ícone**.
3. Apresentar juntos em tamanho real, sobre preto, e obter aprovação do proprietário.
4. Só depois desenvolver os outros estados necessários, conferindo a lista real de condições e ordem no Maker.
5. Se houver automação, usá-la **após** a aprovação do desenho-base e somente para exportação de variantes padronizadas.
6. Testar importação, leitura dos estados e exibição física.

Sem aprovação da etapa 3, não existe pacote climático final.
