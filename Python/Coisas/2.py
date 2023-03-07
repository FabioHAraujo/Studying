# -*- coding: utf-8 -*-
# desenvolvido por Felipe Silva
# 09/08/2017
# 11:28 AM
print ("||#######################||")
print ("||###### SubWrite #######||")
print ("||#######################||")
print ("Digite # e de enter para sair")
print ("0) criar arquivo *.txt")
print ("1) editar arquivo")
opc = input("opção: ")
if opc == "0":
  nome = input("arquivo será: ")
  while 1:
    sub = str(input(""))
    if sub == "#":
      exit()
    else:
      subw = open(nome, "a")
      subw.writelines(sub)
      subw.write("\n")
      subw.close()
elif opc == "1":
  sub = input("arquivo: ")
  subw = open (sub, "r")
  txt = subw.readlines()
  for l in txt:
    print (l)
    subw.close()
    while 1:
      fl = open(sub, "a")
      edit = str(input(""))
      if edit == "#":
        fl.close()
        exit()
      else:
        fl.write("\n")
        fl.writelines(edit)
        fl.write("\n")
        fl.close()
else:
  print ("não entendi!")