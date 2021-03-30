from User import User
from movie import Movie

user = User("Tlokz")
my_movie = Movie("The Matrix", "Sci-fi", True)

user.movies.append(my_movie)
print(user)
print(user.watched_movies())



