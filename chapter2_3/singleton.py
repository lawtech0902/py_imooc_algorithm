# _*_ coding: utf-8 _*_
"""
单例模式实现
__author__ = 'lawtech'
__date__ = '2018/4/24 下午8:10'
"""


# 装饰器实现
def singleton(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton
class A(object):
    pass


# module实现，python天然的单例模式
# singleton.py
class Singleton(object):
    pass


isinstance = Singleton()


# 调用
# from singleton import instance
# instance

# 父类继承实现
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class B(Singleton):
    pass

# 元类实现
class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls.__new__(cls, *args, **kwargs)
        return cls._instance

class C(object,metaclass=Singleton):
    pass

