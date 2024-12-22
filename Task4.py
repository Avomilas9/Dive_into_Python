# Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ●--verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ●--repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse

def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description="Обработка числа и строки с опциями.")

    # Добавление обязательных аргументов
    parser.add_argument("number", type=int, help="Число для обработки.")
    parser.add_argument("text", type=str, help="Строка для вывода.")

    # Добавление опций
    parser.add_argument("--verbose", action="store_true", help="Включить подробный вывод.")
    parser.add_argument("--repeat", type=int, default=1, help="Сколько раз повторить строку (по умолчанию 1).")

    # Парсинг аргументов
    args = parser.parse_args()

    # Если установлен флаг --verbose, выводим дополнительную информацию
    if args.verbose:
        print(f"[INFO] Получено число: {args.number}")
        print(f"[INFO] Получена строка: {args.text}")
        print(f"[INFO] Повторять строку {args.repeat} раз(а)")

    # Повторение строки указанное количество раз
    for i in range(args.repeat):
        print(args.text)

if __name__ == "__main__":
    main()