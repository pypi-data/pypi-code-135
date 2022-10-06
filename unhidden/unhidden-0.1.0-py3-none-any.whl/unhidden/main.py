import json
from datetime import datetime, timedelta
import requests
from requests.exceptions import HTTPError
import typer
import re
import pandas
import os


eyeshadow_names = ['Eclipse', 'Bloody Mary', 'Album', 'Areia Dourada', 'Moon', 'Sera', 'Candy Floss', 'Azure', 'Amethyst', 'Luau', 'Taxi', 'Sage', 'Alpine', 'Eros', 'Lima', 'Flamingo', 'Basic', 'Opal', 'Seafoam', 'Blaze', 'Suede', 'North Node', 'Cinderella', 'Ecru Stone', 'Marina', 'Mulberry Muse', 'Cinnabar', 'Rose Quartz', 'Sugar Plum', 'Frö', 'Barnaby', 'Midnight City', 'Esther', 'Nymph', 'Selva', 'Don Julio', 'Adé', 'Fil', 'Asteroid', 'V.I.P', 'Leo Season', 'Boujie', 'Mink', 'Whoa!', 'Indie', 'Polaris', 'Rain', 'Peaches', 'Ignite', 'Rotorua', 'Pikelet', 'Extra', 'Spice', 'Phia', 'Organza', 'Sunset', 'Stallion', 'Pluto', 'Charmed', 'Bank', 'Pomelo', 'Atacama', 'Sunburn', 'Graphite', 'Volcanic', 'Galactic Velvet', 'Hun!', 'Marte', 'Cents', 'Chrysolite', 'Voké', 'Sunbeam', 'Caiqué', 'Sandcastle', 'Lynda', 'Ay Caramba!', 'Mira', 'En Pointe', 'Shreya']
eyeshadow_ids = [6793563209787, 6794756522043, 6794770677819, 6794878025787, 6793668296763, 6793647226939, 6794876387387, 6792418820155, 6793755066427, 6792458502203, 6792462008379, 6793780232251, 6794883727419, 6794872881211, 6793676947515, 6792411250747, 6792512569403, 6793784229947, 6794856005691, 6794877632571, 6793549971515, 6793805430843, 6794874683451, 6794741514299, 6793895575611, 6794867015739, 6792031502395, 6794861248571, 6792343355451, 6794870980667, 6793749626939, 6794868555835, 6794736894011, 6794863575099, 6793777807419, 6793568485435, 6794880483387, 6793686548539, 6794759831611, 6793771122747, 6792521482299, 6792542322747, 6792532066363, 6792466268219, 6794870227003, 6794884907067, 6792450736187, 6792312553531, 6793538273339, 6792505884731, 6792332279867, 6792535932987, 6792527249467, 6792427601979, 6792454209595, 6794776182843, 6793773514811, 6793659973691, 6794743087163, 6792375271483, 6792442904635, 6795977883707, 6793639821371, 6793683042363, 6793576382523, 6794733977659, 6792446312507, 6793670524987, 6792456601659, 6793731244091, 6793589882939, 6792388018235, 6793733701691, 6793653682235, 6794869178427, 6792492744763, 6793828794427, 6793693560891, 6794795581499]


def strip_word(elt):
    elt2 = elt.replace(",", "").replace("!", "").replace(".", "").replace("-", "").replace("é", "e").replace("+", "").replace("*", "").replace("'", "").replace("~", "").replace('"', '')
    for char in elt2:
        if not char.isascii():
            elt2 = elt2.replace(char, "")
    return elt2


def get_shade_colours(shade, csv):
    for (i, elt) in enumerate(csv['Product']):
        if shade == elt:
            return csv['Colour'][i]
    return None


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')


app = typer.Typer()


