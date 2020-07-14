def encontrarRMC_PorValor(grafo,Origen,Destino,Costo):
  if(Origen == Destino):
    print("Fin:",Destino,"Costo:",Costo)
  else:
    nodo = ""    
    aux = grafo.get(Origen)        

    if aux:
      menor = aux[list(aux.keys())[0]]
      nodo = list(aux.keys())[0]
      for i in aux:
        
        if(aux[i] < menor):                
          menor = aux[i]
          nodo = i
      Costo += menor
      print("Camino :",nodo,":",menor)
      encontrarRMC_PorValor(grafo,nodo,Destino,Costo)      

def encontrarRMC_PorImpulsoDEBUG(grafo,Origen,Destino,Costo,Ruta,Aux):
  #print("Actual:",Origen,"R:",Ruta)
  
  if(Origen == Destino):
    #print("Costo:",Costo,"Ruta",Ruta)
    #print("Ruta:",Ruta)        
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
  print("La menor Ruta encontrada es:",Ruta,"\nCon un costo de:",menor)

def imprimirGrafo(Grafo):
  for i in Grafo:  
    print(i,":",Grafo[i])

grafo = {
  "A":{"B":4,"D":2},
  "B":{"C":1},
  "C":{"A":15},
  "D":{"C":10,"E":2},
  "E":{"C":1}
}

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FProblema_del_camino_m%25C3%25A1s_corto&psig=AOvVaw08n1A-5A3BEERDx5JfzS2X&ust=1594793777833000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODI1r-MzOoCFQAAAAAdAAAAABAD
grafo2 = {
  "A":{"H":10,"D":2,"B":3,"C":5},
  "B":{"A":3,"H":6,"D":8,"G":6,"E":4,"C":5},
  "C":{"A":5,"B":5,"G":9,"F":7,"E":1},
  "D":{"H":14,"A":2,"B":8,"E":12},
  "E":{"C":1,"B":4,"D":12,"G":15},
  "F":{"H":9,"C":7},
  "G":{"H":3,"B":6,"C":9,"E":15},
  "H":{"A":10,"F":9,"B":6,"G":3,"D":14}
}

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
    

#imprimirGrafo(metro)

#encontrarRMC_PorValor(grafo,"A","C",0)
#encontrarRMC_PorImpulso(grafo2,"F","D")
encontrarRMC_PorImpulso(metro,"La Raza","San Lázaro")

    
    

