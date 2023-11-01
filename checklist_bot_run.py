import time
import os
import requests
import re

# variables used throughout whole process
BOT_TOKEN = os.environ.get('BOT_TOKEN')

#
def checklist_bot_update_chats():
    #TODO:
    # - call update API function to get list of new messages to bot
    update_command = ''
    response = requests.get(update_command)

    return response.json() 


def checklist_bot_build_reply_list(msg_list):
    #TODO:
    # - extract all valid commands from all messages to the bot and compile list of replies
    for msg in msg_list:
        re.search('', msg))

def checklist_bot_respond():
    #TODO:
    # - go through list of active chats to reply to recent messages
    reply_command = ''
    response = requests.get(reply_command)

    return response.json() 


while True:
    checklist_bot_update_chats()

