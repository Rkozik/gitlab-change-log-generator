import subprocess
import csv


def find_features_in_release():
    hash_branch_map = load_dict_from_csv()
    in_release = {}
    for i, key in enumerate(hash_branch_map):
        if "tags/" not in hash_branch_map[key] and "feature/" in hash_branch_map[key]:
            in_release[hash_branch_map[key]] = ""
        if "tags/" in hash_branch_map[key] and i != 0:
            break

    print("Branches in this release: ")
    for key in in_release:
        print(key)


def parse_git_log():
    cmd_git_log = 'cd /Users/robertkozik/sites/php2/; git --no-pager log --decorate --oneline --pretty=format:"%h"'
    output = subprocess.check_output(cmd_git_log, shell=True).decode("utf-8")
    commit_hashes = output.splitlines()

    hash_branch_map = load_dict_from_csv()

    hash_branch = {}
    i = 0
    for commit_hash in commit_hashes:
        cmd = "cd /Users/robertkozik/sites/php2/; git name-rev " + commit_hash
        if commit_hash not in hash_branch_map:
            hash_branch[commit_hash] = subprocess.check_output(cmd, shell=True).decode("utf-8")[:-1].split(' ')[1]

        i += 1
        if i == 100:
            with open('master.csv', 'a') as f:
                w = csv.DictWriter(f, hash_branch.keys())
                w.writeheader()
                w.writerow(hash_branch)
            hash_branch = {}
            i = 0


def load_dict_from_csv():
    with open('master.csv', mode='r') as infile:
        file = csv.reader(infile)
        the_dict = {}
        rows = []
        for row in file:
            rows.append(row)

        if rows:
            for i, value1 in enumerate(rows):
                for j, value2 in enumerate(rows[i]):
                    if i % 2 == 0:
                        the_dict[rows[i][j]] = rows[i+1][j]

        return the_dict


if __name__ == "__main__":
    find_features_in_release()
