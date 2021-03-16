import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from .models import Headline


# Create your views here.
def scrape(request):

    title = []
    link = []
    imgx = []
    contentN = []

    # times of india
    url = "https://timesofindia.indiatimes.com/briefs"
    r_toi = requests.get(url)
    toi_news = r_toi.content
    soup_toi = BSoup(toi_news, "html.parser")

    data = soup_toi.find_all('h2')  # for title,link
    image = soup_toi.find_all('div', class_='posrel')  # for image
    details = soup_toi.find_all('div', class_='brief_box')

    toi_title = []
    toi_link = []
    toi_image = []
    toi_content = []

    for news in data:
        toi_title.append(news.text.strip())
        for textlink in news.find_all('a', href=True):
            toi_link.append("https://www.timesofindia.indiatimes.com" + textlink['href'])
            link.append("https://www.timesofindia.indiatimes.com" + textlink['href'])
            title.append(news.text.strip())

    for texts in details:
        for content in texts.find_all('p'):
            toi_content.append(content.text.strip())
            contentN.append(content.text.strip())

    for img in image:
        for imglink in img.find_all('img'):
            toi_image.append(imglink['data-src'])
            imgx.append(imglink['data-src'])

    toi_title = toi_title[0:-12]

    # ndtv
    url1 = "https://www.ndtv.com/india?pfrom=home-mainnavgation"
    r_ndtv = requests.get(url1)
    ndtv_news = r_ndtv.content
    soup_ndtv = BSoup(ndtv_news, 'html.parser')

    data = soup_ndtv.find_all('div', class_="new_storylising_img")  # for title,link,image
    details = soup_ndtv.find_all('div', class_="nstory_intro")

    ndtv_title = []
    ndtv_link = []
    ndtv_image = []
    ndtv_content = []

    for news in data:
        for textlink in news.find_all('a', href=True):
            ndtv_title.append(textlink['title'])
            title.append(textlink['title'])
            ndtv_link.append(textlink['href'])
            link.append(textlink['href'])
            for img in textlink.find_all('img'):
                ndtv_image.append(img['src'])
                imgx.append(img['src'])

    for texts in details:
        ndtv_content.append(texts.text.strip())
        contentN.append(texts.text.strip())

    # hindustan times

    url2 = "https://www.hindustantimes.com/it-s-viral/"
    r_ht = requests.get(url2)
    ht_news = r_ht.content
    soup_ht = BSoup(ht_news, 'html.parser')

    data = soup_ht.find_all('div', class_="media-img")  # for title, link, image
    details = soup_ht.find_all('div', class_="para-txt")  # for detailed content

    ht_title = []
    ht_link = []
    ht_image = []
    ht_content = []

    for news in data:
        for textlink in news.find_all('a', href=True):
            ht_title.append(textlink['title'])
            title.append(textlink['title'])
            ht_link.append(textlink['href'])
            link.append(textlink['href'])
        for image in news.find_all('img'):
            ht_image.append(image['src'])
            imgx.append(image['src'])

    for texts in details:
        ht_content.append(texts.text.strip()[:-9])
        contentN.append(texts.text.strip()[:-9])

    # ht_content = ht_content[0:-2]
    # ht_title = ht_title[0:-16]
    # ht_image = ht_image[0:-16]
    # ht_link = ht_link[0:-16]

    # title_list = ndtv_title + ht_title
    # link_list = ndtv_link + ht_link
    # image_list = ndtv_image + ht_image
    # content_list = ndtv_content + ht_content
    # object_list = zip(toi_title, toi_link, toi_image, toi_content, title_list, link_list, image_list, content_list)

    for i in range(len(title)):
        new_headline = Headline()
        new_headline.title = title[i]
        new_headline.url = link[i]
        new_headline.image = imgx[i]
        new_headline.content = contentN[i]
        new_headline.save()

    print(len(title), len(link), len(imgx), len(contentN))

    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)