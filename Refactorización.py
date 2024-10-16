def seleccionar_proceso():
    print('Seleccione el proceso que desea aplicar:')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')

    while True:
        num = input()
        try:
            num = int(num)
            if 1 <= num <= 3:
                return num
        except ValueError:
            pass
        print('Introduzca un número válido del 1 al 3')


def opciones(num):
    if num == 1:
        while True:
            point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: \n')
            try:
                point = int(point)
                if 1 <= point <= 5:
                    comentario = input('Por favor, introduzca un comentario: \n')
                    post = f'punto: {point} comentario: {comentario}'
                    file_pc = open("data.txt", 'a')
                    file_pc.write(f'{ post } \n')
                    file_pc.close()
                    break
                else:
                    pass
            except ValueError:
                pass
    elif num == 2:
        print('Resultados hasta la fecha.')
        read_file = open("data.txt", "r")
        print(read_file.read())
        read_file.close()
    elif num == 3:
        print('Finalizado')
        return False
    return True


while True:
  valor = seleccionar_proceso()
  if not opciones(valor):
    break