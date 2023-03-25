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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if not isinstance(job['min_salary'], int):
        raise ValueError
    if not isinstance(job['max_salary'], int):
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if not isinstance(salary, (int, str)):
        raise ValueError
    return job["min_salary"] <= int(salary) <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
