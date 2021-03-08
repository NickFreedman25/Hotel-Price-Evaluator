import requests
import json
import csv

count = 0
url = "https://hotels4.p.rapidapi.com/properties/list"

data_file = open('data/hotels_data.csv', 'w')
csv_writer = csv.writer(data_file)

for x in range(1,100):
    querystring = {"destinationId":"726784","pageNumber":str(x),"checkIn":"2021-06-08","checkOut":"2021-06-11","pageSize":"100","adults1":"1","currency":"USD","locale":"en_US"}

    headers = {
        'x-rapidapi-key': "8af83341femsh83dc2756631ebd4p1b42b3jsnec70360b529c",
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.json()


    j_data = json_data['data']['body']['searchResults']['results']

    for k in j_data:
        if count == 0:

            header = k.keys()
            csv_writer.writerow(header)
            count += 1
        try:
            k['ratePlan'] = k['ratePlan']['price']['current']
            k['guestReviews'] = k['guestReviews']['unformattedRating']
        except:
            pass
        try:
            csv_writer.writerow(k.values())
        except:
            pass
    
    print("write " + str(x) + " succesful!")
print("Write successful!")
data_file.close()
