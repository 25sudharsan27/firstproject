itemp={'Soap':30,'Rice':50,'Oil':175,'Bread':26.5,'Jam':20}
oritem=[]
item={1:'Soap',2:'Rice',3:'Oil',4:'Bread',5:'Jam'}
i=0
print('List of items')
print('1.Soap-Rs.3class'
      '0\n2.Rice-Rs.50\n3.Oil-Rs.175')
print('4.Bread-Rs.26.5\n5.Jam-Rs.20\n6.Exit')
print('Enter your choice 1 to 5 for purchase and 6 for exit ')
t=int(input())
while((t>=1)and(t<=5)):
    i=i+1
    print('Number of  quantity required')
    n=int(input())
    t1=item[t]
    t2=itemp[t1]
    tc=n*t2
    oritem=oritem+[item[t],itemp[t1],n,tc]
    print('List of Items')
    print('1.Soap-Rs.30\n2.Rice-Rs.50\n3.Oil-Rs.175')
    print('4.Bread-Rs.26.5\n5.Jam-Rs.20\n6.Exit')
    print('Enter your choice 1 to 5 for purchase and 6 for exit ')
    t = int(input())
print("Retail Bill System")
print("---------------------------------------------")
print("Name \t Price \t Quantity \t Total")
print("---------------------------------------------")
ct=0
ind=0
for x in range(i):
    print("%s\t%0.2f\t\t%d\t\t%0.2f"%(oritem[ind],oritem[ind+1],oritem[ind+2],oritem[ind+3]))
    ct=ct+oritem[ind+3]
    ind=ind+4
print("---------------------------------------------")
print("Total Amount  %0.2f" % ct)