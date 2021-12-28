# Author：D.H
# Place：哈工深
# Time：2021/7/29 14:40
# 练习6-9：喜欢的地方
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"-{place.title()}")