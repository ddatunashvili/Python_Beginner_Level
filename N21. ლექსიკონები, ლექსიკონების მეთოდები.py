'ლექსიკონები'
'ასოციაციური მასივები პროგრამირებაში არის ასოციაციური სიები პითონში'

"--------------------------------------------------"
#ცარიელი ლექსიკონი
d={}
print(type(d))
q=dict()
print(type(q))
'------------------------'
# ლექსიკონებში ინდექსირება არაა
# რომელი ქალაქი რომელი ქვეყნისაა ასოციაციურად
# სტრუქტურა {key:Value} {georgia-tbilisi}
'---------------------------------------------------------------'

d={'georgia':'tbilisi','usa': 'washington','england':'london'}
print(d)
print(len(d),"ramdenia") #რამდენი ელემენტია

c=dict(spain = "madrid")
print(c)

'c=dict(1="madrid") მოგვცემთ შეცდომას 1 იანის გამო'
q={1:"one",2:"two"}
print(q)

q=dict.fromkeys([1,2,3]) # მიაწვდის რამდენიმე გასაღებს
print(q)
q=dict.fromkeys([1,2,3], "numbers") # ყველა გასაღებს მნიშვნელობა მისცა "numbers"

'w={[1,2]:"test"}  [1,2]არ შეიძლება სიის გამოყენებაა, გასაღები უნდა იყოს უცვლადი'

print(d["georgia"]) # d გასაღებზე რა ასოციაციაა

'გასაღების დამატება'
d["italy"] = "Rome"
del d["usa"] # ამოიშლება წყვილი
print(d)

'გადაწერება'
d["england"] = "coventry" # ლონდონს მიაწერა მნიშვნელობა
print(d)
print("usa" in d) # არის ამერიკა d ში?
print("usa" not in d) # არ არის ამერიკა d ში?

'გამოტანა ციკლით(მნიშვნელობები)'
for i in d:
    print(i)
print("(wyvilebi)")
'გამოტანა ციკლით(წყვილები)'
for i in d:
    print(i, d[i]) # d[i] - d გასაღების i მნიშვნელობა ყოველ ჯერზე
print("---------------------")

q.clear()
print(q,"carieli")
print(d.get("italy"))  # გასაღებით გამოიტანს შესაბამის მნიშვნელობას
print(d.get("italy","not such key")) # თუ არარის ტექსტს დაწერს "not such key"

d.setdefault("Norway") # თუ არარის შექმნის
print(d)
d.setdefault("Norway","Oslo")  # თუ არცერთია შეიყვანს და მიამატებს, არ იმუშავა რადგან ძველი "norway" დაინახა
print(d)
d.setdefault("Sweden","Stokholm")
print(d)

d.pop("Norway") #წაშლის მნიშვნელობას გასაღების მიხედვით
print(d)
d.popitem() # შემთხვევით ამოიშლება
print(d)
print(d.keys()) #გამოიტანს გასაღებებს

print(d.values()) # გამოიტანს მნიშვნელობებს

print(d.items()) # წყვილებს გამოიტანს
'------------------------------------'
for i in d:
    print(i) # ყველა გასაღებს გამოიტანს

for key in d.keys():
    print(key) # ყველა გასაღები
for value in d.values():
    print(value) # ყველა მნიშვნელობა
for item in d.items():
    print(item) # ყველა წყვილი
for key, value in d.items():
    print(key, "->", value) # ყველა გასაღები და მნიშვნელობა
'------------------------------------'
word = "John Parker USA 5 4 3 5"
q={}
word = word.split() # დატიხრავს ელემენტებს და დააკვირდება დაშორებებს
print(word)
q["FName"] = word[0]
q["LName"] = word[1]
q["Country"] = word[2]
q["Marks"] = []
'ყველა დანარჩენი უნდა მოვათავსოთ გასაღებში ციკლით'
#            | მე-3 ელემენტიდან დაწყებული
for i in word[3:]:
    q["Marks"].append(int(i))

print(q)
