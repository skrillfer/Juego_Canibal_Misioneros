def mostrar_canibalymisioneros(num_CI,num_MI,num_CD,num_MD,lado):
  #num_CI = numero de canibales del lado izquierdo
  #num_MI = numero de misioneros del lado izquierdo
  #num_CD = numero de canibales del lado izquierdo
  #num_MD = numero de misioneros del lado izquierdo
  mensaje = "---------------------------------------------------------------\n"
  contador=0
  while (contador<num_CI):
    mensaje += "(C)"
    contador=contador+1
  
  contador=0
  while (contador<num_MI):
    mensaje += "(M)"
    contador=contador+1
  #_____________________________________
  mensaje +="\t\t\t\t\t\t"
  contador=0
  while (contador<num_CD):
    mensaje += "(C)"
    contador=contador+1

  contador=0
  while (contador<num_MD):
    mensaje += "(M)"
    contador=contador+1
  mensaje += "\n---------------------------------------------------------------\n"
  
  if lado==1:
    mensaje += "El barco se encuentra del lado IZQUIERDO\n"
    mensaje += "_______________________________________________________________\n"
    mensaje += "BARCO"
  else:
    mensaje += "El barco se encuentra del lado DERECHO\n"
    mensaje += "_______________________________________________________________\n"
    mensaje += "\t\t\t\t\t\t" + "BARCO"
  print(mensaje)


def verificar_cantidad_ingresada(total,ingresado):
  if int(ingresado) >= 1 and int(ingresado) <= 2:
    if int(ingresado) <= total:
      return True
  else:
    print(">>La cantidad ingresada solo puede ser 1 o 2\n")
    return False
  return False


def obtener_canibales(lado,CI,CD):
  #CI= Canibales del lado izquierdo
  #CD= Canibales del lado derecho
  if lado==1:
      return CI
  else:
      return CD

def obtener_misioneros(lado,MI,MD):
  #MI= Misioneros del lado izquierdo
  #MD= Misioneros del lado derecho
  if lado==1:
      return MI
  else:
      return MD


def ver_si_barco_lleno(cantidad,barco):
  if (barco==1 and int(cantidad)==1) or (barco==0 and int(cantidad)==2) or (barco==0 and int(cantidad)==1):
    return False
  else:
    print(">>En el barco solo caben 2 personas\n")
    return True

def esta_lleno_el_barco(barco):
  if barco == 2:
    return True
  else:
    return False

def ver_si_pierde(CI,MI,CD,MD):
  if  CI > MI and MI>0:
    print("Has perdido la cantidad de Canibales por la IZQUIERDA Supera a los Misioneros de la IZQUIERDA")
    return True
  elif  CD > MD and MD>0:
    print("Has perdido la cantidad de Canibales por la DERECHA Supera a los Misioneros de la DERECHA")
    return True
  else:
    return False

def hacer_cambio_lado(lado_barco):
  if lado_barco==1: #esta en el lado izquierdo pasara al lado derecho
    return 2
  else:
    #esta en el lado derecho pasara al lado izquierdo
    return 1

def ver_si_hay_misioneros(lado,MI,MD):
  if lado==1:
    if MI > 0:
      return True
    else:
      return False
  else:
    if MD > 0:
      return True
    else:
      return False

def ver_si_hay_canibales(lado,CI,CD):
  if lado==1:
    if CI > 0:
      return True
    else:
      return False
  else:
    if CD > 0:
      return True
    else:
      return False

def si_es_ganador(MI,CI):
  if MI ==3 and CI ==3:
    print("Has Ganado El Juego")
    return True
  else:
    return False
