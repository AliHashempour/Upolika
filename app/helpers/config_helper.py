import configparser
import os

from pathlib import Path


class ConfigHelper:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./config.ini')

    def get_config(self, tag):
        return self.config[tag]

    def has_tag(self, tag):
        return tag in self.config.keys()

    def has_name(self, tag, name):
        return name in self.config[tag].keys()

    def get(self, tag, name):
        return self.config[tag][name]
