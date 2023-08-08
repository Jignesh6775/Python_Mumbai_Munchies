import json

conditions = True
sum = 0


def AddaSnack():
    id = int(input("Enter Snack id:"))
    name = input("Enter Snack name:")
    price = int(input("Enter Snack price:"))
    available = input("is this snack available?(yes/no):")
    with open("invent.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        arr.append(
            {
                "id": id,
                "name": name,
                "price": price,
                "available": available
            }
        )
        with open("invent.json", "w") as file:
            json.dump(arr, file)
    print("============================")
    print("Snacks added to the menu")
    print("============================")


def UpdateAva():
    itemID = int(input("Enter snacks id:"))
    with open("invent.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["id"] == itemID:
                item["available"] = "yes"
        with open("invent.json", "w") as file:
            json.dump(arr, file)
        print("============================")
        print("Snacks added to the menu")
        print("============================")


def Remove():
    id = int(input("Enter snack id to remove:"))
    with open("invent.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["id"] == id:
                arr.remove(item)
        with open("invent.json", "w") as file:
            json.dump(arr, file)

def SellSnack(sum):
    id = int(input("Enter snack id to sell:"))
    foodname=input("Enter food name:")
    name=input("Enter your name:")
    price=0
    with open("invent.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["name"] == foodname:
              price=item['price']
              sum+=price  
    with open("order.json","r")as file:
        content=file.read()
        arr=json.loads(content)
        arr.append({"orderid":id,"name":name,"price":price,"status":"pending"})
        with open("order.json", "w") as file:
            json.dump(arr, file)
    print("============================")
    print("Snacks sold successfully")
    print("============================")
    return sum


def getOrders():
    print("============================")
    print("Our Menu")
    print("============================")
    with open("invent.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["available"] == "no":
                continue
            else:
                print(f"id:-{item['id']} name:-{item['name']} price:-{item['price']}")


def UpdateStatus():
    id = input("Enter id to update status of snack:")
    change = input("enter that want to change:")
    with open("order.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item["id"] == id:
                item["status"] = change
        with open("order.json", "w") as file:
            json.dump(arr, file)
    print("============================")
    print("Snacks Status Updated successfully")
    print("============================")

def FilterByStatus():
    filter=input("Enter The status to get data:")
    with open("order.json", "r") as file:
        content = file.read()
        arr = json.loads(content)
        for item in arr:
            if item['status']==filter:
                print(f"orderid:-{item['orderid']}")
                print(f"name:-{item['name']}")
                print(f"price:-{item['price']}")
                print(f"status:-{item['status']}")
            print("=====================================")


while conditions:
    print("============================")
    print("============================")
    print(">>>>>>>>  Zomato Chronicles: The Great Food Fiasco  <<<<<<<<")
    print("============================")
    print("============================")
    print("1. Display Menu")
    print("2. Update Availability")
    print("3. Add a snack")
    print("4. Remove a Snack")
    print("5. Buy a Snack")
    print("6. Total Sale")
    print("7. Update Status of Snack")
    print("8. Filter by Status")
    userinput = int(input("Enter the Number to get Details:"))
    if userinput == 1:
        getOrders()
    elif userinput == 2:
        UpdateAva()
    elif userinput == 3:
        AddaSnack()
    elif userinput == 4:
        Remove()
    elif userinput == 5:
        sum+=SellSnack(sum)
    elif userinput == 6:
        print("============================")
        print(f"Total sale:- {sum}")
        print("============================")
    elif userinput==7:
        UpdateStatus()
    elif userinput==8:
        FilterByStatus()
    out = input("Do you want to Quit? (Y/N):")
    if out == "Y" or out == "y":
        conditions = False