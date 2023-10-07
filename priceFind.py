from requests_html import HTMLSession
session = HTMLSession()

def sort_by_price(array):
  def get_price(obj):
    return obj['price']

  array.sort(key=get_price)
  return array


def getProducts(keywords):
    queryString = ""
    for item in keywords:
        queryString = queryString + "+" + item
    queryString = queryString[1:]
    fullURL = 'https://www.google.com/search?q='+queryString+'&tbm=shop&tbs=mr:1,new:1'
    r = session.get(fullURL)
    itemList = r.html.find('.sh-dgr__content')
    finalList = []
    for item in itemList:
        links = list(item.find('.sh-dgr__offer-content')[0].absolute_links)
        link = links[0]
        price = item.search('${}.{}')[0]
        finalList.append({
            "link":link,
            "price": int(price.replace(',', ''))
        })
    finalerList = sort_by_price(finalList[:10])
    return finalerList

print(getProducts(["macbook", "m1", "pro"]))