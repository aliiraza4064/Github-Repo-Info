import requests
import csv

def get_github_org_repos(org_name, token):
    url = f"https://api.github.com/orgs/{org_name}/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    repos = []
    page = 1
    
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}")
        
        page_repos = response.json()
        if not page_repos:
            break
        
        repos.extend(page_repos)
        page += 1
    
    return repos

def get_repo_collaborators(repo_full_name, token):
    url = f"https://api.github.com/repos/{repo_full_name}/collaborators"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    collaborators = []
    page = 1
    
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}")
        
        page_collaborators = response.json()
        if not page_collaborators:
            break
        
        collaborators.extend(page_collaborators)
        page += 1
    
    return [collaborator['login'] for collaborator in collaborators]

def get_repo_teams(repo_full_name, token):
    url = f"https://api.github.com/repos/{repo_full_name}/teams"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    teams = []
    page = 1
    
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}")
        
        page_teams = response.json()
        if not page_teams:
            break
        
        teams.extend(page_teams)
        page += 1
    
    return [team['name'] for team in teams]

def get_repo_branches(repo_full_name, token):
    url = f"https://api.github.com/repos/{repo_full_name}/branches"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    branches = []
    page = 1
    
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}")
        
        page_branches = response.json()
        if not page_branches:
            break
        
        branches.extend(page_branches)
        page += 1
    
    branch_details = []
    for branch in branches:
        branch_name = branch['name']
        last_commit_url = branch['commit']['url']
        last_commit_response = requests.get(last_commit_url, headers=headers)
        if last_commit_response.status_code != 200:
            raise Exception(f"Failed to fetch data: {last_commit_response.status_code}")
        last_commit = last_commit_response.json()
        last_updated = last_commit['commit']['committer']['date']
        branch_details.append({
            "branch_name": branch_name,
            "last_updated": last_updated
        })
    
    return branch_details

def collect_repo_details(repos, token):
    repo_details = []
    for repo in repos:
        collaborators = get_repo_collaborators(repo['full_name'], token)
        teams = get_repo_teams(repo['full_name'], token)
        branches = get_repo_branches(repo['full_name'], token)
        branch_names = [branch['branch_name'] for branch in branches]
        last_updated_branches = [branch['last_updated'] for branch in branches]
        
        repo_details.append({
            "Repo Name": repo['name'],
            "Full Name": repo['full_name'],
            "Description": repo['description'],
            "Private": repo['private'],
            "HTML URL": repo['html_url'],
            "Created At": repo['created_at'],
            "Updated At": repo['updated_at'],
            "Pushed At": repo['pushed_at'],
            "Language": repo['language'],
            "Collaborators": ', '.join(collaborators),
            "Teams": ', '.join(teams),
            "Number of Branches": len(branches),
            "Branch Names": ', '.join(branch_names),
            "Last Updated Branches": ', '.join(last_updated_branches)
        })
    return repo_details

def write_to_csv(repo_details, filename):
    keys = repo_details[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(repo_details)

if __name__ == "__main__":
    org_name = input("Enter the GitHub organization name: ")
    token = input("Enter your GitHub Personal Access Token: ")
    
    repos = get_github_org_repos(org_name, token)
    repo_details = collect_repo_details(repos, token)
    
    output_filename = f"{org_name}_repo_details.csv"
    write_to_csv(repo_details, output_filename)
    
    print(f"Repository details with access information have been written to {output_filename}")
