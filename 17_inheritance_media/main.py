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

def valid(text_value, text_valid, e=int):
    while True:
        try:
            value = e(input(text_value))
            if value:
                return value
            else:
                print(text_valid)
        except ValueError:
            print(text_valid)

media_list = []

while True:
    print('\n1. Добавить фильм')
    print('2. Добавить сериал')
    print('3. Показать все')
    print('4. Выход')
    num = valid('Выберите действие (1-4): ', 'Введите число')
    if not (1 <= num <= 4):
        print('Введите число от 1 до 4')
        continue

    if num == 1 or num == 2:
        title = valid('\nВведите название: ', 'Название не может быть пустым', str)
        year = valid('Введите год выхода: ', 'Год должен быть числом')
        rating = valid('Введите рейтинг от 1 до 10 например 8.9: ', 'Рейтинг должен быть числом', float)
        if num == 1:
            genre = valid('Введите жанр: ', 'Жанр не может быть пустым', str)
            obj = Movie(title, year, rating, genre)
        else:
            seasons = valid('Введите сезон числом: ', 'Сезон должен быть числом')
            episodes = valid('Введите эпизод числом: ', 'Эпизод должен быть числом')
            obj = Series(title, year, rating, seasons, episodes)
        media_list.append(obj)
    elif num == 3:
        if media_list:
            show_media_list(media_list)
        else:
            print('Вы не добавили ни одного фильма и сериала')
    else:
        break