# Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta

def get_future_date(days):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
   
    :param days: Количество дней от текущей даты (int)
    :return: Дата в формате YYYY-MM-DD
    """
    # Получение текущей даты
    current_date = datetime.now()
   
    # Вычисление будущей даты
    future_date = current_date + timedelta(days=days)
   
    # Форматирование будущей даты
    formatted_date = future_date.strftime('%Y-%m-%d')
   
    return formatted_date

# Пример использования
days_to_add = 10
result = get_future_date(days_to_add)
print(f"Дата через {days_to_add} дней: {result}")