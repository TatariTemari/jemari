# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:26:47 2020

@author: IT
"""

SemeMezgeb = ['Abebe','Mahlet','Zeleqe'];
SemeMezgeb = ['Abebe','Mahlet','Zeleqe','Belachew','Abiy','Agedew','Feyisa','Jemal'];
EdmeaMezgeb = [35,5,55,15,41,56,23,37];
#TsotaMezgeb = ['Wonde','Set','Wonde','Wonde','Wonde','Wonde','Wonde','Wonde']

# list of lists (yemzbeboch mezgeb)
MuluMezgeb = [SemeMezgeb,EdmeaMezgeb];
#MuluMezgeb = [SemeMezgeb,EdmeaMezgeb,TsotaMezgeb];

MuluMezgeb = [['Abebe','Mahlet','Zeleqe','Belachew','Abiy','Agedew','Feyisa','Jemal'],[35,5,55,15,41,56,23,37]];
if __name__ == "__main__": 
    #print(NameList)
    yemejemeriawSeme = SemeMezgeb[0];
    YemigemeriaySoste = SemeMezgeb[0:3];
    Yemechereshahulet = SemeMezgeb[-2:];
    
    YemechereshawSawSeme  = MuluMezgeb[0][-1] 
    print('Yemechereshaw Saw Seme',YemechereshawSawSeme)
    YemechereshawSawEdmea =  MuluMezgeb[1][-1];    
    print('Yemechereshaw Saw Edmea',YemechereshawSawEdmea)
    YemechereshawSawSemenaEdmea = MuluMezgeb[0][-1] + '  ' +  str(MuluMezgeb[1][-1]);
    print('Yemechereshaw Saw Semena Edmea ',YemechereshawSawSemenaEdmea)
    semua = 'Mahlet'
 
    if (SemeMezgeb.count(semua) > 0):
        print('Alech')
    else:
        print('Yelechem')
        
    print(SemeMezgeb.indexof('Mahlet'))
 