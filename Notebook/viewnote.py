import text


def main_menu() -> int:
    print(text.menu[0])
    for i, item in enumerate(text.menu[1:], 1):
        print(f'{i:>5} {item}')
    while True:
        select = input(text.menu_select)
        if select.isdigit() and 0 <int(select)<9:
            return int(select)
        print(text.input_menu_error())