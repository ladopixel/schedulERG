def borraLaPantalla():
    return '\033[2J\033[1;1f'

def finColor():
    return '\033[0;m'

def escribirNegro(texto):
    return '\033[1;30m' + texto + '\033[0;m'

def escribirRojo(texto):
    return '\033[1;31m' + texto + '\033[0;m'
def escribirRojoOpacidad(texto):
    return '\033[2;31m' + texto + '\033[0;m'

def escribirVerde(texto):
    return '\033[1;32m' + texto + '\033[0;m'
def escribirVerdeOpacidad(texto):
    return '\033[2;32m' + texto + '\033[0;m'

def escribirAmarillo(texto):
    return '\033[1;33m' + texto + '\033[0;m'
def escribirAmarilloOpacidad(texto):
    return '\033[2;33m' + texto + '\033[0;m'

def escribirAzul(texto):
    return '\033[1;34m' + texto + '\033[0;m'
def escribirAzulOpacidad(texto):
    return '\033[2;34m' + texto + '\033[0;m'

def escribirMorado(texto):
    return '\033[1;35m' + texto + '\033[0;m'
def escribirMoradoOpacidad(texto):
    return '\033[2;35m' + texto + '\033[0;m'

def escribirCian(texto):
    return '\033[1;36m' + texto + '\033[0;m'
def escribirCianOpacidad(texto):
    return '\033[2;36m' + texto + '\033[0;m'

def escribirBlanco(texto):
    return '\033[1;37m' + texto + '\033[0;m'
def escribirBlancoOpacidad(texto):
    return '\033[2;37m' + texto + '\033[0;m'