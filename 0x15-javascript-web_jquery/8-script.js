$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, (data, textStatus) => {
    const movies = data.results;
    const titles = movies.map((movie, index) => `<li>${movie.title}</li>`);
    $('UL#list_movies').append(titles);
  });
});
