import requests
import math
import os
from git import Repo


'''
Refer for REST API integration: https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28
Author : Nandha Ramasamy G
DATE : 26/02/2023
'''
ACCESS_TOKEN = "#######################" # To be created in git hub
ORG_NAME = "mad-street-den"
GITHUB_BASE_URL = "api.github.com"
no_of_repos = 124 # As per the organization
DESTINATION_PATH = "C:/Users/Nandh/Desktop/MSD-repos"


headers = {"Authorization":ACCESS_TOKEN}
url = f"https://{GITHUB_BASE_URL}/orgs/{ORG_NAME}/repos"
max_pages = math.ceil(no_of_repos / 100)

print("URL - ",url)
for page in range(1,max_pages): # Max allowed items per page is 100, so iterating twice to get all repos (more than 100 repos) 
    print(page)
    QUERY_PARAMS = {"per_page":100,"page":page}
    resp = requests.get(url = url,headers=headers,params=QUERY_PARAMS).json()
    for each_repo in resp:
        clone_repo = each_repo["name"]
        repo_url = each_repo["clone_url"]
        print("CLONING REPO - ",clone_repo)
        PATH = f"{DESTINATION_PATH}/{clone_repo}"
        if os.path.exists(PATH):
            print("REPO ALREADY EXISTS! SO CONTINUE")
            continue
        try:
            Repo.clone_from(repo_url, PATH)
        except:
            print("FAILED TO CLONE")
        print(f"REPO {clone_repo} CLONED SUCCESSFULLY!")
