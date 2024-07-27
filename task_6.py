# Задание №6
# Напишите код, который запускается из командной строки  и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import sys
import logging
from collections import namedtuple

# Check if the directory path is provided as a command-line argument
if len(sys.argv) != 2:
    raise ValueError('Usage: python script.py <path_to_directory>')

# The full path is taken from the command line argument
full_path = sys.argv[1]
directory_path = full_path.split('/')
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

if len(directory_path) >= 2:
    parent_directory_name = directory_path[-2]
else:
    raise IndexError('неправильный данные')

data_list = list()
file_or_directory_name = directory_path[-1].split('.')
file_extension = None
if len(file_or_directory_name) == 2:
    file_extension = file_or_directory_name[1]
    file_or_directory_name = file_or_directory_name[0]

    if file_extension is not None:
        data_list.append(file_extension)
else:
    file_or_directory_name = file_or_directory_name[0]
data_list.append(parent_directory_name)
data_list.append(file_or_directory_name)

data = FileInfo(name=file_or_directory_name,
                extension=file_extension,
                is_directory=os.path.isdir(full_path),
                parent_directory=parent_directory_name)
FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='a', filename='data.log',
                    encoding='utf-8')
logger = logging.getLogger('task_6')
logger.info(data)
