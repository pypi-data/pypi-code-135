import asyncio
import wundasmart
import aiohttp

WUNDA_IP = "192.168.3.222"
WUNDA_USER = "root"
WUNDA_PASS = "root"

async def main():
    httpsession = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
    print("Getting list of devices...")
    response = await wundasmart.get_devices(httpsession, WUNDA_IP, WUNDA_USER, WUNDA_PASS)
    print(response)
    print("Getting list of rooms...")
    response = await wundasmart.get_rooms(httpsession, WUNDA_IP, WUNDA_USER, WUNDA_PASS)
    print(response)
    print("Getting status of rooms...")
    response = await wundasmart.get_room_states(httpsession, WUNDA_IP, WUNDA_USER, WUNDA_PASS)
    print(response)
    print("Getting status of devices...")
    response = await wundasmart.get_device_states(httpsession, WUNDA_IP, WUNDA_USER, WUNDA_PASS)
    print(response)
    print("Putting some stuff...")
    #response = await wundasmart.put_room_state(httpsession, WUNDA_IP, WUNDA_USER, WUNDA_PASS, 122, [("stuff", "thing"),("foo", "bar")])
    print(response)
    await httpsession.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

