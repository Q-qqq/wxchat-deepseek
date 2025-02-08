import threading


def threaded(func):
    """多线程化一个目标函数并返回线程或函数结果的装饰器"""

    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread
    return wrapper
