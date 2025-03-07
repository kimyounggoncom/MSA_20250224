from fastapi import APIRouter

from com.kimyounggon.account.staff.supervisor.web.supervisor_controller import SupervisorController


class SupervisorRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = SupervisorController()

