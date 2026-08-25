# Reproduzindo a Listagem do YouTube com Grid Layout

Este projeto reproduz uma página de listagem de vídeos inspirada na interface do YouTube. O desafio foi desenvolvido para praticar a construção de layouts com CSS Grid, trabalhando a organização de uma página em áreas bem definidas: cabeçalho, menu lateral e grade de vídeos.

A página apresenta um cabeçalho com os elementos de navegação, uma barra lateral com opções do menu e uma área principal contendo cards de vídeos. Cada card reúne miniatura, avatar do canal, título, número de visualizações e tempo desde a transmissão.

## Tecnologias utilizadas

- HTML5
- CSS3
- CSS Grid Layout
- Google Fonts com a família Roboto

## Organização do layout

O layout geral utiliza `grid-template-areas` para dividir a tela em duas linhas:

- `header`: ocupa toda a largura da primeira linha;
- `sidebar`: ocupa a coluna lateral da segunda linha;
- `videos`: ocupa o espaço restante e exibe os cards.

Na área principal, os vídeos são distribuídos em quatro colunas com espaçamento uniforme. Os próprios cards também usam Grid para alinhar a miniatura, o avatar e as informações do vídeo.

## Estrutura do projeto

```text
.
├── index.html
├── README.md
└── assets
	├── css
	│   └── style.css
	└── img
		├── Left.png
		├── Center.png
		├── Right.png
		├── Channel_Avatar.png
		└── v1.png a v5.png
```

## Como executar

Como se trata de uma página estática, basta abrir o arquivo `index.html` em um navegador. Também é possível utilizar a extensão Live Server do VS Code para acompanhar a página durante o desenvolvimento.

## Objetivo do desafio

Aplicar conceitos de HTML semântico, dimensionamento, espaçamento e principalmente CSS Grid Layout na reprodução de uma interface conhecida, desenvolvendo uma estrutura visual organizada a partir de um layout de referência.
