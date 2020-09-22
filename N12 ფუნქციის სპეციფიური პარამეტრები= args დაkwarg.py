'''
N12. ფუნქციის სპეციფიური პარამეტრები: *args და **kwargs
როგორ შეიძლება ფუნქციამ იცოდეს რამდენი არგუმენტი მიიღოს
'''
# თუ არგუმენტი print(test(name="test", age=22)), მაშინ ორი ფიფქი გვინდა ფუნქციაშ
def test(**kwargs):
    return kwargs
print("**kwargs")
print(test(name="test", age=22))
#  თუ print(test("test", 22)), მაშინ ერთი ფიფქი
def test(*kwargs):
    return kwargs
print("*kwargs")
print(test("test", 22))
'ან' #შეგვიძია ფიფქის გვერდით ნებისმიერი რამ მივუწეროთ
def test(*dato):
    return dato
print("*dato")
print(test("test", 22))
'----------------------------------------------------------------'
