# Работа с текущим временем и датой
# Напишите скрипт,который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DDHH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime

# Получение текущей даты и времени
now = datetime.now()

# Форматирование даты и времени
formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')

# Получение дня недели
day_of_week = now.strftime('%A')  # Полное название дня недели

# Получение номера недели в году
week_number = now.isocalendar()[1]

# Вывод результатов
print(f"Текущая дата и время: {formatted_date_time}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")
