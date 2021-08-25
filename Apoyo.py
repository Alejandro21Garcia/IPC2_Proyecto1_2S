import xml.etree.ElementTree as ET


def abrirArchivo():
    try:
        xml_file = open('entrada.xml')#apertura
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            lst_plants = xml_data.findall('entrada')
            for plant in lst_plants:
                print(f"Nombre: {plant.find('entrada').text}")
                print("-------------------------------")
        else:
            print(False)
    except Exception as err:
        print("Error:", err)
    finally:
        xml_file.close()