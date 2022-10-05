file_name = 'test1.pt_test1_2'
def test_func():
    print('这是test1.pt_test1_2.test_func')
class Test_class():
    cls_attr = 'test1.pt_test1_2.Test_class.cls_attr'
    def __init__(self):
        self.self_attr = 'test1.pt_test1_2.Test_class.self_attr'
    def self_func(self):
        print('这是test1.pt_test1_2.Test_class.self_func')
    @classmethod
    def cls_func(cls):
        print('这是test1.pt_test1_2.Test_class.cls_func')