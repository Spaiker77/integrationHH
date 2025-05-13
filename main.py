from src.hh import HH
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.utils import (
    filter_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    get_top_vacancies,
    print_vacancies,
)


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    json_saver = JSONSaver()
    hh_api = HH(json_saver)

    print("Добро пожаловать в парсер вакансий с HeadHunter!")
    keyword = input("Введите поисковый запрос: ").strip()

    print("\nЗагружаю вакансии...")
    hh_api.load_vacancies(keyword)
    vacancies = Vacancy.cast_to_object_list(hh_api.vacancies)

    top_n = int(input("\nВведите количество вакансий для вывода в топ N: "))
    filter_words = (
        input("Введите ключевые слова для фильтрации вакансий (через пробел): ")
        .strip()
        .split()
    )

    # Обрабатываем ввод диапазона зарплат
    salary_range_str = input(
        "Введите диапазон зарплат (например: 100000-150000): "
    ).strip()

    try:
        min_salary, max_salary = map(int, salary_range_str.split("-"))
        salary_range = (min_salary, max_salary)  # Преобразуем в кортеж чисел
    except ValueError:
        print(
            "Некорректный формат диапазона зарплат. Фильтрация по зарплате пропущена."
        )
        salary_range = None  # Устанавливаем None, если ввод некорректен

    filtered = filter_vacancies(vacancies, filter_words)

    # Проверяем, что salary_range не None, прежде чем использовать
    if salary_range:
        ranged = get_vacancies_by_salary(filtered, salary_range)
    else:
        ranged = filtered  # Если фильтрация по зарплате пропущена, используем отфильтрованные вакансии

    sorted_vac = sort_vacancies(ranged)
    top_vac = get_top_vacancies(sorted_vac, top_n)

    print("\nРезультаты поиска:")
    print_vacancies(top_vac)

    print(f"\nВсего найдено вакансий: {len(vacancies)}")
    print(f"После фильтрации: {len(top_vac)}")


if __name__ == "__main__":
    user_interaction()
