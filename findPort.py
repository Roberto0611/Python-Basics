#Made by: Roberto Ochoa Cuevas

str = 'x-DSPAM-Confidence: 0.8475';

pos = str.find(':'); #18
port = float(str[pos+1:]);
print(port);