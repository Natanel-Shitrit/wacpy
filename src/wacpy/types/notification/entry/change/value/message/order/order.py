from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List

from .product import Product


@dataclass_json
@dataclass
class Order:
    
    catalog_id: str
    """
    ID for the catalog the ordered item belongs to.
    """

    text: str
    """
    Text message from the user sent along with the order.
    """

    product_items: List[Product]
    """
    Array of product item objects.
    """