import os
from github import Github

# Replace YOUR_ACCESS_TOKEN with your actual access token
g = Github("get and admin token from github")

# Get the authenticated user
user = g.get_user()

# List all repositories for the authenticated user
def list_repos(user):
  for repo in user.get_repos():
    print(repo.name)

# Delete a list of repositories
def delete_repos(repo_names):
  for repo_name in repo_names:
    try:
      repo = user.get_repo(repo_name)
      repo.delete()
      print(f"Deleted repository {repo_name}")
    except Exception as e:
      print(f"Error deleting repository {repo_name}: {e}")

# Example usage: delete repositories named "repo1" and "repo2"
# delete_repos(["repo1", "repo2"])
repos_to_delete = [
  "repo1",
  "repo2",
  "repo3"
  ]

# this is the main function that will be executed when the script is run
if __name__ == "__main__":
#  delete_repos(repos_to_delete)
  list_repos(user)