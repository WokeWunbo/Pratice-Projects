import operator
test = "11+11"
ops = { "+": operator.add, "-": operator.sub } # etc.
numbers = test.split("+")
print(test, "=", ops["+"](int(numbers[0]), int(numbers[1])))

import requests

url = "https://www.w3schools.com/python/demopage.htm"
req = requests.get(url)

status = req.status_code

for x in req.text:
    #print(x, end="")
    pass