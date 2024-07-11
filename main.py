import configparser
import asyncio

from modules.data import get_main_data
from modules.gps import get_location
# from modules.sensor import sensor
from modules.script import run_script
from modules.time import time
from modules.desk import desk
from modules.video import destroy_overlay


# config = configparser.ConfigParser()
# config.read('config.ini')

# equipid = config["configs"]["equipid"]
equipid = "1"
# day = config['configs']['day']
day = "10:30"
# night = config["configs"]["night"]
night = "5:00"
# gmt = config["configs"]["gmt"]
gmt = "+7"


async def start():
    asyncio.gather(time(day, night, "+7"))

    if run_script(equipid):

        response = get_main_data(equipid)
        my_loc_data = get_location()

        if "error" not in my_loc_data:
            my_location = my_loc_data["city"]
            equipip = my_loc_data["ip"]
            gpslat = my_loc_data["latitude"]
            gpslan = my_loc_data["longitude"]

            for data in response:

                server_file_name = data["serverfilename"]
                videoid = data["id"]

                # for item in data['locations']:
                #     if item["enname"].lower() == my_location.lower():
                        # if await sensor():
                
                

                await desk(server_file_name, equipid, videoid, equipip, gpslat, gpslan)
    
    destroy_overlay()

def main():
    asyncio.run(start())

if __name__ == "__main__":
    main()