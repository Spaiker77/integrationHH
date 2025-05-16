import os
import json
import pytest
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


@pytest.fixture
def temp_saver(tmp_path):
    filename = tmp_path / "test_vacancies.json"
    saver = JSONSaver(filename)
    yield saver
    if os.path.exists(filename):
        os.remove(filename)


def test_add_vacancy(temp_saver):
    vacancy_data = {
        "id": "1",
        "name": "Test",
        "alternate_url": "https://test.com",
        "salary": {"from": 100000},
        "employer": {"name": "Test"},
        "snippet": {"requirement": "", "responsibility": ""},
        "experience": {"name": ""},
        "employment": {"name": ""},
    }
    vacancy = Vacancy(**vacancy_data)
    temp_saver.add_vacancy(vacancy)

    # Используем доступ к файлу через путь, переданный в конструктор
    with open(temp_saver._JSONSaver__filename, "r") as f:
        data = json.load(f)
        assert len(data["items"]) == 1
        assert data["items"][0]["name"] == "Test"


def test_delete_vacancy(temp_saver):
    vacancy_data = {
        "id": "1",
        "name": "Test",
        "alternate_url": "https://test.com",
        "salary": None,
        "employer": {"name": "Test"},
        "snippet": {"requirement": "", "responsibility": ""},
        "experience": {"name": ""},
        "employment": {"name": ""},
    }
    vacancy = Vacancy(**vacancy_data)
    temp_saver.add_vacancy(vacancy)
    temp_saver.delete_vacancy(vacancy)

    # Используем доступ к файлу через путь, переданный в конструктор
    with open(temp_saver._JSONSaver__filename, "r") as f:
        data = json.load(f)
        assert len(data["items"]) == 0
