'N20. სიმრავლეები და მათი მეთოდები'
# სიმრავლეები ერჩიან დუბლიკატებს და შლიან
#  მხოლოდ უნიკალურ ელემენტებს აჩერებს სიმრავლეში
# პოზიციები არეულადაა კონსოლში

a={1,2,"text",2}
print(a, " amoagdebs dublikats")
print(type(a), "seti nishnavs simravles")
'ცარიელი სიმრავლე'
b=set()
print(b)
c={} # ამას ლექსიკონი ქვია სხვარამეა
print(type(c))
d=set("text") # არეულად  აჩვენებს დუბლიკატს გააქრობს
print(d)
d=set(range(4))
d=set([1,2,3,]) # სიაში ვათავსებთ, სიას გამოიტანს და არა რიცხვებს
print(d)
'd=set([1,2],[3,4])' # ორი არგუმენტი არ შვრება
d.add("hi") # სიმრავლეს დაემატება hi
print(d)
d.add(3)
print("ar daemateba 3 iani radgan ukve aris")

d.update([4,5,6]) # ბევრ ელემენტს ჩაამატებს
print(d)
d.update("word") # დამარცვლით დაემატება
print(d)
print("ar dashalos")
d.add("word") # არ დაშალოს
print(d)
d.discard(5) # 5 წაშალა,ამოაგდო
print(d, "5 amoagdo")
d.remove(2) # წაშალა
print(d)
d.pop() # წაშლის შემთხვევითობით და გამოიტანს ცხრილს
print(d)
d.clear() # სულ წაშალა
print(d,"washlilia, carieli ")
d={1,2,3,4, " hi"}
print(len(d)) # დაითვლის
print(4 in d) # არი 4 d ში?
print(1 not in d) # არ არი 1 d ში?
a={1,2,3}
b={3,4,5}
'თანაკვეთა'
print(a&b, "tanakveta")
a &= b # a ში შეინახავს შედეგს  {3} და a გახდება {3}
print(a)
a={1,2,3}
b={3,4,5}
print(a, "= 1,2,3 Shevitane")
print(a.intersection(b),"tanakveta") # თანაკვეთა მეთოდი

print(a.intersection_update(b)," igive a &= b ( a={3})") # მეთოდი
print(a)
'გაერთიანება'
print(a|b, "gaertianeba")
print(a.union(b), " gaertianeba metodit")
print(b-a,"b-a(3,4,5 - 1,2,3)") # გამოაკლებს
print(a^a) # ა არ გვხვდება ბ ში ( საპირისპირო ელემენტები)
c={1,2,3}
print(a==c)
print(a<b) # ბ ში არის ა?
c={1,2,3,4}
print(a<c) # ც ში არის ა?

'ციკლი'
for i in d:
    print(i) # გამოიტანს ყველა d ელემენტს
