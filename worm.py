#!/usr/bin/python3

# worm v1.0, Author @guguvk (Axel González)

import shutil, sys, signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

if len(sys.argv) < 2:
    print(f"\n[!]Uso: python3 {sys.argv[0]} numero de copias")
    sys.exit(0)
try:
    counter = int(sys.argv[1])
    while counter > 0:
        #Nombre del archivo a copiar y el nombre al que sera copiado
        shutil.copy(sys.argv[0],"copia"+str(counter))
        counter-=1
except ValueError:
    print("\nTIENE QUE SER NUMERO OBLIGATORIAMENTE")
