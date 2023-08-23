# Задание №7
# * Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# * При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# * В каждом решении нужно вывести время выполнения
# вычислений.
import asyncio
import time
from random import randint

from homework_4.async_task import async_task as at
from homework_4.multiprocessing_task import multiproc_task as multi
from homework_4.single_task_7 import single_task as st
from homework_4.threading_task_7 import my_threads as mt

if __name__ == '__main__':
    start_time = time.time()
    my_array = [randint(1, 100) for i in range(1, 10_000_001)]
    chunk_size = len(my_array) // 4
    chunks = [my_array[i:i+chunk_size] for i in range(0, len(my_array), chunk_size)]
    print(f'Время создания массива {time.time() - start_time:.4f}')

    print(st(chunks))
    print(mt(chunks))
    print(multi(chunks))
    print(asyncio.run(at(chunks)))

    print(f'Общее время выполнения программы {time.time() - start_time:.4f}')


# "C:\Users\TESO\Desktop\Lessions\Frameworks Flask & FastAPI\venv\Scripts\python.exe" "C:\Users\TESO\Desktop\Lessions\Frameworks Flask & FastAPI\homework_4\task_7.py"
# Время создания массива 63.9680
# Время синхронного подхода 5.3996, Сумма элементов массива - 5049954549
# Время многопоточного подхода 5.3627, Сумма элементов массива - 5049954549
# Время многопроцессорного подхода 6.2170, Сумма элементов массива - 5049954549
# Общее время выполнения программы 80.9682
#
# Process finished with exit code 0




