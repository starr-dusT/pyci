# import tempfile
from config import config

#def get_current_hash():
#    # Get current hash
#    head_loc = self.config_dict["git_repo_location"] + "/.git/logs/HEAD"
#    head_file = open(head_loc)
#    current_hash = head_file.read().replace("\n", " ").split(" ")[-7]
#    if current_hash != self.last_hash:
#        # TODO: figure out what to do here. Call a function?
#        print("hash has changed!")
#        self.last_hash = current_hash
#    else:
#        print("hash has not changed")

def eval_state():
    return "ready"
