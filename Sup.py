import os

def display_menu():
    print("Select the desired option:")
    print("1 - Bomber")
    print("2 - Download YouTube")
    print("3 - DDoS")
    print("4 - Facebook Downloader")
    

def run_script(choice):
    if choice == '1':
        os.system('python Bomber.py')
    elif choice == '2':
        os.system('python Download-YouTube.py')
    elif choice == '3':
        os.system('python DDoS.py')  
    elif choice == '4':
        os.system('python Facebook-Downloader.py')  
    elif choice == '0':
        print("خروج از برنامه...")
        exit()
    else:
        print("invalid")

while True:
    display_menu()
    choice = input("انتخاب شما: ")
    run_script(choice)
