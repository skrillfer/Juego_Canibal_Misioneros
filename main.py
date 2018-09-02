import operaciones
mensaje = "En una orilla del río hay 3 misioneros y 3 caníbales. Disponen de una barca vacía para llegar al otro lado del río." + "\n- La barca solo puede transportar a 1 o 2 personas a la vez."+ "\n- La barca solo puede moverse con una persona dentro de la barca."+ "\n- En ningún momento pueden haber más misioneros que caníbales, ya que los caníbales se comerán a los misioneros. Cuenta el que esté en el bote."+"\n\n¿Cómo se gana y cómo se pierde?"+"\n- El jugador gana al llevar a todas las 6 personas a la otra orilla del río."+"\n- El jugador pierde al tener más caníbales que misioneros en un lado del río, ya que los caníbales se comerán a los misioneros y el juego terminará."


print(mensaje)
num_resta_canibal = 0
num_resta_misionero = 0

#Lado donde se encuentra el barco
lado_barco = 2 # 1 si es el lado izquierdo y 2 si es lado derecho

#Número de caníbales del lado izquierdo almacenado en una variable de tipo int.
num_Canibales_izquierdo=0
#Número de caníbales del lado derecho almacenado en una variable de tipo int.
num_Canibales_derecho=3
#Número de misioneros del lado izquierdo almacenado en una variable de tipo int.
num_Misioneros_izquierdo=0
#Número de misioneros del lado derecho almacenado en una variable de tipo int.
num_Misioneros_derecho=3
#Una variable de tipo int input llamada barco que lleve registro de los personajes que van en la barca
barco=0


