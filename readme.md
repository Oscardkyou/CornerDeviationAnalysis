# Анализ эффективности модели предсказания углов комнаты

Репозиторий включает код и анализ для оценки эффективности модели, предсказывающей количество углов в комнате, на основе отклонений пола и потолка от эталонных значений. Анализ осуществляется с использованием Python, pandas для обработки данных и matplotlib для визуализации результатов.

## Цель

Основной целью проекта является оценка точности модели в предсказании количества углов комнаты. Это достигается путем сравнения эталонного количества углов (`Gt_corners`) с количеством углов, определенных моделью (`Rb_corners`), а также анализа отклонений в градусах (среднее, максимальное, минимальное и т.д.).

## Структура Репозитория

- `data/`: Папка, содержащая исходные данные для анализа.
- `notebooks/`: Jupyter notebooks с кодом и анализом данных.
- `src/`: Исходный код модели и другие необходимые скрипты для анализа.
- `requirements.txt`: Файл, содержащий необходимые библиотеки для проекта.

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер.
2. Установите необходимые библиотеки, запустив `pip install -r requirements.txt` в терминале.

## Использование

- Откройте Jupyter notebook в папке `notebooks/` для просмотра и анализа данных.
- Исходный код модели находится в папке `src/`.

## Выводы

Результаты анализа и выводы можно найти в конце Jupyter notebook в папке `notebooks/`.
