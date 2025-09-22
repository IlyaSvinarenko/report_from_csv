def students_performance(data):
    """Генерация отчета об успеваемости студентов."""
    grades_sum = {}
    grades_count = {}

    # Из совокупной инфы из файлов собираем то, что нужно
    for row in data:
        student = row['student_name']
        grade = float(row['grade'])

        if student in grades_sum:
            grades_sum[student] += grade
            grades_count[student] += 1
        else:
            grades_sum[student] = grade
            grades_count[student] = 1

    # Находим среднюю оценку для каждого студента
    students_grades = []
    for student in grades_sum:
        avg_grade = grades_sum[student] / grades_count[student]
        students_grades.append((student, round(avg_grade,
                                               2)))  # Если нужно изменить количество знаков после запятой в средней оценке, то меняем тут - round(avg_grade, 2)
    # Сортируем от большей оценки до меньшей, пузырьком
    for i in range(len(students_grades)):
        max_idx = i
        for j in range(i + 1, len(students_grades)):
            if students_grades[j][1] > students_grades[max_idx][1]:
                max_idx = j
        students_grades[i], students_grades[max_idx] = students_grades[max_idx], students_grades[i]

    result = []
    for idx, (student, grade) in enumerate(students_grades, 1):
        result.append([idx, student, grade])

    headers = ['№', 'student_name', 'grade']
    return headers, result


# Словарь для регистрации отчетов. Ключ - как название отчета вводится в команде. Значение - название функции для отчета
REPORTS = {
    'students-performance': students_performance,
}
