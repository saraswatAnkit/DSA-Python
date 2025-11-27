# Simple Recurrsion Program

count = 0

def func():
    global count
    if count == 4:
        return
    print("Ankit Saraswat")
    count += 1
    func()

func()