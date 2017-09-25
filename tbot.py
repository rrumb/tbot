import requests
from time import sleep

url = 'https://api.telegram.org/bot433006721:AAEUDSy0EKAZK71JctawQLqMyZMWlE0mMgA/'

def get_updates_json(request):
    params = {'timeout': 1000, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    results = data['result']    
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        lu = last_update(get_updates_json(url))
        if update_id == lu['update_id']:
            if lu['message']['text'] == '0001':
                send_mess(get_chat_id(lu), 'error description 0001')
              
            update_id += 1
    sleep(3)

if __name__ == '__main__':
    main()
