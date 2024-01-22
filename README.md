## Определение стоимости недвижимости в Амстердаме

### Описание проекта
Этот проект представляет собой простую модель прогнозирования стоимости недвижимости в Амстердаме.


### Цель и задачи проекта
**Цель проекта:** провести анализ данных, размещенные на [Kaggle](https://www.kaggle.com/datasets/thomasnibb/amsterdam-house-price-prediction), и на их основе обучить модель, предсказывающую стоимость недвижимости на основе признаков.

**Задачи проекта:**
1. Исследовательский анализ данных;
2. Предварительная обработка данных;
3. Обучить модель и выбрать систему оценки качества;
4. Создать телеграм бота, способного обрабатывать запросы пользователя;
5. Развёртывание сервера, установка среды, загрузка бота на сервер.

### Этапы проекта
|№|Название этапа|Решаемая задача|Описание этапа|Инструменты|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 1  | Исследование данных.  | Найти закономерности, аномалии и зависимости в данных.  | Анализ основных свойств данных, выявление распределений, общих зависимостей и аномалий с помощью инструментов визуализации.  |   Jupyter Lab, NumPy, Matplotlib, Seaborn, Pandas, Folium  |
| 2  | Предварительная обработка данных.  | Подготовка данных к подаче в модели.  | Генерация новых признаков, работа с аномалиями и выбросами, разделение данных на выборки, просчет константной модели, выбор системы оценки, созадние PipeLine для подачи в модель.   | Jupyter Lab, Sklearn, NumPy, Pandas |
| 3  | Обучение модели.  | Обучение модели.  | На основе предобработанных данных обучить модели, предсказывающую стоимость недвижимости, найти лучшую модель по качеству.  | Jupyter Lab, Sklearn, CatBoost, LightGBM, Joblib  |
| 4  | Создание телеграм бота.  | Создание телеграм бота.  | Создание телеграм бота с использование API. Создание логики, плашек и кнопок. Интеграция модели в бота. Тестирование на локальной машине.  | PyCharm, Aiogram, Pandas, Joblib, Sklearn, CatBoost  |
| 5  | Развёртывание сервера.  | Развёртка сервера, установка среды.  | Настройка UBUNTU сервера через протоколы SSH, установка среды, загрузка бота на сервер, запуск в фоновом режиме.  | Linux, API, SSH  |

### Файлы
1. Блокнот с исследовательским анализом, предобработкой данных и моделями: [Jupyter](https://nbviewer.org/github/PaulSpirin/Bot-on-real-estate-in-Amsterdam/blob/main/house_price.ipynb);
2. Python файл со всей логикой телеграм бота можно найти [тут](https://github.com/PaulSpirin/Bot-on-real-estate-in-Amsterdam/blob/main/charm_am_bot/handlers.py);
3. Python файл с интеграцие модели в бота можно найти [тут](https://github.com/PaulSpirin/Bot-on-real-estate-in-Amsterdam/blob/main/charm_am_bot/models.py);
4. Другие файлы Вы можете найти в этом [репозитории](https://github.com/PaulSpirin/Bot-on-real-estate-in-Amsterdam/tree/main/charm_am_bot).

### Данные
Все данные были взяты с [Kaggle](https://www.kaggle.com/datasets/thomasnibb/amsterdam-house-price-prediction).

### Лицензия
Распространяется по лицензии GNU General Public License v3.0. см. [тут](https://github.com/PaulSpirin/Bot-on-real-estate-in-Amsterdam/blob/main/charm_am_bot/LICENSE.txt) для получения дополнительной информации.
