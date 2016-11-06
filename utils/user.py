import requests
from bs4 import BeautifulSoup
from PIL import Image
from os import remove
from pytesseract import image_to_string

index_url = 'http://210.35.251.243/reader/login.php'
capture_url = 'http://210.35.251.243/reader/captcha.php'
login_url = 'http://210.35.251.243/reader/redr_verify.php'


def beforc_login():
    data = requests.get(index_url)
    data.encoding = 'utf-8'

    return data.cookies


def get_capture(cookies):
    data = requests.get(capture_url, cookies=cookies)
    with open("./img_cache/" + cookies['PHPSESSID'] + ".gif", "wb+") as f:
        f.write(data.content)

    gif = Image.open("./img_cache/" + cookies['PHPSESSID'] + ".gif")

    png = Image.new("RGB", gif.size)
    png.paste(gif)

    str = image_to_string(png).strip()
    remove("./img_cache/" + cookies['PHPSESSID'] + ".gif")

    return str


def login(user, passwd):
    cookies = beforc_login()

    chk_code = get_capture(cookies)

    post_data = {
        'number': user,
        'passwd': passwd,
        'captcha': chk_code,
        'select': 'cert_no',
        'returnUrl': ''
    }

    data = requests.post(login_url, cookies=cookies, data=post_data)
    data.encoding = 'utf-8'

    soup = BeautifulSoup(data.text, "html5lib")

    status = soup.select(".header_right_font")[1].find_all("a")[1].text

    if status == "注销":
        status = True
    else:
        status = False

    ret_data = {'status': status, 'cookies': 'PHPSESSID=' + cookies['PHPSESSID']}

    return ret_data
