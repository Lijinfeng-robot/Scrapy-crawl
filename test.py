import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
url = 'https://photo.fengniao.com'
res = requests.get(url, headers=headers)
selector = etree.HTML(res.text)
sd = selector.xpath('/html/body/div[@class="picList"]/ul/li[@class="noRight"]/a/@style')
for i in sd:
    img = i[23:-43]
    print(img)
