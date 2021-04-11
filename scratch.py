import os

MAIN_FILE_PATH = os.path.dirname(__file__)
IMAGES_FOLDERS = os.path.join(MAIN_FILE_PATH, "images")
CARDS_FOLDER = os.path.join(MAIN_FILE_PATH, IMAGES_FOLDERS, "cards")

only_png = [f for f in os.listdir(CARDS_FOLDER)]
# print(only_png)

for i in only_png:
    # pass
    print(f"'{i[:-4]}': '{i}',")

# http://acbl.mybigcommerce.com/52-playing-cards/
cards = {'JH': 'JH.png',
         'QD': 'QD.png',
         '3C': '3C.png',
         '6C': '6C.png',
         '9H': '9H.png',
         '7H': '7H.png',
         '8H': '8H.png',
         '3D': '3D.png',
         '5C': '5C.png',
         '8D': '8D.png',
         'AD': 'AD.png',
         'AC': 'AC.png',
         '5D': '5D.png',
         '10H': '10H.png',
         '3H': '3H.png',
         '9C': '9C.png',
         '9S': '9S.png',
         '4H': '4H.png',
         '9D': '9D.png',
         'JS': 'JS.png',
         '4D': '4D.png',
         '7S': '7S.png',
         '8C': '8C.png',
         '10D': '10D.png',
         '4S': '4S.png',
         '10C': '10C.png',
         'AH': 'AH.png',
         '2H': '2H.png',
         '10S': '10S.png',
         '3S': '3S.png',
         '5H': '5H.png',
         'JD': 'JD.png',
         '6D': '6D.png',
         'KH': 'KH.png',
         '7D': '7D.png',
         '6H': '6H.png',
         'JC': 'JC.png',
         '2C': '2C.png',
         '8S': '8S.png',
         'AS': 'AS.png',
         'KD': 'KD.png',
         '5S': '5S.png',
         'QC': 'QC.png',
         'aces': 'aces.png',
         '6S': '6S.png',
         'KC': 'KC.png',
         '4C': '4C.png',
         'KS': 'KS.png',
         'QS': 'QS.png',
         '7C': '7C.png',
         '2S': '2S.png',
         'QH': 'QH.png',
         '2D': '2D.png',
         'purple_back': 'purple_back.png',
         }

# print(cards)

# https://github.com/Bogdan-Muroianu/Python_21_CardTrick.git
# https://github.com/Bogdan-Muroianu/Python21CardTrick/blob/main/table_top.png?raw=true