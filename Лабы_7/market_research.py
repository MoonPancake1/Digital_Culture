"""
Задание:

Проанализировать влияние рекламных каналов (TV, Radio, Newspaper) на продажи
и построить модель для прогнозирования будущих продаж.

! Пишем программу с комментариями

Задачи:
    
    1. Загрузка данных
        • Используйте набор данных advertising.csv, содержащий информацию о бюджетах
        на каждый вид рекламы и продажах
    
    2. Предобработка данных
        • Проверьте данные на наличие пропусков и дубликатов
        • Выведите среднее, медиану, среднеквадратическое отклонение для всех столбцов
        (описательная статистика)
    
    3. Визуализация
        • Постройте гистограммы распределения расходов на каждый рекламный канал
        • Создайте тепловую карту корреляции между переменными
        • Нарисуйте scatter-графики продаж vs бюджета каждого рекламного канала
        
    4. Построение модели прогнозирования
        • Разделите данные на обучающую и тестовую выборки (например, 80/20)
        • Обучите модель линейной регрессии для предсказания продаж на основе
        рекламных бюджетов
        • Оцените модель с помощью метрик: MSE, MAE, R2
    
    5. Анализ результатов
        • Выведите коэффициенты модели, чтобы определить, какой канал рекламы влияет
        на продажи сильнее
        • Сделайте прогноз для тестовой выборки и визуализируйте его (фактические vs
        предсказанные значения)
"""

# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Загрузка данных
def load_data(file_path):
    """Загрузка данных из CSV-файла"""
    try:
        data = pd.read_csv(file_path)
        print("Данные успешно загружены:")
        print(data.head())
        return data
    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что файл advertising.csv находится в правильной директории.")
        return None

# 2. Предобработка данных
def preprocess_data(data):
    """Предварительная обработка и анализ данных"""
    print("\n=== Предобработка данных ===")
    
    # Проверка на пропуски
    print("\nПроверка на пропущенные значения:")
    print(data.isnull().sum())
    
    # Проверка на дубликаты
    print("\nПроверка на дубликаты:")
    print(f"Найдено дубликатов: {data.duplicated().sum()}")
    
    # Описательная статистика
    print("\nОписательная статистика:")
    print(data.describe().loc[['mean', '50%', 'std']].rename(index={'50%': 'median'}))
    
    return data

# 3. Визуализация данных
def visualize_data(data):
    """Визуализация данных"""
    print("\n=== Визуализация данных ===")
    
    # Настройка стиля графиков
    sns.set(style="whitegrid")
    plt.figure(figsize=(15, 10))
    
    # Гистограммы распределения расходов
    plt.subplot(2, 2, 1)
    sns.histplot(data['TV'], bins=20, color='blue', kde=True)
    plt.title('Распределение бюджета на TV рекламу')
    
    plt.subplot(2, 2, 2)
    sns.histplot(data['Radio'], bins=20, color='green', kde=True)
    plt.title('Распределение бюджета на Radio рекламу')
    
    plt.subplot(2, 2, 3)
    sns.histplot(data['Newspaper'], bins=20, color='red', kde=True)
    plt.title('Распределение бюджета на Newspaper рекламу')
    
    plt.subplot(2, 2, 4)
    sns.histplot(data['Sales'], bins=20, color='purple', kde=True)
    plt.title('Распределение продаж')
    
    plt.tight_layout()
    plt.show()
    
    # Тепловая карта корреляции
    plt.figure(figsize=(8, 6))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title('Тепловая карта корреляции')
    plt.show()
    
    # Scatter-графики продаж vs бюджета рекламных каналов
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    sns.scatterplot(x='TV', y='Sales', data=data, color='blue')
    plt.title('TV реклама vs Продажи')
    
    plt.subplot(1, 3, 2)
    sns.scatterplot(x='Radio', y='Sales', data=data, color='green')
    plt.title('Radio реклама vs Продажи')
    
    plt.subplot(1, 3, 3)
    sns.scatterplot(x='Newspaper', y='Sales', data=data, color='red')
    plt.title('Newspaper реклама vs Продажи')
    
    plt.tight_layout()
    plt.show()

# 4. Построение модели прогнозирования
def build_model(data):
    """Построение и оценка модели линейной регрессии"""
    print("\n=== Построение модели ===")
    
    # Разделение данных на признаки (X) и целевую переменную (y)
    X = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']
    
    # Разделение на обучающую и тестовую выборки (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Создание и обучение модели
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Прогнозирование на тестовой выборке
    y_pred = model.predict(X_test)
    
    # Оценка модели
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\nОценка модели:")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R-squared (R2): {r2:.2f}")
    
    return model, X_test, y_test, y_pred

# 5. Анализ результатов
def analyze_results(model, X_test, y_test, y_pred):
    """Анализ результатов моделирования"""
    print("\n=== Анализ результатов ===")
    
    # Коэффициенты модели
    coefficients = pd.DataFrame({
        'Feature': ['TV', 'Radio', 'Newspaper'],
        'Coefficient': model.coef_
    })
    print("\nКоэффициенты модели:")
    print(coefficients)
    
    # Визуализация фактических vs предсказанных значений
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.xlabel('Фактические значения продаж')
    plt.ylabel('Предсказанные значения продаж')
    plt.title('Фактические vs Предсказанные значения продаж')
    plt.show()
    
    # Определение важности признаков
    importance = pd.Series(model.coef_, index=X_test.columns)
    importance.plot(kind='barh', color='green')
    plt.title('Важность рекламных каналов для продаж')
    plt.xlabel('Коэффициент')
    plt.ylabel('Рекламный канал')
    plt.show()

# Основная функция
def main():
    # Загрузка данных
    data = load_data('advertising.csv')
    if data is None:
        return
    
    # Предобработка данных
    data = preprocess_data(data)
    
    # Визуализация данных
    visualize_data(data)
    
    # Построение модели
    model, X_test, y_test, y_pred = build_model(data)
    
    # Анализ результатов
    analyze_results(model, X_test, y_test, y_pred)

if __name__ == "__main__":
    main()
