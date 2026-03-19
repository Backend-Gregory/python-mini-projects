class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
        self.similar = []

    def add_similar(self, movie):
        self.similar.append(movie)

    def get_info(self):
        return f"{self.title} ({self.year}) - {self.genre}, Рейтинг: {self.rating}"


class User:
    def __init__(self, name):
        self.name = name
        self.watched = {}

    def watch(self, movie, rating):
        self.watched[movie] = f"Оценка: {rating}"