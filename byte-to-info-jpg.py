jpg = {};
file = open('imagem.jpeg', 'rb');
bytes = bytes(file.read());
len_bytes = file.tell();
for i in range(len_bytes):
    file.seek(i);
    dois_bytes = file.read(2);
    if b'\xff\xd8' in dois_bytes:
        jpg['Tipo']='JPEG';
        jpg['Tamanho'] = len_bytes;
        marker = file.read(2); #marcação do jpeg que não sei pra que serve
        jpg['marker'] = marker
        lenght = int.from_bytes(file.read(2), byteorder='big', signed=False); #tamanho do segmento, que tb não sei o que é aeuhaeuhae
        jpg['tamanho do campo APP0'] = lenght
        identify = file.read(5);
        jpg['identificador'] = identify
        version = int.from_bytes(file.read(2), byteorder='big', signed=False);
        jpg['version'] = version
        unit = int.from_bytes(file.read(1), byteorder='big', signed=False);
        print (unit)
        height = int.from_bytes(file.read(2), byteorder='big', signed=False);
        print (height)
        width = int.from_bytes(file.read(2), byteorder='big', signed=False);
        print (width)
file.close()
print (jpg)
# {'tamanho': 348527, 'tipo': 'PNG', 'width': 580, 'height': 604, 'profundidade de bit': 8, 'tipo da cor': 6, 'metodo de filtro': 0}
