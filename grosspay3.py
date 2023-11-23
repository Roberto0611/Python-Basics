#Made by Roberto Ochoa Cuevas
#Add try and except

#get variables with input
try:
    hours = float(input('Enter Hours:'));
    rate = float(input('Enter Rate:'));

    #pay calculation
    if 40>hours:
        pay = hours * rate;
        print("pay: ", pay);
    else:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5));
        print('pay:',pay);

except:
    print('Error, please enter numeric input');