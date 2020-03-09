name = input('NAME: ')
age = int(input('AGE: '))

print('\n do you have any of these symptoms?')
fever = int(input('fever (0= no, 1= yes): '))
cough = int(input('cough (0= no, 1= yes): '))
sob = int(input('shortness of breath (0= no, 1= yes): '))
sore = int(input('sore throat or runny nose (0= no, 1= yes): '))
vomit = int(input('vomiting (0= no, 1= yes): '))
ill = int(input('diabetes, kidney, or heart disease (0= no, 1= yes): '))
epi = int(input('have you been in epidemic region, or in contact with person from that region in last 14 days (0= no, 1= yes): '))

risk = fever*2 + cough*2 + sob*2 + sore + vomit + ill

print(/n name)
if epi ==0:
    if risk > 4: 
        print("you don't have high risk of COVID 19, it's probably fever,")
    else: 
        print("you have some risk of COVID 19 infection,")
if epi ==1:
    if risk > 4: 
        print('you have risk of infection, you should wear surgical mask and be isolated until make the test')
    else:
        print("you don't have COVID 19 sign, but may you have risk because of epidemic region, ")