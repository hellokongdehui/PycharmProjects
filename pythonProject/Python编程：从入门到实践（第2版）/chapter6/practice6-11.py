# Author：D.H
# Place：哈工深
# Time：2021/7/29 14:57
# 练习6-11：城市
citis = {
    'santiago': {
        'country': 'chile',
        'population': '6_310_000',
        'nearby mountains': 'andes',
        },
    'talkeetna':{
        'country': 'united states',
        'population': '876',
        'nearby mountains': 'alaska range',
        },
    'kathmandu':{
        'country': 'nepal',
        'population': '975_453',
        'nearby mountains': 'himilaya',
        },
    }

for city, city_info in citis.items():
    print(f"\n{city.title()} is in {city_info['country'].title()}.")
    print(f" It has a population of about {city_info['population']}.")
    print(f" The {city_info['nearby mountains'].title()} mountain are nearby.")
