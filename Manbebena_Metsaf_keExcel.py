# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:30:00 2020

@author: IT
"""

import pandas as pd

if __name__ == "__main__": 
    # ke Excel lay senaneb
    # Ye filu seme ena ye Sheetu seme
    # Ke lay yeteranew ye 'Pandas package' bezuwen sera yeseralenal (astawsu  pd belenewal )
    YeseraMezgeb_hunatea = pd.read_excel('Mezgebu.xlsx',sheet_name='Yesera Mezgeb');
    print(YeseraMezgeb_hunatea)
    print('*********************')    
    print('columns', YeseraMezgeb_hunatea.columns)
    print('*********************')    
    # mene aynet mereja naw?
    print('columns', type(YeseraMezgeb_hunatea.columns))
    print('*********************')  
    # yemereja aynet bezerzer
    print('columns', [z for z in YeseraMezgeb_hunatea.columns])    
    print('*********************')    
    print('ye mereja bezat', len(YeseraMezgeb_hunatea))
    print('ye mereja bezat', YeseraMezgeb_hunatea.shape)

    print('mene aynet mereja naw? introducing "tuples" menteyochu enebelachew?')
    print('ye mereja bezat', type(YeseraMezgeb_hunatea.shape))

    print('*********************')  
    
    print('ye mereja bezat', YeseraMezgeb_hunatea.shape[0])
    print('ye mereja aynet bezat', YeseraMezgeb_hunatea.shape[1])
    
    print('*********************')  
    print('Merejan netelo lemayet')

    SemeBechaMezgeb = YeseraMezgeb_hunatea['Seme']
    print(SemeBechaMezgeb)
    print('*********************') 
    SemeKeEdmeagaMezgeb = YeseraMezgeb_hunatea[['Seme','Edmea']]
    print(SemeKeEdmeagaMezgeb)
    
    print('*********************') 
    print('Kefaflo mayet (sub setting data) WondochBechaMezgeb')
    WondochBechaMezgeb = YeseraMezgeb_hunatea[YeseraMezgeb_hunatea['Tsota'] == 'Wonde']
    print(WondochBechaMezgeb)
    print('************') 
    SetochBechaMezgeb = YeseraMezgeb_hunatea[YeseraMezgeb_hunatea['Tsota'] == 'Set']
    print(SetochBechaMezgeb)
    print('************')     
    TenaYaluBechaMezgeb = YeseraMezgeb_hunatea[YeseraMezgeb_hunatea['Edmea'] >=  50]
    print(TenaYaluBechaMezgeb)    
    '''
    print('*********************') 
    SemeKeEdmeagaWondochBechaMezgeb = YeseraMezgeb_hunatea[['Seme','Edmea']]
    print(SemeKeEdmeagaMezgeb)
    '''