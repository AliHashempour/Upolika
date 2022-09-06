import configparser
import os
import pathlib

from pathlib import Path


class ConfigHelper:
    def __init__(self):
        root_dir = str(Path(__file__).parent.parent.parent)
        config_path = os.path.join(root_dir, "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_config(self, tag):
        return self.config[tag]

    def has_tag(self, tag):
        return tag in self.config.keys()

    def has_name(self, tag, name):
        return name in self.config[tag].keys()

    def get(self, tag, name):
        return self.config[tag][name]
