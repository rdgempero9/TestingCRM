#Global Variable to store data
list_iD = []
list_name = []
list_address = []
list_age = []
list_mobile_no = []

#Global Functions to do any query or task
def add_customer(iD, name, address, age, mobile_no):
    list_iD.append(iD)
    list_name.append(name)
    list_address.append(address)
    list_age.append(age)
    list_mobile_no.append(mobile_no)

def cus_search(iD):
    i = list_iD.index(iD)
    name = list_name[i]
    address = list_address[i]
    age = list_age[i]
    mobile_no=list_mobile_no[i]
    details = "Name:{0}\nAddress:{1}\nAge:{2}\nMobile_Number:{3}".format(name,address,age,mobile_no)
    return details


while (True):
    print('1.Add Customer.\n2.Search Customer.\n3.Modify Customer.\n4.Delete Customer.\n5.Show Customer')
    ch = input('Enter Choice:')
    if ch == '1':
        iD = int(input("Enter ID:"))
        name = input("Enter Name:")
        address = input("Enter Address:")
        age = int(input("Enter Age:"))
        mobile_no = input("Enter Mobile Number:")
        add_customer(iD, name, address, age, mobile_no)
        print("Customer Added Successfully")
    elif ch == '2':
        iD=int(input("Enter ID:"))
        details = cus_search(iD)
        print(details)
    elif ch == '3':
        pass
    elif ch == '4':
        pass
    elif ch == '5':
        pass
    elif ch == '0':
        break
print(add_customer(iD, name, address, age, mobile_no))
