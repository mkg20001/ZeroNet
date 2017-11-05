try:
    from Worker import Worker
    from WorkerManager import WorkerManager
except Exception as err:
    from Worker.Worker import Worker
    from Worker.WorkerManager import WorkerManager
