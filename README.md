# Quiz Geografia — Espaço Urbano (6º ano)

Aplicativo educativo independente baseado nas páginas anexadas do SAE Digital, Geografia, 6º ano, Volume 4, Capítulo 11 — Espaço urbano.

## O que contém
- Sala de estudos com resumo organizado por conceitos do capítulo.
- Quiz principal com 60 questões objetivas (embaralhadas), explicação após resposta, dicas, vidas, cronômetro e botão para enviar a questão ao fim da fila.
- Níveis Fácil (90 s / 3 vidas), Normal (60 s / 4 vidas) e Difícil (30 s / 5 vidas).
- Jogos: associe os conceitos, ligue as colunas, memória, verdadeiro ou falso, caça-palavras e desafio de desafio de palavras por pistas (formato simplificado).
- Interface responsiva, ícone do aplicativo fornecido pelo usuário, efeitos sonoros e trilha procedural aleatória por tela/jogo, com controle de volume.
- PWA com cache offline e empacotamento Android via Capacitor.

## Executar localmente
Requer Node.js 22 ou superior.

```bash
npm install
npm test
npm run build
npm run start
```

## Gerar APK pelo GitHub Actions
1. Crie um repositório GitHub vazio.
2. Envie todo o conteúdo desta pasta para a raiz do repositório (incluindo `.github/workflows/android-apk.yml`).
3. Abra a aba **Actions** e selecione **Build Android APK**.
4. Clique em **Run workflow**. Também inicia automaticamente em push para `main` ou `master`.
5. Quando o processo terminar com indicador verde, abra a execução e baixe o artefato **Quiz-Geografia-Espaco-Urbano-APK**.
6. Extraia o ZIP do artefato e instale `app-debug.apk` no Android. Talvez seja necessário permitir instalação pelo navegador/gerenciador de arquivos.

## Ícone e launcher
- `assets/app-icon.png`: ícone quadrado 1024 × 1024 com transparência, derivado do ícone anexado.
- `assets/icon-512.png`: versão 512 × 512 para PWA.
- `assets/icon-only.png` e `assets/splash.png`: fontes usadas para gerar ícone e tela inicial nativos Android pelo Capacitor Assets.
- `assets/launcher-reference.png`: referência visual enviada para orientar a identidade do aplicativo.

## Observações técnicas
- O conteúdo principal e os jogos funcionam sem conexão depois de carregados/cacheados.
- A trilha é sintetizada localmente pela Web Audio API; não depende de arquivos externos de música.
- Este repositório inclui a fonte e a automação de compilação do APK. O APK só será produzido pelo workflow após o envio ao GitHub ou em ambiente Android com dependências instaladas.
- O quiz foi elaborado a partir do material anexado. As questões que usam números do gráfico mantêm os valores apresentados no livro (1950, 2007, 2020 e projeção de 2050).
