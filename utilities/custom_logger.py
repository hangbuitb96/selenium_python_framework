import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    # get the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # by default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("automation.log", mode='a') # a = append, w = overwrite
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
