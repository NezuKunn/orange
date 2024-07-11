import OPi.GPIO as GPIO
import asyncio


async def sensor():
    GPIO.setmode(GPIO.BOARD)

    # (на вашей плате PI1 соответствует пину 12)
    SENSOR_PIN = 12

    GPIO.setup(SENSOR_PIN, GPIO.IN)

    try:
        index = 0
        while index < 5:
            signal = GPIO.input(SENSOR_PIN)
            if signal == GPIO.HIGH:
                index += 1
            else:
                index = 0
            await asyncio.sleep(0.1)
        
        GPIO.cleanup()
        
        return 1

    except Exception as e:
        print(e)
        return 0