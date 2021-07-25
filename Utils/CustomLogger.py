import logging

class Logsetup:
    @staticmethod
    def getlogparabank():
        logging.basicConfig(filename="Logs\\parademolog.log",
                            format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger