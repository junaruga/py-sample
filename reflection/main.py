from a.filea import ClassA
from a.b.fileb import ClassB


# class_name: foo.bar.Bar
def import_class(class_name):
    components = class_name.split('.')
    module = __import__(components[0])
    for comp in components[1:]:
        module = getattr(module, comp)
    return module


if __name__ == '__main__':
    a = ClassA()
    a.hello()

    b = ClassB()
    b.hello()

    reflection_a =  import_class(a.filea.ClassA)
    reflection_a.hello()
