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
        addDetailClickEvent();
    })
}

function addDetailClickEvent() {
    const details = document.getElementsByClassName('detail');
    for (let i = 0; i < details.length; i++) {
        details[i].addEventListener('click', () => {
            console.log('Detail clicked:', details[i]);
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
