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
    jobs_filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered
