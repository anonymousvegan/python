import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="SHkola.debLinux20.04", database="nikola")
mycursor= mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
   print(i)
#ili : radi samo ako već nije ispisano
# rezultat=mycursor.fetchone # SAMO PRVI- ALI VALJDA SE MORA ISPISATI FOR LUPOM
#FECHALL() ĆE UZETI SVE.
#rezultat= mycursor.fetchall()
#for i in rezultat:
#  print(rezultat)