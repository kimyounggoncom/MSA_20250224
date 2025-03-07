from fastapi import APIRouter
from com.kimyounggon.account.guest.subscriber.web.subscriber_controller import SubscriberController


class SubscriberRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = SubscriberController()
    