@app.command()
def palette_wc(start: str = typer.Argument(None),
               save: bool = typer.Option(False, help="save data as csv file"),
               copy: bool = typer.Option(False, help="copy data to clipboard. then use ctrl+v to paste it into google sheets or excel")):
    if not save:
        if not copy:
            print("choose at least one of the save or copy options and run again")
            return
    if "-" in start:
        starting = start.split("-")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    elif "." in start:
        starting = start.split(".")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    elif "/" in start:
        starting = start.split("/")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    else:
        print("invalid commencing date. valid formats: dd.mm.yy dd-mm-yy dd/mm/yy")
        return

    start_date = datetime(int(starting[2]), int(starting[1]), int(starting[0]))
    if start_date.strftime("%A") != "Monday":
        inp = input("this date isn't monday. do you still want to continue? y/n: ")
        if inp == "n":
            return
    end_date = start_date + timedelta(days=7)

    all_data = []
    likely_test_list = ['tedy999@gmail.com', 'cindy@unhiddenbeautyco.com', 'piotr.zaba@giraffestudioapps.com',
                        'test7891@email.com', 'tom@beautonomy.com', 'josee@unhiddenbeautyco.com', 'shade@gmail.com',
                        'kiemu.salmon@gmail.com', 'chuko@unhiddenbeautyco.com', 'kelly@unhiddenbeautyco.com',
                        'qwerty@gmail.com', 'sandra@unhiddenbeautyco.com']

    with open("paletteDataApi.json", encoding="utf-8") as file:
        saved_palettes = json.load(file)
    with open("paletteDataApiNew.json", encoding="utf-8") as file:
        saved_palettes_new = json.load(file)

    # for new api
    for elt in saved_palettes_new['data']['data']:
        try:
            date = datetime.fromisoformat(elt['updatedAt'][:-1])
        except KeyError:
            continue
        if date >= start_date:
            if date < end_date:
                try:
                    if elt['userEmail'] in likely_test_list:
                        continue
                except KeyError:
                    continue
                if "@unhiddenbeautyco.com" in elt['userEmail']:
                    continue
                if "@mywaybeauty.com" in elt['userEmail']:
                    continue
                if "@beautonomy.com" in elt['userEmail']:
                    continue
                if "giraffestudioapps" in elt['userEmail']:
                    continue
                try:
                    created_at = elt['updatedAt']
                    user_id = elt['userId']
                    user_name = elt['userName']
                    user_email = elt['userEmail']
                    ref_palette = elt['title']
                except KeyError:
                    continue
                data_list = [created_at, user_id, user_name, user_email, ref_palette, "", "", ""]
                all_data.append(data_list)

    headers = ["Save date", "User ID", "User name", "User email", "Name palette", "Zip file",
               "Number of palettes saved",
               "Number of super savers (3 or more palettes)"]
    name = f"saved_palettes_wc_{start}.csv"
    df = pandas.DataFrame(all_data, columns=headers)
    if save:
        df.to_csv(f"{name}.csv", index=False, encoding="utf-8-sig")
        print(f"palettes data is saved. name: {name}. you can open this file with Sheets or Excel.")
    if copy:
        df.to_clipboard(index=False)
        print("data is saved to clipboard. use cmd+v to paste it into google sheets or excel")


