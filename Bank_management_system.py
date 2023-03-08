import mysql.connector
mysql.connector.connect(host= 'localhost', user = 'root', password = 8839, port = 3306, database = 'Bank_management')

def OpenAcc():
    name = input("Enter your name: ")
    acc = input("Enter the Account Number: ")
    dob = input("Enter the Date of Birth: ")
    add = input("Enter the address: ")
    cont = int(input("Enter the Contact Number: "))
    ob = int(input("Enter the opening balance: "))
    data1 = (name, acc, dob, add, cont, ob)
    data2 = (namd, acc, ob)
    sql1 = ('Insert into account values (%s, %s, %s, %s, %s, %s)')
    sql2 = ('Insert into amount values (%s, %s, %s)')
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data entered successfully")
    main()

def DepoAmount():
    amount = input("Enter the amount you want to deposit: ")
    acc = input("Enter the Account Number: ")
    a = 'select balance from amount where AccNo=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] + amount
    sql = 'Update amount set balance where AccNo = %s'
    d = (t, sql)
    x.execute(sql, d)
    mydb.commit()
    main()


def WithdrwAmount():
    amount = input("Enter the amount you want to deposit: ")
    acc = input("Enter the Account Number: ")
    a = 'select balance from amount where AccNo=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = 'Update amount set balance where AccNo = %s'
    d = (t, sql)
    x.execute(sql, d)
    mydb.commit()
    main()


def BalEnq():
    acc = input("Enter the Account Number: ")
    a = 'select * from balance where AccNo=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("The balance for acc:", acc, "is", result[-1])
    main()


def DisCusDetails():
    acc = input("Enter the Account Number: ")
    a = 'select * from account where AccNo=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()


def CloseAcc():
    acc = input("Enter the Account Number: ")
    sql1 = 'delete from account where AccNo=%s'
    sql2 = 'delete from account where AcNo=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    main()

def main():
    print('''
                      1. OPEN NEW ACCOUNT
                      2. DEPOSIT AMOUNT
                      3. WITHDRAW AMOUNT
                      4. BALANCE ENQUIRY
                      5. DISPLAY CUSTOMER DETAILS
                      6. CLOSE AN ACCOUNT''')
    choice = input("Select an option: ")
    if (choice == '1'):
        OpenAcc()
    elif (choice == '2'):
        DepoAmount()
    elif (choice == '3'):
        WithdrwAmount()
    elif (choice == '4'):
        BalEnq()
    elif (choice == '5'):
        DisCusDetails()
    elif (choice == '6'):
        CloseAcc()
    else:
        print("Invalid Input. Please try again.")
        main()

main()

OpenAcc()
