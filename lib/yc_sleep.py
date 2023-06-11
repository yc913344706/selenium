from lib.log import color_logger
from time import sleep


def ycsleep(sleep_time, sleep_info=''):
    color_logger.info(f"start sleep {sleep_time}s for {sleep_info}...")
    sleep(sleep_time)
