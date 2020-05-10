class SingletonMeta(type):
    __instance = None

    def __call__(cls):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls)
        return cls.__instance


class Singleton(metaclass=SingletonMeta):

    def get_instance(self):
        return self
