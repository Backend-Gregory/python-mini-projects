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
        base = super().info()
        return f'{base} - {self.genre}. Рейтинг: {self.rating}'

class Series(Media):
    def __init__(self, title, year, rating, seasons, episodes):
        super().__init__(title, year, rating)
        self.seasons = seasons
        self.episodes = episodes

    def info(self):
        base = super().info()
        return f'{base} - Сезон {self.seasons}: Серия: {self.episodes}. Рейтинг: {self.rating}'
    
    def is_good(self):
        return self.rating >= 8