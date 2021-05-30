from config import config
import time

def get_current_hash():
    # Get current hash
    head_loc = config["git_repo_location"] + "/.git/logs/HEAD"
    head_file = open(head_loc)
    return head_file.read().replace("\n", " ").split(" ")[-8]


def eval_state():
    last_hash = get_current_hash()
    while 1:
        current_hash = get_current_hash()
        if current_hash != last_hash:
            print("hash has changed!")
            return "ready"
        else:
            time.sleep(1)
