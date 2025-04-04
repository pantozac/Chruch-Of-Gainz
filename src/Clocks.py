from datetime import datetime
from typing import List

class Clock():
    '''
    Will work for AMRAP, for time
    '''
    work_set: datetime | List[datetime] | None
    countdown: bool

class Interval(Clock):
    rounds: int
    rest_time: datetime

class EMOM(Clock):
    interval: int


