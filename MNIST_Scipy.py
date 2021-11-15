import numpy as np
import time
from scipy.spatial.distance import cdist
Inicio1=time.time()

ContMaxTest=100
ContMaxTraining=60000
StartTest=1
StartTraining=1

NumClases=10
NumCampos=785

arr=[]
arry=[]

f=open("C:\\mnist_test.csv","r")

Cont=0;
for linea in f:
    Cont=Cont+1
    if Cont<=StartTest: continue
    if Cont > ContMaxTest :break
    lineadelTest =linea.split(",")
   
 
    linea_x =[""]
    z=0
    for x in lineadelTest:
       
        z=z+1
        if z==NumCampos: break
        if z==1: linea_x[0]=int(lineadelTest[z])
        else:  linea_x.append(int(lineadelTest[z]))
  
    arr.append(linea_x)
    arry.append(lineadelTest[0])
     

X_test=np.array(arr)
Y_test=np.array(arry)


f=open("C:\\mnist_train.csv","r")

Cont=0;
for linea in f:
    Cont=Cont+1
    if Cont<=StartTraining: continue
    if Cont > ContMaxTraining :break
    lineadelTrain =linea.split(",")
  
 
    linea_x =[""]
    z=0
    for x in lineadelTrain:
   
        z=z+1
        if z==NumCampos: break
        if z==1: linea_x[0]=int(lineadelTrain[z])
        else:  linea_x.append(int(lineadelTrain[z]))
  
    arr.append(linea_x)
    arry.append(lineadelTrain[0])
    

X_train=np.array(arr)
Y_train=np.array(arry)
Fin1=time.time()
print("Duration of previous preparation time = "+ str(Fin1 - Inicio1))
print( "")

Inicio2=time.time()
Inicio2=time.time()

##########################################################################333
#   https://stackoverflow.com/questions/1871536/minimum-euclidean-distance-between-points-in-two-different-numpy-arrays-not-wit
############################################################################
TotAciertos=0
TotFallos=0
Inicio=time.time()
DifeMatriz =cdist( X_test, X_train )
#print(DifeMatriz)

for i in range (len(X_test) ):  
    DistanciaMax=999999999999
    LineaMax=-1
    DifeFila=DifeMatriz[i]
    
    j=-1
    while j < len(X_train)-1:
         
          j=j+1
         
          
          DistanciaFila=DifeFila[j]
          
          # si no se pone and (DistanciaFila != 0) aparecen todos 
          #como aciertos
          
          if (DistanciaFila < DistanciaMax) and (DistanciaFila != 0):
        
              DistanciaMax = DistanciaFila
              LineaMax=j
            
    print("Predicted Class = "+ str(Y_train[LineaMax]) + " True class = " + str(Y_test[i]) + " Minimal Distance = " + str(DistanciaMax))
               
    if int(Y_train[LineaMax])==int(Y_test[i]):
         TotAciertos=TotAciertos+1
    else:
         TotFallos=TotFallos+1
print("") 
print("Total Hits = " + str(TotAciertos ))
print("Total Failures = " + str(TotFallos))  
print("") 
Fin2 =time.time()  
print ( "procesing time USING SCPY of " + str(ContMaxTest - StartTest) + "  images = "  + str(Fin2 - Inicio2))
print( "Average processing time per image = " + str((Fin2 - Inicio2)/(ContMaxTest - StartTest))) 
