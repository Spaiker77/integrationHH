from dataclasses import dataclass
from typing import Optional, Dict, List


@dataclass
class Vacancy:
    """Класс для представления вакансии с валидацией данных"""

    __slots__ = (
        "id",
        "name",
        "alternate_url",
        "salary",
        "employer",
        "snippet",
        "experience",
        "employment",
    )

    id: str
    name: str
    alternate_url: str
    salary: Optional[Dict]
    employer: Dict
    snippet: Dict
    experience: Dict
    employment: Dict

    def __post_init__(self):
        self._validate()

    def _validate(self) -> None:
        """Приватный метод валидации данных"""
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Название вакансии обязательно")
        if not isinstance(self.alternate_url, str) or not self.alternate_url.startswith(
            "http"
        ):
            raise ValueError("Некорректный URL")

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате"""
        self_salary = self.salary.get("from") if self.salary else 0
        other_salary = other.salary.get("from") if other.salary else 0
        return self_salary < other_salary

    @classmethod
    def cast_to_object_list(cls, vacancies_json: List[Dict]) -> List["Vacancy"]:
        """Преобразование JSON-вакансий в список объектов"""
        return [
            cls(
                id=vacancy.get("id"),
                name=vacancy.get("name"),
                alternate_url=vacancy.get("alternate_url"),
                salary=vacancy.get("salary"),
                employer=vacancy.get("employer", {}),
                snippet=vacancy.get("snippet", {}),
                experience=vacancy.get("experience", {}),
                employment=vacancy.get("employment", {}),
            )
            for vacancy in vacancies_json
        ]
