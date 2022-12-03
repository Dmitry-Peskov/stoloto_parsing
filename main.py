import requests
from bs4 import BeautifulSoup

from database import StolotoDB
from collector import StolotoCollector

if __name__ == "__main__":
    lottery_name = str(input("Введите название лотереи: "))
    db = StolotoDB(lottery_name)
    collector = StolotoCollector(lottery_name)
    start = int(input("Начальный тираж: "))
    end = int(input("Конечный тираж: "))
    for draw_num in range(start, end, -1):
        print(f"Обрабатываем тираж № {draw_num}")
        url = collector.get_url_lottery()+str(draw_num)
        response = requests.get(url).content
        print("Получена страница, парсим...")
        soup = BeautifulSoup(response, "html.parser")
        page_dt = soup.find('div', class_=collector.get_page_class())
        dt = page_dt.find('h1').text.replace(fr'Результаты тиража № {draw_num},  ', '')
        date_lt, time_lt = collector.create_date(dt)
        page_num = soup.find('div', class_="winning_numbers cleared")
        num_list = list()
        special_num = str
        print('Перебираем выпавшие номера')
        for num in page_num.text.split():
            num_list.append(int(num))
        if lottery_name == "5x36":
            special_num = num_list.pop()
            num_list.sort()
            db.record_to_db(draw_num, date_lt, time_lt, *num_list, special_num)
        else:
            num_list.sort()
            db.record_to_db(draw_num, date_lt, time_lt, *num_list)
    print('Парсинг завершён')









