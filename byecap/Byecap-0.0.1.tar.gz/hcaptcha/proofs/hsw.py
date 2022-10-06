from os.path import dirname
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math, atexit, hashlib, subprocess, time, random

wd_opt = Options();
wd_opt.add_argument("start-maximized");
wd_opt.add_argument("--headless");
wd_opt.add_experimental_option("excludeSwitches", ["enable-automation"]);
wd_opt.add_experimental_option('useAutomationExtension', False);
wd_opt.add_experimental_option("excludeSwitches", ["enable-logging"]);
wd_opt.add_argument('--log-level 3')
wd = webdriver.Chrome(chrome_options=wd_opt)


def get_proof(req):
    with open(dirname(__file__) + "\\scripts\\hsw.js") as fp:
        driver = random.choice([wd])
        driver.execute_script(fp.read() + "; window.hsw = hsw")

    proof = driver.execute_async_script("window.hsw(arguments[0]).then(arguments[1])", req)
    return proof
