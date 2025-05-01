from pathlib import Path

def get_cats_info(path):
    try:
        cats_list = []
        p = Path(path)
        with open(p, 'r', encoding='utf-8') as file:
            while True:
                row = file.readline()
                if not row:
                    break
                cats_list.append({'id': row.strip().split(',')[0],
                                  'name': row.strip().split(',')[1],
                                  'age': row.strip().split(',')[2]})
        return cats_list
    except FileNotFoundError:
        print('Файл відсутній')

cats_info = get_cats_info('cats_file.txt')
print(cats_info)
