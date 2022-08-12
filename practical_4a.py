def function_list(a,b):
    for i in a:
        if i in b:
            print("True")
            break

a = input("Enter your first list: ")
b = input("Enter your second list: ")
function_list(a,b)
