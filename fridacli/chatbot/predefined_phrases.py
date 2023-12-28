from fridacli.config.env_vars import BOT_NAME
from fridacli.interface.styles import add_styletags_to_string

START_MESSAGE = "Hello! How may I help you?"
INTERRUPT_CHAT = f"Press {add_styletags_to_string('Ctrl+C','operation')} (keyboard interrupt) to exit the chat"
WELCOME_SUBTITLE = add_styletags_to_string(
    "This is your personal "
    + add_styletags_to_string(f"{BOT_NAME} AI assistant", "bot")
    + ", you can ask any coding related question directly in the command line or type "
    + add_styletags_to_string("!help", "command")
    + " to see the available commands.",
    style="info",
)
CONFIGFILE_OVERWRITE = f"A {add_styletags_to_string('.fridacli',style='code')} configuration file already exists. Do you want to overwrite it?"

# Error messages
ERROR_STR = "This is not a coding related question, is there anything else I can assist you with?"
ERROR_MISSING_CONFIGFILE = f"Missing configuration file. Execute {add_styletags_to_string('frida config', style='code')} to create it."

# Success messages
success_configfile_create = (
    lambda path: f"Configuration file {add_styletags_to_string(path, style='path')} "
    + f"{add_styletags_to_string(f'successfully created', style='success')}."
)
success_configfile_update = (
    lambda path: f"Configuration file {add_styletags_to_string(path, style='path')} "
    + f"{add_styletags_to_string(f'successfully updated', style='success')}."
)
