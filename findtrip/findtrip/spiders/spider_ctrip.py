import scrapy
from findtrip.items import FindtripItem
from scrapy import log

class CtripSpider(scrapy.Spider):
    name = 'Ctrip'
    start_urls = [
            "https://flights.ctrip.com/international/search/oneway-bjs-puq?depdate=2020-10-01"
            ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        fligint_div = "//div[@class='flight-item']"
        dataList = sel.xpath(fligint_div).extract()
        log.msg(">>>>>> Get %s flight html items" % len(dataList), level=log.DEBUG)

        for i in range(len(dataList)):
            filename = response.url.split("/")[-2] + str(i) + '.html'
            with open(filename, 'wb') as f:
                f.write(dataList[i].encode('utf-8').strip())

        '''
        items = []
        for index,each in enumerate(dataList):
            flight_each = fligint_div+'['+str(index+1)+']'
            flight_tr = flight_each+"//tr[@class='J_header_row']"
            istrain = sel.xpath(flight_each + "//div[@class='train_flight_tit']")

            if istrain:
                print "this data is train add"
            else:
                company = sel.xpath(flight_tr + "//div[@class='info-flight J_flight_no']//text()").extract()

                flight_time_from = sel.xpath(flight_tr + "//td[@class='right']/div[1]//text()").extract()
                flight_time_to = sel.xpath(flight_tr + "//td[@class='left']/div[1]//text()").extract()
                flight_time = [flight_time_from,flight_time_to]

                airports_from =  sel.xpath(flight_tr + "//td[@class='right']/div[2]//text()").extract()
                airports_to = sel.xpath(flight_tr + "//td[@class='left']/div[2]//text()").extract()
                airports = [airports_from,airports_to]

                price_middle = sel.xpath(flight_tr + "[1]//td[@class='price middle ']/span//text()").extract()
                price = sel.xpath(flight_tr + "[1]//td[@class='price ']/span//text()").extract()
                if price_middle:
                    price = price_middle
                elif price:
                    price = price
                else:
                    price = ''

                item = FindtripItem()
                item['site'] = 'Ctrip'
                item['company'] = company
                item['flight_time'] = flight_time
                item['airports'] = airports
                item['price'] = price
                items.append(item)

        return items
        '''