import pyax
# from pyax.observer import Observer, start, stop
# from time import time

class App(object):
    def __init__(self):
        acc = pyax.get_application_by_name("Firefox Nightly")
        values = acc.get_multiple_attribute_values("AXRole", "AXRoleDescription", "AXSubrole", "AXTitle", "AXDescription")
        print(values)
        self.observer = pyax.create_observer(acc.pid, self.callback)
        self.observer.add_notifications(*pyax.EVENTS)

    def callback(self, observer, element, notificationName, info):
        print(notificationName, element)
        # self.observer.remove_notification(*pyax.EVENTS)

    def start(self):
      pyax.start()

app = App()
print(app)
app.start()