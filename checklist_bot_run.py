import time
import os
import requests

# variables used throughout whole process
BOT_TOKEN = '6887660248:AAFR7KFmD57LFFgfi_wbdJfMvannOgMA2oE'

#
def checklist_bot_update_chats():
    #TODO:
    # - call update API function to get list of new messages to bot

def checklist_bot_build_reply_list():
    #TODO:
    # - extract all valid commands from all messages to the bot and compile list of replies

def checklist_bot_respond():
    #TODO:
    # - go through list of active chats to reply to recent messages


    


# Set bot token in environment variable
os.environ['BOT_TOKEN'] = BOT_TOKEN

while True:
    checklist_bot_update()
