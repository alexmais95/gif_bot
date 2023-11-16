import logging


class BasicLog:
    def log_config(self, loglevel=logging.INFO):
        logger_name = (__name__)
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        log_file = logging.FileHandler('log_conf/log_list.log')
        formater = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
        log_file.setFormatter(formater)
        logger.addHandler(log_file)
        return logger
