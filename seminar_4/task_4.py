# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте потоки.
#

import os
import threading
import time
from pathlib import Path


def count_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        words = len(f.read().split())

        print(f"{file} count {words} words")


threads = []
start_time = time.time()

files = os.listdir('.')

for file in files:
    f = Path(file)
    if f.is_file():
        thread = threading.Thread(target=count_words, args=[f])
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()

print(f'{time.time() - start_time}')