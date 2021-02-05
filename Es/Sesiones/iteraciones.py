contador_interno = 0 
contador_externo = 0

while contador_externo < 5 : 
    print(contador_externo,contador_interno)
    contador_externo += 1 
    if contador_interno >= 3 : 
     break
    contador_interno += 1

