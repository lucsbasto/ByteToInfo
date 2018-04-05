file = open('imagem.jpg', 'rb');
file1 = open('teste.txt', 'wb');
text = file.readlines();
for i in text:
    file1.write(i);
file1.close()
file.close()
