"""
Inspirado no código do Dunossauro
https://github.com/dunossauro/live-de-python/blob/136e191e2b2cd6e02548e1931928f89f41a3dfe8/codigo/Live50/exemplo_3.py
"""

import sched
import time
from datetime import datetime, timedelta
from typing import Callable

from dynaconf import settings
from typer import run

from fexservice.consumer import fetch_github
from fexservice.logger import logger

cron = sched.scheduler(timefunc=time.time)

logger.info(
    f"The DELAY was set to {settings.DELAY} seconds"
    + f"and PRIORITY to {settings.PRIORITY}"
)


def enqueue(action: Callable):
    new_delay = datetime.now()
    # new_delay = datetime.now().replace(second=0, microsecond=0)
    new_delay += timedelta(seconds=settings.DELAY)
    logger.info(f"Next call will be made at {new_delay}")
    cron.enterabs(
        new_delay.timestamp(), priority=settings.PRIORITY, action=action
    )


def task_fetch_github():
    fetch_github()
    enqueue(task_fetch_github)


def main():
    enqueue(task_fetch_github)
    cron.run(blocking=True)


def cli():
    run(main)
