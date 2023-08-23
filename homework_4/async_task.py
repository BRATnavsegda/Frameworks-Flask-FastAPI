import asyncio
import time
from pathlib import Path


res = 0


async def sum_task(array):
    global res
    for i in array:
        res += i


async def async_task(arrays):
    start_time = time.time()
    tasks = [asyncio.create_task(sum_task(array)) for array in arrays]
    await asyncio.gather(*tasks)
    return f'Время Асинхронного подхода {time.time() - start_time:.4f}, Сумма элементов массива - {res} '


