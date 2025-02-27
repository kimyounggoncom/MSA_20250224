from com.kimyounggon.auth.admin.service.hello_admin import HelloAdmin


strategy_map = {
    "hello_admin": HelloAdmin(),
}

class AdminFactory:
    
    @staticmethod
    def create(strategy: str, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)
