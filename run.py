from requests_html import HTMLSession

url = "https://www.diyifanwen.com/fanwen/rongzhizulin/162221415538512.htm"
session = HTMLSession()
r = session.get(url)
print(r.html.text)
# for html_link in r.html.links:
#     print(html_link)
#     session = HTMLSession
#     text = session.get(html_link)
#     print(text.html.text)
