from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

my_url = 'https://www.ebay.com/sch/13704/i.html?_from=R40&_nkw=&Photo%2520Type=Ambrotype&LH_Complete=1&LH_Auction=1&_ipg=25&_pgn=1'

# browser = webdriver.Safari()
# browser.get(my_url)
# element = browser.find_element_by_tag_name('html')
# containers = browser.find_element_by_tag_name('li',{'class':'s-item'})
# print containers

# element.send_keys(Keys.END)
# time.sleep(8)
# element.send_keys(Keys.HOME)
# browser.close()


# opening connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

count = page_soup.findAll('h1',{'class':'srp-controls__count-heading'})
count_number = count_ 

#grabs each product
containers = page_soup.findAll('li',{'class':'s-item'})

# thumbnails = page_soup.findAll('img',{'class':'s-item__image-img'})
# completed = []

# for thumb in thumbnails:
#     photo = thumb['src']
#     completed.append(photo)

# print page_html

length = len(containers)

for i in range(0, 7):
    container = containers[i]
    listing1 = container.div.div.div.div.img['src']
    print 'first listing: %s' % listing1

for i in range(7, length):
    container = containers[i]
    listing2 = container.div.div.div.div.img['data-src']
    print 'next listing: %s' % listing2


    # if 'data-src' in container:
    #     print 'Unique listing: %s' % listing1
    # else:
    #     print 'Unique data: %s' % listing2
    