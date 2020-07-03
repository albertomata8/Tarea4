# Tarea4
### Parte #1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

La modulación por desplazamiento de fase, conocida como BPSK es una modulación angular que varia la fase portadora entre un número determinado de valores discretos.
Se toman datos codificados en binario y los modula en forma de señales sinusoidales.Esta señal moduladora es una señal digital con un número de estados limitado.
En caso que el dato codificado sea 1, esto significa que la señal es sinosoidal sin desfase, en caso que el dato sea 0, la señal tendrá forma de un seno desplazado 90°.

El enunciado en este caso presenta un archivo con 10 mil datos codificados en binario y se solicita realizar una modulación BPSK. Se utilizó la libreria pandas para
importar los datos del documento externo. Se utilizó una frecuencia de 5000hz,se utilizaron 100 puntos de muestreo por periodo, por ende la frecuencia de muestreo que 
en este caso es la frecuencia de Nyquist equivale a 500kHz. Con esos datos, se creo un método el cual produce que si se encuentra un 1 se asigna un seno y en caso
contrario se asigna un seno negativo que equivale a un seno desplazado 90°. 

La señal modulada obtenida es:

<img src="./imagenes/Senalmodulada.png" width="400">
