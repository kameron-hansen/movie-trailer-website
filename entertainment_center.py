import media
import fresh_tomatoes

# The Martian movie: Movie Title, Story Line, Poster Image, and Trailer URL
the_martian = media.Movie(
  "The Martian",
  "A botanist/engineer trapped on Mars"
  "while the whole world watches",
  "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",  # NOQA
  "https://www.youtube.com/watch?v=ej3ioOneTy8"
  )

# Guardians of the Galaxy movie:
# Movie Title, Story Line, Poster Image, and link to Trailer
guardians_of_the_galaxy = media.Movie(
  "Guardians of the Galaxy",
  "An odd group of criminals face off"
  "against a powerful villain to save the galaxy.",
  "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",  # NOQA
  "https://www.youtube.com/watch?v=d96cjJhvlMA"
  )

# Gladiator movie: Movie Title, Story Line, Poster Image, and Trailer URL
gladiator = media.Movie(
  "Gladiator",
  "A man robbed of his name and his dignity"
  "strives to win them back and gain the freedom of his people",
  "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks",  # NOQA
  "https://www.youtube.com/watch?v=Q-b7B8tOAQU"
  )

# MegaMind movie: Movie Title, Story Line, Poster Image, and Trailer URL
megamind = media.Movie(
  "Megamind",
  "A villian turned hero turned"
  "back villian becomes a hero.",
  "http://cdn.collider.com/wp-content/uploads/megamind_movie_poster_will_ferrell_01.jpg",  # NOQA
  "https://www.youtube.com/watch?v=NPI0eatlo_M"
  )

# Ready Player One movie:
# Movie Title, Story Line, Poster Image, and Trailer URL
ready_player_one = media.Movie(
  "Ready Player One",
  "Wade Watts joins a contest in OASIS,"
  "he finds himself becoming an unlikely hero"
  "in a reality-bending treasure hunt ",
  "https://ih1.redbubble.net/image.223015233.6587/flat,800x800,070,f.u3.jpg",  # NOQA
  "https://www.youtube.com/watch?v=znavw4akfoY"
  )

# Alien movie: Movie Title, Story Line, Poster Image, and Trailer URL
alien = media.Movie(
  "Alien",
  "A crew travelling home through space"
  "receives a distress call from another vessel.",
  "http://t2.gstatic.com/images?q=tbn:ANd9GcRGWyg4tnCNzaiUna7JSzV3I8NcwMaFhpulr1iWSd0FwW-r_89e",  # NOQA
  "https://www.youtube.com/watch?v=LjLamj-b0I8"
  )

# Set which movies will be passed to media.py
movies = [
  the_martian,
  guardians_of_the_galaxy,
  gladiator,
  megamind,
  ready_player_one,
  alien
  ]

# Use webbrowser to open the file fresh_tomatoes.py
# fresh_tomatoes.py has the html needed for the movie website
fresh_tomatoes.open_movies_page(movies)
