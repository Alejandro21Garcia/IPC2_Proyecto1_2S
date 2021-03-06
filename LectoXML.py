import xml.etree.ElementTree as ET
from tkinter import filedialog, Tk
from ListaSimple import *
from os import path

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
        #texto = archivo.read()
        texto = archivo.name
        archivo.close()
        print("Lectura Exitosa\n")
        return texto


def mostrardatos():

    data = abrir()
    try:
        xml_file = open(data)#apertura
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            lst_datos = xml_data.findall('terreno' or 'TERRENO')

            for terrn in lst_datos:

                if terrn.tag == 'TERRENO' or terrn.tag == 'terreno':
                    print(terrn.get('nombre'))

                    for atrib in terrn:

                        if atrib.tag == 'DIMENSION':
                            print("\nDimensiones de la matriz: ")
                            print(f"m: {atrib.find('m').text}")
                            print(f"n: {atrib.find('n').text}")

                        if atrib.tag == 'posicioninicio':
                            print("\nPosiciones de inicio")
                            print(f"Inicio en  x: {atrib.find('x').text}")
                            print(f"Inicio en y: {atrib.find('y').text}")

                        if atrib.tag == 'posicionfin':
                            print("\nPosiciones de fin")
                            print(f"Fin en  x: {atrib.find('x').text}")
                            print(f"Fin en y: {atrib.find('y').text}")

                        """if atrib.tag == 'posicion':
                            print("\nPosicion ")
                            print(f"x: {atrib.get('x')}")
                            print(f"y: {atrib.get('y')}")
                            print(f"Gasto de combustible: {atrib.get('posicion')}")
                           # print(f"x: {atrib.get('x').text}")"""

                print("--------------------------------------------")
        else:
            print(False)
    except Exception as err:
        print("Error:", err)
    finally:
        xml_file.close()