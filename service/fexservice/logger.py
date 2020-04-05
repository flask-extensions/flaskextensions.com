"""
Autor - Jairo Matos da Rocha <devjairomr@gmail.com>
Baseado na Live de Python
https://github.com/dunossauro/live-de-python/blob/master/codigo/Live48/complex/full_log.py
"""
import logging
from dynaconf import settings

def create_logger(name:str):
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(filename)s - %(name)s: %(message)s',
        '%Y-%m-%d %H:%M:%S'
    )


    # Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # File Handler
    try:
        fh = logging.FileHandler(settings.LOGGER_FILE)
    except AttributeError as e:
        fh = logging.FileHandler('log.log')
    try:
        if settings.DEBUG == True:
            fh.setLevel(logging.DEBUG)
        else:
            fh.setLevel(logging.WARNING)
    except AttributeError as e:
        fh.setLevel(logging.WARNING)
    fh.setFormatter(formatter)

    # Adicionando o handlers
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

if __name__ == '__main__':
    logger = create_logger(__name__)
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
