navdet = ["Naveen", "Kumar", "Balani"]
print(navdet)

#--------------

navdet = ["Naveen", "Kumar", "Balani", "Naveen"]
print(navdet)

#---------------

listlen = ["Naveen" , "Kumar"]
print(len(listlen))

#---------------

listdif1 = ["Naveen", "Kumar", "Balani"]
listdif2 = [1,2,3,6,9]
listdif3 = [True, False, True]

print(listdif1,type(listdif1), len(listdif1))
print(listdif2, type(listdif2),len(listdif2))
print(listdif3, type(listdif3),len(listdif3))

#---------------

doub_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(doub_list)


#---------------

aceslis = ["Iphone", "Samsung", "Oneplus"]
print(aceslis[2])

#---------------

endstrt = ["Naveen", "Kumar", "Balani"]
print(endstrt[-1]) #why it removes ""

rndwise = ["Naveen", "Kumar", "Balani"]
print(endstrt[1:-1])

#---------------

lislen_cw = ["When", "specifying", "a", "range,", "the", "return", "value", "will", "be", "a", "new", "list", "with", "the", "specified", "items."]
print(len(lislen_cw), "Words in this list") 
print(lislen_cw[4:12])

#---------------

NegInd = ["Negative", "indexing", "means", "starting", "from", "the", "end", "of", "the" ,"list"]
print(NegInd[-7:-3])

#---------------

detlist = ["Naveen", "Kumar", "Balani", "PECHS", "Karachi"]
if "Karachi" in detlist:
    print("Yes, He is from karachi")

#---------------

chnglist = ["Naveen", "Kumar", "Meghwar"]
chnglist[2] = "Balani"
print(chnglist)

#---------------

chngrng = ["This", "is", "a", "Book"]
chngrng[3:4] = ["Laptop"]
print(chngrng)

chngrng1 = ["Computer","Bag", "tablet","Smart Watch"]
chngrng1[1:2] =  ["Laptop", "Mobile"]
print(chngrng1)

#--------------

chngins = ["Naveen", "Kumar"]
chngins.insert(2,"Balani")
print(chngins)

#--------------

addli = ["Naven", "Kumar"]
addli.append("Balani")
print(addli)

#--------------

add = ["Naveen", "Balani"]
add.insert(1, "Kumar")
print(add)

#--------------

Naveen = ["Naveen", "Kumar", "Balani"]
for x in Naveen:
    print(x)
    
#--------------

Mobile = ["Samsung","Apple", "Xiaomi", "OnePlus", "Oppo", "Vivo", "Honor", "Motorola", "Realme"]
newmoblist = []

for a in Mobile:
    if "o" in a:
        newmoblist.append(a)    
print(newmoblist)

#--------------

Mobile_singal = ["Samsung","Apple", "Xiaomi", "OnePlus", "Oppo", "Vivo", "Honor", "Motorola", "Realme"]
newmobsing = [n for n in Mobile if "a" in n]
print(newmobsing)

#--------------

Veg = ["Potato", "Ash gourd", "Broccoli", "Cucumber", "Ginger"]

newveg = [x for x in Veg]

print(newveg)

#--------------

Veg_word = ["Potato", "Ash gourd", "Broccoli", "Cucumber", "Ginger"]

newvegword = [ 'hello ' + x for x in Veg]

print(newvegword)

#--------------

Fish  = ["Agnatha", "Chondrichthyes", "Osteichthyes", "Actinopterygii ", "Sarcopterygii "]

newfishlist = [x if x != "Chondrichthyes" else "Pisces" for x in Fish]

print(newfishlist)

#--------------

laplist = ["Dell", "Apple", "Asus", "Acer", "BP"]

laplist.sort()

print(laplist)


#numerically

numlist = [100, 50, 65, 82, 23]

numlist.sort()

print(numlist)

#Sort Descending

Uni = ["Qau", "Uaf", "Comsats", "Aku", "Pieas"]

Uni.sort(reverse = True)

print(Uni)

#--------------

def sortcus(a):
  return abs (a - 10)

cussort = [100, 50, 65, 82, 23]

cussort.sort(key = sortcus)

print(cussort)

#--------------

sortcap = ["pechs", "Naveen", "Balani", "kumar"]

sortcap.sort()

print(sortcap)

sortcap2 = ["mithi", "Chandani", "Mehtab", "cousin"]

sortcap3 = sortcap2.sort(key = str.lower)

print(sortcap2)

#--------------

Revsort = ["Naveen", "Kumar", "Balani", "Mithi"]

Revsort.reverse()

print(Revsort) 

#--------------

coplist = ["Ant", "call", "cat"]
copdlist = coplist.copy()
print(copdlist)

#--------------

uselit = ["Axe", "Bell", "Catch"]
madelit = list(uselit)
print(madelit)

#--------------

slic = ["Full", "access", "now"]
sliclis = slic[:]
print(sliclis)


#--------------

#--------------