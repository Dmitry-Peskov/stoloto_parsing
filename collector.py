class StolotoCollector:
    def __init__(self, lottery_name: str):
        """Парсинг тиражей лотереи по её названию"""
        self.__lottery_name = lottery_name
        print(f"Утилиты инициализированы для {lottery_name}")

    def get_url_lottery(self):
        """Получить путь к архиву лотереи по её названию"""
        url_dict = {"5x36": r"https://www.stoloto.ru/5x36plus/archive/",
                    "12x24": r"https://www.stoloto.ru/1224/archive/",
                    "6x45": r"https://www.stoloto.ru/6x45/archive/",
                    "7x49": r"https://www.stoloto.ru/7x49/archive/"}
        return url_dict[self.__lottery_name]

    @staticmethod
    def create_date(dt_text: str):
        """Разбивает строку с датой и временем, приводит дату в формат ДД.ММ.ГГГГ"""
        calendar = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                    'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
        times = (str(dt_text)[::-1][0:5])[::-1]
        date_lottery = str((dt_text[0:len(dt_text) - 8]))
        for key, value in calendar.items():
            if key in date_lottery:
                date = date_lottery.replace(key, str(value)).replace(' ', '.')
                return date, times

    def get_page_class(self):
        """Возвращает класс для поиска на странице по названию лоттереи"""
        class_dict = {"5x36": r"cleared game_567 game_5x36",
                      "12x24": r"cleared game_1224",
                      "6x45": r"cleared game_567 game_6x45",
                      "7x49": r"cleared game_567 game_7x49"}
        return class_dict[self.__lottery_name]
