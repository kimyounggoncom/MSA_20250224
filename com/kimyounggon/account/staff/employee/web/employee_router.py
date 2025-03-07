from fastapi import APIRouter

from com.kimyounggon.account.staff.employee.web.employee_controller import EmployeeController


class EmployeeRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = EmployeeController()

