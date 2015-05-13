import fresh_tomatoes
import media


wreck_it_ralph = media.Movie("Wreck-It Ralph",
                             "2012",
                             "Rich Moore",
                             """A video game villain wants to be a hero and
                             sets out to fulfill his dream, but his quest
                             brings havoc to the whole arcade where he
                             lives.""",
                             ("http://ia.media-imdb.com/images/M/MV5BNzMxNTExO"
                              "TkyMF5BMl5BanBnXkFtZTcwMzEyNDc0OA@@._V1_SX640SY"
                              "720_.jpg"),
                             "https://youtu.be/87E6N7ToCxs")
print(wreck_it_ralph.poster_image_url)

mind_game = media.Movie("Mind Game",
                        "2004",
                        "Masaaki Yuasa, Koji Morimoto",
                        """The film follows Nishi, a loser who has a crush on
                        his childhood girlfriend. After an encounter with the
                        Japanese mafia, the film follows Nishi as he journeys
                        to heaven and back, and ends up trapped in an even
                        more unlikely place. Nishi (and some friends) attempt
                        to break out of their trap, and discover what it truly
                        means to be alive along the way""",
                        ("http://userdisk.webry.biglobe.ne.jp/007/148/47/N00"
                         "0/000/001/125700329351116101248.JPG"),
                        "https://youtu.be/XU4EfF85u60")

waking_life = media.Movie("Waking Life",
                          "2001",
                          "Richard Linklater",
                          """A man shuffles through a dream meeting various
                          people and discussing the meanings and purposes of
                          the universe.""",
                          ("http://ia.media-imdb.com/images/M/MV5BMjExMzA0MT"
                           "UxOF5BMl5BanBnXkFtZTcwMDk3MjMyMQ@@._V1_SX640_SY7"
                           "20_.jpg"),
                          "https://youtu.be/uk2DeTet98o")

the_wind_rises = media.Movie("The Wind Rises",
                             "2013",
                             "Hayao Miyazaki",
                             """A look at the life of Jiro Horikoshi, the man
                             who designed Japanese fighter planes during World
                             War II.""",
                             ("http://ia.media-imdb.com/images/M/MV5BMTU4NDg0"
                              "MzkzNV5BMl5BanBnXkFtZTgwODA3Mzc1MDE@._V1_SX640"
                              "_SY720_.jpg"),
                             "https://youtu.be/imtdgdGOB6Q")

tekkonkinkreet = media.Movie("Tekkonkinkreet",
                             "2006",
                             "Michael Arias",
                             """BLACK and WHITE, two street urchins, battle an
                             array of old-word Yakuza and alien assassins
                             vying to rule the decaying metropolis of Treasure
                             Town - where the moon smiles and young boys can
                             fly.""",
                             ("http://ia.media-imdb.com/images/M/MV5BMTkzMDMz"
                              "MzQwOV5BMl5BanBnXkFtZTgwNDAxNzkwMzE@._V1_SX640"
                              "_SY720_.jpg"),
                             "https://youtu.be/PfQjc2hs34Y")

the_tale_of_princess_kaguya = media.Movie("The Tale of Princess Kaguya",
                                          "2013",
                                          "Isao Takahata",
                                          """Found inside a shining stalk of
                                          bamboo by an old bamboo cutter and
                                          his wife, a tiny girl grows rapidly
                                          in to an exquisite young lady. The
                                          mysterious young princess enthralls
                                          all who encounter her - but
                                          ultimately she must confront her
                                          fate, the punishment for her
                                          crime.""",
                                          ("http://ia.media-imdb.com/images/M"
                                           "/MV5BMTg0ODYyODUzOF5BMl5BanBnXkFt"
                                           "ZTgwMzYzODY3MjE@._V1_SX640_SY720_"
                                           ".jpg"),
                                          "https://youtu.be/tM6hcHp0_kU")

the_girl_who_leapt_through_time = media.Movie("""The Girl Who Leapt Through
                                              Time""",
                                              "2006",
                                              "Mamoru Hosoda",
                                              """A teenage girl finds that she
                                              has the ability to leap through
                                              time. With her newfound power,
                                              she tries to use it to her
                                              advantage, but soon finds that
                                              tampering with time can lead to
                                              some rather discomforting
                                              results.""",
                                              ("http://ia.media-imdb.com/imag"
                                               "es/M/MV5BMTg0ODYzODg4OV5BMl5B"
                                               "anBnXkFtZTcwNDM3NzAwMg@@._V1_"
                                               "SX640_SY720_.jpg"),
                                              "https://youtu.be/U_ULXRMvU7k")


movies = [wreck_it_ralph, mind_game, waking_life, the_wind_rises,
          tekkonkinkreet, the_tale_of_princess_kaguya,
          the_girl_who_leapt_through_time]

fresh_tomatoes.open_movies_page(movies)
