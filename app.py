from selenium import webdriver
from bs4 import BeautifulSoup
import requests as rq
import time
import os

path = input("Enter Path : ")
url = input("Enter URL : ")
output = "output"


def get_url(path, url):
    drivver = webdriver.Chrome(executable_path=r"{}".format(path))
    drivver.get(url)
    print("loading...")
    res = drivver.execute_script("return document.documentElement.outerHTML")
    return res


def get_img_links(res):
    soup = BeautifulSoup(res, "lxml")
    imglinks = soup.find_all("img", src=True)
    return imglinks


def download_img(img_link, index):
    try:
        extensions = [".jpeg", ".jpg", ".png", ".git"]
        extensions = ".jpg"
        for exe in extensions:
            if img_link.find(exe) > o:
                extensions = exe
                break
        img_data = rq.get(img_link).content
        with open(output + "\\" + str(index + 1) + extensions, "wb+") as f:
            f.write(img_data)
        f.close()
    except Exception:
        pass

    result = get_url(path, url)
    time.sleep(60)
    img_links = get_img_links(result)
    if not os.path.isdir(output):
        os.mkdir(output)

    for index, img_link in enumerate(img_links):
        img_link = img_link["src"]
        print("Downloading...")
        if img_link:
            download_img(img_link, index)
    print("Download complete!!!")
