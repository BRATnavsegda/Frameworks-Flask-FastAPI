import time

res = 0



def sum_task(array):
    global res
    for i in array:
        res += i


def single_task(arrays):
    start_time = time.time()
    for array in arrays:
        sum_task(array)

    return f'Время синхронного подхода {time.time() - start_time:.4f}, Сумма элементов массива - {res} '
