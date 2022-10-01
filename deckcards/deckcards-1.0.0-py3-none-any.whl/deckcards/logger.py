import logging

def log(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_file_handler = logging.FileHandler(f"{__name__}.log", mode='w')
    log_file_handler.setLevel(logging.INFO)
    log_console_handler = logging.StreamHandler()
    log_console_handler.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(lineno)s: %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file_handler.setFormatter(formatter)
    log_console_handler.setFormatter(formatter)

    logger.addHandler(log_file_handler)
    logger.addHandler(log_console_handler)
    return logger
