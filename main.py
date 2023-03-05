from bs4 import BeautifulSoup
import requests
import smtplib

my_mail = "test@gmail.com"
password = "************"

headers_amazon = {
    "Accept-Language": "ka-GE,ka;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0"
}

acceptable_price = 25
link = "https://www.amazon.com/Prime-Brands-Group-Wireless-Organizer/dp/B07T4M79QL/ref=sr_1_1_sspa?qid=1678033367&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRDlLNzdIQ08xQjlOJmVuY3J5cHRlZElkPUEwMjExMDQwMUZHVVNDWFFITkdSVCZlbmNyeXB0ZWRBZElkPUEwNTE1ODA3MVg4QVVSOUdCUUhSRiZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
resp = requests.get(link, headers=headers_amazon)
content = resp.text
soup = BeautifulSoup(content, "lxml")

price_class = soup.find(class_="a-offscreen")
price_first_gen = price_class.getText()
price = price_first_gen.translate({ord("$"): None})
print(price)

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(my_mail,password)
        con.sendmail(
            from_addr=my_mail,
            to_addrs="test2@gmIL.COM",
            msg=f"subject:Amazon Notification \n\n Hey Check Item desired by you link:{link}, your accebtable price was {acceptable_price}, current item price is {price}, "
        )
    
if float(price) < acceptable_price:
    send_mail()
else:
    print("Price is high")