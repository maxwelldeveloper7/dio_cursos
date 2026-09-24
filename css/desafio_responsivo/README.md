# Desafio Responsivo: Discord

Projeto desenvolvido como parte de um desafio de CSS da [Digital Innovation One (DIO)](https://www.dio.me/), com o objetivo de reproduzir a página inicial da plataforma Discord e praticar conceitos de responsividade.

## Sobre o projeto

A página apresenta uma interface inspirada no Discord, com:

- Seção inicial com chamada principal e botões de acesso;
- Blocos destacando criação de servidores, canais de voz e ferramentas para comunidades;
- Seção sobre comunicação por voz e vídeo;
- Layout adaptado para desktop e dispositivos móveis.

## Tecnologias utilizadas

- HTML5;
- CSS3;
- Flexbox;
- Media queries;
- Google Fonts: Open Sans e Luckiest Guy;
- Imagens e ícones locais.

## Como executar

1. Clone ou baixe este repositório.
2. Abra o arquivo `index.html` em um navegador.

Por ser um projeto estático, não é necessário instalar dependências ou executar um servidor para visualizá-lo.

## Estrutura do projeto

```text
.
├── index.html
└── assets
    ├── css
    │   └── style.css
    └── img
        ├── conexao.png
        ├── criar.png
        ├── encontrar.png
        ├── header.png
        ├── logo.svg
        └── poucos-muitos.png
```

## Responsividade

O layout utiliza Flexbox e uma media query para reorganizar o conteúdo em telas menores. Em dispositivos com largura de até 428px, os botões passam a ocupar a largura disponível, as seções ficam empilhadas e os textos são redimensionados para melhorar a leitura.

## Objetivo do desafio

Colocar em prática os fundamentos de HTML e CSS, especialmente a construção de layouts flexíveis e a adaptação de uma interface para diferentes tamanhos de tela.
