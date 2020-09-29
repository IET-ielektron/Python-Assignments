from django.db import connection

#connect db and run the query
def get_emp_data():
    try:
        cursor = connection.cursor()
        myQuery = ("select * from demo.get_all_employees()".format())
        cursor.execute(myQuery)
        #list
        columns = [col[0] for col in cursor.description]
        #return converted list to dict
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()]
    except Exception as e:
        raise