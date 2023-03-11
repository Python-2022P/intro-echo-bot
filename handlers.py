import json
import requests

TOKIN = '6097521187:AAHbPqQPSlFP54uT-Sj6MdnJpeBB_5Idsmg'


def get_last_update():
    url = f'https://api.telegram.org/bot{TOKIN}/getUpdates'
    data = requests.get(url)
    return data.json()['result'][-1]

def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    data = requests.get(url, params={'chat_id':chat_id, 'text':text})
    return data.json()

def sendDocument(chat_id, document):
    url = f'https://api.telegram.org/bot{TOKIN}/sendDocument'
    data = requests.get(url, params={'chat_id':chat_id, 'text':document})
    return data.json()

def sendPhoto(chat_id, photo):
    url = f'https://api.telegram.org/bot{TOKIN}/sendPhoto'
    data = requests.get(url, params={'chat_id':chat_id, 'photo':photo})
    return data.json()

def sendDice(chat_id, emoji):
    url = f'https://api.telegram.org/bot{TOKIN}/sendDice'
    data = requests.get(url, params={'chat_id':chat_id, 'emoji':emoji})
    return data.json()

def sendSticker(chat_id, sticker):
    url = f'https://api.telegram.org/bot{TOKIN}/sendSticker'
    data = requests.get(url, params={'chat_id':chat_id, 'sticker':sticker})
    return data.json()

def sendVideo(chat_id, video):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVideo'
    data = requests.get(url, params={'chat_id':chat_id, 'video':video})
    return data.json()

def sendAudio(chat_id, audio):
    url = f'https://api.telegram.org/bot{TOKIN}/sendAudio'
    data = requests.get(url, params={'chat_id':chat_id, 'audio':audio})
    return data.json()

def sendVoice(chat_id, voice):
    url = f'https://api.telegram.org/bot{TOKIN}/sendVoice'
    data = requests.get(url, params={'chat_id':chat_id, 'voice':voice})
    return data.json()