while(not operaciones.esta_lleno_el_barco(barco)):
  GANA=operaciones.si_es_ganador(num_Canibales_izquierdo,num_Misioneros_izquierdo)
  if GANA:
    print("Juego Terminado")
    break;
  operaciones.mostrar_canibalymisioneros(num_Canibales_izquierdo,num_Misioneros_izquierdo,num_Canibales_derecho,num_Misioneros_derecho,lado_barco)

  mensaje_opciones =  "Ingresa el numero de la opcion que quieres realizar:"
  mensaje_opciones += "\n1. Seleccionar el numero de CANIBALES para subir al barco"
  mensaje_opciones += "\n2. Seleccionar el numero de MISIONEROS para subir al barco"

  print(mensaje_opciones)#imprimo el mensaje de opciones
  numero_ingresado = input()#pido que ingrese un numero

  while( numero_ingresado != "1" and numero_ingresado !="2"):
    print("el numero ingresado es incorrecto\n\n")
    print(mensaje_opciones)#imprimo el mensaje de opciones
    numero_ingresado = input()# vuelvo a pedir que ingrese un numero

  if numero_ingresado=="1":
    Hay=operaciones.ver_si_hay_canibales(lado_barco,num_Canibales_izquierdo,num_Canibales_derecho)
    if not Hay:
      print("\n>>Selecciona de nuevo, ya que no hay CANIBALES disponibles\n")
      continue
    # quiere seleccionar numero de canibales
    mensaje_opciones ="Ingresa la cantidad de CANIBALES a subir al barco:\n"
    print(mensaje_opciones)
    cantidad = input()
    #obtengo la cantidad de canibales dependiendo de que lado me encuentre
    cantidad_canibales = operaciones.obtener_canibales(lado_barco,num_Canibales_izquierdo,num_Canibales_derecho)
    
    #Verifico que la cantidad ingresada de CANIBALES es correcta
    cumple=operaciones.verificar_cantidad_ingresada(cantidad_canibales,cantidad)
    barco_lleno = operaciones.ver_si_barco_lleno(cantidad,barco)

    while(not cumple or  barco_lleno):
      # quiere seleccionar numero de canibales
      mensaje_opciones ="Ingresa la cantidad de CANIBALES a subir al barco"
      print(mensaje_opciones)
      cantidad = input()
      #obtengo la cantidad de canibales dependiendo de que lado me encuentre
      cantidad_canibales = operaciones.obtener_canibales(lado_barco,num_Canibales_izquierdo,num_Canibales_derecho)
      
      #Verifico que la cantidad ingresada de CANIBALES es correcta
      cumple=operaciones.verificar_cantidad_ingresada(cantidad_canibales,cantidad)
      barco_lleno = operaciones.ver_si_barco_lleno(cantidad,barco)

    #Mostrar los CANIBALES subidos en el barco
    num_resta_canibal = num_resta_canibal + int(cantidad)
    barco = barco + int(cantidad)
    print("En el Barco hay:" + cantidad + " CANIBALES listos para ser transportados\n")

    #_______________________________________________________________
    print("Deseas hacer el movimiento, de transladar los MISIONEROS/CANIBALES al otro LADO?\n")
    print("INGRESA LA PALABRA si PARA HACER EL MOVIMIENTO")
    print("INGRESA LA PALABRA no PARA COMENZAR DE NUEVO")
    print("INGRESA LA PALABRA me rindo PARA TERMINAR EL JUEGO")
    print("INGRESA LA PALABRA continuar PARA SEGUIR LLENANDO EL BARCO")

    palabra = input()

    if palabra == "si":
      if lado_barco == 2:
        #estoy del lado derecho y me muevo al lado izquierdo
        
        #RESTAR del lado derecho los valores
        num_Canibales_derecho  =  num_Canibales_derecho - num_resta_canibal
        num_Misioneros_derecho =  num_Misioneros_derecho - num_resta_misionero

        #SUMAR del lado izquierdo los valores
        num_Canibales_izquierdo  =  num_Canibales_izquierdo + num_resta_canibal
        num_Misioneros_izquierdo =  num_Misioneros_izquierdo + num_resta_misionero
      else:
        #estoy del lado izquierdo y me muevo al lado derecho
        
        #RESTAR del lado Izquierdo los valores
        num_Canibales_izquierdo  =  num_Canibales_izquierdo - num_resta_canibal
        num_Misioneros_izquierdo =  num_Misioneros_izquierdo - num_resta_misionero

        #SUMAR del lado Derecho los valores
        num_Canibales_derecho  =  num_Canibales_derecho + num_resta_canibal
        num_Misioneros_derecho =  num_Misioneros_derecho + num_resta_misionero

      #Verificar la cantidad de canibales y misioneros de ambos lados
      perdio=operaciones.ver_si_pierde(num_Canibales_izquierdo,num_Misioneros_izquierdo,num_Canibales_derecho,num_Misioneros_derecho
      )
      if perdio:
        print("Has perdido el juego\n")
        lado_barco=operaciones.hacer_cambio_lado(lado_barco)

        operaciones.mostrar_canibalymisioneros(num_Canibales_izquierdo,num_Misioneros_izquierdo,num_Canibales_derecho,num_Misioneros_derecho,lado_barco)

        exit()
      else:
        #Si no pierde entonces se debe hacer el cambio de lado de barco
        lado_barco=operaciones.hacer_cambio_lado(lado_barco)
        num_resta_canibal = 0
        num_resta_misionero = 0
        barco = 0
        continue
         
    elif palabra == "no":
      num_resta_canibal=0
      num_resta_misionero=0
      barco = 0
      continue
    elif palabra == "me rindo":
      exit()
    elif palabra == "continuar":
      continue
  else:
    Hay=operaciones.ver_si_hay_misioneros(lado_barco,num_Misioneros_izquierdo,num_Misioneros_derecho)
    if not Hay:
      print("\n>>Selecciona de nuevo, ya que no hay MISIONEROS disponibles\n")
      continue

    # quiere seleccionar numero de misioneros
    mensaje_opciones ="Ingresa la cantidad de MISIONEROS a subir al barco\n"
    print(mensaje_opciones)
    cantidad = input()
    #obtengo la cantidad de misioneros dependiendo de que lado me encuentre
    cantidad_misioneros = operaciones.obtener_misioneros(lado_barco,num_Misioneros_izquierdo,num_Misioneros_derecho)
    
    #Verifico que la cantidad ingresada de MISIONEROS es correcta
    cumple=operaciones.verificar_cantidad_ingresada(cantidad_misioneros,cantidad)
    barco_lleno = operaciones.ver_si_barco_lleno(cantidad,barco)

    while(not cumple or  barco_lleno):
      # quiere seleccionar numero de misioneros
      mensaje_opciones ="Ingresa la cantidad de MISIONEROS a subir al barco\n"
      print(mensaje_opciones)
      cantidad = input()
      #obtengo la cantidad de misioneros dependiendo de que lado me encuentre
      cantidad_misioneros = operaciones.obtener_misioneros(lado_barco,num_Misioneros_izquierdo,num_Misioneros_derecho)
      
      #Verifico que la cantidad ingresada de MISIONEROS es correcta
      cumple=operaciones.verificar_cantidad_ingresada(cantidad_misioneros,cantidad)
      barco_lleno = operaciones.ver_si_barco_lleno(cantidad,barco)
    
    #Mostrar los MISIONEROS subidos en el barco
    num_resta_misionero = num_resta_misionero + int(cantidad)
    barco = barco + int(cantidad)
    print("En el Barco hay:" + cantidad + " MISIONEROS listos para ser transportados\n")

    #_______________________________________________________________
    print("Deseas hacer el movimiento, de transladar los MISIONEROS/CANIBALES al otro LADO?\n")
    print("INGRESA LA PALABRA si PARA HACER EL MOVIMIENTO")
    print("INGRESA LA PALABRA no PARA COMENZAR DE NUEVO")
    print("INGRESA LA PALABRA me rindo PARA TERMINAR EL JUEGO")
    print("INGRESA LA PALABRA continuar PARA SEGUIR LLENANDO EL BARCO")

    palabra = input()

    if palabra == "si":
      if lado_barco == 2:
        #estoy del lado derecho y me muevo al lado izquierdo
        
        #RESTAR del lado derecho los valores
        num_Canibales_derecho  =  num_Canibales_derecho - num_resta_canibal
        num_Misioneros_derecho =  num_Misioneros_derecho - num_resta_misionero

        #SUMAR del lado izquierdo los valores
        num_Canibales_izquierdo  =  num_Canibales_izquierdo + num_resta_canibal
        num_Misioneros_izquierdo =  num_Misioneros_izquierdo + num_resta_misionero
      else:
        #estoy del lado izquierdo y me muevo al lado derecho
        
        #RESTAR del lado Izquierdo los valores
        num_Canibales_izquierdo  =  num_Canibales_izquierdo - num_resta_canibal
        num_Misioneros_izquierdo =  num_Misioneros_izquierdo - num_resta_misionero

        #SUMAR del lado Derecho los valores
        num_Canibales_derecho  =  num_Canibales_derecho + num_resta_canibal
        num_Misioneros_derecho =  num_Misioneros_derecho + num_resta_misionero

      #Verificar la cantidad de canibales y misioneros de ambos lados
      perdio=operaciones.ver_si_pierde(num_Canibales_izquierdo,num_Misioneros_izquierdo,num_Canibales_derecho,num_Misioneros_derecho
      )
      if perdio:
        print("Has perdido el juego\n")
        lado_barco=operaciones.hacer_cambio_lado(lado_barco)

        operaciones.mostrar_canibalymisioneros(num_Canibales_izquierdo,num_Misioneros_izquierdo,num_Canibales_derecho,num_Misioneros_derecho,lado_barco)

        exit()
      else:
        #Si no pierde entonces se debe hacer el cambio de lado de barco
        lado_barco=operaciones.hacer_cambio_lado(lado_barco)
        barco = 0 
        num_resta_canibal = 0
        num_resta_misionero = 0

        continue

    elif palabra == "no":
      num_resta_canibal=0
      num_resta_misionero=0
      barco = 0
      continue
    elif palabra == "me rindo":
      exit()
    elif palabra == "continuar":
      continue
