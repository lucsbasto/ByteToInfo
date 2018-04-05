def getWidth():
    width = int.from_bytes(file.read(4), byteorder='big', signed=False)
    return width

def getHeight():
    height=int.from_bytes(file.read(4), byteorder='big', signed=False);
    return height

def getProfundidadeDeBits():
    deep_bit = int.from_bytes(file.read(1), byteorder='big', signed=False);
    return deep_bit

def getTipoDeCor():
    color_type = int.from_bytes(file.read(1), byteorder='big', signed=False);
    return color_type

def getMetodoDeFiltro():
    filter_method = int.from_bytes(file.read(1), byteorder='big', signed=False);
    return filter_method
    

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
    if oito_bytes == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": 
        ihdr = file.read(8);
        width = getWidth()
        height = getHeight();
        deep_bit = getProfundidadeDeBits();
        color_type = getTipoDeCor();
        filter_method = getMetodoDeFiltro();
        interlace_method = int.from_bytes(file.read(1), byteorder='big', signed=False);#metodo de enlace
        png['Tipo'] = 'PNG';
        png['Largura'] = width;
        png['Altura'] = height
        png['profundidade de bits'] = deep_bit;
        png['Tipo da cor'] = color_type;
        png['Metodo de filtro'] = filter_method;
        
print (png);
data.close()
file.close()
