import redis


class TritonConnection:
    def __init__(self, host='localhost', port=6379, db=0, queue='triton'):
        self._conn = redis.Redis(host=host, port=port, db=db)
        self._queue = queue
        self._results = queue + '_results'
