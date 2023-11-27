#Made by: Roberto Ochoa Cuevas

fname = input('Enter file name: ');
count = 0;

try:
    fhand = open(fname);
    for line in fhand:
        line = line.lstrip();

        if line.startswith('From '):
            count = count + 1;
            #Separate the string and get the email
            str_line = line.split();
            print(str_line[1]);
    print("There were", count, "lines in the file with From as the first word")
except:
    print('File not found :(')
    exit();
