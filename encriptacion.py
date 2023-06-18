from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
import binascii
import re
def desencriptar_contraseña(ciphertext_hex, clave):
    # Convertir la clave de hexadecimal a bytes
    clave = binascii.unhexlify(clave)
    
    # Crear un objeto Cipher con el algoritmo AES en modo ECB
    cipher = Cipher(algorithms.AES(clave), modes.ECB(), backend=default_backend())
    
    # Obtener el desencriptador del objeto Cipher
    decryptor = cipher.decryptor()
    
    # Convertir el texto cifrado de hexadecimal a bytes
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    # Desencriptar el texto cifrado
    texto_plano = decryptor.update(ciphertext) + decryptor.finalize()
   
    # Devolver el resultado como una cadena de texto
    var1= texto_plano.decode("utf-8")
    var2= re.sub(r'\W+', '', var1)
  
    return var2

def convertir_a_hexadecimal(clave):
    # Convertir la clave de texto a bytes
    clave_bytes = clave.encode('utf-8')
    
    # Convertir los bytes a formato hexadecimal
    clave_hex = binascii.hexlify(clave_bytes)
    
    # Devolver la clave en formato hexadecimal como una cadena de texto
    return clave_hex.decode('utf-8')

def encriptar_contraseña(contraseña, clave):
    # Convertir la clave de hexadecimal a bytes
    clave = binascii.unhexlify(clave)
    
    # Rellenar la contraseña para que sea múltiplo de 16 bytes
    contraseña = contraseña.ljust(16, '\0')
    
    # Crear un objeto Cipher con el algoritmo AES en modo ECB
    cipher = Cipher(algorithms.AES(clave), modes.ECB(), backend=default_backend())
    
    # Obtener el encriptador del objeto Cipher
    encryptor = cipher.encryptor()
    
    # Encriptar la contraseña
    ciphertext = encryptor.update(contraseña.encode('utf-8')) + encryptor.finalize()
    
    # Devolver el resultado como una cadena de texto en formato hexadecimal
    return binascii.hexlify(ciphertext).decode('utf-8')