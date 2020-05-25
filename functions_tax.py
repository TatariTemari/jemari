# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:26:47 2020

@author: IT
"""

#SemeMezgeb = ['Abebe','Mahlet','Zeleqe'];
SemeMezgeb = ['Abebe','Mahlet','Zeleqe','Belachew','Abiy','Agedew','Feyisa','Jemal'];
EdmeaMezgeb = [35,5,55,15,41,56,23,37];
DemozMezgeb = [3500,5000,25005,15,410,506,2300,3700];
#TsotaMezgeb = ['Wonde','Set','Wonde','Wonde','Wonde','Wonde','Wonde','Wonde']

# list of lists (yemzbeboch mezgeb)
MuluMezgeb = [SemeMezgeb,EdmeaMezgeb,DemozMezgeb];
def Teqlala_Tax_Selete(YeDemozachewMezgeb,tax_rate):
    teqlala_taxachen = 0;
    for d in YeDemozachewMezgeb:
        tax = d*tax_rate;
        teqlala_taxachen = teqlala_taxachen + tax;
        
    return teqlala_taxachen

def Yegeleseb_Tax_Selete(Demoz,tax_rate):
    tax = Demoz*tax_rate
    return tax
if __name__ == "__main__": 
    tax_rate = 0.35;

    for demoz in DemozMezgeb:
        tax = Yegeleseb_Tax_Selete(demoz,tax_rate)
        print('tax',tax)

    print('--------------------------------')
    
    for kuter,demoz in enumerate(DemozMezgeb):
        tax = Yegeleseb_Tax_Selete(demoz,tax_rate)
        print('seme ena tax',SemeMezgeb[kuter],tax)

    print('--------------------------------')
    print('teqlala tax',Teqlala_Tax_Selete(DemozMezgeb,tax_rate))

    for kuter,seme in enumerate(SemeMezgeb):
        print('kuter ena seme -',kuter,seme )

         