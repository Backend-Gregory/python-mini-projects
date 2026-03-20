import json
from collections import Counter
import os

FILE_MOVIES = 'movies.json'
FILE_USERS = 'users.json'
MIN_COUNT = 3

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
        self.watched[movie] = rating

class Recommender:
    @staticmethod
    def top_rated(all_movies, n):
        return sorted(all_movies, key=lambda m: m.rating, reverse=True)[:n]
    
    @staticmethod
    def by_genre(watched, all_movies):
        count_genre = Counter()
        sum_rating_genre = {}
        for movie in watched:
            genre = movie.genre
            sum_rating_genre[genre] = sum_rating_genre.get(genre, 0) + watched[movie]
            count_genre[genre] += 1
        
        if not sum_rating_genre:
            return []
        
        favorite = max(sum_rating_genre, key=lambda g: sum_rating_genre[g] / count_genre[g] if count_genre[g] >= MIN_COUNT else 0)

        candidates = [
            m for m in all_movies
            if m.genre == favorite and m not in watched
        ]

        return sorted(candidates, key=lambda m: m.rating, reverse=True)[:3]
    
def find_movie_by_title(title, movie_dict):
    return movie_dict.get(title)

def watched_to_strings(watched):
    return {movie.title: rating for movie, rating in watched.items()}

def strings_to_watched(watched_dict, movie_dict):
    result = {}
    for title, rating in watched_dict.items():
        movie = movie_dict.get(title)
        if movie:
            result[movie] = rating
    return result

def save_users(users, movie_dict):
    data_to_save = []
    for u in users:
        data_to_save.append({
            "name": u["name"],
            "watched": watched_to_strings(u["watched"])
        })
    with open(FILE_USERS, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=2)

def load_users(movie_dict):
    if not os.path.exists(FILE_USERS):
        return [], []
    
    try:
        with open(FILE_USERS, encoding='utf-8') as f:
            raw_users = json.load(f)
    except json.JSONDecodeError:
        print('Ошибка! Файл пользователей поврежден. Создаю новый')
        return [], []
    
    users = []
    name_users = []
    for raw in raw_users:
        watched = strings_to_watched(raw["watched"], movie_dict)
        users.append({
            "name": raw["name"],
            "watched": watched
        })
        name_users.append(raw["name"])
    return users, name_users

try:
    with open(FILE_MOVIES, encoding='utf-8') as f:
        raw_movies = json.load(f)
except FileNotFoundError:
    print("Файл фильмов не найден")
    exit()
except json.JSONDecodeError:
    print('Файл фильмов поврежден')
    exit()

all_movies = []
for item in raw_movies:
    title = item['title']
    year = item["release_date"][:4] if item["release_date"] else "неизвестно"
    try:
        genres_data = json.loads(item["genres"])
        genres_list = [g['name'] for g in genres_data]
        genre_str = ', '.join(genres_list)
    except:
        genre_str = "неизвестно"
    
    try:
        rating = float(item["vote_average"])
    except (TypeError, ValueError):
        rating = 0.0
    
    all_movies.append(Movie(title, year, genre_str, rating))

movie_by_title = {m.title: m for m in all_movies}

users, name_users = load_users(movie_by_title)

username = input("Введите имя: ")
user = User(username)

if username not in name_users:
    users.append({"name": username, "watched": {}})
    save_users(users, movie_by_title)
else:
    for u in users:
        if u["name"] == username:
            user.watched = u["watched"]
            break

while True:
    print(f"\nПривет, {username}!")
    print("1. Добавить просмотр")
    print("2. Получить рекомендации")
    print("3. Выйти")

    try:
        choice = int(input("Выбери действие: "))
        if choice not in [1, 2, 3]:
            print("Ошибка! Введите 1, 2 или 3")
            continue
    except ValueError:
        print("Ошибка! Введите число")
        continue

    if choice == 1:
        title = input('Введите просмотренный фильм: ').strip()
        if not title:
            print('Ошибка! Название не может быть пустым')
            continue

        try:
            rating = int(input('Оценка (1-10): '))
            if not (1 <= rating <= 10):
                print('Ошибка! Оценка от 1 до 10')
                continue
        except ValueError:
            print('Ошибка! Введите число')
            continue

        movie = movie_by_title.get(title)
        if not movie:
            print("Фильм не найден")
            continue

        user.watch(movie, rating)
        
        for i, u in enumerate(users):
            if u["name"] == username:
                users[i]["watched"] = user.watched
                break
        
        save_users(users, movie_by_title)
        print(f"✅ Добавлено: {movie.title} — {rating}")

    elif choice == 2:
        if not user.watched:
            print("Вы ещё не оценили ни одного фильма. Добавьте просмотры!")
            continue
        
        rec_rating = Recommender.top_rated(all_movies, 3)
        rec_genre = Recommender.by_genre(user.watched, all_movies)
        recs = set(rec_rating + rec_genre)
        
        print("\nРекомендации:")
        for m in recs:
            if m not in user.watched:
                print(m.get_info())

    elif choice == 3:
        break