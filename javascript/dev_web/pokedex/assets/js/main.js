const pokemonList = document.getElementById('pokemonList');
const loadMoreButton = document.getElementById('loadMoreButton');
const detail = document.getElementsByClassName('pokemon');
const maxRecords = 151;
const limit = 10;
let offset = 0;


function loadPokemonItens(offset, limit) {
    pokeApi.getPokemons(offset, limit).then((pekemons = []) => {
        const newHtml = pekemons.map((pokemon) => `
            <li class="pokemon ${pokemon.type}" data-pokemon='${JSON.stringify(pokemon)}'>
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
    }).then(() => {
        addClickEventToPokemonItems();
    });
}


function addClickEventToPokemonItems() {
    const pokemonItems = document.querySelectorAll('.pokemon');
    pokemonItems.forEach(item => {
        item.addEventListener('click', function() {
            const pokemonData = this.getAttribute('data-pokemon');
            localStorage.setItem('currentPokemon', pokemonData);
            window.location.href = 'detail.html';
        });
    });
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
