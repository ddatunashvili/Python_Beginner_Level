
# ყველა l  ასოს გამოტოვებს წინადადებაში
for i in "hello,world!":
    'l ასოებს ამოაგდებს'
    if i =="l":
        'მიმდინარე ნაბიჯი გამოტოვე(l არ გამოიტანო)'
        continue

    print(i,end="")


#-----------------------------------
# w ასოსთან შეწყვეტს წინადადებას ან სიტყვას
for i in "hello,world!":
    'w ასოსთან შეჩერდება'
    if i =="w":
        'შეაჩერე პროცესი'
        break

    print(i,end="")
#-----------------------------------
# თუ ა ასო არის შეჩერდება სხვა შემთხვევაში დაწერს რომ არარის
for i in "hello,world!":
    'a ასოსთან შეჩერდება'
    if i =="a":
        'შეაჩერე პროცესი'
        break
#წინააღმდეგ შემთხვევაში
else:

    print("ა არარის წინადადებაში")
#-----------------------------------
