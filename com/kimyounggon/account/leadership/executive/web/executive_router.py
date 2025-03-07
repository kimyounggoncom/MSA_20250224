from fastapi import APIRouter

from com.kimyounggon.account.leadership.executive.web.executive_controller import ExecutiveController


class ExecutiveRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = ExecutiveController()

