async function fetchProfileData(){
    const url = 'https://raw.githubusercontent.com/maxwelldeveloper7/dio_cursos/main/javascript/criando_portifolio/data/profile.json'
    const fetching = await fetch(url)
    return await fetching.json()
}

