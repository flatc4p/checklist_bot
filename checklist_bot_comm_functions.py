"""
Provides basic bot funtionality to communicate with telegram
Sending messages to chats
Receiving updates from telegram
"""
import os
import logging
import re
import requests

message_list = []
logging.basicConfig(filename='checklist_bot.log', encoding='utf-8', level=logging.DEBUG)

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
        logging.error("Timeout occured during sending message to Telegram API")

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
        logging.debug("Update ID found: ")
        offset = int(os.environ.get('UPDATE_ID')) + 1
        logging.debug(offset)
        logging.debug("Offset calculated to: %s", str(offset))
        update_command = update_command + '?offset=' + str(offset)
    else:
        logging.debug("No update id stored yet")

    try:
        response = requests.get(update_command, timeout=10)
    except TimeoutError:
        logging.error("Timeout occured during reading updates from Telegram API")
    response_json = response.json()
    logging.debug('')
    logging.debug("Received %i messages.", len(response_json['result']))
    logging.debug('')
    if len(response_json['result']):
        logging.debug(response_json['result'][-1])
        logging.debug('')
        logging.debug("Update ID: %i", (response_json['result'][-1]['update_id']))
        update_id = response_json['result'][-1]['update_id']
        os.environ['UPDATE_ID'] = str(update_id)
    return response_json['result']

def checklist_bot_build_reply_list(msg_list):
    """
    Builds a list of actions and replies out of received messages
    """
    #TODO:
    # - extract all valid commands from all messages to the bot and compile list of replies
    for entry in msg_list:
        msg = entry['message']
        logging.debug("Message number %i: %s", msg['message_id'], msg['text'])

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
