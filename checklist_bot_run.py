"""
Run script to run the checklist bot
Calling all the necessary functions to manage communication and
logic of task list management from ddedicated modules
"""
import time
import os
import checklist_bot_comm_functions as comm
import checklist_bot_setenv as botenv

def main():
    """
    Running the bot (looping checking for updates and reply/react)
    """
    # variables used throughout whole process
    botenv.checklist_bot_setenv()
    bot_token = os.environ.get('BOT_TOKEN')
    api_url = os.environ.get('CHAT_ID')

    while True:
        messages = comm.checklist_bot_update_chats()
        comm.checklist_bot_build_reply_list(messages)
        time.sleep(10)

if __name__ == "__main__":
    main()
