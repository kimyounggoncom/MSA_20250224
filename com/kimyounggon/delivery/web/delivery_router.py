from fastapi import APIRouter
from com.kimyounggon.delivery.web.delivery_controller import DeliveryController


router = APIRouter()
controller = DeliveryController()

@router.get(path= "/")
async def hello_delivery():
    return controller.hello_delivery()