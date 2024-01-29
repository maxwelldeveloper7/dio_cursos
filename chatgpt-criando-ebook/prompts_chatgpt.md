# Prompts para geração de conteúdo

## Prompt:
```chatgpt
crie um título de um ebook sobre o tema de css, o ebook é do nicho de programação e o subnicho é de css, o titulo deve ser épico e curto, e tenha uma temática de star wars no título, me liste 10 variações de títulos
```
## Resposta:
1. "As Guerras do Estilo: Domine o CSS como um Jedi"
2. "O Império dos Estilos: Guiando-se pelo CSS como um Mestre"
3. "A Ascensão do CSS: Uma Saga de Habilidades de Programação"
4. "CSS Wars: A Batalha Épica pelo Controle Estilístico"
5. "O Despertar do Estilo: Mestre CSS em Treinamento"
6. "A Órbita do CSS: Navegando pela Galáxia de Estilos"
7. "O Último Estilo: CSS e a Jornada do Desenvolvedor Jedi"
8. "A Força do CSS: Desbravando o Universo de Estilos"
9. "CSS Além das Estrelas: A Saga de um Desenvolvedor Galáctico"
10. "Rogue Styles: A Rebelião do CSS no Universo da Programação"


## Prompt:
```
combine os dois titulos abaixo para gerar novos títulos poderosos
"A Força do CSS: Desbravando o Universo de Estilos"
"O Despertar do Estilo: Mestre CSS em Treinamento"
```
## Resposta:
1. "O Despertar da Força CSS: Mestre em Treinamento Desbravando Estilos"
2. "A Força Desperta: CSS Mestre em Treinamento no Universo Estilístico"
3. "CSS: A Força Desperta no Universo do Estilo com um Mestre em Treinamento"
4. "Desbravando Estilos com a Força do CSS: A Jornada do Mestre em Treinamento"
5. "A Força do Estilo: CSS Desperta com um Mestre em Treinamento"


## Prompt:
```
faça um texto para ebook, com foco em CSS, listando os principais seletores CSS com exemplos em código de acordo com estas [REGRAS]

{REGRAS}
>Explique sempre de uma maneira simples
>Deixe o texto enxuto
>Sempre traga exemplos de códigos em contextos reais
>sempre deixe um título sugestivo por tópico
```
## Resposta:
**Capítulo 1: Seletores Básicos**

*O Caminho Inicial para o Estilo*

Neste capítulo, vamos começar com os fundamentos. Os seletores básicos são a espinha dorsal do CSS, permitindo que você alcance e estilize elementos HTML de maneira eficaz.

**1.1 - Seletores de Elemento**

Os seletores de elemento são simplesmente o nome do elemento HTML que você deseja estilizar. Veja um exemplo:

```css
p {
  color: blue;
}
```

Este código tornará todos os parágrafos (`<p>`) em azul.

**1.2 - Seletores de Classe**

As classes oferecem uma maneira eficaz de estilizar vários elementos da mesma maneira. Veja como você pode usar uma classe:

```css
.button {
  background-color: #008CBA;
  color: white;
}
```

Aqui, todos os elementos com a classe "button" terão um fundo azul e texto branco.

**1.3 - Seletores de ID**

IDs são únicos em uma página e permitem estilos específicos para um único elemento. Exemplo:

```css
#destaque {
  font-weight: bold;
  color: red;
}
```

Este código tornará o elemento com o ID "destaque" em negrito e vermelho.

---

**Capítulo 2: Seletores Avançados**

*Refinando sua Habilidade de Seleção*

Agora, vamos explorar seletores mais avançados para alcançar elementos específicos com maior precisão.

**2.1 - Seletores de Descendência**

Eles permitem selecionar elementos que são descendentes de outro elemento. Exemplo:

```css
article p {
  font-style: italic;
}
```

Isso aplicará estilo apenas aos parágrafos dentro de elementos `<article>`.

**2.2 - Seletores de Filho Direto**

Semelhante ao anterior, mas apenas seleciona os filhos diretos do elemento. Exemplo:

```css
ul > li {
  list-style-type: square;
}
```

Estiliza apenas os itens de lista (`<li>`) diretamente dentro de uma lista não ordenada (`<ul>`).

**2.3 - Seletores de Atributo**

Estes são úteis para selecionar elementos com base em seus atributos. Exemplo:

```css
input[type="text"] {
  border: 1px solid #999;
}
```

Isso adicionará uma borda a todos os campos de texto.

---

**Capítulo 3: Seletores Avançados**

*Dominando a Arte da Seleção*

Agora, vamos explorar seletores mais avançados para alcançar elementos específicos com maior precisão.

**3.1 - Pseudo-classes**

Elas são usadas para selecionar elementos em estados específicos. Exemplo:

```css
a:hover {
  text-decoration: underline;
}
```

Este código sublinha um link quando o mouse está sobre ele.

**3.2 - Pseudo-elementos**

Semelhantes às pseudo-classes, mas selecionam partes específicas de um elemento. Exemplo:

```css
p::first-line {
  font-weight: bold;
}
```

Isso aplica negrito apenas à primeira linha de todos os parágrafos.

**3.3 - Seletores Combinadores**

Permitem combinar múltiplos seletores para uma regra. Exemplo:

```css
h2 + p {
  font-style: italic;
}
```

Isso tornará os parágrafos imediatamente após um título `<h2>` em itálico.

Com esses seletores, você está equipado para criar estilos robustos e precisos em seus projetos CSS. Explore, experimente e domine a arte da estilização!


## Prompt:
```
crie uma introdução para este conteúdo com um texto enxuto
```
## Resposta:
**Introdução: Desbravando o Universo Estilístico do CSS**

Bem-vindo a uma jornada épica pelo reino da estilização web! Dominar o CSS é essencial para qualquer desenvolvedor que busque criar experiências visuais extraordinárias. Neste eBook, mergulharemos nos segredos dos seletores CSS, desde os fundamentos básicos até as técnicas avançadas que transformarão seus projetos.

Prepare-se para explorar os poderosos seletores de elementos, classes e IDs que formam a base do seu arsenal estilístico. Avançaremos para técnicas mais refinadas, como seletores de descendência e pseudo-classes, que permitem um controle preciso sobre cada elemento na sua página. Juntos, embarcaremos em uma jornada pelo código, desvendando os mistérios do CSS e elevando suas habilidades de estilização a novas alturas.

Esteja preparado para se tornar um mestre na arte de dar estilo às suas criações web. Sem mais delongas, vamos iniciar essa incrível jornada pelo universo fascinante do CSS!