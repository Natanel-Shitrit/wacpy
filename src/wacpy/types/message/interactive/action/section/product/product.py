from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional


@dataclass_json
@dataclass
class Product:

    product_retailer_id: str
    """
    Required for Multi-Product Messages.

    Unique identifier of the product in a catalog.
    
    To get this ID, go to the Meta Commerce Manager (https://business.facebook.com/commerce/),
    select your account and the shop you want to use.
    Then, click Catalog > Items, and find the item you want to mention.
    The ID for that item is displayed under the item's name.
    """