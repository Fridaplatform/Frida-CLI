import os

from fridacli.interface.system_console import SystemConsole
from fridacli.interface.styles import (
    file_list_with_styles,
    format_to_columns,
    format_to_table,
    print_padding,
)
from fridacli.config.env_vars import BOT_NAME
from fridacli.commands.subcommands.subcommands_info import get_commands_df
from fridacli.commands.subcommands.predefined_phrases import ERROR_PATH_DOES_NOT_EXIST


def ls_subcommand(*args, **kwargs) -> None:
    """"""
    system_console: SystemConsole = kwargs["system_console"]
    root = args[0] if args else os.getcwd()
    valid_path = os.path.exists(root) and os.path.isdir(root)
    if not valid_path:
        system_console.notification(ERROR_PATH_DOES_NOT_EXIST(root))
        return
    file_list = file_list_with_styles(sorted(os.listdir(root)))
    columns_output = format_to_columns(file_list)
    system_console.print(columns_output)


def pwd_subcommand(*args, **kwargs):
    """"""
    pass


def cd_subcommand(*args, **kwargs) -> None:
    """"""
    system_console: SystemConsole = kwargs["system_console"]
    new_directory = args[0] if args else os.path.expanduser("~")
    valid_path = os.path.exists(new_directory) and os.path.isdir(new_directory)
    if not valid_path:
        system_console.notification(ERROR_PATH_DOES_NOT_EXIST(new_directory))
        return
    os.chdir(new_directory)
    print_padding()


def help_subcommand(*args, **kwargs) -> None:
    """"""
    subcommands_df = get_commands_df()
    table_output = format_to_table(
        subcommands_df, box=None, padding=True, expand=True, ratio=[1, 3, 1]
    )
    system_console: SystemConsole = kwargs["system_console"]
    system_console.print(table_output, bottom=0, alignment="center")


def exit_subcommand(*args, **kwargs) -> None:
    """"""
    system_console: SystemConsole = kwargs["system_console"]
    system_console.notification(f"{BOT_NAME}CLI Chat session ended")
    exit()
