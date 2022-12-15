try:
    import git
    from git import Repo
    import os,sys
    import shutil
    import configparser
    import subprocess
except ModuleNotFoundError:
    print("you have to install the below packages to run")
    sys.exit("install all modules")

# For reference --> https://www.analyticsvidhya.com/blog/2021/05/30-useful-methods-from-python-os-module/
# For reference --> https://digitalvarys.com/git-operations-with-python-scripting/#Git_Init
# For reference --> https://gitpython.readthedocs.io/en/stable/tutorial.html#using-git-directly
# For reference --> https://gitpython.readthedocs.io/en/stable/reference.html#module-git.diff
# For reference --> https://stackoverflow.com/questions/33733453/get-changed-files-using-gitpython
# For reference --> https://stackoverflow.com/questions/25556696/get-a-list-of-changed-files-between-two-commits-or-branches
# For reference --> https://masnun.com/2012/01/28/fetching-changed-files-diff-between-two-git-commits-in-python.html#:~:text=We%20call%20the%20iter_commits(),it%20to%20a%20list%20item.&text=To%20compare%20one%20commit%20to,has%20all%20the%20changed%20files.
# For reference --> https://gitpython.readthedocs.io/en/0.1.7/tutorial.html
# For reference --> https://stackoverflow.com/questions/34939445/list-file-that-have-changed-since-last-commit-with-gitpython

print(os.getcwd())#printing the currrent working diectory

if 0:
    # creating the folder if not exists for github
    if not os.path.isdir(os.path.join(os.path.dirname(__file__),'github_practice')):
        print("creating the folder for storing the github repo")
        os.mkdir('github_practice')
        print("folder created")

# creating the github repository
local_github=os.path.join(os.getcwd(),'github_practice')

if 0:
    if not os.path.exists(os.path.join(local_github,'github_configurations.ini')):
        print("copying the configuration file from other older to github folder")
        src_path = os.path.join(os.getcwd(),'github_configurations.ini')
        dst_path = os.path.join(local_github,'github_configurations.ini')
        shutil.copy(src_path, dst_path)
        print('Copied')


#importing values from the config file
config=configparser.ConfigParser()
try:
    config.read(os.path.join(local_github,'github_configurations.ini')) #reading the config file
except FileNotFoundError:
    sys.exit("file not present. please check file")

init = int(config["GITHUBSettings"]["init"])
clone = int(config["GITHUBSettings"]["clone"])
pull = int(config["GITHUBSettings"]["pull"])
push = int(config["GITHUBSettings"]["push"])

# initializing the repository
# making one folder in local machine as github repo
if init:
    print("initialising the local folder as local git repository")
    repository = Repo.init(local_github)
    print("created local repository")

if clone:
    print("cloning is started")
    git.Git(local_github).clone("https://github.com/adaveniprashanth/MyData.git")
    print("cloning is completed")

# creating the handle for repository
repo=git.Repo(os.path.join(local_github,'MyData'))

if pull:
    print("pull request running")
    repo.git.checkout('master')#checkout to the particular branch
    origin = repo.remote(name='origin')
    origin.pull()
    print("pull request completed")


if 1:
    # copying the current python file to local git repository.
    print("copying the current python file to local git repository.")
    src_path = os.path.join(os.getcwd(), 'github_automation.py')
    dst_path = os.path.join(local_github,'MyData','github_automation.py')
    shutil.copy(src_path, dst_path)
    print('Copied')

# repo.git.checkout('-b','new_branch')#to create a PR, we can create new branch
# and push changes from the branch

if push:
    if 1:#one logic
        print("push request running")
        repo.git.add('--all')
        repo.git.commit('-m', 'commit message from python script1')
        origin = repo.remote('origin')
        origin.push()
        print("push request completed")

    if 0:#Another logic
        print("push request running")
        repo.git.add('--all')
        repo.index.add(['bla.txt'])#for sing file addition
        repo.index.commit('my commit description')
        origin = repo.remote('origin')
        origin.push()
        print("push request completed")

if 0:#printing the commits from specific branch
    print("printing the commits from branch")
    for i in list(repo.iter_commits('master', max_count=10)):
        print(i)

if 0:
    commits_list = list(repo.iter_commits())
    print("total commits", len(commits_list))
    print("latest commit id: ", commits_list[0])
    print("first commit id: ", commits_list[-1])
    head = commits_list[0]
    print(head)
    print(head.author)
    print("accessing the tree")
    tree = commits_list[0].tree

    if 0:
        print("printing the file names")
        print("blobs",tree.blobs)
        print("blob1",tree.blobs[0])
        for b,i in enumerate(tree.blobs):
            print(b,i.name)
    if 0:
        print("printing the folder names")
        print("trees",tree.trees)
        print("trees1",tree.trees[0])
        for b,i in enumerate(tree.trees[0].trees[0].blobs):
            print(b,i.name)

if 0:#printing the files changed between specified commits
    if 0:#first logic
        print("getting all commits")
        commits_list = list(repo.iter_commits())

        print("printing the files changed between specified commits")
        changed_files = []
        for x in commits_list[0].diff(commits_list[25]):
            if x.a_blob.path not in changed_files:
                changed_files.append(x.a_blob.path)

            if x.b_blob is not None and x.b_blob.path not in changed_files:
                changed_files.append(x.b_blob.path)

        for i in changed_files:
            print(i)

    if 0:#Another method
        print("printing the files changed between specified commits1")
        diff = repo.git.diff('HEAD~25..HEAD', name_only=True)
        print(diff)

    if 0:#Other logic
        print("printing the files changed between specified commit and last commit")
        for item in repo.index.diff("HEAD~25"):
            print(item.a_path)


'''
# to display the file changes between pulls
# git diff --name-only -r HEAD~5 HEAD | xargs
# diff = repo.git.diff('HEAD~1..HEAD', name_only=True)
# print(diff)
'''