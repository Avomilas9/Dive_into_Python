# Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

# Настройка логгера
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Создание обработчика для сообщений уровней DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)

# Создание обработчика для сообщений уровней WARNING и выше
warning_errors_handler = logging.FileHandler('warnings_errors.log')
warning_errors_handler.setLevel(logging.WARNING)

# Настройка форматов сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_info_handler.setFormatter(formatter)
warning_errors_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warning_errors_handler)

# Логирование сообщений различных уровней
logger.debug('Сообщение уровня DEBUG')
logger.info('Сообщение уровня INFO')
logger.warning('Сообщение уровня WARNING')
logger.error('Сообщение уровня ERROR')
logger.critical('Сообщение уровня CRITICAL')