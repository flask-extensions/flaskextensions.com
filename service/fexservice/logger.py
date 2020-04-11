"""
Autor - Jairo Matos da Rocha <devjairomr@gmail.com>
"""
from dynaconf import settings
from loguru import logger

formatter = "[ {level.icon}{level:^10}] {time:YYYY-MM-DD hh:mm:ss} {file} - {name}: {message}"


try:
    level = settings.LOGGER_LEVEL
except AttributeError:
    level = "INFO"
try:
    file_name = settings.LOGGER_FILE
except AttributeError:
    file_name = "logger.log"

# logger.add(sys.stderr, format=formatter, level=level,colorize=True)
logger.add(
    file_name, format=formatter, level=level, rotation="500 MB", colorize=True
)


if __name__ == "__main__":
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")
