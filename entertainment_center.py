import media
import fresh_tomatoes

the_martian = media.Movie("The Martian",
                        "A botanist/engineer trapped on Mars while the whole world watches",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                        "https://www.youtube.com/watch?v=ej3ioOneTy8")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                     "An odd group of criminals face off against a powerful villain to save the galaxy.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                     "https://www.youtube.com/watch?v=d96cjJhvlMA")

gladiator = media.Movie("Gladiator",
                        "A man robbed of his name and his dignity strives to win them back and gain the freedom of his people ",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcRuhegCaGHfcQc-Owpib9vGSO0hUlSUMTojO2s4ih8oXqHBw2ks",
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")
megamind = media.Movie("Megamind",
                       "A villian turned hero turned back villian becomes a hero.",
                       "http://cdn.collider.com/wp-content/uploads/megamind_movie_poster_will_ferrell_01.jpg",
                       "https://www.youtube.com/watch?v=NPI0eatlo_M")
ready_player_one = media.Movie("Ready Player One",
                               "Wade Watts joins a contest in OASIS, he finds himself becoming an unlikely hero in a reality-bending treasure hunt ",
                               "https://ih1.redbubble.net/image.223015233.6587/flat,800x800,070,f.u3.jpg",
                               "https://www.youtube.com/watch?v=znavw4akfoY")

alien = media.Movie("Alien",
                    "A crew travelling home through space receives a distress call from another vessel.",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcRGWyg4tnCNzaiUna7JSzV3I8NcwMaFhpulr1iWSd0FwW-r_89e",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

movies = [the_martian, guardians_of_the_galaxy, gladiator, megamind, ready_player_one, alien]
fresh_tomatoes.open_movies_page(movies)

