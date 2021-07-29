import json

# Opening JSON file
f = open('data.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

glory = [] #the json array
  
# Iterating through the json
# list
for i in data['notes']:
    for j in i['sectionNotes']:
        glory.append({"type": j[1], "time": j[0]+3900})

glory.append({"type": 10, "time": glory[-1]['time']+10})

with open('app.json', 'w', encoding='utf-8') as f:
    json.dump(glory, f, ensure_ascii=False, indent=4)

# Closing file
f.close()

#stolen code from online, modified lol
