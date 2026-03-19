class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
        self.similar = []
    
    def add_similar(self, movie):
        self.similar.append(movie)