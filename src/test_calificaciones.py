aciertos = int(input('Nº de aciertos: '))
errores = int(input('Nº de errores: '))
total_respuestas = int(input('Nº de respuestas: '))

def calcula_nota_cuestionario():
    
    nota = (((aciertos*10)/total_respuestas)-errores/50-total_respuestas)
    return nota 

calcula_nota_cuestionario()