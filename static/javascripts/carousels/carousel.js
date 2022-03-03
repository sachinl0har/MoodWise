const sliders = document.querySelector(".carousel-box")

var scrollPerClick;
var imagepadding = 20

showMovieData()

async function showMovieData() {
    const api_key = '05480c9212035931d585cd5d29ce6030';

    var result = await axios.get(
        "https://api.themoviedb.org/3/movie/popular?api_key=${api_key}&language=en-US&page=1"
    )

    console.log(result);
}