@app.command()
def customer_wc(start: str = typer.Argument(None),
                month: bool = typer.Option(False, help="analyze monthly report instead")):
    if "-" in start:
        starting = start.split("-")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    elif "." in start:
        starting = start.split(".")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    elif "/" in start:
        starting = start.split("/")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    else:
        print("invalid commencing date. valid formats: dd.mm.yy dd-mm-yy dd/mm/yy")
        return
    start_date = datetime(int(starting[2]), int(starting[1]), int(starting[0]))
    if start_date.strftime("%A") != "Monday":
        inp = input("this date isn't monday. do you still want to continue? yes/no: ")
        if inp == "no":
            return
    end_date = start_date + timedelta(days=7)
    if month:
        end_date = start_date + timedelta(days=30)
    week_commencing = f"{start_date.day}.{start_date.month}.22"
    try:
        shopify_file = get_download_path() + f"/sales_{str(start_date)[:10]}_{str(end_date + timedelta(days=-1))[:10]}.csv"
    except FileNotFoundError:
        print("make sure to have correct csv report exported from shopify into your downloads folder")
        return
    shopify_csv = pandas.read_csv(shopify_file, keep_default_na=False)
    try:
        trying = shopify_csv['Number of saved palettes']
        print("note: number of saved palettes column is already added to this csv file.")
    except:
        pass
    new_column = []
    saved_palettes_bought = 0
    total_saved = 0
    total_purchaser = 0
    with open("paletteDataApiNew.json", encoding="utf-8") as file:
        saved_palettes_new = json.load(file)
    for (count, elt) in enumerate(shopify_csv['customer_email']):
        saved = 0
        # for new api
        for elt2 in saved_palettes_new['data']['data']:
            if elt:
                try:
                    if elt == elt2['userEmail']:
                        date = datetime.fromisoformat(elt2['updatedAt'][:-1])
                        if date >= start_date:
                            if date < end_date:
                                saved += 1
                except KeyError:
                    continue
            else:
                try:
                    if shopify_csv['customer_name'][count] == elt2['userName']:
                        date = datetime.fromisoformat(elt2['updatedAt'][:-1])
                        if date >= start_date:
                            if date < end_date:
                                saved += 1
                except KeyError:
                    continue
        new_column.append(saved)
        if shopify_csv['product_type'][count] in ['Eyeshadow', 'Pre-made Palette', 'Custom palette', 'Pre-made palette', 'cmp-8-shade-palette-private',
                                                      'cmp-12-shade-palette-private', 'cmp-20-shade-palette-private']:
            total_purchaser += 1
        if saved > 0:
            if shopify_csv['product_type'][count] in ['Eyeshadow', 'Pre-made Palette', 'Pre-made palette',
                                                      'Custom palette', 'cmp-8-shade-palette-private',
                                                      'cmp-12-shade-palette-private', 'cmp-20-shade-palette-private']:
                saved_palettes_bought += 1
                total_saved += saved
    shopify_csv['Number of saved palettes'] = new_column
    try:
        shopify_csv.to_csv(shopify_file, index=False)
        print("the column 'number of saved palettes' is added to the csv file.")
    except PermissionError:
        print("file is currently opened and can't be overwritten. please close it first.")
        return
    print(f"mean number of palettes saved per purchaser: {round(total_saved / total_purchaser, 2)}")
    print(f"number of saved palettes bought: {saved_palettes_bought}")

    returning = []
    for (count, elt) in enumerate(shopify_csv['customer_type']):
        if elt == "Returning":
            if shopify_csv['customer_name'][count] not in returning:
                returning.append(shopify_csv['customer_name'][count])
    bought = {}
    saved = {}
    for elt in returning:
        bought[elt] = 0
        saved[elt] = 0
    for (count, elt) in enumerate(shopify_csv['customer_name']):
        if elt in returning:
            if shopify_csv['product_type'][count] in ['Eyeshadow', 'Pre-made Palette', 'Pre-made palette', 'Custom palette',
                                                      'cmp-8-shade-palette-private',
                                                      'cmp-12-shade-palette-private', 'cmp-20-shade-palette-private']:
                bought[elt] += 1
                saved[elt] = shopify_csv['Number of saved palettes'][count]
    users_of_interest = []
    for elt in bought.keys():
        if saved[elt] > 1:
            users_of_interest.append([week_commencing, "Both", elt, bought[elt], saved[elt], ""])
        else:
            users_of_interest.append([week_commencing, "Repeat", elt, bought[elt], saved[elt], ""])

    palette_count = 0
    users_saved_palette = []
    users_saved_more_than_a_palette = []
    users_saved_more_than_a_palette_name = []
    users_saved_more_than_two_palettes = []
    users_saved_more_than_two_palettes_name = []
    likely_test_list = ['tedy999@gmail.com', 'cindy@unhiddenbeautyco.com', 'piotr.zaba@giraffestudioapps.com',
                        'test7891@email.com', 'tom@beautonomy.com', 'josee@unhiddenbeautyco.com', 'shade@gmail.com',
                        'kiemu.salmon@gmail.com', 'chuko@unhiddenbeautyco.com', 'kelly@unhiddenbeautyco.com',
                        'qwerty@gmail.com', 'sandra@unhiddenbeautyco.com']
    # for new api
    for elt in saved_palettes_new['data']['data']:
        try:
            date = datetime.fromisoformat(elt['updatedAt'][:-1])
        except KeyError:
            continue
        if date >= start_date:
            if date < end_date:
                try:
                    if elt['userEmail'] in likely_test_list:
                        continue
                except KeyError:
                    continue
                if "@unhiddenbeautyco.com" in elt['userEmail']:
                    continue
                if "@mywaybeauty.com" in elt['userEmail']:
                    continue
                if "@beautonomy.com" in elt['userEmail']:
                    continue
                if "giraffestudioapps" in elt['userEmail']:
                    continue
                palette_count += 1
                if elt['userEmail'] not in users_saved_palette:
                    users_saved_palette.append(elt['userEmail'])
                else:
                    if elt['userEmail'] not in users_saved_more_than_a_palette:
                        users_saved_more_than_a_palette.append(elt['userEmail'])
                        try:
                            users_saved_more_than_a_palette_name.append(elt['userName'])
                        except KeyError:
                            users_saved_more_than_a_palette_name.append("Unknown name")
                    else:
                        if elt['userEmail'] not in users_saved_more_than_two_palettes:
                            users_saved_more_than_two_palettes.append(elt['userEmail'])
                            try:
                                users_saved_more_than_two_palettes_name.append(elt['userName'])
                            except KeyError:
                                users_saved_more_than_two_palettes_name.append("Unknown name")
    max_dict = {}
    for user in users_saved_more_than_a_palette:
        max_dict[user] = 0
    for elt in saved_palettes_new['data']['data']:
        try:
            date = datetime.fromisoformat(elt['updatedAt'][:-1])
        except KeyError:
            continue
        if date >= start_date:
            if date < end_date:
                try:
                    max_dict[elt['userEmail']] += 1
                except KeyError:
                    continue
    all_purchasing_mails = []
    for (count, elt) in enumerate(shopify_csv["customer_email"]):
        if shopify_csv['product_type'][count] in ['Eyeshadow', 'Pre-made Palette', 'Pre-made palette', 'Custom palette',
                                                  'cmp-8-shade-palette-private',
                                                  'cmp-12-shade-palette-private', 'cmp-20-shade-palette-private']:
            all_purchasing_mails.append(elt)
    for (count, elt) in enumerate(users_saved_more_than_a_palette):
        if elt not in all_purchasing_mails:
            if users_saved_more_than_a_palette_name[count] == "Unknown name":
                users_of_interest.append([week_commencing, "Supersaver", users_saved_more_than_a_palette_name[count], 0, max_dict[elt], elt])
            else:
                users_of_interest.append([week_commencing, "Supersaver", users_saved_more_than_a_palette_name[count], 0, max_dict[elt], ""])
    df = pandas.DataFrame(users_of_interest, columns=[f"Week commencing {week_commencing}", "Repeat/Saver", "Name",
                                                      "Number of palettes bought", "Number of palettes saved",
                                                      "Contact details"])
    df.to_clipboard(index=False)
    print(f"users of interest for the week commencing {week_commencing} is copied to clipboard. use cmd+v to paste it into google sheets or excel.")


