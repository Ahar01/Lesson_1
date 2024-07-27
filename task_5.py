# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import re
from datetime import datetime
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def get_nth_weekday_of_month(nth, weekday, month, year):
    weekdays = {
        'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6,
        '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6
    }
    months = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
        'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12,
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
    }

    weekday_num = weekdays.get(str(weekday).lower())
    month_num = months.get(str(month).lower())

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


def parse_date(text, nth=None, weekday=None, month=None):
    try:
        if text:
            match = re.match(r'(\d+)-[яй] (\S+|\d+) (\S+|\d+)', text)
            if not match:
                data = text.split()
                try:
                    nth = int(data[0])
                    weekday = data[1]
                    month = data[2]
                except Exception:
                    pass
            else:
                nth = int(match.group(1))
                weekday = match.group(2)
                month = match.group(3)

        current_date = datetime.now()
        nth = nth if nth is not None else 1
        weekday = weekday if weekday is not None else current_date.weekday()
        month = month if month is not None else current_date.month

        current_year = current_date.year
        date = get_nth_weekday_of_month(nth, weekday, month, current_year)
        return date.strftime('%Y-%m-%d')

    except Exception as e:
        logging.error(f"Error parsing date: {text} - {e}")
        return None


dt = input()
print(parse_date(dt))


