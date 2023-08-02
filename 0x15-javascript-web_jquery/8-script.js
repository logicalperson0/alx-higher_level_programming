const moviesUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $movieListing = $('#list_movies');

$.ajax({
  url: moviesUrl,
  dataType: 'json'
}).done((data) => {
  const Starmovies = data.results;

  for (let x = 0; x < Starmovies.length; x++) {
    const starTitle = Starmovies[x].title;
    const li = `<li>${starTitle}</li>`;
    $movieListing.append(li);
  }
});