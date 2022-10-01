# It renders a template, saves it as an HTML file, and render a screenshot of
# the HTML file.
import asyncio, os

try:
    from pyppeteer import launch
    import jinja2
except:
    os.system('pip install pyppeteer')
    os.system('pip install jinja2')
    from pyppeteer import launch
    import jinja2

# > The Markup class is a container for the markup of a document
class Markup():
    def __init__(self):
        self.__html = f'{__file__.replace(f"{os.path.basename(__file__)}", "index.html")}'

        self.__view = {
            'width': 800,
            'height': 600,
            'deviceScaleFactor': 1
        }

    async def __initialize(self):
        """
        It launches a headless browser, creates a new page, and returns the browser and page
        :return: The browser and page objects.
        """
        browser = await launch({ 'headless': True, 'args': ['--no-sandbox', '--disable-setuid-sandbox'] })
        page = await browser.newPage()
        return browser, page

    def renderFile(self, path: str, data: any = {}) -> None:
        """
        It takes a path to a template file, and a dictionary of data, and renders the template file with
        the data, and writes the result to a file
        
        :param path: The path to the template file
        :type path: str
        :param data: The data to be rendered in the template
        :type data: any
        """
        with open(path, 'r', encoding = 'utf-8') as template:
            template = jinja2.Environment(loader = jinja2.BaseLoader).from_string(template.read())
            
            with open(self.__html, 'w', encoding = 'utf-8') as file:
                file.write(template.render(data))

    def render(self, template: str, data: any = {}) -> None:
        """
        It takes a template and data, renders the template with the data, and writes the rendered
        template to a file
        
        :param template: The template to render
        :type template: str
        :param data: The data that will be passed to the template
        :type data: any
        """
        template = jinja2.Environment(loader = jinja2.BaseLoader).from_string(template)

        print(self.__html)

        with open(self.__html, 'w', encoding = 'utf-8') as file:
            file.write(template.render(data))

    def setViewport(self, width: int = 800, height: int = 600, deviceScaleFactor: int = 1) -> None:
        """
        This function sets the viewport of the page
        
        :param width: The width of the viewport in pixels, defaults to 800
        :type width: int (optional)
        :param height: The height of the viewport in pixels, defaults to 600
        :type height: int (optional)
        :param deviceScaleFactor: Specifies the device scale factor used to render the page. Defaults to
        1, defaults to 1
        :type deviceScaleFactor: int (optional)
        """
        self.__view = {
            'width': width,
            'height': height,
            'deviceScaleFactor': deviceScaleFactor
        }

    async def save(self, savePath: str = None, fullPage: bool = False, transparent: bool = False):
        """
        It takes a HTML file, opens it in a headless browser, and takes a screenshot of it
        
        :param savePath: The path to save the image to. If this is not specified, it will return a
        buffer
        :type savePath: str
        :param fullPage: If true, takes a screenshot of the full scrollable page. Defaults to false,
        defaults to False
        :type fullPage: bool (optional)
        :param transparent: If set to true, the background of the image will be transparent, defaults to
        False
        :type transparent: bool (optional)
        :return: A buffer of the image.
        """
        browser, page = await self.__initialize()
        
        await page.setViewport(self.__view)
        
        await page.goto(f'file:///{self.__html}', { 'waitUntil': 'load', 'timeout': 0 })

        if isinstance(savePath, str):
            buffer = await page.screenshot({ 'path': savePath, 'fullPage': fullPage, 'omitBackground': transparent })
            await browser.close()
            return buffer
        else:
            buffer = await page.screenshot({ 'fullPage': fullPage, 'omitBackground': transparent })
            await browser.close()
            return buffer