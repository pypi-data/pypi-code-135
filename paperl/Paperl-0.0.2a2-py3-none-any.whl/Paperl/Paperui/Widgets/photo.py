from Paperl.Paperui.Widgets.label import Label
from Paperl.Paperui.Widgets.image import Image
from Paperl.Paperui.Widgets.widget import Widget


class Photo(Label):
    def __init__(self, parent: Widget, image: Image):
        super().__init__(parent)
        self.setImage(image.export())
