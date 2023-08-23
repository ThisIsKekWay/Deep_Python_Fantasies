import logging
import __main__


FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}"\n' \
         'в строке {lineno:03d} функция "{funcName}()"' \
         'записала сообщение:\n{msg}\n'

logging.basicConfig(
    format=FORMAT,
    style='{',
    filename=f'{__main__.__file__} logs.log',
    filemode='a',
    encoding='utf-8',
    level=logging.DEBUG)
logger = logging.getLogger(__main__.__file__)


def log_warn (msg):
    logger.warning(msg)


def log_info (msg):
    logger.info(msg)
