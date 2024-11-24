from celery import shared_task
from myapp.utils.github import analyze_code

@shared_task
def analyze_repo_code(url,pr_number,github_token=None):
    return analyze_code(url,pr_number,github_token)
    
