from threading import Thread
import time

def say_hello():
    while True:
        print("Hello ")
        time.sleep(1)

def main():
    print("Main Program Started")
    t=Thread(target=say_hello,daemon=True)
    t.start()
    print("Main Program Ended")

if __name__=="__main__":
    main()