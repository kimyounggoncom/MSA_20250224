from fastapi import APIRouter

from com.kimyounggon.account.staff.worker.web.worker_controller import WorkerController


class WorkerRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = WorkerController()