@app.command()
def full_analysis(name: str = typer.Option("saved_palette_data")):
    all_data = []
    likely_test_list = ['tedy999@gmail.com', 'cindy@unhiddenbeautyco.com', 'piotr.zaba@giraffestudioapps.com',
                        'test7891@email.com', 'tom@beautonomy.com', 'josee@unhiddenbeautyco.com', 'shade@gmail.com',
                        'kiemu.salmon@gmail.com', 'chuko@unhiddenbeautyco.com', 'kelly@unhiddenbeautyco.com',
                        'qwerty@gmail.com', 'sandra@unhiddenbeautyco.com', 'akkaya.burak@outlook.com']
    all_templates = ['https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/70s_Pattern_8-EYE_Marble_8-Eye-1.png','https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/70s_Pattern_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/70s_Pattern_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/70s_Pattern_v2_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/70s_Pattern_v2_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/70s_Pattern_v2_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Patterns_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Patterns_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Patterns_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Print_Cats_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Print_Cats_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Print_Cats_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Print_Pink_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Print_Pink_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Animal_Print_Pink_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Galaxy_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Galaxy_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Galaxy_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Holographic_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Holographic_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Holographic_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Leaves_8-EYE_Leaves-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Leaves_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Leaves_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Pink_Marble_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Pink_Marble_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Pink_Marble_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Psychedelic_8-EYE_Portrait_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Psychedelic_8-EYE_Portrait_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Psychedelic_8-EYE_Portrait_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Retro_Floral_8-EYE_Retro_Floral-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Retro_Floral_8-EYE_Retro_Floral-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Retro_Floral_8-EYE_Retro_Floral-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Starry_Landscape_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Starry_Landscape_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Starry_Landscape_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Starry_Nights_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Starry_Nights_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Starry_Nights_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Tie_Dye_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Tie_Dye_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Tie_Dye_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/WhiteMarble_8-EYE_Marble_8-Eye-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/WhiteMarble_8-EYE_Marble_8-Eye-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/WhiteMarble_8-EYE_Marble_8-Eye-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Zodiac_8-EYE_Zodiac-1.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Zodiac_8-EYE_Zodiac-2.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Zodiac_8-EYE_Zodiac-3.png', 'https://palette.unhiddenbeautyco.com/files/images/CustomPhoto/Zodiac_8-EYE_Zodiac-4.png', 'https://dev-unhidden-beauty-storage.s3.amazonaws.com/backgrounds/Barbie_repeat_customiser+box1_12.jpg', 'https://dev-unhidden-beauty-storage.s3.amazonaws.com/backgrounds/Barbie_repeatcustomiser_box2_12.jpg']
    # load the below static data here !!!
    colour_list = pandas.read_csv("shade_colours.csv")

    # this needs to be updated as per new api !!!
    with open("paletteDataApiNew.json", encoding="utf-8") as file:
        data = json.load(file)
        for i in data['data']:
            for (count, elt) in enumerate(i['data']):
                data_list = []
                shade_count = 0
                a = elt.keys()
                for key in a:
                    ref_palette = key
                try:
                    created_at = elt[ref_palette]['data']['createdData']
                    user_id = elt[ref_palette]['data']['user']['userId']
                    user_name = elt[ref_palette]['data']['user']['firstName'] + " " + elt[ref_palette]['data']['user'][
                        'lastName']
                    user_email = elt[ref_palette]['data']['user']['email']
                    zip_url = "https://palette.unhiddenbeautyco.com" + elt[ref_palette]['zipUrl']
                    pdf_url = "https://palette.unhiddenbeautyco.com" + elt[ref_palette]['pdfUrl']
                    palette_name = elt[ref_palette]['data']['coverText']['text']
                    palette_image = elt[ref_palette]['data']['coverImage']['file']
                    front_palette = elt[ref_palette]['data']['designImage']
                    inside_palette = elt[ref_palette]['data']['mainImage']
                except KeyError:
                    continue
                original_shades, custom_shades = [], []
                for shade in elt[ref_palette]['data']['selectedShades']:
                    try:
                        original_shades.append(get_shade_colours(shade['title'], colour_list))
                        if not get_shade_colours(shade['title'], colour_list):
                            print(f"this shade has no colour name: {shade['title']}")
                            return
                        custom_shades.append(shade['customName'])
                        shade_count += 1
                    except TypeError:
                        original_shades.append("")
                        custom_shades.append("")
                if original_shades == custom_shades:
                    shades_renamed = "No"
                else:
                    shades_renamed = "Yes"
                if shade_count == 8:
                    shades_added = "Yes"
                elif shade_count == 0:
                    shades_added = "No"
                else:
                    shades_added = f"Incomplete ({shade_count} shades added)"
                if user_email in likely_test_list:
                    likely_test = 'Yes'
                elif "@unhiddenbeautyco.com" in user_email:
                    likely_test = 'Yes'
                elif "@mywaybeauty.com" in user_email:
                    likely_test = 'Yes'
                elif "@beautonomy.com" in user_email:
                    likely_test = 'Yes'
                elif "@giraffestudioapps.com" in user_email:
                    likely_test = 'Yes'
                else:
                    likely_test = 'No'
                if palette_image in all_templates:
                    template_used = 'Yes'
                else:
                    template_used = 'No'

                # those keywords make sure palette is a gift
                gift_keywords = ['birthday', 'bday', 'gift', 'mom', 'mommy', 'mother', 'friend', 'sister', 'sis',
                                 'beloved', 'family', 'friends', 'moms', 'mothers', 'bestie', 'best', 'day', '16th',
                                 '15th', '20th', 'anniversary', 'prom', 'aunt', 'bitch', 'love', 'friendship',
                                 'princess', 'you', 'princesses', 'bride', 'daddy', 'wedding', 'wifey', 'yours',
                                 'babes', 'cousins']
                intent = ''
                split_word = str(ref_palette).split(" ")
                for word in split_word:
                    word = strip_word(word.lower())
                    if word in gift_keywords:
                        intent = 'Gift'
                        break
                    elif word == str(elt[ref_palette]['data']['user']['firstName']).lower():
                        intent = 'Self'
                        break
                    elif word == str(elt[ref_palette]['data']['user']['lastName']).lower():
                        intent = 'Self'
                        break
                    elif str(elt[ref_palette]['data']['user']['firstName']).lower() in word:
                        intent = 'Self'
                        break
                    elif str(elt[ref_palette]['data']['user']['lastName']).lower() in word:
                        intent = 'Self'
                        break
                    elif word == 'test':
                        intent = 'Testing'
                        break
                    elif word in ["cosmetic", "cosmetics"]:
                        intent = 'Sell'
                        break
                if intent == '':
                    split_word = str(palette_name).split(" ")
                    for word in split_word:
                        word = strip_word(word.lower())
                        if word in gift_keywords:
                            intent = 'Gift'
                            break
                        elif word == str(elt[ref_palette]['data']['user']['firstName']).lower():
                            intent = 'Self'
                            break
                        elif word == str(elt[ref_palette]['data']['user']['lastName']).lower():
                            intent = 'Self'
                            break
                        elif str(elt[ref_palette]['data']['user']['firstName']).lower() in word:
                            intent = 'Self'
                            break
                        elif str(elt[ref_palette]['data']['user']['lastName']).lower() in word:
                            intent = 'Self'
                            break
                        elif word == 'test':
                            intent = 'Testing'
                            break
                        elif word in ['cosmetic', 'cosmetics']:
                            intent = "Sell"
                            break
                        elif word in ['angel', 'dance', 'memories', 'edition', 'mine', 'home',
                                      'collection', 'inspired', 'dream', 'vibez', 'vibes']:
                            intent = "Self"
                            break

                data_list.append(created_at)
                data_list.append(user_id)
                data_list.append(user_name)
                data_list.append(user_email)
                data_list.append(ref_palette)
                data_list.append(zip_url)
                data_list.append(pdf_url)
                data_list.append(likely_test)
                data_list.append(palette_name)
                data_list.append(template_used)
                if template_used == "Yes":
                    data_list.append(palette_image)
                else:
                    data_list.append("")
                data_list.append(front_palette)
                data_list.append(inside_palette)
                data_list.append("8-eye")
                data_list.append(shades_added)
                data_list.append(shades_renamed)
                for shade in original_shades:
                    data_list.append(shade)
                for shade in custom_shades:
                    data_list.append(shade)
                data_list.append(intent)

                all_data.append(data_list)

    headers = ["saved date", "user id", "username", "user email", "ref palette", "zip url", "pdf url", "likely test?",
               "name of palette on image", "template used?", "which template used?", "image of front of palette",
               "image of inside of palette", "type of palette", "shades added?", "shades renamed?",
               "original colours", "", "", "", "", "", "", "", "custom shade names", "", "", "", "", "", "", "",
               "intention of recipient"]
    df = pandas.DataFrame(all_data, columns=headers)
    try:
        df.to_csv(f"{name}.csv", index=False, encoding="utf-8-sig")
    except PermissionError:
        print("file is currently opened and can't be overwritten. please close it first.")
        return
    print(f"palette analysis data is saved. name: {name}.csv")


