# coding: utf-8
class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
    
A()
class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(*args, **kwargs)
        
    
A()
object.__new__
get_ipython().magic('pinfo object.__new__')
help(type)
help(type)
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new')
        super().__new__(meta_cls, name, bases, attr_dict)
        
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new')
        super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init')
    def __call__(meta_cls, *args, **kwargs):
        print('call')
        return super().__call__(meta_cls, *args, **kwargs)
        
class B(meta_class=A): pass
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new')
        super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init')
    def __call__(meta_cls, *args, **kwargs):
        print('call')
        return super().__call__(*args, **kwargs)
        
        
class B(meta_class=A): pass
class B(metaclass=A): pass
class A(type):
    # def __new__(meta_cls, name, bases, attr_dict):
    #     print('new')
    #     super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init')
    def __call__(meta_cls, *args, **kwargs):
        print('call')
        return super().__call__(*args, **kwargs)
        
        
class B(metaclass=A): pass
class C(metaclass=A): pass
C()
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new')
        super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init')
    def __call__(meta_cls, *args, **kwargs):
        print('call')
        return super().__call__(*args, **kwargs)
        
        
class D(metaclass=A): pass
D()
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new')
        return super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init')
    def __call__(meta_cls, *args, **kwargs):
        print('call')
        return super().__call__(*args, **kwargs)
        
        
class E(metaclass=A): pass
D()
E()
class F(metaclass=A):
    def __new__(cls, *args, **kwargs):
        print('f new')
        return super().__new__(*args, **kwargs)
    def __init__(self, *args, **kwargs):
        print('f init')
        
F()
class F(metaclass=A):
    def __new__(cls, *args, **kwargs):
        print('f new')
        return super().__new__(cls, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        print('f init')
        
F()
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new, ', meta_cls)
        return super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init, ', new_cls)
    def __call__(meta_cls, *args, **kwargs):
        print('call, ', meta_cls)
        return super().__call__(*args, **kwargs)
        
        
class F(metaclass=A):
    def __new__(cls, *args, **kwargs):
        print('f new, ', cls)
        return super().__new__(cls, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        print('f init, ', self)
        
        
F()
class A(type):
    def __new__(meta_cls, name, bases, attr_dict):
        print('new, ', meta_cls)
        return super().__new__(meta_cls, name, bases, attr_dict)
    def __init__(new_cls, name, bases, attr_dict):
        print('init, ', new_cls)
    def __call__(meta_cls, *args, **kwargs):
        print('call, ', meta_cls)
        return 'a'
        # return super().__call__(*args, **kwargs)
        
        
class F(metaclass=A):
    def __new__(cls, *args, **kwargs):
        print('f new, ', cls)
        return super().__new__(cls, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        print('f init, ', self)
        
        
F()
