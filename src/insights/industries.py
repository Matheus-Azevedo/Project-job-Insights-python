from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_dict = read(path)
    industries = set()
    for job in jobs_dict:
        industries.add(job['industry'])
    return list(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_filtered = []
    for job in jobs:
        if job['industry'] == industry:
            industry_filtered.append(job)
    return industry_filtered
