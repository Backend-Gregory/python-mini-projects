import time
def log_calls(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time() - start
        name = func.__name__

        with open('log.txt', 'a', encoding='utf-8') as log:
            log.write(f'→ {name} {args, kwargs}\n')
            log.write(f'← Результат: {res}\n')
            log.write(f'⏱ Время выполнения: {end:.4f} сек\n\n')

        return res
    return wrapper