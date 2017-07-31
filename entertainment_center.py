import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

print(avatar.storyline)
#avatar.show_trailer()

saving_private_ryan = media.Movie("Saving Private Ryan",
                        "A group of selected men put themselves in harms way to rescue one private that lost all 4 of his brothers",
                        "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                        "https://www.youtube.com/watch?v=zwhP5b4tD6g")

print(saving_private_ryan.storyline)
#saving_private_ryan.show_trailer()

movies = [toy_story, avatar, saving_private_ryan]
fresh_tomatoes.open_movies_page(movies)
