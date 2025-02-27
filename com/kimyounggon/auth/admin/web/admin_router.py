from fastapi import APIRouter

from com.kimyounggon.auth.admin.web.admin_controller import AdminController


router = APIRouter()
controller = AdminController()

@router.get(path= "/")
async def hello_admin():
    return controller.hello_admin()