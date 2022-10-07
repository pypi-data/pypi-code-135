import webbrowser
import requests
from bs4 import BeautifulSoup
import json

def quicktask(cmid):
   """

   Takes a cmid as input and starts a quicktask using it

   """
   webbrowser.open(f'http://localhost:5776/qt?solana_input={cmid}&fee_protection_mode=medium')


def get_LMNFT(webpage):
   """

   Gets cmid from LMNFT webpage

   """
   # If webpage isn't a LMNFT site, error message is printed and program is stopped
   try:
      # Load webpage
      page = requests.get(webpage)
      soup = BeautifulSoup(page.content, "html.parser")

      # Find the tag that contains CMID, and index into the dictionary containing it
      result = str(soup.find(id="__NEXT_DATA__")).replace(r'<script id="__NEXT_DATA__" type="application/json">',"").replace(r"</script>","")
      res = json.loads(result)
      cmid = res["props"]["pageProps"]["collection"]["newCandyMachineAccountId"]

      return cmid
   except:
      print("Link isn't a LMNFT site")