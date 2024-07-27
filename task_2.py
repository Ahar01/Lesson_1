# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging
# import os


FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
        'в строке {lineno:03d} функция "{funcName}()" ' \
        'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='a', filename='task_1_error.log',
                    encoding='utf-8')
logger = logging.getLogger('task_02')
#
# logging.basicConfig(format=FORMAT, style='{', level=logging.NOTSET, filemode='a', filename='task_2_1_error.log',
#                     encoding='utf-8')
handler2 = logging.FileHandler('task_2_1_error.log', mode='a', encoding='utf-8') # handler2 = logging.FileHandler(f"{__name__}.log, mode='a'")
handler2.setLevel(logging.DEBUG)
formatter2 = logging.Formatter(FORMAT, style='{')
handler2.setFormatter(formatter2)
logger.addHandler(handler2)


def my_loger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'result': result, 'args': args, **kwargs}
        logger.info(info_dict)
        logger.debug(info_dict)

        return result

    return wrapper


@my_loger
def sum_numbers(*args, **kwargs):
    return sum(args)

#
# def mult_numbers(*args, **kwargs):
#     return args[0] * args[1]
#
#
# mult_numbers = my_loger(mult_numbers)
# mult_numbers(100, 999)


if __name__ == '__main__':
    sum_numbers(10, 5, 15, 16, z=8, c='Привет')
    sum_numbers(x=20, y=3)
    sum_numbers(100, 999)
