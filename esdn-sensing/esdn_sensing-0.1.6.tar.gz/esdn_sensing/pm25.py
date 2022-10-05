"""
`pm25`
================================================================================

Python library for PM25 Air Quality Sensor.

**Author(s):** `Colby Sawyer <https://github.com/ColbySawyer7>`_

Implementation Notes
--------------------
**Hardware:**
* ``_

**Software and Dependencies:**

"""

# pylint: disable=unused-import
import time
import serial
import logging
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
from esdn_sensing import SensorError


class PM25:
    pm10_std= 0
    pm25_std= 0
    pm100_std= 0
    pm10_env= 0
    pm25_env= 0
    pm100_env= 0
    part_03um= 0
    part_05um= 0
    part_10um= 0
    part_25um= 0
    part_50um= 0
    part_100um= 0

    def __init__(self,pm10_std= 0,pm25_std= 0,pm100_std= 0,pm10_env= 0,pm25_env= 0,pm100_env= 0,part_03um= 0,part_05um= 0,part_10um= 0,part_25um= 0,part_50um= 0,part_100um= 0):
    
        self.pm10_std= 0
        self.pm25_std= 0
        self.pm100_std= 0
        self.pm10_env= 0
        self.pm25_env= 0
        self.pm100_env= 0
        self.part_03um= 0
        self.part_05um= 0
        self.part_10um= 0
        self.part_25um= 0
        self.part_50um= 0
        self.part_100um= 0

    def get_date(self, sample_size=10,dec_factor=100):

        reset_pin = None
        # If you have a GPIO, its not a bad idea to connect it to the RESET pin

        # reset_pin = DigitalInOut(board.G0)
        # reset_pin.direction = Direction.OUTPUT
        # reset_pin.value = False

        # For use with Raspberry Pi/Linux:
        uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)


        # Connect to a PM2.5 sensor over UART
        # from adafruit_pm25.uart import PM25_UART
        # pm25 = PM25_UART(uart, reset_pin)

        # Create library object, use 'slow' 100KHz frequency!
        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        # Connect to a PM2.5 sensor over I2C
        pm25 = PM25_I2C(i2c, reset_pin)

        print("Found PM2.5 sensor, reading data...")

        try:
            aqdata = pm25.read()
            logging.info("Concentration Units (standard)")
            logging.info("---------------------------------------")
            logging.info(
                "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
                % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
            )
            logging.info("Concentration Units (environmental)")
            logging.info("---------------------------------------")
            logging.info(
                "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
                % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
            )
            logging.info("---------------------------------------")
            logging.info("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
            logging.info("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
            logging.info("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
            logging.info("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
            logging.info("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
            logging.info("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])

            self.pm10_std= aqdata["pm10 standard"]
            self.pm25_std= aqdata["pm25 standard"]
            self.pm100_std= aqdata["pm100 standard"]
            self.pm10_env= aqdata["pm10 env"]
            self.pm25_env= aqdata["pm25 env"]
            self.pm100_env= aqdata["pm100 env"]
            self.part_03um= aqdata["particles 03um"]
            self.part_05um= aqdata["particles 05um"]
            self.part_10um= aqdata["particles 10um"]
            self.part_25um= aqdata["particles 25um"]
            self.part_50um= aqdata["particles 50um"]
            self.part_100um= aqdata["particles 100um"]


            pm10_std = int((self.pm10_std*dec_factor))
            logging.info("pm10 standard: %0.1f %%" % pm10_std)

            pm25_std = int((self.pm25_std*dec_factor))
            logging.info("pm25 standard: %0.1f %%" % pm25_std)

            pm100_std = int((self.pm100_std*dec_factor))
            logging.info("pm100 standard: %0.1f %%" % pm100_std)

            pm10_env = int((self.pm10_env*dec_factor))
            logging.info("pm10 env: %0.1f %%" % pm10_env)

            pm25_env = int((self.pm25_env*dec_factor))
            logging.info("pm25 env: %0.1f %%" % pm25_env)

            pm100_env = int((self.pm100_env*dec_factor))
            logging.info("pm100 env: %0.1f %%" % pm100_env)

            part_03um = int((self.part_03um*dec_factor))
            logging.info("Particles > 0.3um / 0.1L air:: %0.1f %%" % part_03um)

            part_05um = int((self.part_05um*dec_factor))
            logging.info("Particles > 0.5um / 0.1L air:: %0.1f %%" % part_05um)

            part_10um = int((self.part_10um*dec_factor))
            logging.info("Particles > 1.0um / 0.1L air:: %0.1f %%" % part_10um)

            part_25um = int((self.part_25um*dec_factor))
            logging.info("Particles > 2.5um / 0.1L air:: %0.1f %%" % part_25um)

            part_50um = int((self.part_50um*dec_factor))
            logging.info("Particles > 5.0um / 0.1L air:: %0.1f %%" % part_50um)

            part_100um = int((self.part_100um*dec_factor))
            logging.info("Particles > 10.0um / 0.1L air:: %0.1f %%" % part_100um)
 
            #print(aqdata)
            sensor_data = bytearray(24)

            sensor_data[0] = (pm10_std >> 8) & 0xff
            sensor_data[1]= pm10_std & 0xff
            
            sensor_data[2] = (pm25_std >> 8) & 0xff
            sensor_data[3] = pm25_std & 0xff
            
            sensor_data[4] = (pm100_std >> 8) & 0xff
            sensor_data[5] = pm100_std & 0xff

            sensor_data[6] = (pm10_env >> 8) & 0xff
            sensor_data[7] = pm10_env & 0xff

            sensor_data[8] = (pm25_env >> 8) & 0xff
            sensor_data[9] = pm25_env & 0xff

            sensor_data[10] = (pm100_env >> 8) & 0xff
            sensor_data[11] = pm100_env & 0xff

            sensor_data[12] = (part_03um >> 8) & 0xff
            sensor_data[13] = part_03um & 0xff

            sensor_data[14] = (part_05um >> 8) & 0xff
            sensor_data[15] = part_05um & 0xff

            sensor_data[16] = (part_10um >> 8) & 0xff
            sensor_data[17] = part_10um & 0xff

            sensor_data[18] = (part_25um >> 8) & 0xff
            sensor_data[19] = part_25um & 0xff

            sensor_data[20] = (part_50um >> 8) & 0xff
            sensor_data[21] = part_50um & 0xff

            sensor_data[22] = (part_100um >> 8) & 0xff
            sensor_data[23] = part_100um & 0xff

            return sensor_data

        except: 
            raise SensorError('Unable to connect')
