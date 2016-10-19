class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls, json_data):
        # return Movie(json_data['name'], json_data['genre'], json_data['watched'])
        return Movie(**json_data) # Create set of named parameters (argument unpacking)
