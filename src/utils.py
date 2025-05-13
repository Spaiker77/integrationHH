from typing import List, Optional
from src.vacancy import Vacancy


def filter_vacancies(
    vacancies: List[Vacancy], filter_words: List[str]
) -> List[Vacancy]:
    """
    Фильтрация вакансий по ключевым словам
    :param vacancies: Список вакансий
    :param filter_words: Список ключевых слов
    :return: Отфильтрованный список вакансий
    """
    if not filter_words:
        return vacancies

    filtered = []
    for vacancy in vacancies:
        text = (
            f"{vacancy.snippet.get('requirement', '')} "
            f"{vacancy.snippet.get('responsibility', '')}"
        ).lower()
        if all(word.lower() in text for word in filter_words):
            filtered.append(vacancy)
    return filtered


def get_vacancies_by_salary(
    vacancies: List[Vacancy], salary_range: Optional[tuple]  # Изменили тип на tuple
) -> List[Vacancy]:
    """
    Фильтрация вакансий по диапазону зарплат
    :param vacancies: Список вакансий
    :param salary_range: Диапазон зарплат (кортеж: (min_salary, max_salary))
    :return: Отфильтрованный список вакансий
    """
    if not salary_range:  # Теперь salary_range - кортеж, а не строка
        return vacancies

    min_salary, max_salary = salary_range  # Получаем значения из кортежа

    ranged = []
    for vacancy in vacancies:
        if not vacancy.salary:
            continue

        salary_from = vacancy.salary.get(
            "from"
        )  # Просто получаем значение (может быть None)
        salary_to = vacancy.salary.get(
            "to"
        )  # Просто получаем значение (может быть None)

        if salary_from is None:  # Проверяем, что salary_from не None
            continue  # Если salary_from None, пропускаем вакансию

        salary_from = int(
            salary_from
        )  # Преобразуем в int только после проверки на None

        # Явные проверки для salary_to
        if salary_to is None:
            salary_to = float("inf")
        else:
            salary_to = int(salary_to)  # Преобразуем в int, если не None

        if (
            min_salary <= salary_from <= max_salary
            or min_salary <= salary_to <= max_salary
        ):
            ranged.append(vacancy)
    return ranged


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате (по убыванию)"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Получение топ N вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Вывод вакансий в удобном формате"""
    for i, vacancy in enumerate(vacancies, 1):
        print(f"{i}. {vacancy.name}")
        print(f"   Компания: {vacancy.employer.get('name')}")

        salary = vacancy.salary or {}
        salary_from = salary.get("from", "не указана")
        salary_to = salary.get("to", "не указана")
        currency = salary.get("currency", "")
        print(f"   Зарплата: от {salary_from} до {salary_to} {currency}")

        print(f"   Требования: {vacancy.snippet.get('requirement')}")
        print(f"   Обязанности: {vacancy.snippet.get('responsibility')}")
        print(f"   Опыт: {vacancy.experience.get('name')}")
        print(f"   Занятость: {vacancy.employment.get('name')}")
        print(f"   Ссылка: {vacancy.alternate_url}")
        print()
