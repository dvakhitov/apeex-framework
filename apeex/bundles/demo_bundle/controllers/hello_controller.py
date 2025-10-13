class HelloController:
    """Example controller using HelloService."""

    def __init__(self, service):
        self.service = service

    def greet(self, name: str) -> str:
        return self.service.say_hello(name)
