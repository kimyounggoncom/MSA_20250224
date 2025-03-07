from fastapi import APIRouter

from com.kimyounggon.account.leadership.director.web.director_controller import DirectorController


class DirectorRouter:
    def __init__(self):
        pass

    router = APIRouter()
    controller = DirectorController()

