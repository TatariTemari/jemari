# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:30:00 2020

@author: IT
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__": 
    # ke Excel lay senaneb
    # Ye filu seme ena ye Sheetu seme
    # Ke lay yeteranew ye 'Pandas package' bezuwen sera yeseralenal (astawsu  pd belenewal )
    YeseraMezgeb_hunatea = pd.read_excel('Mezgebu.xlsx',sheet_name='Yesera Mezgeb');

    print('*********************') 
    SemeKeEdmeagaMezgeb = YeseraMezgeb_hunatea[['Seme','Edmea']]
    plt.figure()
    plt.scatter(SemeKeEdmeagaMezgeb['Seme'],SemeKeEdmeagaMezgeb['Edmea'])
    plt.xlabel('Seme')
    plt.ylabel('Edmea')
    plt.title('beten plot')
    print('*********************') 
    plt.figure()
    SemeKeEdmeagaMezgeb.plot()
    plt.title('yanchi line plot')
    print('*********************')     
    plt.figure()
    plt.bar(SemeKeEdmeagaMezgeb['Seme'],SemeKeEdmeagaMezgeb['Edmea'])
    plt.title('yenea bar plot')
    
    print('*********************')    
    print('Kefelefay mayet') 
    KeFelefayMezgeb = YeseraMezgeb_hunatea.groupby('Tsota').max().reset_index() 
    print('KeFelefayMezgeb',KeFelefayMezgeb)

    plt.figure()
    plt.bar(KeFelefayMezgeb['Tsota'],KeFelefayMezgeb['Edmea'])

    KeFelefayMezgeb = YeseraMezgeb_hunatea.groupby('Tsota').min().reset_index()      
    plt.figure()
    plt.bar(KeFelefayMezgeb['Tsota'],KeFelefayMezgeb['Demoz'])
    '''
    plt.figure()
    plt.bar(SemeKeEdmeagaMezgeb['Seme'],SemeKeEdmeagaMezgeb['Edmea'])
    plt.title('yenea bar plot')
    '''