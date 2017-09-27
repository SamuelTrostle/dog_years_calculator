#Samuel Trostle
import time
firstname = input("What is your first name?: ")
lastname = input("What is your last name?: ")
age = input("What is your age?: ")
dogage =  int(age)*7
print("barkulating your age...")
time.sleep(0.6)
print("...")
time.sleep(0.5)
print("Hi, " + firstname + " " + lastname + ", you may be " + age + " years old but in dog years you are " + str(dogage) + " old so get busy living!")
exit = input("Press any key to exit")
