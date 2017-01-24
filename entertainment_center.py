import media
import fresh_tomatoes

# Six instances of the class Movie
wizard_of_oz = media.Movie(
    "Wizard of oz",
    "https://upload.wikimedia.org/wikipedia/commons/6/69/Wizard_of_oz_movie_poster.jpg",
    "https://www.youtube.com/watch?v=Cg8PrPVqCd8")

jurassic_park = media.Movie(
    "Jurassic Park",
    "http://img.moviepostershop.com/jurassic-park-movie-poster-1992-1020141477.jpg",
    "https://youtu.be/lc0UehYemQA")

meet_me_in_stlouis = media.Movie(
    "Meet me in St. Louis",
    "https://upload.wikimedia.org/wikipedia/commons/1/1a/Meet_Me_in_St._Louis_poster.jpg",
    "https://youtu.be/hdEouRM7Xv8")

the_exorcist = media.Movie(
    "The Exorcist",
    "http://vignette3.wikia.nocookie.net/uncyclopedia/images/5/51/Exorcist.jpg/revision/20111231123200",
    "https://youtu.be/YDGw1MTEe9k")

zombieland = media.Movie(
    "Zombieland",
    "http://www.freemovieposters.net/posters/zombieland_2009_2439_poster.jpg",
    "https://youtu.be/8m9EVP8X7N8")

dancer_in_the_dark = media.Movie(
    "Dancer in the Dark",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Dancer_in_the_Dark_movie_poster.jpg",
    "https://youtu.be/53vr9EiOH7g")

movies = [wizard_of_oz, jurassic_park, meet_me_in_stlouis, the_exorcist, zombieland, dancer_in_the_dark]

# Create and open the movie website .html file

fresh_tomatoes.open_movies_page(movies)
