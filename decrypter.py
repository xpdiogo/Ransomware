import os                                                               # Importa a biblioteca para manipulação de arquivos do SO
import pyaes                                                            # Importa a biblioteca do python para criptografia e descriptografia

file_name = input("Digite o nome do arquivo a ser descriptografafo: ")  # A variável file_name recebe a entrada do usuário com o nome do arquivo para encriptar
file = open(file_name, "rb")                                            # É aberto o arquivo no método de leitura
file_data = file.read()                                                 # A variável file_data recebe o conteúdo do arquivo
file.close()                                                            # É fechado o arquivo

key = b"testeransomwares"                                               # A variável key recebe a chave de criptografia
aes = pyaes.AESModeOfOperationCTR(key)                                  # A variável aes recebe o resultado da criptografia do texto com a chave de criptografia
decrypt_data = aes.decrypt(file_data)                                   # A variável decrypt_data recebe a decriptação do conteúdo da variável file_data

os.remove(file_name)                                                    # O arquivo criptografado é excluído

new_file = "teste.txt"                                                  # A variável new_file recebe a variável file_name adicionado do texto .DADOCRIPTOGRAFADO
new_file = open(f'{new_file}', "wb")                                    # A variável new_file recebe, pelo método de escrita, o conteúdo de new_file
new_file.write(decrypt_data)                                            # O conteúdo da variável new_file é escrito da variável crypto_data
new_file.close()                                                        # É fechado o arquivo