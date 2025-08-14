import requests
from bs4 import BeautifulSoup

def fetch_html_tag(url, tag_name, attrs=None, multiple=False, encoding=None):
    """
    通用 HTML 标签抓取函数

    :param url: 目标网址
    :param tag_name: 标签名，例如 'div', 'a', 'title'
    :param attrs: 过滤属性，例如 {'id': 'main'} 或 {'class': 'nav'}
    :param multiple: True 返回列表，False 返回单个
    :param encoding: 指定编码（默认自动检测）
    :return: 标签对象或标签列表（BeautifulSoup Tag 对象）
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    
    # 自动或手动设置编码
    if encoding:
        response.encoding = encoding
    else:
        response.encoding = response.apparent_encoding
    
    soup = BeautifulSoup(response.text, "lxml")

    if multiple:
        return soup.find_all(tag_name, attrs=attrs)
    else:
        return soup.find(tag_name, attrs=attrs)


if __name__ == "__main__":
    # 抓取百度首页 title 标签
    tag = fetch_html_tag("https://www.baidu.com", "title")
    print("Title:", tag.text if tag else "未找到")

    # 抓取百度首页所有 a 标签
    texts = fetch_html_tag("https://www.baidu.com", "span", {"class": "title-content-title"}, multiple=True)
    for text in texts[:5]:  # 只打印前5个
        print(text.text)
