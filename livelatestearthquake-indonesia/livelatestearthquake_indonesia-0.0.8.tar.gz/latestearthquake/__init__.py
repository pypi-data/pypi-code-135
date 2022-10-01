import requests
from bs4 import BeautifulSoup

description = "to get the live latest earthquake in indonesia from bmkg.go.id"

def ekstraksi_data():
    # global magnitude
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(',')
        date = result[0]
        time = result[1]

        result = soup.find('div', {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren('li')
        i = 0
        magnitude = None
        depth = None
        ls = None
        bt = None
        central = None
        desc = None

        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                coordinate = res.text.split(' - ')
                ls = coordinate[0]
                bt = coordinate[1]
            elif i == 4:
                central = res.text
            elif i == 5:
                desc = res.text
            i = i + 1

        hasil = dict()
        hasil["date"] = date
        hasil["time"] = time
        hasil["magnitude"] = magnitude
        hasil["depth"] = depth
        hasil["coordinate"] = {"ls": ls, "bt": bt}
        hasil["central"] = central
        hasil["desc"] = desc
        return hasil
    else:
        return None


def show_data(result):
    if result is None:
        print("Unable to Find Recent Earthquake Data")
        return

    print('\nGempa Terakhir Berdasarkan BMKG')
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Coordinate Location: LS = {result['coordinate']['ls']}, BT = {result['coordinate']['bt']}")
    print(f"Location Quake: {result['central']}")
    print(f"Description: {result['desc']}")


if __name__ == '__main__':
    print(f'description: {description}\n')
    print('~~~Live Earthquake Application~~~')
    result = ekstraksi_data()
    show_data(result)
