from github import Github
import os
import sys

username = ""  # Insert Github username here
password = ""  # Insert Github password here

directory = ""  # Insert path to your projects here
# Example: /Users/YourName/Dev/


def create():
    projectName = str(sys.argv[1])
    os.makedirs(directory + projectName)
    gUser = Github(username, password).get_user()
    gRepo = gUser.create_repo(projectName)
    print("Created repo {}".format(projectName))


if __name__ == "__main__":
    create()