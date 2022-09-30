
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from datetime import datetime
from enum import Enum, IntEnum
from typing import List, Optional

from pydantic import constr, EmailStr, root_validator


from trove_fm.app.models.company import CompanyPublic
from trove_fm.app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin
from trove_fm.app.models.image import BarcodeImage, ProductImage
from trove_fm.app.models.profile import PersonProfileCreate, PersonProfilePublic


class ProductBase(CoreModel):
    sku: str
    upc: str
    barcode: str
    barcode_image: Optional[BarcodeImage]
    collection: str
    vendor: CompanyPublic
    name: str
    description: str
    image: Optional[List[ProductImage]]
    tags: Optional[List[str]]
    date_added: datetime
