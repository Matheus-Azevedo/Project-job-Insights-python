from functools import lru_cache
from typing import List, Dict
from csv import DictReader


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r') as file_csv:
        jobs_dict = DictReader(file_csv, delimiter=',')
        return list(jobs_dict)


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


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
