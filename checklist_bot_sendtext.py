import requests
import os

def checklist_bot_sendtext(message):

    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    CHAT_ID = os.environ.get('CHAT_ID')
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)

    return response.json()

test = checklist_bot_sendtext("This is a test")
print(test)

