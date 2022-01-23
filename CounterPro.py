class CounterPro:
  def __init__(self,llista):
    self.llista = llista
    self.diccionario = {}
  
  def __ordenar_lista__(self):
    self.llista.sort()
    return self.llista

#definimos una funcion privada de la clase cuyos parámetro es el numero que se quiere evaluar en la lista y contar las veces que se repite. Es por eso que retorna el valor acumulado.
  
  def __mirar_cantidad_numeros_acumulados__(self,numero_evaluado):
    acumulado = 0
    for e in self.llista:
      if e == numero_evaluado:
        acumulado += 1
    return acumulado

    
#Funcion privada de la classe que le entra el numero que se quiere evaluar y mediante con la implementacion del diccionario llamamos a la funcion de arriba para que ejecute la fase de el acumulado de cada numero. 
  
  def __agrega_numero_diccionario__(self,numero):
    if numero not in self.diccionario:
      self.diccionario[numero] = self.__mirar_cantidad_numeros_acumulados__(numero) / len(self.llista)* 100
    else:
      pass
    return self.diccionario

#Funcion publica que crea el diccionario llamando a la funcion anterior que llama a la vez a la anterior. Utilizamos un for va iterar con cada elemento de la lista y ejecutamos las funciones privadas.
  
  def __crear_diccionario__(self):
    self.__ordenar_lista__()
    for i in self.llista:
      self.__agrega_numero_diccionario__(i)
  
    return self.diccionario

#Finalmente, al acabar, con un for se itera con cada elemento de el diccionario y imprime cada apartado con el diccionario final incluïdo. También llama a la funcion crear diccionario para que se active el metodo de funcionamiento de  la clase. 
  
  def __str__(self):
    string = "["
    self.__crear_diccionario__()
    for e in self.diccionario:
      string += f"\n->El numero {e} ha aparecido {self.diccionario[e]} % de veces."
    string += "\n]"
    return string
  def retornar_diccionario(self):
    return self.diccionario
      
