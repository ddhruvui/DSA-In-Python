point = dict(x=1, y=2)
print("x:",point["x"])
# get prevents error and failure
# returns none if key not present
# can seperately pass the default value
print("a:",point.get("a", 0))