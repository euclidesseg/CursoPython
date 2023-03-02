#Represa Hidroituango

#Entradas
nivelAgua = float(input("Ingrese el nivel de agua"));
#Proceso

if(nivelAgua <= 250 ):
    print(f"El sensor marca:{nivelAgua}, muy bajo..");
    
elif(nivelAgua > 250 and nivelAgua < 400):
    print(f"El sensor marca:{nivelAgua}, Operando normal..");
    
else:
    print(f"El sensor marca:{nivelAgua}, PELIGRO..");
    