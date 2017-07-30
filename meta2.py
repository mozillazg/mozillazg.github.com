# coding: utf-8
class A(type):
    test = {}
    def __new__(meta_cls, name, bases, attr_dict):
        print('new, ', meta_cls)
        return super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init, ', new_cls)
    def __call__(meta_cls, *args, **kwargs):
        print('call, ', meta_cls)
        return 'a'
        # return super().__call__(*args, **kwargs)
        
        
class G(metaclass=A):pass
G.test
