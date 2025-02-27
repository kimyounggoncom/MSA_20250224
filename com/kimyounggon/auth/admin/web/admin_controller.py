from com.kimyounggon.auth.admin.web.admin_factory import AdminFactory


class AdminController:
    def __init__(self):
        pass
    
    def hello_admin(self, **kwargs):
        return AdminFactory.create(strategy="hello_admin", **kwargs)