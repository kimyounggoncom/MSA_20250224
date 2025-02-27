
from com.kimyounggon.auth.user.service.abstract_user import AbstractUser


class HelloAdmin(AbstractUser):
     
    def handle(self, **kwargs):
        return "Hello, Admin"