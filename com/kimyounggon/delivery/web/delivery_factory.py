from com.kimyounggon.delivery.service.hello_delivery import HelloDelivery


strategy_map = {
    "hello_delivery": HelloDelivery(),
}

class DeliveryFactory:
    
    @staticmethod
    def create(strategy: str, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)