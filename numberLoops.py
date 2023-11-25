#Made by: Roberto Ochoa Cuevas
#Print total, Count and average.

#Set variables
total = 0;
count = 0;
current_input = None;

#While loop
while True:
    current_input = input("Enter a number (or 'done' to quit): "); #Ask number
    #Ask if the input is done to break
    if current_input != 'done':
        try:
            total = total + float(current_input);
            count = count + 1;
        except:
            print("Invalid input");
    else:
        print(total, count, (total/count)) #Print total, count, average
        break;
