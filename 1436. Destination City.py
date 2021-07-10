def destCity(paths) -> str:
    current = dict(paths)
    d = dict(paths)
    for city in d.values():
        if city not in d.keys():
            return city
print(destCity([["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))