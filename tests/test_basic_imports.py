def test_import_core_modules():
    from apeex.http import HttpKernel
    from apeex.contracts.http import RequestInterface, ResponseInterface, HttpKernelInterface
    assert HttpKernel is not None
    assert RequestInterface is not None
    assert ResponseInterface is not None
    assert HttpKernelInterface is not None
