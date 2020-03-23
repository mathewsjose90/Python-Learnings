from string import Template

templ=Template("Hello ${name} , ${greeting} ,How are you doing")

wish1=templ.substitute(name="Mathews",greeting="Good Morning")
wish2=templ.substitute(name="XYZ",greeting="GM")
wish={'name':"John",'greeting':"Good night"}
wish3=templ.substitute(wish)
print(wish1)
print(wish2)
print(wish3)