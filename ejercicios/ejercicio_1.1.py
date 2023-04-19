promedio_video_editado = 4
video_editado_min = 2.5
video_editado_max = 7
curso_actual = 1.5

crudo_promedio = 5
crudo_actual = 3.5

diferencia_con_min = 100 - curso_actual / video_editado_min * 100
diferencia_con_max = 100 - curso_actual / video_editado_max * 100
diferencia_con_promedio = 100 - curso_actual / promedio_video_editado * 100

tiempo_vacio_promedio = 100 - promedio_video_editado / crudo_promedio * 100
tiempo_vacio_actual = 100 - curso_actual / crudo_actual * 100

diferencia_diez_horas = promedio_video_editado / curso_actual * 10
diferencia_diez_horas_reverse = curso_actual / promedio_video_editado * 10

print(f'el curso actual dura un {diferencia_con_min}% menos que el más rapido')
print(f'el curso actual dura un {round(diferencia_con_max, 1)}% menos que el más lento')
print(f'el curso actual dura un {diferencia_con_promedio}% menos que el promedio')
print(f'un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'el curso actual elimina un {round(tiempo_vacio_actual, 1)}% de tiempo vacio')
print(f'10 horas de este curso equivalen a {round(diferencia_diez_horas, 1)} de otro curso')
print(f'10 horas de otro curso equivalen a {round(diferencia_diez_horas_reverse, 1)} de este')