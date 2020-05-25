# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:26:47 2020

@author: IT
"""

#SemeMezgeb = ['Abebe','Mahlet','Zeleqe'];
SemeMezgeb = ['Abebe','Mahlet','Zeleqe','Belachew','Abiy','Agedew','Feyisa','Jemal'];
EdmeaMezgeb = [35,5,55,15,41,56,23,37];
#TsotaMezgeb = ['Wonde','Set','Wonde','Wonde','Wonde','Wonde','Wonde','Wonde']

# list of lists (yemzbeboch mezgeb)
MuluMezgeb = [SemeMezgeb,EdmeaMezgeb];
#MuluMezgeb = [SemeMezgeb,EdmeaMezgeb,TsotaMezgeb];

MuluMezgeb = [['Abebe','Mahlet','Zeleqe','Belachew','Abiy','Agedew','Feyisa','Jemal'],[35,5,55,15,41,56,23,37]];
if __name__ == "__main__": 
    #print(NameList)
    for seme in SemeMezgeb:
        print('seme',seme)
    print('--------------------------------')
    for seme in SemeMezgeb[-2:]:
        print('seme',seme)
    print('--------------------------------')
    for kuter in range(5):
        print('seme',SemeMezgeb[kuter])
    print('--------------------------------')
    for kuter in range(len(SemeMezgeb)):
        print('seme',SemeMezgeb[kuter])
        
    print('--------------------------------')
    for kuter,seme in enumerate(SemeMezgeb):
        print('kuter ena seme -',kuter,seme )
         