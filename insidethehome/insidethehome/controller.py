import MySQLdb


def setup():
    con = MySQLdb.connect('localhost', 'root', 'root', 'wemodb')
    return con.cursor()


def add_hostname(hostname, mac):
    cursor = setup()
    table = "mac_addr"
    mac_column = "mac"
    hostname_column = "hostname"
    insert_statement =\
        "INSERT INTO {table} ({mac_column}, {hostname_column}) VALUES ({mac_value},{hostname});"\
        .format(table=table,
                mac_column=mac_column,
                hostname_column=hostname_column,
                mac=mac,
                hostname=hostname)
    cursor.execute(insert_statement)
    cursor.close()

def 
