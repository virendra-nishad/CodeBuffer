import json

with open('afterCount.json') as json_file: 
    data = json.load(json_file)
    # print(data)
    temp = sorted(data.items(), key=lambda item : item[1], reverse=True)

    for item in temp:
        print(item)
