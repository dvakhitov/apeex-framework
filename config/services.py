from apeex.adapters.http.router_adapter import RouterAdapter
from apeex.adapters.orm.orm_adapter import OrmAdapter
from apeex.adapters.config.yaml_loader_adapter import YAMLLoaderAdapter
from apeex.http.http_kernel import HttpKernel
from apeex.adapters.http.fastapi_response_emitter import FastAPIResponseEmitter

# Services dictionary: key - name in the container, value - class or factory
SERVICES = {
    "router": RouterAdapter,
    "orm": OrmAdapter,
    "config_loader": YAMLLoaderAdapter,
    "http_kernel": lambda c: HttpKernel(c),
    "response_emitter": FastAPIResponseEmitter,
}
