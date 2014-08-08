import MySQLdb
import datetime

from sql import update_statement, select_statement


def setup():
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='insidethehouse')
    return con


def teardown(con):
    con.commit()
    con.close()


def get_device_by_name(hostname):
    cursor = setup().cursor()
    table = "device"
    host_col = "hostname"
    get_statement = "SELECT * FROM {table} where {host_col} = '{hostname}';"\
                    .format(table=table, host_col=host_col, hostname=hostname)
    cursor.execute(get_statement)
    cursor.close()


def get_device_by_mac(mac_addr):
    cursor = setup().cursor()
    table = "device"
    mac_col = "mac"
    get_statement = select_statement.format(table=table,
                                            property='*',
                                            column=mac_col,
                                            value=mac_addr)
    cursor.execute(get_statement)
    device = cursor.fetchall()
    print get_statement
    print len(device)
    cursor.close()
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
    print insert_statement
    cursor.execute(insert_statement)
    cursor.close()
    teardown(con)


def set_time(mac):
    cursor = setup().cursor()
    table = "device"
    property = "startTime"
    mac_column = "mac"
    device = get_device_by_mac(mac)
    if device:
        set_statement = update_statement.format(table=table,
                                                property=property,
                                                column=mac_column,
                                                value=mac)
        cursor.execute(set_statement)
        cursor.close()


def get_history(mac):
    cursor = setup().cursor()
    table = "history"
    statement = select_statement.format(table=table)
    cursor.close()


def set_history(mac):
    cursor = setup().cursor()
    device_table = "device"
    history_table = "history"
    mac_column = "mac"

    statement = select_statement.format(table=device_table,
                                        property='id',
                                        column=mac_column,
                                        value=mac)
    id_ = cursor.execute(statement)

    statement = select_statement.format(table=device_table,
                                        property='startTime',
                                        column=mac_column,
                                        value=mac)
    start_time = cursor.execute(statement)

    statement = "INSERT INTO {table} (device_id, startTime, endTime) VALUES \
                ({id}, {start_time}, {end_time});"\
                .format(table=history_table,
                        id=id_,
                        start_time=start_time,
                        end_time=datetime.now())
    cursor.execute(statement)
    cursor.close()


def get_state():
    cursor = setup().cursor()
    cursor.close()


def set_state():
    cursor = setup().cursor()
    cursor.close()
