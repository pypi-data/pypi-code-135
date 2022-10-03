import requests
import os


def getProxies(protocol, count, country, ssl, anonymity):
    url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout={count}&country={country}&ssl={ssl}&anonymity={anonymity}"
    proxyList = []

    r = requests.get(url)
    with open("proxies.txt", "w") as f:
        f.write(r.text)
    with open("proxies.txt", "r") as f:
        lines = f.readlines()
    os.remove("proxies.txt")
    for proxy in lines:
        proxyList.append(proxy.strip())
    return proxyList
    
def checkProxies(proxyList):
    workingProxies = []
    print("Checking proxies...")
    for i in range(len(proxyList)):
        proxy = proxyList[i]
        try:
            response = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
            if response.status_code == 200:
                workingProxies.append(proxy)
        except:
            pass

