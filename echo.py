import time
from handlers import (
    get_last_update,
    sendMessage,
    sendSticker,
    sendContact,
)
from pprint import pprint  


def main():
    last_update_id = 3
    while True:
        current_update = get_last_update()
        current_update_id = current_update['update_id']

        if last_update_id != current_update_id:
            message = current_update['message']
            chat_id = message['chat']['id']
            
            sticker = message.get('sticker', False)
            if sticker != False:
                file_id = sticker['file_id']
                sendSticker(chat_id, file_id)

            text = message.get('text', False)
            if text != False:
                sendMessage(chat_id, text)

            contact = message.get('contact', False)
            if contact != False:
                phone_number = contact['phone_number']
                first_name = contact['first_name']
                sendContact(chat_id, phone_number, first_name)

            last_update_id = current_update_id
        
        time.sleep(1)

main()