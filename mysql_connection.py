import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host='yhdb.c8nbdutl9vtz.ap-northeast-2.rds.amazonaws.com',
        database='recipe_db',
        user='recipe_user1234',
        password='recipe1234' )
    return connection