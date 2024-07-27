# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import re
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def get_nth_weekday_of_month(nth, weekday, month, year):
    weekdays = {
        'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6
    }
    months = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
        'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
    }

    weekday_num = weekdays.get(weekday.lower())
    month_num = months.get(month.lower())

    if weekday_num is None or month_num is None:
        raise ValueError("Invalid weekday or month")

    first_day_of_month = datetime(year, month_num, 1)
    first_weekday = first_day_of_month.weekday()

    if first_weekday <= weekday_num:
        day_of_month = 1 + (weekday_num - first_weekday)
    else:
        day_of_month = 1 + (7 - first_weekday + weekday_num)

    day_of_month += (nth - 1) * 7

    return first_day_of_month.replace(day=day_of_month)


def parse_date(text):
    try:
        match = re.match(r'(\d+)-[яй] (\S+) (\S+)', text)
        if not match:
            raise ValueError("Invalid format")

        nth = int(match.group(1))
        weekday = match.group(2)
        month = match.group(3)

        current_year = datetime.now().year
        date = get_nth_weekday_of_month(nth, weekday, month, current_year)
        return date.strftime('%Y-%m-%d')

    except Exception as e:
        logging.error(f"Error parsing date: {text} - {e}")
        return None


print(parse_date("1-й четверг ноября"))  # Пример корректного ввода
print(parse_date("3-я среда мая"))  # Пример корректного ввода
print(parse_date("5-я суббота июля"))  # Пример некорректного ввода (если в месяце нет 5-й субботы)
print(parse_date("неправильный формат"))  # Пример некорректного ввода
