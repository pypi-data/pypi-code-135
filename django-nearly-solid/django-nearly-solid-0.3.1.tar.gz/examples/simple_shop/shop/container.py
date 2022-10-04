from ns.auth.interface import IAuthProvider
from ns.auth.provider import DjangoAuthProvider
from ns.di.abc import Container

from shop.image_storage import IImageStorage
from adapters.image_storage import FileSystemImageStorage


class ShopContainer(Container):
    auth_provider: IAuthProvider = DjangoAuthProvider()
    images_storage: IImageStorage = FileSystemImageStorage()
