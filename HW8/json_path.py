# Решить задания, которые не успели решить на семинаре.
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import json
import pandas as pd
import pickle


def path_to_dict (path: str) -> dict:
    data = {
        'name': os.path.basename(path),
        'size': os.path.getsize(path),
        'parent': os.path.relpath(os.path.join(path, os.pardir))
    }
    if os.path.isdir(path):
        data['type'] = "directory"
        data['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        data['type'] = "file"
    return data


with open('file.json', 'w', encoding='utf-8') as f_write:
    json.dump(path_to_dict('root_dir'), f_write, ensure_ascii=False, indent=2)



# JSON получился шикарный, но такие данные писать в csv - получилась жаба, пришлось костылить через pandas
pd.DataFrame(path_to_dict('root_dir')).to_csv('file.csv', index=False)

with open('file.pickle', 'wb') as f:
    pickle.dump(path_to_dict('root_dir'), f)
