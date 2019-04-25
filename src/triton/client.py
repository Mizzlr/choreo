import json
from triton.result import Result
from triton.base import TritonConnection
import ulid


class TritonClient(TritonConnection):
    def submit(self, func, *args, **kwargs):
        taskid = ulid.ulid().lower()
        message = self._create_message(taskid, func, args, kwargs)
        print(f'Submitting {message} into queue {self._queue}')
        self._conn.lpush(self._queue, message)
        return Result(taskid)

    def _create_message(self, taskid, func, args, kwargs):
        return json.dumps({
            'func': str(func),
            'args': args,
            'kwargs': kwargs,
            'taskid': taskid,
        })


if __name__ == '__main__':
    client = TritonClient()
    results = []
    for i in range(10):
        result = client.submit('math.sqrt', i)
        results.append(result)

    for result in results:
        print('Getting result', result, '!')
        result.get()
