import controller


def main():
    name = "test"
    mac = "00:00:00:00:00:00"
    print controller.get_device_by_mac(mac)

if __name__ == '__main__':
    main()
