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
        png['tipo'] = 'PNG'

data.close()
file.close()