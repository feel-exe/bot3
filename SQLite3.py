import sqlite3

def sqlite3_example_create_bd():
    #  Соединяемся с базой данных, если базы данных нет, то создается новая с таким именем
    con = sqlite3.connect('Py_db.db')

    # Создаем объект курсора
    cur = con.cursor()

    # Создаем таблицу если таболицы не существует
    cur.execute('CREATE TABLE IF NOT EXISTS core_fes(Well TEXT, '
                                                    'Sample TEXT, '    
                                                    'Porosity FLOAT, '   
                                                    'Swr FLOAT, '    
                                                    'Permeability Float)')


    # Добавляем данные в таблицу
    cur.execute('INSERT INTO core_fes VALUES ("Yellow snake creek", "Sample #666", 25.6, 38, 16)')

    # Подтверждаем внесение данных в таблицу
    con.commit()

    cur.close()
    con.close()


sqlite3_example_create_bd()


def print_data_2d(columns_name, data):
    print(columns_name)
    for line in data:
        print(line)
    print('number of lines in database table is ' + str(len(data)))

def sqlite3_simple_read_bd(data_base, table, column_name = None):
    con = sqlite3.connect('Py_db.db')

    cur = con.cursor()

    query_columns = 'pragma table_info('+table+')'

    cur.execute(query_columns)

    columns_description = cur.fetchall()

    columns_names = []

    for columns in columns_description:
        columns_names.append(columns[1])
    print(columns_names)



    if column_name is None:
        query = 'SELECT * FROM '+table
        cur.execute(query)
        data = cur.fetchall()

    else:
        # чтение построчно из БД
        query1 = 'SELECT'+column_name+' FROM ' + table
        cur.execute(query1)
        data = cur.fetchall()


    print_data_2d(columns_names, data)

    #cur.execute('SELECT Sample, Well, Porosity, Swr, Permeability FROM core_fes ORDER BY Well')
    #data = cur.fetchall()
    #cur.close()
    #con.close()


data_base = '/Py_db.db'
table = 'core_fes'
sqlite3_simple_read_bd(data_base, table, 'Sample')


