import tempfile
import yaml


class pyci:

    def __init__(self, yaml_file):
        # import settings from yaml file
        stream = open(yaml_file, "r")
        self.config_dict = yaml.load(stream)

        # find the last hash value
        last_hash_file = open(self.config_dict["last_hash_location"])
        last_hash = last_hash_file.read().replace("\n", " ").split(" ")
        if len(last_hash) != 2:
            raise Exception("Last hash file can only contain one hash value.")
        self.last_hash = last_hash[0]

    def has_hash_changed(self):
        # Get current hash
        head_loc = self.config_dict["git_repo_location"] + "/.git/logs/HEAD"
        head_file = open(head_loc)
        current_hash = head_file.read().replace("\n", " ").split(" ")[-7]
        if current_hash != self.last_hash:
            # TODO: figure out what to do here. Call a function?
            print("hash has changed!")
            self.last_hash = current_hash
        else:
            print("hash has not changed")

    def
