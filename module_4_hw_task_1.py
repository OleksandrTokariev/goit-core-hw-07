from pathlib import Path

def total_salary(path):
    try:
        salaries_list = []
        p = Path(path)
        with open(p, 'r', encoding='utf-8') as file:
            while True:
                row = file.readline()
                if not row:
                    break
                salaries_list.append(int(row.strip().split(',')[1]))
        return sum(salaries_list), sum(salaries_list)/len(salaries_list)
    except FileNotFoundError:
        print('Файл відсутній')

try:
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception as e:
    print(f'Пошкоджений файл або помилка в даних: {e}')

