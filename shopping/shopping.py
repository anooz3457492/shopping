import requests
from bs4 import BeautifulSoup
import csv
base_url = "https://www.sastodeal.com/"
response = requests.get(base_url+"/sastodeal/cta-t-shirts-and-sleeveless-m-520")
soup = BeautifulSoup(response.content,"lxml")
classes = soup.find_all("div",{"class":"categoryWrap row"})
table = classes[0]

csv_file = open("shopping.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["S.No","Tshirt","price"])
sn=0

for table in soup.find_all( class_="prod-detail"):
    sn = sn +1
    print(sn)
    tshirt = table.find_all("b", class_="title")
    Ts = tshirt[0].text.strip()
    print(Ts)
    
    rupees = table.find_all( class_="mrp offer-price")
    Rs = rupees[0].text.replace("रू","")
    print(Rs)
    
    csv_writer.writerow([sn,Ts,Rs])
    
csv_file.close()