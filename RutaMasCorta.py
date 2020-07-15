def encontrarRMC_PorImpulsoDEBUG(grafo,Origen,Destino,Costo,Ruta,Aux):
  #print("Actual:",Origen,"R:",Ruta)
  if(Origen == Destino):
    aux = Ruta
    Aux.append([aux,Costo])
  else:        
    aux = grafo[Origen]    
    
    if aux:
      for i in aux:
        if(i not in Ruta):
          
          Costo += aux[i]
          Ruta.append(i)
          encontrarRMC_PorImpulsoDEBUG(grafo,i,Destino,Costo,Ruta.copy(),Aux)
          Ruta.pop()
          Costo -= aux[i]

def encontrarRMC_PorImpulso(grafo,Origen,Destino):
  Aux = []
  encontrarRMC_PorImpulsoDEBUG(grafo,Origen,Destino,0,[Origen],Aux)

  Ruta = Aux[0][0]
  menor = Aux[0][1]
  for i in Aux:
    if(i[1] < menor):
      menor = i[1]
      Ruta = i[0]
  #print("La menor Ruta encontrada es:",Ruta,"\nCon un costo de:",menor)
  return Origen,Destino,menor,Ruta

def imprimirGrafo(Grafo):
  for i in Grafo:  
    print(i,":",Grafo[i])

def cargarArchivo():  
  metro = {}
  archivo = open("MetroCDMX.txt","r",encoding="utf-8")
  lineas = archivo.readlines()

  for i in lineas:
    if("#" not in i):
      aux = i.split("-")
      aux[1].replace("\n","")
      detalles = aux[1].split(":")
      #print(detalles)
      if(aux[0] not in metro):    
        metro[aux[0]]={str(detalles[0]):int(detalles[1])}    
      else:
        metro[aux[0]][str(detalles[0])]=int(detalles[1])
  archivo.close()
  return metro

def generarRegistros(metro):
  lista_estaciones1 = list(metro)
  lista_estaciones2 = list(metro)

  archivo = open("./Registros/Registros.txt","w",encoding="utf-8")

  for i in lista_estaciones1:
    for j in lista_estaciones2:
      if i != j:
        print("Calculando de:",i,"a",j)
        Origen,Destino,menor,Ruta = encontrarRMC_PorImpulso(metro,i,j)        
        registro = str(Origen)+"-"+str(Destino)+"-"+str(menor)+"-"+str(Ruta)+"\n"
        archivo.write(registro)
  archivo.close()
if __name__ == "__main__":
  metro = cargarArchivo()
  generarRegistros(metro)
  #encontrarRMC_PorImpulso(metro,"Nezahualcóyotl","Universidad")

    



