from werkzeug.security import generate_password_hash
from database import get_connection
name=input("enter admin name:")
email=input("enter admin email:")
password=input("enter admin password:")
hashed_password=generate_password_hash(password)
connection=get_connection()
cursor=connection.cursor()
cursor.execute("insert into admins (name,email,password) values (%s,%s,%s)",(name,email,hashed_password))
connection.commit()
cursor.close()
connection.close()
print("admin created successfully!")