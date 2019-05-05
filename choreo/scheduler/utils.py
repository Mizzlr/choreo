import calendar
import croniter

from datetime import datetime, timedelta
import logging

from choreo.multirq.utils import ColorizingStreamHandler


# from_unix from times.from_unix()
def from_unix(string):
    """Convert a unix timestamp into a utc datetime"""
    return datetime.utcfromtimestamp(float(string))


# to_unix from times.to_unix()
def to_unix(dt):
    """Converts a datetime object to unixtime"""
    return calendar.timegm(dt.utctimetuple())


def get_next_scheduled_time(cron_string):
    """Calculate the next scheduled time by creating a crontab object
    with a cron string"""
    itr = croniter.croniter(cron_string, datetime.utcnow())
    return itr.get_next(datetime)


def setup_loghandlers(level='INFO'):
    logger = logging.getLogger('choreo.scheduler.scheduler')
    if not logger.handlers:
        logger.setLevel(level)
        formatter = logging.Formatter(fmt='%(asctime)s %(message)s',
                                      datefmt='%H:%M:%S')
        handler = ColorizingStreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)


def rationalize_until(until=None):
    """
    Rationalizes the `until` argument used by other functions. This function
    accepts datetime and timedelta instances as well as integers representing
    epoch values.
    """
    if until is None:
        until = "+inf"
    elif isinstance(until, datetime):
        until = to_unix(until)
    elif isinstance(until, timedelta):
        until = to_unix((datetime.utcnow() + until))
    return until
