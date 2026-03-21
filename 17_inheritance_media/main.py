class Media:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating
    
    def info(self):
        return f'{self.title} ({self.year})'

    def is_good(self):
        return self.rating >= 7

class Movie(Media):
    def __init__(self, title, year, rating, genre):
        super().__init__(title, year, rating)
        self.genre = genre
    
    def info(self):
        return f'{self.title} ({self.year}) - {self.genre}. Рейтинг: {self.rating}'