import pyodbc

#DEFINE VARIABLES
server = "serwer" + "\SQLEXPRESS"
database = 'base'
username = 'user'
password = 'password'

#CONNECT
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#EXECUTE
komendasql="SELECT * FROM Fruits"
cursor.execute(komendasql)

#READ RESPONSE
res=cursor.fetchall()

#CHECK IF RESPONSE IS EMPTY OR NOT
if len(res)==0:
    print("No results. Maybe you should check your request?")
else:
    print(res)
    res=str(res)