from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Product:
    
    product_retailer_id: str
    """
    Unique identifier of the product in a catalog.
    """

    quantity: str
    """
    Number of items.
    """

    item_price: str
    """
    Price of each item.
    """

    currency: str
    """
    Price currency.
    """