import os
from fridacli.commands.recipes.angular_voyager import exec_angular_voyager
from .predefined_phrases import create_asp_prompt, create_document_prompt
from fridacli.interface.spinner import Spinner
from fridacli.common import (
    file_manager,
    chatbot_agent,
    chatbot_console,
    frida_coder,
)
from fridacli.logger import Logger

logger = Logger()


def angular_voyager(args=None):
    """
    Recipe that migrates a angular project from an old version to a new version
    """
    path = args if args is not None else os.getcwd()
    exec_angular_voyager(path)


def asp_voyager(*args, **kwargs):
    """
    Recipe that migrates a asp project from an old version to a new version
    """
    logger.info(__name__, f"ASP voyager running")
    files = file_manager.get_files()
    spinner = Spinner()
    for file_name in files:
        spinner.start_spinner(text=f"ASP updating {file_name}")
        code = frida_coder.get_code_from_path(file_manager.get_file_path(file_name))
        prompt = create_asp_prompt(code)
        #print("prompt", prompt)
        response = chatbot_agent.chat(prompt, True)
        #print("response", response)
        spinner.stop_spinner()
        chatbot_console.response(response)

def document(*args, **kwargs):
    """
    Recipe to document the files in file manager
    """
    logger.info(__name__, f"Documenting files")
    files = file_manager.get_files()
    spinner = Spinner()
    for file in files:
        _, extension = os.path.splitext(file)
        if frida_coder.is_programming_language_extension(extension):
            spinner.start_spinner(text=f"Documenting {file}")
            full_path = file_manager.get_file_path(file)
            code = frida_coder.get_code_from_path(full_path)
            prompt = create_document_prompt(code)
            response = chatbot_agent.chat(prompt, True)
            if len(response) > 0:
                #print("response", response)
                code_blocks = frida_coder.get_code_block(response)
                if len(code_blocks) > 0:
                    documented_code = code_blocks[0]['code']
                    frida_coder.write_code_to_path(full_path, documented_code)
            spinner.stop_spinner()
