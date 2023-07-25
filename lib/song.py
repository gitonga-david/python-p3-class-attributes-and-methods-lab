class Song:

    count = 0
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_genre_count()
        self.add_artist_count()

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    def add_to_artists(self, artist):
        self.artists.append(artist)

    @classmethod
    def add_genre_count(cls):
        cls.genre_count = {genre: cls.genres.count(
            genre) for genre in cls.genres}

    @classmethod
    def add_artist_count(cls):
        cls.artist_count = {artist: cls.artists.count(
            artist) for artist in cls.artists}
