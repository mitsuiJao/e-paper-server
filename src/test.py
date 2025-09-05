from weather_map import string_icon, string_map

keys1 = string_icon.keys()
keys2 = string_map.values()

for k in keys2:
    if k in keys1:
        print(k)