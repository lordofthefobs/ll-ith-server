import MySQLdb

from sql import update_statement, select_statement


def setup():
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='insidethehouse')
    return con


def teardown(con):
    con.commit()
    con.close()


def get_device_by_name(hostname):
    con = setup()
    cursor = con.cursor()
    table = "device"
    host_col = "hostname"
    get_statement = select_statement.format(table=table,
                                            property='*',
                                            column=host_col,
                                            value=hostname)
    cursor.execute(get_statement)
    output = cursor.fetchall()
    device = sanitize(output)
    cursor.close()
    teardown(con)
    return device


def get_device_by_mac(mac_addr):
    con = setup()
    cursor = con.cursor()
    table = "device"
    mac_col = "mac"
    get_statement = select_statement.format(table=table,
                                            property='*',
                                            column=mac_col,
                                            value=mac_addr)
    cursor.execute(get_statement)
    output = cursor.fetchall()
    device = sanitize(output)
    cursor.close()
    teardown(con)
    return device


def add_hostname(hostname, mac):
    con = setup()
    cursor = con.cursor()
    table = "device"
    mac_column = "mac"
    hostname_column = "name"
    insert_statement =\
        "INSERT INTO {table} ({hostname_column}, {mac_column}) VALUES \
        ('{hostname}', '{mac_value}');".format(table=table,
                                               mac_column=mac_column,
                                               hostname_column=hostname_column,
                                               mac_value=mac,
                                               hostname=hostname)
    cursor.execute(insert_statement)
    cursor.close()
    teardown(con)


def set_time(mac, time):
    con = setup()
    cursor = con.cursor()
    table = "device"
    mac_column = "mac"
    time_column = "startTime"
    device = get_device_by_mac(mac)
    if device:
        set_statement = update_statement.format(table=table,
                                                property=time_column,
                                                value=time,
                                                column=mac_column,
                                                match=mac)
        cursor.execute(set_statement)
    cursor.close()
    teardown(con)


def get_history(mac):
    con = setup()
    cursor = con.cursor()
    table = "history"
    statement = select_statement.format(table=table)
    cursor.close()


def set_history(mac, time):
    con = setup()
    cursor = con.cursor()
    history_table = "history"

    # statement = select_statement.format(table=device_table,
    #                                     property='id',
    #                                     column=mac_column,
    #                                     value=mac)
    # cursor.execute(statement)
    # output = cursor.fetchall()
    device = get_device_by_mac(mac)
    id_ = device[0]

    # statement = select_statement.format(table=device_table,
    #                                     property='startTime',
    #                                     column=mac_column,
    #                                     value=mac)
    # start_time = cursor.execute(statement)
    start_time = device[4]

    statement = "INSERT INTO {table} (device_id, startTime, endTime) VALUES \
                ('{id}', '{start_time}', '{end_time}');"\
                .format(table=history_table,
                        id=id_,
                        start_time=start_time,
                        end_time=time)
    cursor.execute(statement)
    cursor.close()
    teardown(con)


def get_state():
    con = setup()
    cursor = con.cursor()
    cursor.close()


def set_state():
    con = setup()
    cursor = con.cursor()
    cursor.close()


def sanitize(input):
    if len(input) == 1:
        return input[0]
    else:
        return input
