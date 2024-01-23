# text.py

greet = (f'Привет, я бот, использующий модель ИИ CatBoost от Яндекса.'
         f' Задавай мне парметры недвижимости в Амстердаме и я постараюсь предсказать цену ☺')
menu = f'Главное меню'

text_inform = (f'Этот бот умеет предсказывать цену на недвижимость в Амстердаме по трем признакам:\n'
               f'- Площадь,\n- Количество комнат,\n- Район (4-значный код).\n'
               f'Модель обученна на данных от 2021 года.')

district_map = (f'Это почтовая карта Амстердама. Она показывает районы города, по которым Вы сможете выбрать свой.'
                f' Для этого выберите район и запомните 4-х значный код, затем напишите их боту.\n')

ds_inform = (f'В проекте используется модель CatBoost.\n'
             f'Результаты на обучение:\n'
             f'Best CatBoost MAE: 67366.96957536072\n'
             f'Best CatBoost parameters: {{"regressor__learning_rate": 0.1, "regressor__iterations": 520, "regressor__depth": 8}}\n'
             f'CPU times: user 2.41 s, sys: 318 ms, total: 2.72 s\n'
             f'Wall time: 5.66 s\n'
             f'---\n'
             f'Результаты на тестовых данных:\n'
             f'Best CatBoost MAE on Test data: 62035.051703360274\n'
             f'Best CatBoost R2 on Test data: 0.8017567955761038\n'
             f'---\n'
             f'С этим и другими моими проектами Вы можете познакомитсяна моем GitHub: https://github.com/PaulSpirin.\n'
             f'А так же связаться со мной LinkedIn: https://www.linkedin.com/in/pavelspirin/ и Telegram: @PaulSpirin')

start_bot_gen = (f'Начнем предсказание.\nВведите параметры недвижимости через запятую в формате '
                 f'"площадь, количество комнат, район (4 знака)".\n'
                 f'Пример: 78, 3, 1181')

help_inform = (f'Ошибка генерации. Возможные причины:\n'
               f'1. Перегружен сервер\n2. Не правильно введены данные\n3. Ошибка в работе бота\n'
               f'Если Вы столкнулись с проблемой, свяжитесь с модератором: в "@PaulSpirin" или по почте '
               f'"agro.spirin@gmai.com"')
