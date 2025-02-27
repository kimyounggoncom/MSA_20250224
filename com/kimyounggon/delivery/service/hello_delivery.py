from com.kimyounggon.auth.user.service.abstract_user import AbstractUser


class HelloDelivery(AbstractUser):
     
     def handle(self, **kwargs):
        return "Hello, Delivery"