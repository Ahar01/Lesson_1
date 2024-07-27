# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

import logging

FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='a', filename='Error.log',
                    encoding='utf-8')
logger = logging.getLogger('task_1_1')

def get_num():
    while True:
        num = input('Enter a number: ')
        try:
            res = int(num)
            return res
        except ValueError as e:
            try:
                res = float(num)
                return res
            except ValueError as e:
                logger.error('ValueError')


if __name__ == '__main__':
    print(get_num())
