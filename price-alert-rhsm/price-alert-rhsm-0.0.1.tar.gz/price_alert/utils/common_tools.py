import logging

from time import sleep

import schedule




def header(msg: str):
    print('=' * 60)
    print(msg.center(60))
    print('=' * 60)


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end=' ')
        sleep(1)
        num_of_secs -= 1


def footer(time: int):
    print('=' * 60)
    new_msg = f'Waiting {time} seconds for new request'
    print('=' * 60)
    return new_msg.center(60)


def schedule_function(function, time_seconds):
    try:
        schedule.every(time_seconds).seconds.do(function)
        while True:
            schedule.run_pending()
            print(f"{footer(time_seconds)}")
            sleep(time_seconds)
    except KeyboardInterrupt:
        print('User stop the script!')


if __name__ == '__main__':
    logging.info(schedule_function(footer(), 2))
