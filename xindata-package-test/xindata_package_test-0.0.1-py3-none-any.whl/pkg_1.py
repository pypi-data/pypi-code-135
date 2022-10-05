file_name = 'package_test.pkg_1'
def test_func():
    print('这是package_test.pkg_1.test_func')
class Test_class():
    cls_attr = 'package_test.pkg_1.Test_class.cls_attr'
    def __init__(self):
        self.self_attr = 'package_test.pkg_1.Test_class.self_attr'
    def self_func(self):
        print('这是package_test.pkg_1.Test_class.self_func')
    @classmethod
    def cls_func(cls):
        print('这是package_test.pkg_1.Test_class.cls_func')