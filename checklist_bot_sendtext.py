import requests

def checklist_bot_sendtext(message):

    bot_token = '6887660248:AAFR7KFmD57LFFgfi_wbdJfMvannOgMA2oE'
    bot_chatID = '11456116'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)

    return response.json()

test = checklist_bot_sendtext("This is a test")
print(test)

