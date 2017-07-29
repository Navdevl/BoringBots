from logger import *
import yaml
from processor import Processor

CONFIG_FILE = 'config.yml'

class PriceBot:
  def __init__(self):
    logging.info('Program Started')
    with open(CONFIG_FILE, 'r') as file:
      data = yaml.load(file)

    config_type = data['configuration']['type']
    parameters = data['configuration']['parameters']
    urls = data['urls']

    processor = Processor(parameters, urls)
    if config_type == 'price_change':
      logging.info("{0} function is called".format(config_type))
      processor.price_change()

    elif config_type == 'schedule':
      logging.info("{0} function is called".format(config_type))
      processor.schedule()
    else:
      print 'Configuration type can be either "price" or "schedule".'
      logging.error("Config-type value error.")

PriceBot()