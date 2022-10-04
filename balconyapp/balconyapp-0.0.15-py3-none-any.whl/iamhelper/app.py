from balcony.app import AppConfig, app_registry, AppBase


class MyApp(AppBase):
    name = 'MyApp'
    

class MyAppConfig(AppConfig):
    name = "MyAppConfig"
    verbose_name = "MyApplication"


class YourAppConfig(AppConfig):
    name = "YourAppConfig"
    verbose_name = "YourApplication"
