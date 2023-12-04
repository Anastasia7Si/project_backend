from enum import Enum


class AllowStatus(str, Enum):
    markup = 'markup'
    unclaimed = 'unclaimed'
    postponed = 'postponed'
    waiting = 'waiting'
