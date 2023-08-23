# Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.

import threading
import requests
import time

urls = [
'https://www.google.com/',
'https://www.python.org/',
'https://habr.com/ru/all/',
'https://yahoo.com/',
'https://youtube.com/',
'https://gb.ru/',
'https://dzen.ru/',
'https://rambler.ru/']


def get_urls(url):
    response = requests.get(url)
    filename = 'threads_' + url.replace('https://', '').replace('/', '').replace('.', '_') + '.html'
    with open('Files/' + filename, 'w', encoding='utf-8') as f:
        f.write(response.text)


start_time = time.time()
threads = []
for u in urls:
    t = threading.Thread(target=get_urls, args=[u])
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print(f'Time: {time.time() - start_time:.10f} sec.')