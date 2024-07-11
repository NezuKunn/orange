import requests
import subprocess

def run_script(equipid):
    try:
        response = requests.get(f'https://api.olhar.media/?getconfigupdate&equipid={equipid}').json()
        script = response[0]["listing"]

        with open("temp/script_server.py", "w") as file:
            file.write(script)
        
        subprocess.run(['python', 'temp/script_server.py'], check=True)
        print(0)
        resp = requests.get(f'https://api.olhar.media/?getconfigupdate=1&equipid={equipid}')
        return 1
    except:
        resp = requests.get(f'https://api.olhar.media/?getconfigupdate=2&equipid={equipid}')
        print("Error with script")
        return 0