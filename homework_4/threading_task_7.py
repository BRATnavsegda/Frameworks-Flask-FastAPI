import threading
import time


res = 0


def result(array):
    global res
    for num in array:
        res += num


def my_threads(arrays):
    threads = []
    thread_time = time.time()

    for array in arrays:
        t = threading.Thread(target=result, args=(array,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return f'Время многопоточного подхода {time.time() - thread_time:.4f}, Сумма элементов массива - {res} '
