from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "Fr@nco0784688102", "cooldb"), pool_pre_ping=True)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

employees_data =[
    {'name':'francis', 'email':'fracis_951@live.com', 'age':50},
    {'name':'moris', 'email':'moris_952@live.com','age':45},
    {'name':'john', 'email':'john_952@live.com', 'age':46},
    {'name':'doe', 'email':'doe_952@live.com','age':47},
    {'name':'jojo', 'email':'jojo_952@live.com', 'age':99}
]
for employee_data in employees_data:
    new_employee = Employee(name= employee_data['name'], email=employee_data['email'], age=employee_data['age'])
    session.add(new_employee)
session.commit()
employees = session.query(Employee).all()
for employee in employees:
    print(employee.id, employee.name, employee.email, employee.age)
session.close()

# import MySQLdb
# connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Fr@nco0784688102", db="cooldb", charset="utf8")
# cursor = connection.cursor()
# create_table = """
# CREATE TABLE IF NOT EXISTS users(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(50) UNIQUE NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     age INT
#     )
# """
# insert_data = """
# INSERT INTO users(username, email, age) VALUES 
# ('francis', 'francis_952@live.com', 49),
# ('moris', 'moris_952@live.com', 45),
# ('john', 'john_952@live.com', 46),
# ('doe', 'doe_952@live.com', 47),
# ('jojo', 'jojo_952@live.com', 99)
# """
# cursor.execute(create_table)
# cursor.execute(insert_data)
# connection.commit()
# select_data = """ SELECT * FROM users"""
# cursor.execute(select_data)
# users = cursor.fetchall()
# for user in users:
#     print(user)
# cursor.close()
# connection.close()
