import streamlit as st
import pandas as pd

st.title("Училищен дневник - Оценки")

# Инициализация на данните за оценки
# По скалата от 2 до 6
if "grades" not in st.session_state:
    st.session_state.grades = {
        "Отличен (6)": 0,
        "Много добър (5)": 0,
        "Добър (4)": 0,
        "Среден (3)": 0,
        "Слаб (2)": 0
    }

# Списък с ученици (можеш да добавиш още имена тук)
students_list = ["Иван Петров", "Мария Георгиева", "Георги Иванов", "Елена Стоянова"]

st.subheader("Въвеждане на нова оценка")

# Избор на ученик и оценка
student = st.selectbox("Избери ученик:", students_list)
grade = st.selectbox("Избери оценка:", list(st.session_state.grades.keys()))

if st.button("Запази оценката"):
    st.session_state.grades[grade] += 1
    st.success(f"Оценката на {student} е записана успешно!")

st.divider()

st.subheader("Статистика на класа")

# Графика за разпределението на оценките
st.write("Разпределение на оценките по брой ученици")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой ученици"]
)

# Показваме колонна диаграма
st.bar_chart(grades_df)

# Показваме и таблица за по-голяма точност
st.table(grades_df)
