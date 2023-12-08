from enum import Enum


class AllowStatus(str, Enum):
    """Статусы разметки."""

    markup = 'markup'
    unclaimed = 'unclaimed'
    postponed = 'postponed'
    waiting = 'waiting'
