import pytest
from src.vacancy import Vacancy


def test_vacancy_creation():
    vacancy_data = {
        "id": "1",
        "name": "Python Developer",
        "alternate_url": "https://hh.ru/vacancy/1",
        "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
        "employer": {"name": "Test Company"},
        "snippet": {
            "requirement": "Python experience",
            "responsibility": "Develop software",
        },
        "experience": {"name": "1-3 years"},
        "employment": {"name": "Full-time"},
    }
    vacancy = Vacancy(**vacancy_data)
    assert vacancy.name == "Python Developer"
    assert vacancy.salary["from"] == 100000
    assert vacancy.experience["name"] == "1-3 years"


def test_vacancy_without_salary():
    vacancy_data = {
        "id": "2",
        "name": "Developer",
        "alternate_url": "https://hh.ru/vacancy/2",
        "salary": None,
        "employer": {"name": "Test"},
        "snippet": {"requirement": "", "responsibility": ""},
        "experience": {"name": ""},
        "employment": {"name": ""},
    }
    vacancy = Vacancy(**vacancy_data)
    assert vacancy.salary is None


def test_cast_to_object_list():
    vacancies_json = [
        {
            "id": "1",
            "name": "Python",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": {"from": 100000},
            "employer": {"name": "Test"},
            "snippet": {"requirement": "Python", "responsibility": "Code"},
            "experience": {"name": "1-3 years"},
            "employment": {"name": "Full-time"},
        }
    ]
    vacancies = Vacancy.cast_to_object_list(vacancies_json)
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
