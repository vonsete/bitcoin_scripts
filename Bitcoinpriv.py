# -*- coding: utf-8 -*-

import hashlib # SHA-256 hash function
import bip32utils
import binascii

# 1. start with a 32-byte hexadecimal private key

privatekey = input("\nEnter the blockchain.info wallet 'priv:' key: ")


# 2. add prefix (80 = mainet, ef = testnet)
data = "80" + privatekey

# 3. add compression byte (optional)
data = data + "01"

# 4. add checksum (hash256 the prefix+data+checksum, then take the first 4 bytes)
print ("hash1: ")
hash1 = hashlib.sha256(bytes.fromhex(data)).digest() # convert hex string to raw bytes before hashing
print (hash1)
hash2 = hashlib.sha256(hash1).hexdigest() # return result as hex string
print ("hash2: " + hash2)
checksum = hash2[0:8] # checksum is the first 4 bytes
print ("checksum: " + checksum)
data = data + checksum # add checksum to the end of the data
print ("data: " + data)
# 5. set base58 characters
characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 6. convert hex data to integer so we can convert it to base58
i = int(data, 16)

# 7. create a buffer for holding the base58 string
base58 = ''

# 8. keep dividing the integer by 58 and taking the remainder to work out each base58 character
while i > 0:
  i, remainder = divmod(i, 58) # divide and get the remainder
  base58 = characters[remainder] + base58 # use the remainder to get the character, and add it to the start of the string

# note: during normal base58 encoding you convert leading 00 bytes in hex to 1s in base58, but leading zero bytes will not be present when creating a wif private key so we're skipping that step here

# 9. show result (wif private key)
print(base58) #=> L5EZftvrYaSudiozVRzTqLcHLNDoVn7H5HSfM9BAN6tMJX8oTWz6




# Clave privada cruda en formato hexadecimal (256 bits)

# Convertir la clave privada cruda a formato bytes utilizando binascii
private_key_bytes = binascii.unhexlify(privatekey)

# Crear la clave maestra BIP32 desde la clave privada cruda
root_key = bip32utils.BIP32Key.fromEntropy(private_key_bytes)

# Generar la clave privada extendida BIP32 (XPRV)
xprv = root_key.ExtendedKey()

# Imprimir la clave privada extendida BIP32 XPRV
print("XPRV (clave privada extendida):", xprv)


