def test_import_core_modules():
    from apeex.http import Kernel, RequestInterface, ResponseInterface, HttpKernelInterface
    assert Kernel is not None
    assert RequestInterface is not None
    assert ResponseInterface is not None
    assert HttpKernelInterface is not None
