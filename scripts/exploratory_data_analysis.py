# -*- coding: utf-8 -*-

import logging
import json
import logging.config
#import descriptive_statistics

def main():
        try:
            logging.getLogger(__name__)
            with open('../resources/logging.json') as log_config:    
                logging.config.dictConfig(json.load(log_config))
            logging.info('main')
            eda = ExploratoryDataAnalysis()
            eda.get_config_info()
        except Exception as e:
            logging.error('__init__: ', exc_info=True)
            
class ExploratoryDataAnalysis:
    def __init__(self, logger=None):
        logging.getLogger(__name__)
    def get_config_info(self):
        try:
            logging.info('ExploratoryDataAnalysis: get_config_info()')
            with open('../resources/config.json') as config:    
                folder_paths = json.load(config)["dataset_paths"]
            for path in folder_paths:
                print(path)
                #ds = descriptive_statistics.DescriptiveStatistics()
                #ds._calulate_descriptive_statistics(path)
        except Exception as e:
            logging.error('get_config_info', exc_info = True)

if __name__ == '__main__':
    main()
