from com.kimyounggon.delivery.web.delivery_factory import DeliveryFactory


class DeliveryController:
    def __init__(self):
        pass

    def hello_delivery(self, **kwargs):
        return DeliveryFactory.create(strategy="hello_delivery", **kwargs)
