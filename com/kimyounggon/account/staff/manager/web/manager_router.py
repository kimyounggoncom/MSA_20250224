from fastapi import APIRouter

from com.kimyounggon.account.staff.manager.web.manager_controller import ManagerController


class ManagerRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = ManagerController()

