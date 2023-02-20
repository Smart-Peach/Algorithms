import subprocess
import os


def binary_search(commits, repository, command):
    l = 0
    r = len(commits)
    middle = 0
    while l < r:
        middle = l + (r - l) // 2
        subprocess.run(['git', 'checkout', commits[middle]])
        output = subprocess.run(['python', repository + command])
        if output.returncode == 0:
            r = middle
        else:
            l = middle + 1
    return commits[middle]


def git_bisect(repository, start, finish, command):
    os.chdir(repository)
    commits = subprocess.check_output(
        ['git', 'log', start, finish, '--pretty=format:%h']).decode("utf-8").split('\n')
    start_ind = commits.index(start) + 1
    finish_ind = commits.index(finish)
    suitable_commits = commits[finish_ind:start_ind]
    result = binary_search(suitable_commits, repository, command)
    print("result: ", result)


start = 'f3edc5d'
finish = '708a9ff'
git_bisect('C:\\Users\\Home\\Desktop\\PYTHON\\Testing', start, finish, '\\main.py')
