students={}
while True:
    print("\n1.Add 2.Display 3.Search 4.Delete 5.Exit")
    ch=input("Choice: ")
    if ch=="1":
        n=input("Name: ")
        students[n]=input("Branch: ")
    elif ch=="2":
        print(students)
    elif ch=="3":
        n=input("Search Name: ")
        print(students.get(n,"Not Found"))
    elif ch=="4":
        n=input("Delete Name: ")
        students.pop(n,None)
    elif ch=="5":
        break
