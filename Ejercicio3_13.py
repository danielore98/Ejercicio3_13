# Calculo de Calificaciones numericas y literales

#INICIO

print('Dame la calificacion: ', end="")
calificacion = float(input())


if(calificacion > 9.0):
    print("La calificación es A.")
elif (calificacion > 8.0):
    print("La calificación es B.")
elif (calificacion >= 7.5):
    print("La calificación es 7.5.")
else:
    print("La calificacion es R.")