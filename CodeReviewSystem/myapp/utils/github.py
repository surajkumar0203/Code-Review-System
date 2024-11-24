import requests
import base64
from urllib.parse import urlparse
from myapp.AIIntelligent.graq_cloud import code_analysis
from uuid import uuid4

def get_username_repo(url):
    passed_url=urlparse(url)
    path_len=passed_url.path.strip("/").split('/')
   
    if len(path_len)>=2:
        owner,repo=path_len[0],path_len[1]
        return owner, repo
    return None,None

def fetch_file(url,pr_number,github_token=None):
    owner, repo=get_username_repo(url)
    if owner and repo:
        headers = {}
        if github_token:
            headers['Authorization'] = f'token {github_token}'
        git_url=f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files'
        response = requests.get(git_url, headers=headers)
        response.raise_for_status()
        return response.json()
    else:
        return None


def fetch_contents(url,filename,github_token=None):
    owner, repo=get_username_repo(url)
    if owner and repo:
        headers = {}
        if github_token:
            headers['Authorization'] = f'token {github_token}'
        git_url=f'https://api.github.com/repos/{owner}/{repo}/contents/{filename}'
        response = requests.get(git_url, headers=headers)
        response.raise_for_status()
        content=response.json()
        return base64.b64decode(content['content']).decode()
    else:
        return None

def analyze_code(url,pr_number,github_token=None):
    unique_id=str(uuid4())
    try:
        fetch_pr=fetch_file(url,pr_number,github_token)
        results=[]
        for file in fetch_pr:
            filename=file['filename']
            content=fetch_contents(url,filename,github_token)
            results.append(code_analysis(content, filename))
        return {"id":unique_id,"results": results}
    except Exception as e:
        return {"id":unique_id,"error":str(e)}
        