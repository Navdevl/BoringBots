import json
import requests
import time
from logger import *

class Processor:
    def __init__(self, parameters, urls):
        self.parameters = parameters
        self.urls = urls

    def get_price(self):
        """ Modify this function as per your need. """
        while(True):
            try:
                logging.info('Getting Price')
                response = requests.get(self.urls['price_api'])
                content = response.content
                price_dict = json.loads(content.decode())
                return price_dict
            except:
                time.sleep(3000)

    def send_response(self, currency, price):
        statement = "The current price of {0}: USD is {1}, INR is {2}. Bot by NavDevl".format(currency, price['USD'], price['INR'])
        payload = {"text": statement}
        payload = json.dumps(payload)
        print payload
        for name, url in self.urls['post_api'].iteritems():
            logging.info('Sending response to {0}'.format(name))
            print url
            response = requests.post(url, data=payload)


    def schedule(self):
        while(True):
            price_dict = self.get_price()
            for currency, price in price_dict.iteritems():
                self.send_response(currency, price)
            time_to_sleep = self.parameters['frequency'] * 60 * 60
            logging.info('Hibernating for {0} hours'.format(self.parameters['frequency']))
            time.sleep(time_to_sleep)
            logging.info('Awake')


    def price_change(self):
        last_price = 0
        threshold = self.parameters['price_change']
        while(True):
            price = self.get_price()
            change_in_price = abs(price - last_price)
            if change_in_price >  threshold:
                logging.info('Price change went above threshold.')
                self.send_response(price)
            else:
                logging.info('Price change is still below the threshold')

            time_to_sleep = self.parameters['check_every_x_mins'] * 60
            logging.info('Hibernating for {0} mins'.format(self.parameters['check_every_x_mins']))
            time.sleep(time_to_sleep)
            logging.info("Listening again..")

