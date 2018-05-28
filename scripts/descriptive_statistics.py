# -*- coding: utf-8 -*-
"""
Created on Mon May 21 09:12:30 2018

@author: Minu
"""
import pandas as pd

class DescriptiveStatistics:
    def _calulate_descriptive_statistics(file_path, logger):
        logger.info('DescriptiveStatistics:_calulate_descriptive_statistics')
        dataset = pd.read_excel(file_path, header=None, skiprows=4, sheet_name=0, index_col=0, parse_cols=4)
        print(dataset.head())
        """
        print(dataset.shape)
        print(dataset.tail())
        print(dataset.sort_values(['price'], ascending=False).head(10).plot(kind="hist")) #barh
        print(dataset.describe())
        print(dataset["price"]).mean()
        print(dataset.columns)
        """