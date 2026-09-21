import psycopg2
def get_connection():
    connection=psycopg2.connect(host="localhost", database="prepmate",user="postgres",
                                password="sms123",port="5432")
    return connection

if __name__ == "__main__":
    connection=get_connection()
    print("Database connected successfully!")
    connection.close()