import requests 
import json

s = requests.Session()
header = {
    "Content-type":"application/json;charset=UTF-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
}

postdata = {"userid":"admin", "password":"DFYOPS1RrpdVlu2U"}  
r = s.post("https://jd.spacecig.com/iam/saml/login",data=postdata)
print(r.cookies)   
r = s.get('https://jd.spacecig.com/zhzlbackend/realPerson/person/familyPersons1?keyword=&personType=&dwdm=null&name=&cardNum=&gender=&maritalStatus=&politicalStatus=&education=&startBirthdayDate=&endBirthdayDate=&focusService=&focusControl=&isActualAddr=&death=&offset=0&limit=10&orderby=&ordertype=')
print(r.json())
