from github import Github
import os
import sys

username = ""  # Insert Github username here
password = ""  # Insert Github password here

directory = ""  # Insert path to your projects here
# Example: /Users/YourName/Dev/


def makeDir():
    projectName = str(sys.argv[1])
    os.makedirs(directory + str(sys.argv[1]))
    gUser = Github(username, password).get_user()
    gRepo = gUser.create_repo(str(sys.argv[1]))
    print("Created repo {}".format(sys.argv[1]))


if __name__ == "__main__":
    makeDir()