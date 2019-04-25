from triton.base import TritonConnection
import time
import json


class Result(TritonConnection):
    def __init__(self, taskid):
        super(Result, self).__init__()
        self._taskid = taskid

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self._taskid}>'

    def get(self):
        while not self._conn.hexists(self._results, self._taskid):
            print(f'Waiting for result of {self._taskid} from {self._results}')
            time.sleep(0.1)

        result = self._conn.hget(self._results, self._taskid)
        result = json.loads(result.decode())
        self._conn.hdel(self._results, self._taskid)
        print(f'Got result for taskid {self._taskid}: {result}')
        return result
