from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class ProductReferral:

    catalog_id: str
    """
    Unique identifier of the Meta catalog linked to the WhatsApp Business Account.
    """

    product_retailer_id: str
    """
    Unique identifier of the product in a catalog.
    """