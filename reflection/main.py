from a.filea import ClassA
from a.b.fileb import ClassB


# class_name: foo.bar.Bar
def import_class(class_name):
    components = class_name.split('.')
    module = __import__(components[0])
    for comp in components[1:]:
        # print(repr(comp))
        module = getattr(module, comp)
    return module


if __name__ == '__main__':
    a = ClassA()
    print(repr(a))
    a.hello()

    b = ClassB()
    print(repr(b))
    b.hello()

    reflection_clsa = import_class('a.filea.ClassA')
    print(repr(reflection_clsa))
    reflection_a = reflection_clsa()
    print(repr(reflection_a))
    reflection_a.hello()

    reflection_clsb = import_class('a.b.fileb.ClassB')
    print(repr(reflection_clsb))
    reflection_b = reflection_clsb()
    print(repr(reflection_b))
    reflection_b.hello()
