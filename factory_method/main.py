from factory_method.concrete_factory import Tangram

if __name__ == '__main__':
    print(Tangram.create_geometric_form(3, 4, 5))  # <Triangle at 0x7f921119f4f0>
    print(Tangram.create_geometric_form(3, 4, 5, 6))  # <Rectangle at 0x7f921119f4f0>
    print(Tangram.create_geometric_form(3, 3, 3, 3))  # <Square at 0x7f921119f4f0>
