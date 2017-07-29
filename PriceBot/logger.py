import logging
logging.getLogger(__name__)
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='pricebot.log',level=logging.DEBUG, format=log_format)
formatter = logging.Formatter(log_format)