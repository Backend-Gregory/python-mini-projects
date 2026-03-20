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
        self.watched[movie] = f"Оценка: {rating}"

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