from fastapi import APIRouter

from com.kimyounggon.account.common.user.web.user_controller import UserController

router = APIRouter()
controller = UserController()
