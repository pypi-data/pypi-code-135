import logging

if __name__ == '__main__':
    logging_level = logging.DEBUG
    main_logger = logging.getLogger()
    main_logger.setLevel(logging_level)
    logging_handler = logging.FileHandler("log.log")
    logging_handler.setLevel(logging_level)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging_handler.setFormatter(formatter)
    main_logger.addHandler(logging_handler)

    from create_project import test

