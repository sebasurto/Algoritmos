import time
import taskaa as tsk

entradas = ["100","500","1000","5000","10000"]
for n in range(5):
  print ("\nPrueba #",n+1," \n")
  for i in entradas:
    data =tsk.loadFile (i +".csv")
    data =tsk.convertListToInt (data)
    inicio = time.time()
    tsk.mergeSort(data,0,len(data)-1)
    fin = time.time()
    print("Tiempo con "+i+ " datos:\n",(fin-inicio)%.7)

#print (data)