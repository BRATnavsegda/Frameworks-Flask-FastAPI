import multiprocessing
import time

# res = multiprocessing.Value('i', 0)
#
#
# def result(array):
#     global res
#     result = 0
#     for num in array:
#         result += num
#     with res.get_lock():
#         res.value += result
#
# def multiproc_task(arrays):
#     processes = []
#     start_time = time.time()
#     for array in arrays:
#         proc = multiprocessing.Process(target=result, args=(array, ))
#         processes.append(proc)
#         proc.start()
#     for proc in processes:
#         proc.join()
#
#     return f'Время многопроцессорного подхода {time.time() - start_time:.4f}, Сумма элементов массива - {res.value} '


def sum_list(lst):
    res = 0
    for i in lst:
        res += i

    return res


def multiproc_task(sep_list):
    start_time = time.time()

    pool = multiprocessing.Pool(processes=4)
    result = pool.map(sum_list, sep_list)
    return f'Время многопроцессорного подхода {time.time() - start_time:.4f}, Сумма элементов массива - {sum(result)} '

