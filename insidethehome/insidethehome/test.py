import controller
import datetime


def main():
    name = "test"
    mac = "00:00:00:00:00:00"
    time = datetime.datetime.now()
    print controller.set_history(mac, time)

if __name__ == '__main__':
    main()
