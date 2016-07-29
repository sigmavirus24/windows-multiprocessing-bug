import multiprocessing

import mccabe


def _target(queue):
    (cls, attribute, value) = queue.get()
    print('%r.%s = %r ... Expecting %r' % (
        cls, attribute, getattr(cls, attribute), value
    ))


def main():
    job_queue = multiprocessing.Queue()
    mccabe.McCabeChecker.max_complexity = 10
    job_queue.put((mccabe.McCabeChecker, 'max_complexity', 10))
    job_queue.put((mccabe.McCabeChecker, 'max_complexity', 10))
    job_queue.put((mccabe.McCabeChecker, 'max_complexity', 10))
    job_queue.put((mccabe.McCabeChecker, 'max_complexity', 10))
    job_queue.put((mccabe.McCabeChecker, 'max_complexity', 10))
    procs = [multiprocessing.Process(target=_target, args=(job_queue,))
             for _ in range(5)]
    for proc in procs:
        proc.join()
