from datetime import datetime
import locale

def format_date(input_date):
    try:
        date_obj = datetime.strptime(input_date, "%d.%m.%Y")
        formatted_date = date_obj.strftime("%A, %d %B %Y года")
        return formatted_date
    except ValueError as e:
        raise ValueError("Ошибка!!") from e

def main():
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    except locale.Error:
        print("Ощибка. не удалось установить локаль")
        return

    input_date = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
    try:
        result = format_date(input_date)
        print("Вывод: ", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()