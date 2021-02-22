from caesarcipher import CaesarCipher

def menu():
    try:
        file = input ("\nIngrese el nombre del archivo: ")
        with open(file,'r') as f:
            archivo =  f.read().replace('Ã±', '!9!')
            archivo = archivo.replace('Ã‘','!8!')
            print(archivo)
    except:
        print("Error con el archivo.\n")
    try:
        sl = input("\n1) Cifrar\n2) Descifrar \nIngrese seleccion -->: ")
        opt = int(sl)
    except ValueError:
        print("Opción Inválida\n")
    try:
        sl2 = input("\nIngrese el numero de posiciones deseado: ")
        rot = int(sl2)
    except ValueError as e:
        print("\nError: " + str(e))


    return archivo, rot, opt, file

def cifrado(file, posiciones):
    c = CaesarCipher(file, offset = posiciones)
    archivo_cifrado = c.encoded

    return archivo_cifrado

def descifrado(file, posiciones):

    d = CaesarCipher(file, offset = posiciones)
    archivo_descifrado = d.decoded

    return archivo_descifrado

def main():
    archivo, rot, opt, file = menu()
    if opt == 1:
        newfile = cifrado(archivo,rot)
        with open(file, 'w') as nf:
            nf.write(newfile)
        print("\nArchivo crifado exitosamente!")


    elif opt == 2:
        newfile = descifrado(archivo,rot)
        n = newfile.replace('!9!', 'Ã±')
        n = n.replace('!8!','Ã‘')
        with open(file, 'w') as nf:
            nf.write(n)
        print("\nArchivo descrifado exitosamente!")
    else:
        print("Entrada Invalida. Error.")

if __name__ == '__main__':
    main()
