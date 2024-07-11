import asyncio
from datetime import datetime
import pytz

from modules.brightness import bright_mode

async def time(day, night, gmt_range):
    while True:
        gmt_timezone = pytz.timezone(f'Etc/GMT{0 - int(gmt_range)}')

        current_time_gmt = datetime.now(gmt_timezone)

        hours = current_time_gmt.hour
        minutes = current_time_gmt.minute

        day_h = int(day.split(":")[0])
        day_m = int(day.split(":")[1])
        night_h = int(night.split(":")[0])
        night_m = int(night.split(":")[1])

        if (hours > day_h) or (hours >= day_h and minutes >= day_m):
            bright_mode(100)
        elif (hours > night_h) or (hours >= night_h and minutes >= night_m) or (hours < night_h and hours < day_h):
            bright_mode(10)
        
        await asyncio.sleep(1)