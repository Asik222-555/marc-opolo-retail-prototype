import streamlit as st

# Заголовок приложения
st.title("Marc O'Polo Retail Prototype")

# Информация о проекте
st.markdown("""
## Добро пожаловать в приложение для Marc O'Polo!
Это прототип для ретейла Marc O'Polo с фильтрацией продуктов, системой бронирования и AI Tutor.
""")

# Выбор категории и стиля для фильтрации продуктов
st.sidebar.header("Фильтр товаров")
category = st.sidebar.selectbox("Выберите категорию", ["Куртки", "Свитера", "Футболки"])
style = st.sidebar.selectbox("Выберите стиль", ["Smart Casual", "Business Casual", "Casual"])

# Показываем результаты по фильтрам
if st.button("Показать продукты"):
    st.success(f"Показаны товары категории '{category}' в стиле '{style}'")

    st.markdown("### Продукт 1: Свитер из шерсти")
    st.image("https://images.unsplash.com/photo-1602810313324-d9d3b9f813c0", width=250)
    st.write("**Стиль:** Smart Casual  \n**Размеры:** M, L, XL  \n**Цена:** 45,000 ₸")

    st.markdown("### Продукт 2: Классическая рубашка")
    st.image("https://images.unsplash.com/photo-1585386959984-a41552263b7d", width=250)
    st.write("**Стиль:** Business Casual  \n**Размеры:** S, M, L  \n**Цена:** 35,000 ₸")

# Интерактивность с AI Tutor
question = st.text_input("Введите ваш вопрос или ошибку", "Почему этот ответ неверен?")
explanation_type = st.selectbox("Выберите стиль объяснения", ["Стандартное", "Упрощенное", "С аналогией"])

if st.button("Задать вопрос AI Tutor"):
    st.write("🧠 Ответ AI Tutor:")
    
    if explanation_type == "Стандартное":
        st.info("Ответ неверен, потому что концепция 'эластичности' в физиологии относится к способности ткани возвращаться в исходную форму.")
    elif explanation_type == "Упрощенное":
        st.success("Эластичность — это как быстро что-то возвращается в форму после растяжения, как резинка.")
    else:
        st.success("Представьте легкие как воздушные шарики. Эластичность — это как они легко сдуваются после надувания.")

# Функция для резервирования товара в магазине
if st.checkbox("Забронировать товар для примерки в магазине"):
    city = st.text_input("Введите город")
    store_location = st.text_input("Введите место магазина")
    appointment_time = st.time_input("Выберите время")
    st.button("Подтвердить бронирование")
    st.success(f"Товар забронирован для примерки в {city}, {store_location} на {appointment_time}.")
