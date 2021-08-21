
#patika proje bitim sonu ödevi.
#algoritmik problem çözme becerileri için hazırlanmıştır.

#problem1 :

""" input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]"""


#problem düzleştirme/flaten problemi iç içe liste yapısı orantısız olduğundan.
#for döngüsü ile tek seferde for ve karar noktalarıyla çözülemez bu sepeble;
#parçalarına ayırarak çözme yöntemi kullanılabilir. 
#çünkü liste elemanı 
#yeniden hesaplatmak /yeniden düzenlemek gerekli. bu yüzden reküsiv yöntem
#ile çözmek daha ölçekli.
            
            
#problem2 :
"""input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""

#problem liste elamanları liste olduğundan tek seferde ters çevirip
#sonra onu for içinde i inci elemanınını ters çevirerek yeni listeye ekleyip döndürüyoruz.
            
            





#problem1 cevap:
aliste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]


def düzleştirmek(liste):
    yeni_liste=list()
    for i in liste:
        if type(i)!=type(list()):
            yeni_liste.append(i)
        else:
            yeni_liste.extend(düzleştirmek(i))
            
    return yeni_liste


z=düzleştirmek(aliste)
            



#problem2 cevap:
bliste=[[1, 2], [3, 4], [5, 6, 7]]



def tersçevirmek(liste):
    
    liste=liste[::-1]
    yeni_liste=list()
    
    for i in liste:
        yeni_liste.append(i[::-1])
        
        
        
    return yeni_liste




k=tersçevirmek(bliste)