import time
import datetime

FILE = 'log.txt'
class logger:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        self.date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        self.time = datetime.strftime(datetime.now(), '%H-%M-%S')
        with open(FILE, 'a', encoding='utf-8') as log:
            log.write(f'[{self.date}] НАЧАЛО в {self.time}: {self.name}')
        return self