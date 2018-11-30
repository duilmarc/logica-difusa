import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt



#arange (inicio,fin,paso)
temperatura = np.arange(0,100,1)
humedad = np.arange(0, 100, 1)


#fuzz.trimf(funcion a trabajar,[inicio,medio,fin]) de forma triangular

temperatura_baja = fuzz.trimf(temperatura, [0, 0, 10])
temperatura_media = fuzz.trimf(temperatura, [0, 25, 100])
temperatura_alta = fuzz.trimf(temperatura, [25, 100, 100])
humedad_bajo = fuzz.trimf(humedad, [0, 0, 25])
humedad_medio = fuzz.trimf(humedad, [0, 25, 100])
humedad_alta = fuzz.trimf(humedad, [50, 100, 100])

#Grafica de las Funciones
fig, (ax0, ax1,ax2 ) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(temperatura, temperatura_baja, 'r', linewidth=1.5, label='Baja')
ax0.plot(temperatura, temperatura_media, 'g', linewidth=1.5, label='Media')
ax0.plot(temperatura, temperatura_alta, 'b', linewidth=1.5, label='Alta')
ax0.set_title('Temperatura')
ax0.legend()

ax1.plot(humedad, humedad_bajo, 'r', linewidth=1.5, label='Sin Humedad')
ax1.plot(humedad, humedad_medio, 'g', linewidth=1.5, label='Normal')
ax1.plot(humedad, humedad_alta, 'b', linewidth=1.5, label='Muy Humedo')
ax1.set_title('Humedad')
ax1.legend()

r1= fuzz.classic_relation(temperatura,temperatura_alta)
print("R1 entre temperatura y temperatura baja")
print(r1)

r2=fuzz.classic_relation(humedad,humedad_alta)
print("R2 entre humedad y humedad alta")
print(r2)

print(' ')

composicion=fuzz.maxmin_composition(r1,r2)
print('COMPOSICION ENTRE R1 y R1')
print(composicion)

#probando operacion and
union = fuzz.fuzzy_or(temperatura,temperatura_alta,humedad,humedad_alta)


uni= union[0]
union_a_b= union[1]


ax2.plot(uni, union_a_b, 'b', linewidth=1.5, label='Union temperatura_alta Humedad_alta')
ax2.set_title('Union')
ax2.legend()
# desaparece los cuadros de arriba y derecha (mas kawaii)

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

fig, (ax ) = plt.subplots(nrows=1, figsize=(3, 3))

complemento= fuzz.fuzzy_not(temperatura_alta)
ax.plot(temperatura, complemento, 'R', linewidth=1.5, label='Complemento temperatura alta')
ax.set_title('Complemento')
ax.legend()

plt.tight_layout()
plt.show()