# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:56:35 2020

@author: IT
"""

import pandas as pd

if __name__ == "__main__": 
    # ke Excel lay senaneb
    # Ye filu seme ena ye Sheetu seme
    # Ke lay yeteranew ye 'Pandas package' bezuwen sera yeseralenal (astawsu  pd belenewal )
    YeseraMezgeb_hunatea = pd.read_excel('Mezgebu.xlsx',sheet_name='Yesera Mezgeb');
 
    #print(YeseraMezgeb_hunatea)
    print('*************************')
    temp_YeseraMezgeb_DictionaryStyle = YeseraMezgeb_hunatea.to_dict()
    #print(temp_YeseraMezgeb_DictionaryStyle)
    YeseraMezgeb_DictionaryStyle = temp_YeseraMezgeb_DictionaryStyle['Demoz']
    print(YeseraMezgeb_DictionaryStyle)
    print('*************************')
    
    print(YeseraMezgeb_DictionaryStyle[0])
    print('*************************')
 
    for i in YeseraMezgeb_DictionaryStyle.keys():
        print(temp_YeseraMezgeb_DictionaryStyle['Seme'][i])

    print('*************************')
    AddisDemozDict= dict()
    for i in YeseraMezgeb_DictionaryStyle.keys():
        AddisDemozDict[temp_YeseraMezgeb_DictionaryStyle['Seme'][i]] = temp_YeseraMezgeb_DictionaryStyle['Demoz'][i]
    print(AddisDemozDict)
    
    print('*************************')
    AddisDict= dict()
    for i in YeseraMezgeb_DictionaryStyle.keys():
        AddisDict[temp_YeseraMezgeb_DictionaryStyle['Seme'][i]] = {'Zemen':temp_YeseraMezgeb_DictionaryStyle['Edmea'][i],'Demoz':temp_YeseraMezgeb_DictionaryStyle['Demoz'][i],'Tsota':temp_YeseraMezgeb_DictionaryStyle['Tsota'][i]}
    print(AddisDict)
    
    print(AddisDict['Feyisa']['Demoz'])
    print(AddisDict['Meron']['Tsota'])