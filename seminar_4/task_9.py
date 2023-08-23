# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле,
# название которого соответствует названию изображения в URL-адресе.
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# - Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# - Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# - Программа должна выводить в консоль информацию о времени скачивания каждого изображения
# и общем времени выполнения программы.
#

import requests
import threading
import time

urls = ['https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg',
'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-48.jpg',
'http://chudo-prirody.com/uploads/posts/2021-08/1628917339_87-p-foto-malenkikh-rizhikh-kotyat-98.jpg',
'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663579262_51-mykaleidoscope-ru-p-veselie-koshechki-krasivo-54.jpg',
'https://www.ejin.ru/wp-content/uploads/2017/09/9-1022.jpg',
'https://s1.1zoom.ru/b5050/667/Cats_Kittens_Grass_Bokeh_590075_3840x2400.jpg',
'https://www.sunny-cat.ru/datas/users/1-elefant017.jpg',
'https://w-dog.ru/wallpapers/0/14/503116390422985/porodistyj-kotenok-na-beloj-prostyne.jpg',
'https://rare-gallery.com/uploads/posts/881890-Cats-Grass-Kittens-Bokeh.jpg',
'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-47.jpg',
]


def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'

    with open('task_9_files/' + filename, "wb") as f:
        f.write(response.content)

    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
