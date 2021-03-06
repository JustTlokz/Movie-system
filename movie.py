class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return " Movie: {} / Genre: {}".format(self.name, self.genre)

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True


    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        return Movie(**json_data)
