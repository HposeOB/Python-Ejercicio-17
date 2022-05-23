f =  open("hola.txt", "w")
f.write("Primer acceso""\n")
f.close()

f = open("hola.txt", "a")
f.write("Segundo acceso")
f.close()
print("Finalizado")
