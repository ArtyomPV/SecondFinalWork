menu = '''Главное меню
1. открыть файл
2. сохранить файл
3. показать заметку
4. добавить заметку
5. найти заметку
6. изменить заметку
7. удалить заметку
8. выход
'''

menu_select = 'выбирите пункт меню'


def input_menu_error():
    error = len(menu.split('\n'))
    return f'ошибка ввода! выбирете пункт от 1 до {error - 1}'