import json
import csv
def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
            yield json.loads(chunk)
            chunk = ""
        except ValueError:
            pass
def Run_Convert():
    flag=0
    csv_file=csv.writer(open("data.csv", 'w'))
    with open('repositories-01.json') as f:
        for item in load_json_multiple(f):
            if flag==0:
                csv_file.writerow(['User_ID','User_Name','User_Type','Repo_Id','Repo_Name','Full_Name','Followers','First_Month','Second_Month','Third_Month','Fourth_Month','Fifth_Month','Sixth_Month','Seventh_Month','Eighth_Month','Ninth_Month','Tenth_Month','Eleventh_Month','Twelveth_Month'])
                flag=1
            else:
                csv_file.writerow([item['owner_id'], item['owner'],item['owner_type'] , item['id'], item['name'],item['full_name'], item['followers'], item['First_Month'], item['Second_Month'], item['Third_Month'], item['Fourth_Month'], item['Fifth_Month'], item['Sixth_Month'], item['Seventh_Month'], item['Eighth_Month'], item['Ninth_Month'], item['Tenth_Month'], item['Eleventh_Month'], item['Twelveth_Month']])
