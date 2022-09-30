#!/usr/bin/env python3
from lucidic import Lucidic
from imgcat import imgcat
from pyppeteer import launch
import asyncio
import re


def filterObjects(obj, keys=[], accepts=[], rejects=[], strict=True):
    """
    Filter a Neseted Object by Keyword

    Args:
        key: (str) - should be a dict key, not value
        rejects: (list) - keys you wish to keep for matches found
        strict: (boolean) - True = exclusive keyword match, False = partial match
    Returns:
        filtered_obj: (list) - list of filtered objects
    """
    total_keys = []
    a_keys = []
    r_keys = []
    queries = []
    results = []

    for key in keys:
        temp_obj = Lucidic({"stuff": obj}) if isinstance(obj, list) else Lucidic(obj)
        query = temp_obj.search(key, strict=strict)
        queries.append(query)
        total_keys += [x["keypath"][0] for x in query]
        if accepts:
            a_keys += [x["keypath"][0] for x in query if x["match"][key] in accepts]
        if rejects:
            r_keys += [x["keypath"][0] for x in query if x["match"][key] in rejects]
    if accepts:
        filtered_keys = sorted((set(total_keys) & set(a_keys)) - set(r_keys))
    else:
        filtered_keys = sorted(set(total_keys) - set(r_keys))
    for f_key in filtered_keys:
        m = re.search(r"(?P<key>.+)\[(?P<index>\d+)\]", f_key).groupdict()
        results.append(temp_obj.dict[m["key"]][int(m["index"])])
    return results

def getHTML(url='', options={"width": 1920, "height": 1080}):
    html = asyncio.get_event_loop().run_until_complete(_getHTML(url, options))
    return html

async def _getHTML(url, options={}):
    browser = await launch({'ignoreHTTPSErrors': True})
    page = await browser.newPage()
    await page.setViewport(options)
    await page.goto(url)

    await page.emulateMedia('screen')
    html = await page.content()
    await browser.close()
    return html

def convertHTMLtoPDF(url='', options={"width": 1920, "height": 1080}):
    pdf = asyncio.get_event_loop().run_until_complete(_convertHTMLtoPDF(url, options))
    return pdf

async def _convertHTMLtoPDF(url, options={}):
    browser = await launch({'ignoreHTTPSErrors': True, 'headless': True})
    page = await browser.newPage()
    await page.setViewport(options)
    await page.goto(url)

    await page.emulateMedia('screen')
    pdf = await page.pdf()
    await browser.close()
    return pdf

def convertHTMLtoPNG(url='', options={"width": 1920, "height": 1080}, img_opts={}):
    png = asyncio.get_event_loop().run_until_complete(_convertHTMLtoPNG(url, options, img_opts))
    return png

async def _convertHTMLtoPNG(url='', options={}, img_opts={}):
    # options = {"path": "pyppeteer.png", "fullPage": True}
    browser = await launch({'ignoreHTTPSErrors': True})
    page = await browser.newPage()
    await page.setViewport(options)
    await page.goto(url)

    await page.emulateMedia('screen')
    png = await page.screenshot(img_opts)
    await browser.close()
    return png

def showScreenshot(url='', options={"width": 1920, "height": 1080}, img_opts={}):
    asyncio.get_event_loop().run_until_complete(_showScreenshot(url, options, img_opts))

async def _showScreenshot(url='', options={}, img_opts={}):
    # options = {"fullPage": True}
    browser = await launch({'ignoreHTTPSErrors': True})
    page = await browser.newPage()
    await page.setViewport(options)
    await page.goto(url)

    await page.emulateMedia('screen')
    imgcat(await page.screenshot(img_opts))
    await browser.close()
