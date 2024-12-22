# Запуск из команднойстроки
# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования
logging.basicConfig(
    filename="directory_contents.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Определение namedtuple
FileInfo = namedtuple("FileInfo", ["name", "extension", "is_directory", "parent_directory"])

def collect_directory_contents(directory):
    """
    Собирает информацию о содержимом директории.
   
    :param directory: Путь до директории.
    :return: Список объектов FileInfo.
    """
    contents = []
   
    if not os.path.isdir(directory):
        logging.error(f"Указанный путь '{directory}' не является директорией.")
        return []

    # Перебираем содержимое директории
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        parent_directory = os.path.basename(directory)

        if os.path.isdir(item_path):
            file_info = FileInfo(name=item, extension="", is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(item)
            file_info = FileInfo(name=name, extension=extension.lstrip("."), is_directory=False, parent_directory=parent_directory)

        contents.append(file_info)
        logging.info(f"Обработан объект: {file_info}")

    return contents

def main():
    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Собрать информацию о содержимом директории.")
    parser.add_argument("directory", type=str, help="Путь до директории для обработки.")
    args = parser.parse_args()

    # Сбор информации
    directory_contents = collect_directory_contents(args.directory)

    # Вывод информации в консоль
    for item in directory_contents:
        print(item)

if __name__ == "__main__":
    main()