#create an array of customer dictionary
#Enter Customer (yes/No): y
#enter customer name: Derek Banas
#enter customer (yes/no): y
#enter customer name: sally smith
#enter customer (yes/no): n
'''Derek Banas
Sally Smith'''

dic = [ ]
while True:
    creatent = input("Enter Customer (yes/No): ")
    creatent = creatent[0].lower()

    if creatent == 'n':
        break

    else:
        fname, lname = input("Enter Custormer Name: ").split()

        dic.append({'fName': fname, 'lName':lname})


for c in dic:
    print(c['fName'], c['lName'])

        
 
