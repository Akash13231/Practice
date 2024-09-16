import logging

def test_logging_demo():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')

    formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    filehandler.setFormatter(formater)

    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')