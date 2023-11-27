#Made by: Roberto Ochoa Cuevas

#Ask for the file and stablish some variables
fname = input('Enter file name: ');
count = 0;
mails = [];

#Open the File and check if it exists
try:
    fhand = open(fname);
except FileNotFoundError:
    print('File not found :(')
    exit();

#Get every line of the txt file
for line in fhand:
        line = line.lstrip();

        #Check if the line start with From 
        if line.startswith('From '):
            #Separate the string and add the mails to an array
            str_line = line.split();
            mails.append(str_line[1]);

#Dictionary with all the elements in the array.
count = dict();
for mail in mails: 
    count[mail] = count.get(mail, 0) + 1;

#Get the most repeated
maxKey = None;
maxValue = None;

for key in count:
    if maxKey is None or count[key] > maxValue:
        maxKey = key;
        maxValue = count[key];
print(maxKey,maxValue)