# models.py

import joblib
import pandas as pd


def load_model(model_path='real_estate_model.joblib'):
    # Загрузка модели из файла
    model = joblib.load(model_path)
    return model


def predict_price(model, area, rooms, district):
    # Предсказание цены с преобразованием параметров в DataFrame
    input_data = pd.DataFrame([[area, rooms, district]], columns=['Area', 'Room', 'District'])
    result = model.predict(input_data)

    return result[0]


# Загрузка модели при импорте модуля
model = load_model()
