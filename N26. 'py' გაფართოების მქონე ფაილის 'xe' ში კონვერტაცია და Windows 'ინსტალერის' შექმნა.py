'-------------------------------------------------------'
'-------------------------------------------------------'
'N26. "py" გაფართოების მქონე ფაილის "exe"-ში კონვერტაცია და Windows "ინსტალერის" შექმნა'
'პითონის გამშვების მომზადება windows ის თვის'
'-------------------------------------------------------'
# .exe ფაილის ბილდერის დაყენება
'pip install pyinstaller'
# პითონის განახლება
# c:\users\davit\appdata\local\programs\python\python38-32\python.exe -m pip install --upgrade pip'
'-------------------------------------------------------'
# how to run
'open cmd and write: pyinstaller ("file location directory")   '
'-------------------------------------------------------'
'DONE!!'
'-------------------------------------------------------'
'ჩემი დაწერილი პროგრამა'
#--------------------------------------------------------------------------------------------------------
# START
#--------------------------------------------------------------------------------------------------------
'------------------------------------------------------------------'
#                          starting
'------------------------------------------------------------------'

#ხმოვნებისა და თანხმოვნების დათვლა
წინადადება=input("sheiyvane teqsti: ")
#შეგვყავს ტექსტი
ხმოვნისდამთვლელი=0
#საწყისი ხმოვნების და თანხმოვნების კალათა ცარიელია
თანხმოვნისდამთვლელი=0
#ხმოვნების ჩამონათვალი ცვლადში
ხმოვნები=["ა","ი","ე","ო","უ","a","i","e","o","u"]
#წინადადება შეყავს
ნაბოზარი="ase kargad sad iswavle"
for ch in წინადადება:
    #ყოველთვის, როცა "ხმოვნებიდან" ვარდება ხმოვანი ტექსტშიო
    if ch.lower()in ხმოვნები:
        #ხმოვნისკალათას დაუმატე ყოველჯერზე 1
        ხმოვნისდამთვლელი=ხმოვნისდამთვლელი+1
    #სხვა შემთხვებაში თუ თანხმოვნებიაო
    else:
        #ყოველ შემოსულ თანხმოვანს აჯამებს
        თანხმოვნისდამთვლელი=თანხმოვნისდამთვლელი+1
        #თუ ტოლია გამოტოვე და "ნაბოზარი" გამოიტანე
    if თანხმოვნისდამთვლელი==ხმოვნისდამთვლელი:
        continue
        #თუ თანხმოვანია მეტი ხმოვნებზე დაწერე "რეებს იძახის ეს ნაბოზარი"
    if თანხმოვნისდამთვლელი>ხმოვნისდამთვლელი+1:
        ნაბოზარი="reebs idzaxis es nabozari"
        #თუ თანხმოვანია ნაკლებია ხმოვნებზე დაწერე "რეებს იძახის ეს ნაბოზარი"
    if 1+თანხმოვნისდამთვლელი<ხმოვნისდამთვლელი:
        ნაბოზარი="reebs idzaxis es nabozari"

#გამოაქვს დაჯამებული შედეგები
print(f'{თანხმოვნისდამთვლელი} tanxmovani.')
print(f'{ხმოვნისდამთვლელი}  ა xmovani.')
print(f'{ნაბოზარი}.')

'------------------------------------------------------------------'
#                         ending
'------------------------------------------------------------------'
#--------------------------------------------------------------------------------------------------------
# END
#--------------------------------------------------------------------------------------------------------
'ბილდერი'
# ტკინტერი
'-------------------------------------------------------'
from tkinter import * # უმარტივესი ფანჯრიანი პროგრამა
# ობიექტების ბაზა მთავარი ფანჯარა
root=Tk()
# წარწერა
label=Label(root, text="zdarova chemo dzmao !!")
label.pack()
root.mainloop()
'ამ კოდის შემთხვევაში ჯერ კონსოლი გაეშვება და მერე ფანჯარა'
'-------------------------------------------------------'
'ამ ერორს ასწორებს'
# pyinstaller --onefile -w (" my_program.py ")
'-------------------------------------------------------'
'ინსტალერის მომზადება ვინდოუსისათვის'
# საჭიროა პროგრამა NSIS
# საჭიროა პროგრამა დაიზიპოს Winrar
# installer based on .ZIP file და შევიტანოთ
# set modern
'-------------------------------------------------------'
# პროგრამის გამორთვას შეაჩერებს და დავინახავთ პასუხს და შემდეგ იხურება
#input()_ ის მეშვეობით
input()
