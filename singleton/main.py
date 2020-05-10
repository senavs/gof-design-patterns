from singleton.singleton import Singleton

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton().get_instance()
    s4 = Singleton().get_instance()

    print(s1 == s2 == s3 == s4)
