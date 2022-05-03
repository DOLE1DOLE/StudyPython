# 구글 웹페이지 긁어오기 2
import requests as req

res=req.get('https://www.google.com')
#print(res.status_code)
print(res._content)