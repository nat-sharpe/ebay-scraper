# Imports libraries
from bs4 import BeautifulSoup
import requests

unique_listings = {
    "https://i.ebayimg.com/thumbs/images/g/FDAAAOSw0F9bntMB/s-l225.jpg" : {'title': '1/6 Plate Ambrotype In Case Cross—eyed Woman', 'listing_URL': 'https://www.ebay.com/itm/1-6-Plate-Ambrotype-In-Case-Cross-eyed-Woman/202439561494?hash=item2f22569116:g:FDAAAOSw0F9bntMB', 'img_URL': 'https://i.ebayimg.com/thumbs/images/g/FDAAAOSw0F9bntMB/s-l225.jpg', 'price': '$49.95'},
    'https://i.ebayimg.com/thumbs/images/g/OOwAAOSwWxNYzs7m/s-l225.jpg' : {'title': 'Antique Ambrotype Photo, Gentleman', 'listing_URL': 'https://www.ebay.com/itm/Antique-Ambrotype-Photo-Gentleman/332808350434?hash=item4d7cec6ae2:g:OOwAAOSwWxNYzs7m', 'img_URL': 'https://i.ebayimg.com/thumbs/images/g/OOwAAOSwWxNYzs7m/s-l225.jpg', 'price': '$60.00'}
}

def write_page():
    request = "https://www.ebay.com/b/Ambrotypes/13704?LH_Auction=1&Photo%2520Type=Ambrotype&rt=nc&_from=R40&_ipg=25&_nkw=&_pgn=1&_sop=10"

    # Scrapes the listings from the DOM
    print("Scraping listings... ", end="")
    response = requests.get(request)
    soup = BeautifulSoup(response.text, "html.parser")

    containers = soup.findAll('li',{'class':'s-item'})

    def get_listings(start, stop, containers, tag):
        all_fresh = []
        for i in range(start, stop):
            container = containers[i]
            key = str(container.div.div.div.div.img[tag])
            if key not in unique_listings:
                single_fresh = {}
                single_fresh["title"] = str(container.div.div.div.div.img['alt'])
                single_fresh["listing_URL"] = str(container.div.div.a['href'])
                single_fresh["img_URL"] = key
                single_fresh["price"] = str(container.div.find("div", {"class" : "s-item__info clearfix"}).find("div", {"class" : "s-item__details clearfix"}).div.span)

                all_fresh.append(single_fresh)

                unique_listings[key] = single_fresh

        return all_fresh

    list1 = get_listings(0, 7, containers, "src")
    list2 = get_listings(7, len(containers), containers, "data-src")

    # Writes the HTML
    print("Generating HTML file... ", end="")
    f = open("index.html", "w")

    # Loops thru lists of dictionaries and writes each listing
    def print_listing(list_to_check):
        for listing in list_to_check:
            # Writes the picture 
            f.write('<img src="' + listing['img_URL'] + '"/><br/>')
             # Writes the listing title & link
            f.write('<a href"' + listing['listing_URL'] + '"/>' + listing['title'] + '</a><br/>')
            # Writes the price
            f.write('<h3>' + listing['price'] + '</h3><br/>')
            # Adds space
            f.write("<br/>")

    print_listing(list1)
    print_listing(list2)
    
    f.close()
    print("done")

write_page()