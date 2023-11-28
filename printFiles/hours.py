#Made by: Roberto Ochoa Cuevas

#fname = input('Enter file name: ');
fname = 'printFiles/mbox-short.txt'
count = 0;
hours = dict();
sorted_hours = list();

try:
    fhand = open(fname);
except:
    print('File not found :(')
    exit();

for line in fhand:
    line = line.lstrip();

    if line.startswith('From '):
        count = count + 1;
        #Separate the string and get the email
        str_line = line.split();
        fullHour = str_line[5];
        shortHour = fullHour.split(':')[0];
        hours[shortHour] = hours.get(shortHour,0) + 1;
#end of the loop and the if 
#Order the dictionary
for k,v in hours.items():
    sorted_hours.append((k,v));
sorted_hours = sorted(sorted_hours);

for k,v in sorted_hours:
    print(k,v)  