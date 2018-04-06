def getMarker():
    marker = file.read(2);
    return marker

def getLenght():
    lenght = int.from_bytes(file.read(2), byteorder='big', signed=False);
    return lenght

def getIdentify():
    identify = file.read(5);
    return identify

def getVersion():
    version = int.from_bytes(file.read(2), byteorder='big', signed=False);
    return version

jpg = {};
file = open('imagem.jpg', 'rb');
bytes = bytes(file.read());
len_bytes = file.tell();
for i in range(len_bytes):
    file.seek(i);
    dois_bytes = file.read(2);
    if b'\xff\xd8' in dois_bytes:
        
             
        marker = getMarker();
        lenght = getLenght();
        identify = getIdentify();
        version = getVersion();
        
        
        unit = int.from_bytes(file.read(1), byteorder='big', signed=False);
        
        jpg['Tipo']='JPEG';
        jpg['Tamanho'] = len_bytes;
        jpg['marker'] = marker
        jpg['tamanho do campo APP0'] = lenght
        jpg['identificador'] = identify
        jpg['version'] = version
       

file.close()
print (jpg)

