from shop.image_storage import IImageStorage


class FileSystemImageStorage(IImageStorage):

    def __init__(self):
        print('XYI')

    def upload_image(self, data: bytes) -> str:
        print('upload image')
        return ''
