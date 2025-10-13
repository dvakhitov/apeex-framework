from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    id: Optional[int] = None
    sku: str = ""
    name: str = ""
    price: float = 0.0
    # association example (eager by default)
    category_id: Optional[int] = None