from src import db_handler as h
from src.menus import main_menu

def main():
    h.create_tables()
    main_menu()

if __name__ == "__main__":
    main()
