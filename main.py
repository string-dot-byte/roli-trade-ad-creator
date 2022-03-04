import requests, json, time

cookie = '_ga=...; _RoliVerification=...'
baseUrl = 'https://www.rolimons.com/tradeapi/create'

item1 = input('\nItem ID you are offering >')
item2 = input('Item ID #2 you are offering (optional) >')
item3 = input('Item ID #3 you are offering (optional) >')
item4 = input('Item ID #4 you are offering (optional) >')

ItemsOffering = []
ItemsOffering.insert(1, int(item1))
if item2.isnumeric():
    ItemsOffering.insert(1, int(item2))
    if item3.isnumeric():
        ItemsOffering.insert(1, int(item3))
        if item4.isnumeric():
	        ItemsOffering.insert(1, int(item4))

tagInfo = {
	'1': 'any',
	'2': 'rap',
	'3': 'demand',
	'4': 'rares',
	'5': 'robux',
	'6': 'upgrade',
 	'7': 'downgrade',
	'8': 'wishlist',
	'9': 'projecteds',
	'10': 'adds'
}

print('''
    Options:
        Insert item ID;
        1 > ANY;
        2 > RAP;
        3 > DEMAND;
        4 > RARES;
        5 > ROBUX;
        6 > UPGRADE;
        7 > DOWNGRADE;
        8 > WISHLIST;
''')

item1 = input('\nRequest >')
item2 = input('Request #2 (optional) >')
item3 = input('Request #3 (optional) >')
item4 = input('Request #4 (optional) >')

ItemsRequesting = []
RequestingTags = []
if int(item1) <= 8:
    RequestingTags.insert(1, tagInfo[str(item1)])
else:
    ItemsRequesting.insert(1, int(item1))
if item2.isnumeric():
    if int(item2) <= 8:
	    RequestingTags.insert(1, tagInfo[str(item2)])
    else:
        ItemsRequesting.insert(1, int(item2))
    if item3.isnumeric():
        if int(item3) <= 8:
            RequestingTags.insert(1, tagInfo[str(item3)])
        else:
            ItemsRequesting.insert(1, int(item3))
        if item4.isnumeric():
            if int(item4) <= 8:
                RequestingTags.insert(1, tagInfo[str(item4)])
            else:
                ItemsRequesting.insert(1, int(item4))

data = json.dumps({
    "player_id":528525965,
    "offer_item_ids":ItemsOffering,
    "request_item_ids":ItemsRequesting,
    "request_tags": RequestingTags
    }, separators=(',', ':')
)

while True:
	r = requests.post(baseUrl, data=data, headers={'cookie': f'.ROBLOSECURITY={cookie}', 'Content-Type': 'application/json'})
	print(r.json())
	time.sleep(901)
