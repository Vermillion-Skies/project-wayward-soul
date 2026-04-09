import Scripts
#Internal debugging tool, commenting will be minimum as all functions are explained in source code and docs
Scripts.screenclear()
print("----------")
print("Wayward Soul internal debug tool")
activeinput = 1
while activeinput == 1:
    print("----------")
    print("1) screenclear")
    print("2) savegame")
    print("3) loadgame")
    print("4) statcheck")
    print("5) checkcache")
    print("6) writecache")
    print("7) sprint")
    print("Q) quit")
    answer = str(input("Choice: "))
    if answer == str("1"):
        Scripts.screenclear()
        print("screenclear run successfully")
        pass
    elif answer == str("2"):
        print("This will erase any content in save.txt")
        answer2 = str(input("Continue? (y/n) "))
        if answer2 == str("y"):
            testlist = ["1", "2", "3", "4"]
            Scripts.savegame(testlist)
            print("File written correctly")
            pass
        else:
            pass
        pass
    elif answer == str("3"):
        varprint = Scripts.loadgame()
        print(varprint)
        print("File loaded successfully")
        pass
    elif answer == str("4"):
        x = int(input("Please input the minimum stat (integer): "))
        y = int(input("Please input the stat to check (integer): "))
        print(Scripts.statcheck(x, y))
        print("statcheck run successfully")
        pass
    elif answer == str("5"):
        x = int(input("Please input the cache value to check (integer): "))
        print(Scripts.checkcache(x))
        pass
    elif answer == str("6"):
        x = int(input("Please input the line to write to (integer): "))
        y = str(input("Please input the value to plant at this location: "))
        Scripts.writecache(x, y)
        print("Please check the cache file or run debug function 5 to verify success")
        pass
    elif answer == str("7"):
        x = str(input("Please type a string to to test "))
        Scripts.sprint(x)
        Scripts.sprint("sprint run successfully")
        pass
    elif answer == str("q"):
        quit()
    else:
        print("Improper input, try again")
        pass
    pass
