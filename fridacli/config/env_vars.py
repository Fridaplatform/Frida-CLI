from typing import Dict
import os


HOME_PATH = os.path.expanduser("~")
config_file_path = f"{HOME_PATH}/.fridacli"
BOT_NAME = "Frida"


def config_file_exists(path: str = config_file_path) -> bool:
    """Check if the configuration file already exists."""
    return os.path.exists(path)


def get_config_vars(path: str = config_file_path) -> Dict:
    """Retrieve configuration variables from a given configuration file."""
    config_variables = {}
    with open(path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            config_variables[key] = value
    return config_variables


def get_username() -> str:
    """Returns the name of the current user."""
    try:
        username = os.getlogin()
    except OSError:
        username = "user"
    return username
