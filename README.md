Propósito de la Asignación de la Serie de Gramática Básica de Python
Las asignaciones de series son para determinar si ha logrado los objetivos de la serie.

Objetivos de la serie Gramática básica de Python

Ser capaz de escribir programas comprendiendo los objetos del mundo de Python
Aprenda gramática y métodos básicos que le servirán de base para adentrarse en el desarrollo a gran escala.
3. Problema: dividamos el programa del tablón de anuncios en métodos
Modifiquemos el programa anterior y dividámoslo en métodos.

El código anterior es el siguiente.

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    num = input()
    
    if num.isdecimal():
        num = int(num)
        if num == 1:
            while True:
                print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                point = input()
                
                if point.isdecimal():
                    point = int(point)
                    
                    if point <= 0 or point > 5:  # Expresión condicional que verifica si es menor que 0 o mayor que 5
                        print('Indíquelo en una escala de 1 a 5')
                    else:
                        print('Por favor, introduzca un comentario')
                        comment = input()
                        post = f'punto: {point} comentario: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write(f'{ post } \n')
                        file_pc.close()
                        break
                else:
                    print('Por favor, introduzca la puntuación en números')
        
        elif num == 2:
            print('Resultados hasta la fecha.')
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
        
        elif num == 3:
            print('Finalizando')
            break  # Sentencia para finalizar el procesamiento
        
        else:
            print('Introduzca un número del 1 al 3')
    else:
        print('Introduzca un número del 1 al 3')
 
¿Dónde recortar como método?
Todo el código consiste en sentencias if, pero el código es largo, con sentencias condicionales dentro de sentencias condicionales.

Para que la sentencia if sea más fácil de entender, reorganicémosla de la siguiente manera.

if num == 1:
    # llamada al método
elif num == 2:
    # llamada al método
elif num == 3:
    print('Finalizando')
    break
else:
    print('Introduzca un número del 1 al 3')
 
Piense en un nombre que facilite la comprensión del tipo de procesamiento que está realizando, defina un método y llámelo.

4. Requisitos de aprobación
Hay que definir nuevos métodos y dividir el proceso.
Los nombres de los métodos deben nombrarse en relación con el proceso.
Cuando se introduce una opción distinta de 1 a 3 para la selección del proceso a realizar, aparece el mensaje "Por favor, introduzca del 1 a 3" y se ejecutará el proceso para volver a realizar la elección.
Si se introduce un valor distinto de 1 a 5 para un punto de valoración, aparece el mensaje "Por favor, introduzca un valor entre el 1 y 5" y se ejecutará el proceso para que el usuario introduzca de nuevo el punto de valoración.
Poder introducir puntos de evaluación y comentarios.
Poder comprobar los resultados hasta la fecha.
Poder finalizar el proceso.
5. Método de presentación.
Envía la URL del repositorio de GitHub.
