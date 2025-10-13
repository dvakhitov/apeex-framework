from apeex.container.container import Container
from apeex.examples.sample_bundle import SampleBundle
from apeex.examples.services import UserService, Logger

def test_bundle_services():
    container = Container()
    bundle = SampleBundle()
    container.build_bundle(bundle)

    logger = container.get("Logger")
    assert isinstance(logger, Logger)

    user_service = container.get("UserService")
    assert isinstance(user_service, UserService)
    assert user_service.logger is logger

    user_service2 = container.autowire(UserService)
    assert user_service2 is user_service  # singleton confirmed
