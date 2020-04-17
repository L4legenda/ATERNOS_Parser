import requests
from lxml import html

url = "https://aternos.org/server/"

cookies = {'ATERNOS_SESSION': "Wr60Rm75lHrm0nVSpqnHxNmm6r7kbOgvxGtveVj8jnZJUma5iqa1PF6BZ6pIcgN487pZU9EiYd4DalBepFJEoLOThxjCPDszISYL"}

def parse():
    siteText = requests.get(url, cookies=cookies)
    tree = html.fromstring(siteText.text)
    r = {}
    typeOfExpectation = tree.xpath('/html/body/div[1]/main/section/div[3]/div[3]/div[1]/div/span[2]/span')[0].text.strip()

    if typeOfExpectation == "Waiting in queue":
        time = tree.xpath('/html/body/div[1]/main/section/div[3]/div[3]/div[1]/div/span[1]')[0].text.strip()
        slot = tree.xpath('/html/body/div[1]/main/section/div[3]/div[3]/div[1]/div/span[3]')[0].text.strip()

        r["time"] = time
        r["slot"] = slot
    return r
