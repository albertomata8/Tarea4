# Tarea4
### Parte #1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

La modulación por desplazamiento de fase, conocida como BPSK es una modulación angular que varia la fase portadora entre un número determinado de valores discretos.
Se toman datos codificados en binario y los modula en forma de señales sinusoidales.Esta señal moduladora es una señal digital con un número de estados limitado.
En caso que el dato codificado sea 1, esto significa que la señal es sinosoidal sin desfase, en caso que el dato sea 0, la señal tendrá forma de un seno desplazado 180°.

El enunciado en este caso presenta un archivo con 10 mil datos codificados en binario y se solicita realizar una modulación BPSK. Se utilizó la libreria pandas para
importar los datos del documento externo. Se utilizó una frecuencia de 5000hz,se utilizaron 100 puntos de muestreo por periodo, por ende la frecuencia de muestreo que 
en este caso es la frecuencia de Nyquist equivale a 500kHz. Con esos datos, se creo un método el cual produce que si se encuentra un 1 se asigna un seno y en caso
contrario se asigna un seno negativo que equivale a un seno desplazado 180°. 

La señal modulada obtenida es:

<img src="./imagenes/Senalmodulada.png" width="400">

### Parte #2:Calcular la potencia promedio de la señal modulada generada

La potencia promedio se puede ver como:

<img src="./imagenes/potenciapromedio.png" width="400">

Por ende para calcuar la integral de la señal al cuadrado, dividida entre el doble de tiempo fue necesario utilizar la función integrate.trapz. Como resultado se 
obtuvo la potencia promedio de pp=0.49999999999999983


### Parte #3:Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 d3.
Primeramente se tiene que la relación señal-a-ruido esta dada por:

<img src="./imagenes/relaciondB.png" width="200">

Para simular un canal ruidoso desconocido, primeramente se utilizó esta relación de señal-a-ruido en cunjunto con la potencia promedio que se había obtenido en la parte anterior,ya que así se pudo obtener el parámetro de potencia del ruido para SNR. Con esta potencia se pudo obtener sigma mediante la función de numpy de np.sqrt. Se calculó el ruidp para -2dB, -1dB, 0dB, 1dB, 2dB y 3dB, cabe mencionar que dicho ruido se realizó mediante valores aleatorios con una distribucion normal. Se creó la señal Rx la cual es la suma de la señal modulada obtenida en la primera parte con el ruido obtenida en esta sección. 

Gráficando las señales para las distintas frecuencias en decibeles se obtiene:

<img src="./imagenes/-2.png" width="400"><img src="./imagenes/-1.png" width="400">
<img src="./imagenes/0.png" width="400"><img src="./imagenes/1.png" width="400">
<img src="./imagenes/2.png" width="400"><img src="./imagenes/3.png" width="400">

### Parte #4: Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

Aplicando el método de Welch, se logró calcular la densidad espectral de potencia.

La gráfica de la señal modulada sin ruido correspondería a:

<img src="./imagenes/inicial.4.png" width="400">

Las gráficas con ruido para cada SNR corresponden a:

<img src="./imagenes/-2.4.png" width="400"><img src="./imagenes/-1.4.png" width="400">
<img src="./imagenes/0.4.png" width="400"><img src="./imagenes/1.4.png" width="400">
<img src="./imagenes/2.4.png" width="400"><img src="./imagenes/3.4.png" width="400">

### Parte #5:Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

Para realizar la demodulación, fue necesario un análisis energético. Primeramente fue necesario calcular la energía de la onda original que vendría siendo la de la señal sinusoidal. Posteriormente se realizó la inicialización de bits recibidos utilizando la función np.zero. Para la decodificación de la señal  se calculó la 
energía Ep realizando la sumatoria del producto entre la señal Rx que posee ruido y la señal limpia.Si esta energía calculada resulta ser mayor de la energía de onda original dividida entre 1.5, entonces se le asignaba un 1 a la demodulación y por ende en caso contrario se le asignaba un 0.Cabe mencionar que se escogió que fuera de Estos datos se almacenaron dentro de una lista llamada bitsRx para posteriormente restar los datos originales con estos recién obtenidos y así hallar el error, osea los bits que no concuerdan. Estos errores se almacenan en la lista erroresBER. Para -2dB se obtuvo 17 errores, en 10000 bits, por ende una tasa de error 0.0017. Para -1dB se obtuvo 8 errores, en 10000 bits, por ende una tasa de error 0.0008.Para 0dB se obtuvo 1 error, en 10000 bits, por ende una tasa de error 0.0001. Para los casos de 1dB,2dB y 3dB no se obtuvieron errores en 100 bits por ende la tasa de error es de 0.

### Parte #6:Graficar BER versus SNR

Debido a los resultados se puede concluir que entre más dB se utilicen, menos errores se presentarán. La gráfica de BER vs SNR corresponde a :

<img src="./imagenes/BER.png" width="400">
