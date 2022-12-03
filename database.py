import sqlite3
import os


class StolotoDB:
    def __init__(self, lottery_name: str):
        """Запись разыгранных тиражей в БД stoloto.db"""
        self.__db = os.path.join(os.getcwd(), 'stoloto.db')
        self.__lottery_name = lottery_name
        print(f"Методы работы с БД инициализированы для {lottery_name}")

    def __connect(self):
        """Подключение к базе данных"""
        return sqlite3.connect(self.__db)

    def __get_sql_request(self) -> str:
        """Получить SQL запрос записи в БД под указанную лоттерею"""
        sql_dict = {"5x36": """INSERT INTO result_5x36 (draw_num, date, time, n1, n2, n3, n4, n5, n_special)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    "12x24": """INSERT INTO result_12x24
                     (draw_num, date, time, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    "6x45": """INSERT INTO result_6x45 (draw_num, date, time, n1, n2, n3, n4, n5, n6)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    "7x49": """INSERT INTO result_7x49 (draw_num, date, time, n1, n2, n3, n4, n5, n6, n7)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""}
        return sql_dict[self.__lottery_name]

    def record_to_db(self, draw_num: int, date: str, time: str, *args: str):
        """Запись тиража в БД"""
        sql = self.__get_sql_request()
        with self.__connect() as connect:
            cursor = connect.cursor()
            cursor.execute(sql, (draw_num, date, time, *args,))
            connect.commit()
            print(f'Тираж {draw_num} лотереи {self.__lottery_name} от {date} {time} записан в БД')


