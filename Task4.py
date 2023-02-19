from github import Github
import subprocess


def check(commit, command):
    commit.get_check_runs(command)


# def binary_search(nums, command):
#     l = 0
#     r = len(nums)
#
#     while l < r:
#         middle = l + (r - l) // 2
#         if check(nums[middle], command):
#             return middle
#         elif nums[middle] < target:
#             l = middle + 1
#         else:
#             r = middle
#     return -1


def git_bisect(repository, start, finish, command):
    #  Получаем нужные коммиты
    g = Github()
    repo = g.get_repo(repository)
    commits = []
    for commit in repo.get_commits():
        commits.append(commit.sha)
    start_ind = commits.index(start) + 1
    finish_ind = commits.index(finish)
    commits = commits[finish_ind:start_ind]  # Массив необходимых коммитов
    # answer = binary_search(commits, command)
    # for i in repo.get_commits():
    #     i.get_check_runs(check_name=command, )
    cmd = ('python3', '-m', 'pycodestyle', 'main.py', '--ignore', 'W191')
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if result.returncode == 0:
        print('good')
        return 1
    else:
        print('Oh...')
        return 0


start = "e98664f26daea85836902023e05b1fb785a566b2"
finish = "708a9ff9ed19df7a730a708ef52911616ecf3789"
git_bisect('Smart-Peach/Testing', start, finish, 'main.py')
