import time
def log_calls(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time() - start
        name = func.__name__
        print(f'<<< {name} {args, kwargs}')
        print(f'Вызов {name} с args={args}, kwargs={kwargs}')
        print(f'Результат: {res}')
        print(f'Время выполнения: {end}')
        return res
    return wrapper