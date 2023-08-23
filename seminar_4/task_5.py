# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте асинхронный подход.

import asyncio
import time
from pathlib import Path


my_directory = Path().cwd()
start_time = time.time()


async def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    split_text = text.split()
    print(f'{Path(file_path).stem}: {len(split_text)} words')


async def main():
    tasks = [asyncio.create_task(count_words(file)) for file in my_directory.rglob('*.py')]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print(f'{time.time() - start_time:.10f} sec.')
