import requests
import random
from lxml import etree
import multiprocessing

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"

    ]

headers = {
    'User-Agent':random.choice(my_headers)
}

host_url = 'http://desk.zol.com.cn/'


def get_img_url(url):
    html = requests.get(host_url+url)
    html.encoding = 'gbk'
    etree_text = etree.HTML(html.text)
    img_url = etree_text.xpath('//*[@id="showImg"]/li/a/@href')
    return img_url


def Downloads(url,title1):
    data = requests.get(url,headers=headers)
    with open('img\\' + title1 + '.jpg','wb+') as f:
        f.write(data.content)

img_url = []
def get_img_src(url_list):
    for url in url_list:
        html = requests.get(host_url + url)
        html.encoding = 'gbk'
        etree_text = etree.HTML(html.text)

        img_url.append(etree_text.xpath('//*[@id="bigImg"]/@src')[0])
    return img_url



if __name__ == "__main__":
    get_img_url('/bizhi/7336_90603_2.html')
    print(get_img_src(get_img_url('/bizhi/7336_90603_2.html')))


    for title1, url in enumerate(img_url):
        p2 = multiprocessing.Process(target=Downloads,args=(url,str(title1,)))
        p2.start()