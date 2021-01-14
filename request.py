import requests

url = "https://superheroapi.com/api/2619421814940190/"
resp = requests.get(url)

names_list = ['Hulk', 'Captain America', 'Thanos']


def get_id(heroes_list):
    heroes_result_dict = {}
    for name in heroes_list:
        hero_data = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{name}")
        name = hero_data.json()['results'][0]['name']
        heroes_result_dict[name] = hero_data.json()['results'][0]['id']
    return heroes_result_dict


def get_powerstats(data_dict):
    intelligence_dict = {}
    for name, name_id in data_dict.items():
        data = requests.get(f"https://superheroapi.com/api/2619421814940190/{name_id}/powerstats")
        powerstats = data.json()
        intelligence_dict[name] = powerstats['intelligence']
    return intelligence_dict


# names = get_id(names_list)
# print(names)
# intlgns = get_powerstats(names)
# print(intlgns)
# best_intelligence = get_powerstats(get_id(names_list))
# print(best_intelligence)
