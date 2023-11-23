#Made by Roberto Ochoa Cuevas
#when hours worked are above 40, rate will be 1.5 of the original rate
hours = float(input('Enter Hours:'));
rate = float(input('Enter Rate:'));

if 40>hours:
    pay = hours * rate;
    print("pay: ", pay);
else:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5));
    print('pay:',pay);
