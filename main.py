from tkinter import filedialog, Tk
import os
import LectoXML



def menu():
    print('\n------------------------------------------------------------------------')
    print('Bienvenido al programa, por favor eliga una de las siguientes opciones')
    print('\n1. Cargar archivo de entrada')
    print('2. Procesar archivo')
    print('3. Escribir un archivo de salida')
    print('4. Mostrar datos del Estudiante')
    print('5. Generar Gráfica')
    print('6. Salir')
    opcion = input('Ingrese su opcion: ')
    return opcion
if __name__=='__main__':

    clear = lambda: os.system('cls')


    #txt = abrir()

    ciclo = True


    while (ciclo):

        opcion = menu()

        if opcion == "1":
            print('\nCargando archivo de entrada')
            datos = LectoXML.mostrardatos()

        elif opcion == "2":
            print('Procesar archivo')
           ## print(analizador(txt))


        elif opcion == "3":
            print('Escribir archivo de salida')

        elif opcion == "4":
            print('\nMostrar datos del Estudiante')
            print(">Alejandro José García Hernández"
                  "\n>201800939"
                  "\n>Introducción a la Programación y Computación 2 sección E"
                  "\n>Ingenieria en Ciencias y Sistemas"
                  "\n>4to Semestre")

        elif opcion == "5":
            print('Generar Gráfica')


        elif opcion == "4":
            print('\nProgrma Finalizado')


        elif opcion == "5":
            print('\nProgrma Finalizado')

        elif opcion == "6":
            print('\nProgrma Finalizado')
            ciclo = False


        else:
            print("Opcion no valida")
            clear()

