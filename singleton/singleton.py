class SingletonMeta(type):
    __instance = None

    def __call__(cls):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls)
        return cls.__instance


class Singleton(metaclass=SingletonMeta):

    def get_instance(self):
        return self


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton().get_instance()
    s4 = Singleton().get_instance()

    print(s1 == s2 == s3 == s4)
