#dictionary:-
thisdict= {"brand":"Maruti", "model":"Ciaz", "year": 2021}
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
print(thisdict.keys())
print(thisdict.values())

thisdict["year"] = 2019
print(thisdict)
thisdict.update({"year":2018})
print(thisdict)
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color":"blue"})
print(thisdict)
thisdict.pop("model")
print(thisdict)
del thisdict["color"]
print(thisdict)

mydict = thisdict.copy()
print(mydict)


def my_function(fname, lname):
    print(fname + " Hello, Welcome to a new programming language! " + lname)

my_function("Shrestha", "PYTHON")

#def my_funct(**fname):
    #print(" Hello, Welcome to a new programming language! " + fname["lname"])

#my_funct(fname="Shrestha", lname="PYTHON")

