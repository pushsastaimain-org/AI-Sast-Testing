import os
import subprocess


def checkout_branch(branch_name: str) -> None:
    cmd = "git checkout " + branch_name
    os.system(cmd)

def clone_repo(repo_url: str, target_dir: str) -> None:
    os.system(f"git clone {repo_url} {target_dir}")


def show_commit_log(author: str) -> str:
    command = "git log --author=%s" % author
    result = subprocess.check_output(command, shell=True)
    return result.decode()


def diff_against_ref(ref: str) -> None:
    subprocess.call("git diff " + ref, shell=True)

def run_git_grep(request_params: dict) -> str:
    pattern = request_params.get("pattern", "")
    cmd = f"git grep {pattern}"
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, _ = proc.communicate()
    return out.decode()

def get_git_tag_info(tag: str) -> str:
    stream = os.popen("git show " + tag)
    return stream.read()


def apply_patch(patch_path: str) -> None:
    cmd = "git apply {}".format(patch_path)
    subprocess.run(cmd, shell=True)


def checkout_branch_sanitized_but_broken(branch_name: str) -> None:
    safe_ish = branch_name.replace("|", "")
    os.system(f"git checkout {safe_ish}")


def checkout_branch_safe(branch_name: str) -> None:
    subprocess.run(["git", "checkout", branch_name], shell=False, check=True)


if __name__ == "__main__":
    print("This file is a SAST test fixture. Do not run against live input.")