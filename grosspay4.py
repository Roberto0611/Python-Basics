#Made by Roberto Ochoa Cuevas
#Add a function call compute pay

#get variables with input

def computePay(hours,rate):
        if 40>hours:
            pay = hours * rate;
            print("pay: ", pay);
        else:
            pay = (40 * rate) + ((hours - 40) * (rate * 1.5));
            print('pay:',pay);

try:
    hours = float(input('Enter Hours:'));
    rate = float(input('Enter Rate:'));
    computePay(hours,rate);
except:
     print('Invalid input');



