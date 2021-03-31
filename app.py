from User import User
from movie import Movie


user = User.load_from_file('Tlokz.txt')
print(user.name)
print(user.movies)



