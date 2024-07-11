import asyncio
import ndef

tasks = []

async def nfc(url):
    try:
        ndef_message = ndef.UriRecord(url)

        def on_startup(target):
            print("Подключен NFC модуль")

        def on_connect(tag):
            print("Подключен тег")
            try:
                tag.ndef.message = [ndef_message]
                print(f"Ссылка '{url}' успешно передана")
                return True
            except Exception as e:
                print(f"Ошибка при записи на тег: {e}")
            return False
        
        try:
            with nfc.ContactlessFrontend('usb') as clf:
                if clf.connect(rdwr={'on-startup': on_startup, 'on-connect': on_connect}):
                    return True
        except Exception as e:
            print(f"Ошибка подключения: {e}")

        asyncio.sleep(1)

    except asyncio.exceptions.CancelledError:
        return

def start_nfc(url):
    nfc_task = asyncio.create_task(nfc(url))
    tasks.append(nfc_task)

def stop_nfc():
    if tasks != []:
        for task in tasks:
            task.cancel()