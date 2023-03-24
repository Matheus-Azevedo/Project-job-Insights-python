from functools import lru_cache
from typing import List, Dict
from csv import DictReader


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r') as file_csv:
        jobs_dict = DictReader(file_csv, delimiter=',')
        return list(jobs_dict)


def get_unique_job_types(path: str) -> List[str]:
    jobs_dict = read(path)
    job_types = set()
    for job in jobs_dict:
        job_types.add(job['job_type'])
    return list(job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
