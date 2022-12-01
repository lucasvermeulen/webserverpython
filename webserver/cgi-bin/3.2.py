import cgi,cgitb
#Create instance of FieldStorage
get=cgi.FieldStorage()

#Getdatafromfields

tafel=get.getvalue('tafel')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello-SecondCGIProgram</title>")
print("</head>")
print("<body>")
for i in range(11):
    rek = int(tafel) * i
    print(rek)
print("</body>")
print("</html>")