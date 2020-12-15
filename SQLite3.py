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



