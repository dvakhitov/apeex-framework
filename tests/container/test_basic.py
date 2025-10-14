from apeex.container import Container

class ServiceA:
    pass

class ServiceB:
    def __init__(self, service_a: ServiceA):
        self.service_a = service_a

def test_set_and_get_service():
    container = Container()
    a = ServiceA()
    container.set("ServiceA", a)
    assert container.get("ServiceA") is a

def test_autowire_service():
    container = Container()
    b = container.autowire(ServiceB)
    assert isinstance(b, ServiceB)
    assert isinstance(b.service_a, ServiceA)

def test_singleton_scope():
    container = Container()
    a1 = container.autowire(ServiceA)
    a2 = container.autowire(ServiceA)
    assert a1 is a2
