import requests
from typing import List, Dict
from src.abstract_classes import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Наследуется от абстрактного класса Parser
    """

    def __init__(self, file_worker):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        self.file_worker = file_worker

    def _connect(self) -> None:
        """Приватный метод для проверки подключения к API"""
        response = requests.get(self.__url, headers=self.__headers)
        response.raise_for_status()

    def load_vacancies(self, keyword: str) -> None:
        """
        Загрузка вакансий по ключевому слову
        :param keyword: Ключевое слово для поиска вакансий
        """
        self._connect()
        self.__params["text"] = keyword

        while self.__params.get("page") != 20:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            response.raise_for_status()
            data = response.json()
            self.vacancies.extend(data.get("items", []))
            self.__params["page"] += 1

        self.file_worker.save_to_file(self.vacancies)
