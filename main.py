from tkinter import filedialog, Tk
import os

def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo XML",
        initialdir = "./",
        filetypes = (
            ("Archivos XML", "*.xml"),
            ("Todos los archivos","*.*")
        )
    )

    if archivo is None:
        print("Error de lectura")
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print("Lectura Exitosa")
        return texto

def menu():
    print('\n------------------------------------------------------------------------')
    print('Bienvenido al programa, por favor eliga una de las siguientes opciones')
    print('\n1. Cargar archivo de entrada')
    print('2. Procesar archivo')
    print('3. Escribir un archivo de salida')
    print('4. Mostrar datos del Estudiante')
    print('3. Generar Gráfica')
    print('4. Salir')
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

            txt = abrir()
            if txt is not None:
                if txt == '':
                    print("Archivo vacio")
                else:
                    print(txt)
                 ##   print(analizador(txt))

            else:
                print("Vuelva a intentarlo por favor")


        elif opcion == "2":
            print('Procesar archivo')
           ## print(analizador(txt))


        elif opcion == "3":
            print('Escribir archivo de saida')

        elif opcion == "4":
            print('Mostrar datos del Estudiante')

        elif opcion == "5":
            print('Generar Gráfica')


        elif opcion == "4":
            print('\nProgrma Finalizado')
            input()
            ciclo = False

        else:
            print("Opcion no valida")
            clear()

