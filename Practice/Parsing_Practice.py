import json

datafile = open('D:\Project\Site_Parsing\Practice\webinars.json', 'r', encoding='utf-8')
data = json.load(datafile)

# [webinar['speaker'] for webinar in data]
for webinar in data:
    print(webinar['speaker'])
