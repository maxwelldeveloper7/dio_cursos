const pokemonList = document.getElementById('pokemonList');
const loadMoreButton = document.getElementById('loadMoreButton');
const detail = document.getElementsByClassName('pokemon');
const maxRecords = 151;
const limit = 10;
let offset = 0;


function loadPokemonItens(offset, limit) {
    pokeApi.getPokemons(offset, limit).then((pekemons = []) => {
        const newHtml = pekemons.map((pokemon) => `
            <li class="pokemon ${pokemon.type}">
                <span class="number">#${pokemon.number}</span>
                <span class="name">${pokemon.name}</span>

                <div class="detail">
                    <ol class="types">
                        ${pokemon.types.map((type) => `<li class="type ${type}">${type}</li>`).join('')}
                    </ol>
                    <img src=${pokemon.photo}
                    alt="${pokemon.name}">
                </div>
            </li>
        `).join('');
        pokemonList.innerHTML += newHtml;
        addPokemonClickEvent();
    })
}


function addPokemonClickEvent() {
    const pokemonItems = document.getElementsByClassName('pokemon');
    for (let i = 0; i < pokemonItems.length; i++) {
        pokemonItems[i].addEventListener('click', function() {
            const pokemonData = {
                number: this.querySelector('.number').textContent,
                name: this.querySelector('.name').textContent,
                types: Array.from(this.querySelectorAll('.type')).map(type => type.textContent),
                photo: this.querySelector('img').src
            };

            // Armazenar os dados no localStorage para acesso em detail.html
            localStorage.setItem('currentPokemon', JSON.stringify(pokemonData));

            // Redirecionar para a página de detalhes
            window.location.href = 'detail.html';
        });
    }
}

loadPokemonItens(offset, limit);

loadMoreButton.addEventListener('click', () => {
    offset += limit;

    const qtdRecordNextPage = offset + limit;

    if (qtdRecordNextPage >= maxRecords) {
        const newLimit = maxRecords - offset;
        loadPokemonItens(offset, newLimit);
        loadMoreButton.parentElement.removeChild(loadMoreButton);
        return;
    } else {
        loadPokemonItens(offset, limit);
    }
});
