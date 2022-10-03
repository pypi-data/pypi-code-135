from src.Kiwrious.KiwriousService import KiwriousService
import time

def print_sensor_object(service: KiwriousService, sensor_type):
    for n in range(5):
        print(service.get_sensor_reading())
        time.sleep(1)

def sensor_disconnect():
    print('a sensor diconnected')

#def main():

    #my_service = KiwriousService()
    #my_service.start_service()

    #my_service.on_sensor_disconnection(sensor_disconnect, my_service.TEMPERATURE, 0, False)
    #my_service.on_sensor_connection(print_sensor_object, my_service.TEMPERATURE, 0, True, my_service, my_service.TEMPERATURE)
    


#if __name__ == '__main__':
    #main()





