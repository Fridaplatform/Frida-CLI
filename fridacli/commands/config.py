import os

from fridacli.chatbot.predefined_phrases import (
    CONFIGFILE_OVERWRITE,
    ERROR_MISSING_CONFIGFILE,
    message_config_file_path,
    success_configfile_create,
    success_configfile_update,
)
from fridacli.config.env_vars import config_file_exists, config_file_path, HOME_PATH
from fridacli.interface.system_console import SystemConsole
from fridacli.interface.styles import format_path
from fridacli.logger import Logger

logger = Logger()
system = SystemConsole()


# ========= frida config --list =========


def read_config_file(path: str = config_file_path) -> str:
    """Read the contents of a configuration file and returns it."""
    try:
        with open(path, "r") as file_content:
            configfile_content = file_content.read()
        return configfile_content.rstrip("\n")
    except Exception as e:
        logger.error(__name__, f"Error reading cong file: {e}")


def print_config_list() -> None:
    """Print the contents of the configuration file."""
    if config_file_exists():
        formatted_config_file_path = format_path(config_file_path, HOME_PATH)
        config_output = message_config_file_path(formatted_config_file_path)
        config_output += "\n" + read_config_file()
        system.print(config_output)
    else:
        system.notification(ERROR_MISSING_CONFIGFILE)


# ========= frida config =========


def write_config_to_file(keys: dict, path: str = config_file_path) -> None:
    """Write the configuration file with the API key."""
    try:
        if config_file_exists():
            os.remove(path)
        for key, value in keys.items():
            command = f"echo {key}={value} >> {path}"
            os.system(command)
    except Exception as e:
        logger.error(__name__, f"Error configurating api keys: {e}")


def print_configuration_success(created_file: bool) -> None:
    """Prints a success message for creating/updating a configuration file."""
    formatted_path = format_path(config_file_path, HOME_PATH)
    success_message = (
        success_configfile_create(formatted_path)
        if created_file
        else success_configfile_update(formatted_path)
    )
    system.notification(success_message)


def configurate_api_keys() -> None:
    """Configure the API keys and write them to the configuration file."""
    try:
        new_configfile = not config_file_exists()
        if not new_configfile:
            overwrite = system.confirm(CONFIGFILE_OVERWRITE)
            if not overwrite:
                return
        keys = {}
        key = system.password("Enter your Softtek SKD API key", top=1)
        keys["LLMOPS_API_KEY"] = key
        key = system.password("Enter Chat Model Name", top=1)
        keys["CHAT_MODEL_NAME"] = key
        write_config_to_file(keys)
        print_configuration_success(created_file=new_configfile)
    except Exception as e:
        logger.error(__name__, f"Error configurating api keys: {e}")

def configurate_python_env():
    try:
        configuration = read_config_file()
        result_dict = {
            key_value.split("=")[0]: key_value.split("=")[1]
            for key_value in configuration.split("\n")
        }
        key = system.password("Enter your python enviroment path", top=1)
        result_dict["PYTHON_ENV_PATH"] = key
        logger.info(__name__, f"Configurating python env as {key}")
        write_config_to_file(result_dict)
    except Exception as e:
        logger.error(__name__, f"Error configurating python env: {e}")


# ========= config command =========


def exec_config(list_option: bool, python_env: bool) -> None:
    """Execute the configuration command."""
    if list_option:
        print_config_list()
    elif python_env:
        configurate_python_env()
    else:
        configurate_api_keys()
