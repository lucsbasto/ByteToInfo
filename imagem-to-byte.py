png = {};
file = open('imagem.png', 'rb');
data = open('teste.txt', 'wb');
text = file.readlines();
for i in text:
    data.write(i);
len_bytes = file.tell();
png['tamanho'] = len_bytes;
is_png = False;
for i in range(len_bytes):
    file.seek(i);
    oito_bytes = file.read(8);
    if oito_bytes == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": #8 primeiros bytes do PNG
        ihdr = file.read(8); #os 8 primeiros bytes depois da assinatura são do ihdr
        print (ihdr);
        width = file.read(4); #os 4 primeiros bytes depois do ihdr são da largura
        width = int.from_bytes(width, byteorder='big', signed=False);#converte de byte pra inteiro
        height=file.read(4);#os 4 primeiros bytes depois da largura são da altura
        height=int.from_bytes(height, byteorder='big', signed=False);
        png['tipo'] = 'PNG';
        png['width'] = width;
        png['height'] = height
data.close()
file.close()

print (png)