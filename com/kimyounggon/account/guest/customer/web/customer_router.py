from fastapi import APIRouter
from com.kimyounggon.account.guest.customer.web.customer_controller import CustomerController


class CustomerRouter:
    def __init__(self):
        pass

router = APIRouter()
controller = CustomerController()