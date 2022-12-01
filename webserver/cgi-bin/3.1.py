import cgi,cgitb
#Create instance of FieldStorage
get=cgi.FieldStorage()

#Getdatafromfields
first_name=get.getvalue('first_name')
last_name=get.getvalue('last_name')
hobby=get.getvalue('hobby')
vak=get.getvalue('vak')


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello-SecondCGIProgram</title>")
print("</head>")
print("<body>")
print("<h2>Welkom %s, leuk dat je %s als hobby hebt.</h2>"%(first_name, hobby))
if hobby==vak:
    print("<h2>Super dat je favoriete vak ook je hobby is!</h2>")
else:
    print("<h2>Je favoriete vak niet je hobby begrijp ik. Kunnen we daar iets aan doen?</h2>")


print("</body>")
print("</html>")