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
    
def show_media_list(media_list):
    for i in media_list:
        info = i.info()
        good = '✅' if i.is_good() else '❌'
        print(info, good)

media_list = []

print('1. Добавить фильм')
print('2. Добавить сериал')
print('3. Показать все')
print('4. Выход')

num = int(input('Выберите действие: '))
if num == 1 or num == 2:
    title = input('Введите название: ')
    year = int(input('Введите год выхода фильма: '))
    rating = float(input('Оцените фильм от 1 до 10: '))
    if num == 1:
        genre = input('Введите жанр: ')
        obj = Movie(title, year, rating, genre)
    else:
        seasons = int(input('Введите сезон числом: '))
        episodes = int(input('Введите эпизод числом: '))
        obj = Series(title, year, rating, seasons, episodes)
    media_list.append(obj)