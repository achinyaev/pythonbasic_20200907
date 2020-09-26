import requests
import os
import unit.my_utils
from unit.my_utils import some

def get_html(url):
    #url = 'https://geekbrains.ru/'
    response = requests.get(url)
    return response.text

def get_img(url) -> bytes:
    response = requests.get(url)
    return response.content

def save_img(file_path, bytes):
    with open(file_path,'wb') as file:  # менеджер контекста
        file.write(bytes)



def save_html_to_file(file_path,html_text):
    with open(file_path,'w',encoding='UTF-8') as file:  # менеджер контекста
        file.write(html_text)

if __name__ == '__main__':
    file_name = 'temp.html'
    file_folder = os.path.dirname(__file__) # текущий каталог
    file_path = os.path.join(file_folder, file_name)
    html_text = get_html('http://geekbrains.ru')
    save_html_to_file(file_path,html_text)
    img_url = 'https://ichip.ru/images/cache/2020/5/20/fit_960_530_false_crop_1000_562_0_51_q90_408212_a7ed96f385b4f8eed2a34bb4a.webp'
    img_file = 'fit_960_530_false_crop_1000_562_0_51_q90_408212_a7ed96f385b4f8eed2a34bb4a.webp'
    image_bytes = get_img(img_url)
    save_img(img_file,image_bytes)

