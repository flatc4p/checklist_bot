"""
Provides basic bot funtionality to communicate with telegram
Sending messages to chats
Receiving updates from telegram
"""
import os
import re
import requests

def checklist_bot_sendtext(message, chat_id):
    """
    Send text message to telegram chat.
    Message is passed as parameter to function.
    """
    #TODO: support multiple chat ids
    send_text = os.environ.get('API_URL') + os.environ.get('BOT_TOKEN') \
    + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    try:
        response = requests.get(send_text, timeout=10)
    except TimeoutError:
        print("Timeout occured during sending message to Telegram API")

    return response.json()

def checklist_bot_update_chats():
    """
    Checking all messages sent to bot or in chats where bot is present. 
    Built list of messages to react to.
    """
    #TODO:
    # - DONE:call update API function to get list of new messages to bot 
    # - Store received messages in appropriate data structure
    # - add error handling to avoid incorrect bot tokens
    update_command = os.environ.get('API_URL') + os.environ.get('BOT_TOKEN') + '/getUpdates'
    if os.environ.get('UPDATE_ID'):
        print("Update ID found: ")
        offset = int(os.environ.get('UPDATE_ID')) + 1
        print(offset)
        print("Offset calculated to: " + str(offset))
        update_command = update_command + '?offset=' + str(offset)
    else:
        print("No update id stored yet")

    try:
        response = requests.get(update_command, timeout=10)
    except TimeoutError:
        print("Timeout occured during reading updates from Telegram API")
    response_json = response.json()
    print('')
    print('')
    print(len(response_json['result']))
    print('')
    print('')
    if len(response_json['result']):
        print(response_json['result'][-1])
        print('')
        print('')
        print(response_json['result'][-1]['update_id'])
        update_id = response_json['result'][-1]['update_id']
        os.environ['UPDATE_ID'] = str(update_id)

    return response_json

def checklist_bot_build_reply_list(msg_list):
    """
    Builds a list of actions and replies out of received messages
    """
    #TODO:
    # - extract all valid commands from all messages to the bot and compile list of replies
    for msg in msg_list:
        re.search('', msg)

def checklist_bot_respond():
    """
    Working through list of reply list
    """
    #TODO:
    # - go through list of active chats to reply to recent messages
    reply_command = ''
    try:
        response = requests.get(reply_command, timeout=10)
    except TimeoutError:
        print("Timeout occured during sending response to Telegram API")

    return response.json()
