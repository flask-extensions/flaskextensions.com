"""
Inspirado no código do Dunossauro
https://github.com/dunossauro/live-de-python/blob/136e191e2b2cd6e02548e1931928f89f41a3dfe8/codigo/Live50/exemplo_3.py
"""

import sched, time
from dynaconf import settings
from typer import run
from typing import Callable
from datetime import datetime, timedelta
from fexservice.consumer import fetch_github

cron = sched.scheduler(timefunc=time.time)


def enqueue(action: Callable):
    new_delay = datetime.now().replace(second=0, microsecond=0)
    new_delay += timedelta(seconds=settings.DELAY)
    print(new_delay)
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
