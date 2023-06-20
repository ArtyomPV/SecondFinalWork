from Notebook import text


def main_menu() -> int:
    print(text.menu)
    while True:
        select = input(text.menu_select)
        if select.isdigit() and 0 <int(select)<9:
            return int(select)
        print(text.input_menu_error())