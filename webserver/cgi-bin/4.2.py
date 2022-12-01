import cgi,cgitb
from tabulate import tabulate
#Create instance of FieldStorage
get=cgi.FieldStorage()

#Getdatafromfields
roepnaam=get.getvalue('roepnaam')
tussenvoegsel=get.getvalue('tussenvoegsel')
achternaam=get.getvalue('achternaam')
geslacht=get.getvalue('geslacht')
vak=get.getvalue('vak')
klas=get.getvalue('klas')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello-SecondCGIProgram</title>")
print("</head>")
print("<body>")
print("welkom %s, leuk dat je het vak %s het leukst vindt!"%(roepnaam, vak))
print("<p>")

table = [[roepnaam, tussenvoegsel, achternaam], 
         [geslacht, vak, klas]]
    
print(tabulate(table, tablefmt='html'))

print("</body>")
print("</html>")


