from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class Parser(ABC):
    """Абстрактный класс для работы с API платформ с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Загрузка вакансий по ключевому слову"""
        pass


class Saver(ABC):
    """Абстрактный класс для работы с хранилищем вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: "Vacancy") -> None:
        """Добавление вакансии в хранилище"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[Dict] = None) -> List[Dict]:
        """Получение вакансий по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: "Vacancy") -> None:
        """Удаление вакансии из хранилища"""
        pass
