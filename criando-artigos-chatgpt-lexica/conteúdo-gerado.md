## Introdução
Diretivas no Angular são como regrinhas mágicas que você usa para dar superpoderes ao seu HTML. Elas ajudam a controlar como os elementos da sua página se comportam, como se fossem mini feitiços para o seu código.

## Diretivas de estruturais
Diretivas estruturais são como varinhas mágicas especiais que podem fazer aparecer ou sumir partes do seu HTML. Um exemplo é a `*ngIf`, que faz com que um pedaço do código só apareça se uma condição for verdadeira. Tipo um truque de mágica!

**Exemplos de diretivas estruturais:**
```html
<!-- Aparece só se a condição for verdadeira -->
<div *ngIf="mostrarMensagem">Olá, mundo!</div>

<!-- Repete o elemento para cada item na lista -->
<ul>
  <li *ngFor="let item of listaItens">{{ item }}</li>
</ul>
```

## Diretivas de atributos
Diretivas de atributos são como adesivos mágicos que você coloca nos elementos HTML para dar um toque especial a eles. Por exemplo, o `ngStyle` é uma diretiva de atributo que deixa você mudar o estilo de um elemento com facilidade.

**Exemplos de diretivas de atributos:**
```html
<!-- Muda a cor do texto com base em uma condição -->
<p [ngStyle]="{ color: condicao ? 'verde' : 'vermelho' }">Texto colorido!</p>

<!-- Adiciona ou remove a classe 'destaque' com base em uma condição -->
<div [ngClass]="{ 'destaque': mostrarDestaque }">Destaque!</div>
```

## Conclusão
Gostou deste conteúde? Ele foi gerado por inteligência artificial, más foi revisado por alguém 100% Humano.
Quer mais dicas de magia no mundo do front-end? 🚀 Sigam-me nas redes sociais para ficarem por dentro! Vamos criar juntos! 🌟 #FrontEndMagic #CodeWizard #TechJourney

**Fontes de produção**
- Ilustrações de capa: gerada pela lexica.art
- Conteúdo gerado por: ChatGPT e revisões humanas


**Hashtags:**
#Angular #Diretivas #Frontend
