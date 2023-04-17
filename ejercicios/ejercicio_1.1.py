promedio_video_editado = 4
video_editado_min = 2.5
video_editado_max = 7
curso_actual = 1.5

crudo_promedio = 5
crudo_actual = 3.5

diferencia_con_min = 100 - curso_actual / video_editado_min * 100
diferencia_con_max = 100 - curso_actual * 1000 // video_editado_max / 10
diferencia_con_promedio = 100 - curso_actual / promedio_video_editado * 100

tiempo_vacio_promedio = 100 - promedio_video_editado * 1000 // crudo_promedio / 10
tiempo_vacio_actual = 100 - curso_actual * 1000 // crudo_actual / 10

diferencia_diez_horas = promedio_video_editado * 100 // curso_actual / 10
diferencia_diez_horas_reverse = curso_actual * 100 // promedio_video_editado / 10

print(f'el curso actual dura un {diferencia_con_min}% menos que el más rapido')
print(f'el curso actual dura un {diferencia_con_max}% menos que el más lento')
print(f'el curso actual dura un {diferencia_con_promedio}% menos que el promedio')
print(f'un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'el curso actual elimina un {tiempo_vacio_actual}% de tiempo vacio')
print(f'10 horas de este curso equivalen a {diferencia_diez_horas} de otro curso')
print(f'10 horas de otro curso equivalen a {diferencia_diez_horas_reverse} de este')