import json
import os
from typing import List, Dict, Optional
from src.abstract_classes import Saver


class JSONSaver(Saver):
    """Класс для работы с JSON-файлом, наследуется от Saver"""

    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def save_to_file(self, data: List[Dict]) -> None:
        """Сохранение данных в файл (специфичный метод для HH)"""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump({"items": data}, f, ensure_ascii=False, indent=2)

    def add_vacancy(self, vacancy: "Vacancy") -> None:
        """Добавление вакансии в файл"""
        vacancies = self.get_vacancies()
        vacancy_data = {
            "id": vacancy.id,
            "name": vacancy.name,
            "alternate_url": vacancy.alternate_url,
            "salary": vacancy.salary,
            "employer": vacancy.employer,
            "snippet": vacancy.snippet,
            "experience": vacancy.experience,
            "employment": vacancy.employment,
        }

        if not any(v["id"] == vacancy.id for v in vacancies):
            vacancies.append(vacancy_data)
            self.__save_vacancies(vacancies)

    def get_vacancies(self, criteria: Optional[Dict] = None) -> List[Dict]:
        """Получение вакансий из файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                vacancies = data.get("items", [])
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        if criteria:
            return [
                v
                for v in vacancies
                if all(
                    str(v.get(k, "")).lower() == str(v).lower()
                    for k, v in criteria.items()
                )
            ]
        return vacancies

    def delete_vacancy(self, vacancy: "Vacancy") -> None:
        """Удаление вакансии из файла"""
        vacancies = self.get_vacancies()
        self.__save_vacancies([v for v in vacancies if v["id"] != vacancy.id])

    def __save_vacancies(self, vacancies: List[Dict]) -> None:
        """Приватный метод сохранения вакансий"""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump({"items": vacancies}, f, ensure_ascii=False, indent=2)
