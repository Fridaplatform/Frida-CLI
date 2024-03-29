from fridacli.chatfiles.file_manager import FileManager
from fridacli.chatfiles.path_utilities import (
    check_samepath,
    check_valid_dir,
    change_directory,
    get_relative_path,
    get_current_dir,
)
from fridacli.interface.system_console import SystemConsole
from fridacli.predefined_phrases.chat_command import (
    CONFIRM_RELOAD_PROJECT,
    CONFIRM_OPEN_NEW_PROJECT,
    ERROR_PATH_DOES_NOT_EXIST,
    WARNING_ARGUMENT_REQUIRED,
)

from fridacli.interface.styles import add_styletags_to_string

from fridacli.common import system_console, file_manager
from fridacli.logger import Logger

logger = Logger()


def open_subcommand(*args, **kwargs):
    """"""
    if not args:
        system_console.notification(WARNING_ARGUMENT_REQUIRED("path"), bottom=0)
        return

    path_to_open = args[0]
    valid_path = check_valid_dir(path_to_open)

    if not valid_path:
        system_console.notification(ERROR_PATH_DOES_NOT_EXIST(path_to_open), bottom=0)
        return

    logger.info(__name__, f"Open command with path: {path_to_open}")
    active_folder = file_manager.get_folder_status()
    current_folder_active = check_samepath(get_current_dir(), path_to_open)

    if active_folder:
        confirm_message = (
            CONFIRM_RELOAD_PROJECT
            if current_folder_active
            else CONFIRM_OPEN_NEW_PROJECT
        )
        if system_console.confirm(confirm_message):
            close_subcommand(file_manager=file_manager)

    project_type, tree_str = file_manager.load_folder(path=path_to_open)
    change_directory(path_to_open)

    formatted_path = get_relative_path(path_to_open)
    system_console.notification(
        f"{formatted_path} ({add_styletags_to_string(project_type, 'success')})",
        bottom=0,
    )
    system_console.steps_notification(tree_str)


def close_subcommand(*args, **kwargs):
    """"""
    logger.info(__name__, "Closing file manager")
    file_manager.close_folder()