@app.command()
def update_api(api_key: str = typer.Argument(None, help="API key")):
    print("updating palette data... this will take a few seconds...")
    try:
        method = "get"
        url = "https://api.unhiddenbeautyco.com/v1/palette?perPage=25000"
        headers = {
            'Content-type': 'application/json',
            'Authorization': api_key
        }
        response = requests.request(method, url, headers=headers)
        response.raise_for_status()
        json_response = response.json()
        with open('paletteDataApiNew.json', 'w') as json_file:
            json.dump(json_response, json_file)
        print("data updated in the file: paletteDataApiNew.json")
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


@app.command()
def palette(start: str = typer.Argument(None, help="give starting date or write 'today', 'yesterday', 'lastweek',"
                                                   "'lastXhours', 'lastXdays', 'lastXweeks' (those options don't "
                                                   "require ending date)"),
            end: str = typer.Argument(None, help="give ending date or write 'now' to make it to-date"),
            count: str = typer.Option(None, help="returns list of users with saved palettes number equal to input"),
            compare: bool = typer.Option(False, help="compares time interval with previous interval of same length")):
    if "-" in start:
        starting = start.split("-")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    elif "." in start:
        starting = start.split(".")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    elif "/" in start:
        starting = start.split("/")
        if len(starting[2]) == 2:
            starting[2] = "20" + starting[2]
    else:
        if start not in ["today", "yesterday", "lastweek"]:
            if re.search("^last", start) is None:
                print("invalid starting date")
                return
    if start not in ["today", "yesterday"]:
        if re.search("^last", start) is None:
            if "-" in end:
                ending = end.split("-")
                if len(ending[2]) == 2:
                    ending[2] = "20" + ending[2]
            elif "." in end:
                ending = end.split(".")
                if len(ending[2]) == 2:
                    ending[2] = "20" + ending[2]
            elif "/" in end:
                ending = end.split("/")
                if len(ending[2]) == 2:
                    ending[2] = "20" + ending[2]
            else:
                if end != "now":
                    print("invalid ending date")
                    return

    if start == "today":
        start_date = datetime.today().date()
        start_date = datetime(start_date.year, start_date.month, start_date.day)
        end_date = start_date + timedelta(days=1)
        end_date = datetime(end_date.year, end_date.month, end_date.day)
    elif start == "yesterday":
        start_date = datetime.today().date() + timedelta(days=-1)
        start_date = datetime(start_date.year, start_date.month, start_date.day)
        end_date = start_date + timedelta(days=1)
        end_date = datetime(end_date.year, end_date.month, end_date.day)
    elif start == "lastweek":
        now = datetime.now() + timedelta(days=-1)
        while now.strftime("%A") != "Sunday":
            now = now + timedelta(days=-1)
        end_date = datetime(now.date().year, now.date().month, now.date().day) + timedelta(days=1)
        start_date = end_date + timedelta(days=-7)
    elif re.search("^last", start) is not None:
        type = ""
        no = ""
        for i in start[4:]:
            if not i.isdigit():
                type += str(i)
            else:
                no += str(i)
        if "day" in type:
            start_date = datetime.today().date()
            start_date = datetime(start_date.year, start_date.month, start_date.day)
            start_date = start_date + timedelta(days=-int(no)+1)
            end_date = datetime.now()
        elif "week" in type:
            start_date = datetime.today().date()
            start_date = datetime(start_date.year, start_date.month, start_date.day)
            start_date = start_date + timedelta(weeks=-int(no)) + timedelta(days=1)
            end_date = datetime.now()
        elif "hour" in type:
            end_date = datetime.now()
            start_date = end_date + timedelta(hours=-int(no))
        else:
            print("invalid argument")
            return
    else:
        start_date = datetime(int(starting[2]), int(starting[1]), int(starting[0]))
        if end == "now":
            end_date = datetime.now()
        else:
            end_date = datetime(int(ending[2]), int(ending[1]), int(ending[0]))
            end_date = end_date + timedelta(days=1)

    if end_date <= start_date:
        print("invalid date range")
        return

    if compare:
        days = (end_date - start_date).days
        end_date_c = start_date
        if days == 0:
            hours = (end_date - start_date).seconds*60*60
            start_date_c = start_date + timedelta(hours=-hours)
        else:
            start_date_c = start_date + timedelta(days=-days)
        palette_count_c = 0
        users_saved_palette_c = []
        users_saved_more_than_a_palette_c = []
        users_saved_more_than_two_palettes_c = []

    palette_count = 0
    users_saved_palette = []
    users_saved_more_than_a_palette = []
    users_saved_more_than_two_palettes = []
    likely_test_list = ['tedy999@gmail.com', 'cindy@unhiddenbeautyco.com', 'piotr.zaba@giraffestudioapps.com',
                        'test7891@email.com', 'tom@beautonomy.com', 'josee@unhiddenbeautyco.com', 'shade@gmail.com',
                        'kiemu.salmon@gmail.com', 'chuko@unhiddenbeautyco.com', 'kelly@unhiddenbeautyco.com',
                        'qwerty@gmail.com', 'sandra@unhiddenbeautyco.com', 'akkaya.burak@outlook.com']

    with open("paletteDataApiNew.json", encoding="utf-8") as file:
        saved_palettes_new = json.load(file)

    # new api data below
    for elt in saved_palettes_new['data']['data']:
        try:
            date = datetime.fromisoformat(elt['updatedAt'][:-1])
            email = elt['userEmail']
        except KeyError:
            continue
        if date >= start_date:
            if date < end_date:
                if email in likely_test_list:
                    continue
                if "@unhiddenbeautyco.com" in email:
                    continue
                if "@mywaybeauty.com" in email:
                    continue
                if "@beautonomy.com" in email:
                    continue
                if "giraffestudioapps" in email:
                    continue
                palette_count += 1
                if email not in users_saved_palette:
                    users_saved_palette.append(email)
                else:
                    if email not in users_saved_more_than_a_palette:
                        users_saved_more_than_a_palette.append(email)
                    else:
                        if email not in users_saved_more_than_two_palettes:
                            users_saved_more_than_two_palettes.append(email)
        if compare:
            if date >= start_date_c:
                if date < end_date_c:
                    try:
                        if email in likely_test_list:
                            continue
                    except KeyError:
                        continue
                    if "@unhiddenbeautyco.com" in email:
                        continue
                    if "@mywaybeauty.com" in email:
                        continue
                    if "@beautonomy.com" in email:
                        continue
                    if "@giraffestudioapps.com" in email:
                        continue
                    palette_count_c += 1
                    if email not in users_saved_palette_c:
                        users_saved_palette_c.append(email)
                    else:
                        if email not in users_saved_more_than_a_palette_c:
                            users_saved_more_than_a_palette_c.append(email)
                        else:
                            if email not in users_saved_more_than_two_palettes_c:
                                users_saved_more_than_two_palettes_c.append(email)

    max_dict = {}
    for user in users_saved_palette:
        max_dict[user] = 0
    for elt in saved_palettes_new['data']['data']:
        try:
            date = datetime.fromisoformat(elt['updatedAt'][:-1])
        except KeyError:
            continue
        if date >= start_date:
            if date < end_date:
                try:
                    max_dict[elt['userEmail']] += 1
                except KeyError:
                    continue
    # these two below give user who saved max palette and number of it
    try:
        max_no_of_saved_palette_user = max(max_dict, key=max_dict.get)
    except ValueError:
        print("no palettes were saved. you can update data with update-data command")
        return
    max_no_of_saved_palette = max_dict[max_no_of_saved_palette_user]

    if compare:
        max_dict_c = {}
        for user in users_saved_palette_c:
            max_dict_c[user] = 0
        for elt in saved_palettes_new['data']['data']:
            try:
                date = datetime.fromisoformat(elt['updatedAt'][:-1])
            except KeyError:
                continue
            if date >= start_date_c:
                if date < end_date_c:
                    try:
                        max_dict_c[elt['userEmail']] += 1
                    except KeyError:
                        continue

        # these two below give user who saved max palette and number of it
        try:
            max_no_of_saved_palette_user_c = max(max_dict_c, key=max_dict_c.get)
        except ValueError:
            print("no palettes were saved. you can update data with update-data command")
            return
        max_no_of_saved_palette_c = max_dict_c[max_no_of_saved_palette_user_c]

    if count:
        if count[0] == "=":
            print("")
            print(f"users below saved {count[1:]} palettes between {start_date} - {end_date}")
            total = 0
            for user in max_dict.keys():
                try:
                    if max_dict[user] == int(count[1:]):
                        print(user)
                        total += 1
                except ValueError:
                    print("invalid number! give an integer after '=' sign.")
                    return
            print(f"TOTAL: {total}")
            print("")
            if compare:
                print(f"users below saved {count[1:]} palettes between {start_date_c} - {end_date_c}")
                total = 0
                for user in max_dict_c.keys():
                    if max_dict_c[user] == int(count[1:]):
                        print(user)
                        total += 1
                print(f"TOTAL: {total}")
                print("")
        elif count[0] == ">":
            print("")
            print(f"users below saved more than {count[1:]} palettes between {start_date} - {end_date}")
            total = 0
            for user in max_dict.keys():
                try:
                    if max_dict[user] > int(count[1:]):
                        print(max_dict[user], " - ", user)
                        total += 1
                except ValueError:
                    print("invalid number! give an integer after '=' sign.")
                    return
            print(f"TOTAL: {total}")
            print("")
            if compare:
                print("")
                print(f"users below saved {count[1:]} palettes between {start_date_c} - {end_date_c}")
                total = 0
                for user in max_dict_c.keys():
                    if max_dict_c[user] > int(count[1:]):
                        print(max_dict_c[user], " - ", user)
                        total += 1
                print(f"TOTAL: {total}")
                print("")
        else:
            print("count value should start with '=' or '>' followed by an integer.")
            return
    else:
        if compare:
            print("")
            print('SAVED PALETTE METRICS FOR:', start_date, '-', end_date)
            print('number of saved palettes: ', palette_count, f'({str(round((palette_count / palette_count_c)*100, 2))}%)')
            print('number of users who saved a palette: ', len(users_saved_palette), f'({str(round((len(users_saved_palette) / len(users_saved_palette_c))*100, 2))}%)')
            print('mean number of palettes saved per person: ', str(round(palette_count / len(users_saved_palette), 2)), f'({str(round(((palette_count / len(users_saved_palette)) / (palette_count_c / len(users_saved_palette_c)))*100, 2))}%)')
            print('number of users saved more than a palette: ', len(users_saved_more_than_a_palette), f'({round((len(users_saved_more_than_a_palette) / len(users_saved_more_than_a_palette_c))*100, 2)}%)')
            print('number of users saved more than two palettes: ', len(users_saved_more_than_two_palettes), f'({str(round((len(users_saved_more_than_two_palettes) / len(users_saved_more_than_two_palettes_c))*100, 2))}%)')
            print('max number of palettes saved by a user: ', max_no_of_saved_palette, '- saved by',
                  max_no_of_saved_palette_user, f'({str(round((max_no_of_saved_palette / max_no_of_saved_palette_c)*100, 2))}%)')
            print("")
            print('SAVED PALETTE METRICS FOR:', start_date_c, '-', end_date_c)
            print('number of saved palettes: ', palette_count_c)
            print('number of users who saved a palette: ', len(users_saved_palette_c))
            print('mean number of palettes saved per person: ', str(round(palette_count_c / len(users_saved_palette_c), 2)))
            print('number of users saved more than a palette: ', len(users_saved_more_than_a_palette_c))
            print('number of users saved more than two palettes: ', len(users_saved_more_than_two_palettes_c))
            print('max number of palettes saved by a user: ', max_no_of_saved_palette_c, '- saved by',
                  max_no_of_saved_palette_user_c)
            print("")
        else:
            print("")
            print('SAVED PALETTE METRICS FOR:', start_date, '-', end_date)
            print('number of saved palettes: ', palette_count)
            print('number of users who saved a palette: ', len(users_saved_palette))
            print('mean number of palettes saved per person: ', str(round(palette_count / len(users_saved_palette), 2)))
            print('number of users saved more than a palette: ', len(users_saved_more_than_a_palette))
            print('number of users saved more than two palettes: ', len(users_saved_more_than_two_palettes))
            print('max number of palettes saved by a user: ', max_no_of_saved_palette, '- saved by',
                  max_no_of_saved_palette_user)
            print("")


# if __name__ == "__main__":
#     app()
