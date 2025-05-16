import pytest
from src.vacancy import Vacancy
from src.utils import (
    filter_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    get_top_vacancies,
)


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy(
            id="1",
            name="Python Developer",
            alternate_url="https://hh.ru/vacancy/1",
            salary={"from": 100000, "to": 150000, "currency": "RUR"},
            employer={"name": "Company A"},
            snippet={"requirement": "Python experience", "responsibility": "Develop"},
            experience={"name": "1-3 years"},
            employment={"name": "Full-time"},
        ),
        Vacancy(
            id="2",
            name="Java Developer",
            alternate_url="https://hh.ru/vacancy/2",
            salary={"from": 120000, "to": 180000, "currency": "RUR"},
            employer={"name": "Company B"},
            snippet={"requirement": "Java experience", "responsibility": "Code"},
            experience={"name": "3-5 years"},
            employment={"name": "Full-time"},
        ),
        Vacancy(
            id="3",
            name="Data Scientist",
            alternate_url="https://hh.ru/vacancy/3",
            salary=None,
            employer={"name": "Company C"},
            snippet={"requirement": "Python, SQL", "responsibility": "Analyze"},
            experience={"name": "2+ years"},
            employment={"name": "Remote"},
        ),
    ]


def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["python"])
    assert len(filtered) == 2
    assert filtered[0].name == "Python Developer"
    assert filtered[1].name == "Data Scientist"


def test_get_vacancies_by_salary(sample_vacancies):
    ranged = get_vacancies_by_salary(sample_vacancies, (110000, 160000))
    assert ranged[0].name == "Python Developer"


def test_get_vacancies_by_salary_no_range(sample_vacancies):
    ranged = get_vacancies_by_salary(sample_vacancies, None)
    assert len(ranged) == 3


def test_sort_vacancies(sample_vacancies):
    sorted_vac = sort_vacancies(sample_vacancies)
    assert sorted_vac[0].name == "Java Developer"
    assert sorted_vac[1].name == "Python Developer"
    assert sorted_vac[2].name == "Data Scientist"


def test_get_top_vacancies(sample_vacancies):
    top = get_top_vacancies(sample_vacancies, 2)
    assert len(top) == 2
    assert top[0].name == "Python Developer"
    assert top[1].name == "Java Developer"
