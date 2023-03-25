from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_dict = read(path)
    max_salary_list = []
    for job in jobs_dict:
        if len(job['max_salary']) > 0 and job['max_salary'].isdigit():
            max_salary_list.append(int(job['max_salary']))
    return max(max_salary_list)


def get_min_salary(path: str) -> int:
    jobs_dict = read(path)
    min_salary_list = []
    for job in jobs_dict:
        if len(job['min_salary']) > 0 and job['min_salary'].isdigit():
            min_salary_list.append(int(job['min_salary']))
    return min(min_salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary = int(salary)
    except Exception:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    find_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                find_jobs.append(job)
        except Exception:
            pass
    return find_jobs

