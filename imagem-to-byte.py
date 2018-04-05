png = {};
file = open('imagem.png', 'rb');
data = open('teste.txt', 'wb');
text = file.readlines();
for i in text:
    data.write(i);
len_bytes = file.tell();
png['tamanho'] = len_bytes;
for i in range(len_bytes):
    file.seek(i);
    oito_bytes = file.read(8);
    if oito_bytes == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": #8 primeiros bytes do PNG
        ihdr = file.read(8); #os 8 primeiros bytes depois da assinatura são do ihdr
        width = int.from_bytes(file.read(4), byteorder='big', signed=False);#os 4 primeiros bytes depois do ihdr são da largura
        height=int.from_bytes(file.read(4), byteorder='big', signed=False);#os 4 primeiros bytes depois da largura são da altura
        deep_bit = int.from_bytes(file.read(1), byteorder='big', signed=False);#o 1 byte depois da altura é a profundidade do bit
        # 0, 2 ,3 ,4 e 6 são validos
        color_type = int.from_bytes(file.read(1), byteorder='big', signed=False);#o 1 bit depois da profundidade do bit é o tipo da cor
        filter_method = int.from_bytes(file.read(1), byteorder='big', signed=False);#o proximo big depois da profundidade é o filtro
        interlace_method = int.from_bytes(file.read(1), byteorder='big', signed=False);#metodo de enlace
        png['tipo'] = 'PNG';
        png['width'] = width;
        png['height'] = height
        png['profundidade de bit'] = deep_bit;
        png['tipo da cor'] = color_type;
        png['metodo de filtro'] = filter_method;
data.close()
file.close()

