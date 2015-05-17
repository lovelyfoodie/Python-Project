import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")



avatar = media.Movie("Avatar", "A fatansy world of peeps",
                     "http://benfx.com/images/wordpressImages/WP_poster_AVATAR.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

nodame = media.Movie("Nodame Cantabile", "A girl who learns love and sheet music",
                      "http://img.photobucket.com/albums/v418/DarkScape/dorama/nodame.gif",
                      "https://www.youtube.com/watch?v=XjWiWr1SVnY&noredirect=1")

schoolOfRock = media.Movie("School of Rock", "A high school music teacher",
                      "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                      "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnightInParis = media.Movie("Midnight in Paris", "Some romance story?",
                      "http://www.dvd-covers.org/d/272782-5/Midnight_in_Paris_label_copy.jpg",
                      "https://www.youtube.com/watch?v=atLg2wQQxvU")

ratatouille = media.Movie("Ratatouille", "A chef rat",
                      "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                      "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#create a list of movies to pass into the open movies function in fresh tomatoes
movies = [toy_story, avatar, nodame, schoolOfRock, midnightInParis, ratatouille]

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__name__)
print(media.Movie.__module__)
#fresh_tomatoes.open_movies_page(movies)

#print(toy_story.storyline)
#nodame.play_trailer()
#avatar.play_trailer()
#print(avatar.storyline)


