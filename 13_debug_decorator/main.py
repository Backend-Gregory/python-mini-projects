import time
from datetime import datetime
def log_calls(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        data = now.strftime('%Y-%m-%d')
        time_now = now.strftime('%H:%M')
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time() - start
        name = func.__name__

        try:
            with open('log.txt', 'a', encoding='utf-8') as log:
                log.write(f'Дата: {data}\n')
                log.write(f'Время вызова декоратора: {time_now}\n')
                log.write(f'→ {name} {args, kwargs}\n')
                log.write(f'← Результат: {res}\n')
                log.write(f'⏱ Время выполнения: {end:.4f} сек\n\n')
        except (IOError, PermissionError) as e:
            print(f"⚠️ Не удалось записать лог: {e}")
        except Exception as e:
            print(f'Неизвестная ошибка: {e}')

        return res
    return wrapper