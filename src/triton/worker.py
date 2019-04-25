from triton.base import TritonConnection
import json
import importlib
import traceback
import time


class TritonWorker(TritonConnection):

    def run(self):
        print('Worker started')
        while True:
            try:
                _, task = self._conn.brpop(self._queue)
                print('brpoped:', task)
                task = json.loads(task.decode())
                taskid, result = self._execute(task)
                self._conn.hset(self._results, taskid, json.dumps(result))
            except Exception:
                traceback.print_exc()
                print('Well continuing anyways ... ')

    def _execute(self, task):
        func = task['func']
        args = task['args']
        kwargs = task['kwargs']
        taskid = task['taskid']
        module = importlib.import_module(self._get_module_name(func))
        func = getattr(module, self._get_func_name(func))
        time.sleep(4)
        result = func(*args, **kwargs)
        print(f'Task: {task}, result: {result}')
        return taskid, result

    def _get_module_name(self, func):
        return '.'.join(func.split('.')[:-1])

    def _get_func_name(self, func):
        return func.split('.')[-1]


if __name__ == '__main__':
    worker = TritonWorker()
    worker.run()
