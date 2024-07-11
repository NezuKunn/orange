
from modules.video import download_video, view_video
from modules.qr import qr
from modules.nfc import start_nfc, stop_nfc
import requests

async def desk(server_file_name, equipid, videoid, equipip, gpslat, gpslan):
    download_video(server_file_name)

    url = f"https://link.olhar.media/?golink=1&equipid={equipid}videoid={videoid}&equipip={equipip}&gpslat={gpslat}&gpslan={gpslan}"

    await qr(url)

    start_nfc(url)

    await view_video()

    stop_nfc()

    resp = requests.get(f"https://api.olhar.media/?regview=1&equipid={equipid}&videoid={videoid}&vq=1&equipip={equipip}&gpsposlat={gpslat}&gpsposlon={gpslan}")