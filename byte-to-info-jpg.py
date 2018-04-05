jpg = {};
file = open('imagem.jpg', 'rb');
data = open('teste.txt', 'wb');
text = file.readlines();
for i in text:
    data.write(i);
len_bytes = file.tell();
dois_bytes = file.read(10);
file.seek(0);
print (text)
for i in range(len_bytes):
    file.seek(i);
    quatro_bytes = file.read(2);
    if b'\xff\xd8' in quatro_bytes:
        jpg['Tipo']='JPEG';
        jpg['Tamanho'] = len_bytes;
        marker = int.from_bytes(file.read(2), byteorder='big', signed=False); #marcação do jpeg que não sei pra que serve
        lenght = int.from_bytes(file.read(2), byteorder='big', signed=False); #tamanho do segmento, que tb não sei o que é aeuhaeuhae
        identify = file.read(5) #int.from_bytes(file.read(5), byteorder='big', signed=False); # pegando o identificador => JFIF
        version = int.from_bytes(file.read(2), byteorder='big', signed=False); #versão do JFIF


data.close()
file.close()
print (jpg)
# {'tamanho': 348527, 'tipo': 'PNG', 'width': 580, 'height': 604, 'profundidade de bit': 8, 'tipo da cor': 6, 'metodo de filtro': 0}
