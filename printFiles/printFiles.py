#Made by: Roberto Ochoa Cuevas
fname = input('Enter file name: ');
print(fname)
try:
    fhand = open(fname);
    for line in fhand:
        line = line.upper().lstrip();
        print(line);
except:
    print('File not found :(')
    exit();