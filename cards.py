class Card:
    def __init__(self, name, surname, mail, number):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.number = number

    def __repr__(self):
        return f"Card(name={self.name}, surname={self.surname}, mail={self.mail}, number={self.number})"
   


card_one=Card(name='Janusz', surname='Walczak', mail='jan.walczuk@.pl', number='+48 123098345')
card_two=Card(name='Tomasz', surname='Majewski', mail='tom.maj@pl', number='+48 123321122')
print(Card)


cardList=(card_one, card_two)
for cards in cardList:
    print(cards)

print('\n')

class BaseContact(Card):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    def contact(self):
        print(f"Wybieram numer {self.number} i dzwonię do {self.name} {self.surname}")
    
    def label_length(self):
        print(f"Liczba znaków {len(self.name)} {len(self.surname)}")

   

person_one = BaseContact(name='Adam', surname='Duda', mail='a.duda@qp.pl', number='+48 123334344')
paerson_one = BaseContact(name='Paweł', surname='Kowalczyk', mail='pako@gmail.com', number='+48 123001230')
person_three = BaseContact(name='Andrzej', surname='Nowacki', mail='nowa.a@mail.pl', number='+48 663445364')
print(person_one)
person_one.contact()
person_one.label_length()
person_three.label_length()


class BusinessContact(Card):
    def __init__(self, company, position, businessNum,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.businessNum = businessNum
    def contact(self):
        print(f"Wybieram numer {self.businessNum} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        print(f"Liczba znaków {len(self.name)} {len(self.surname)}")



staff_one = BusinessContact(name='Paweł', surname='Kowalczyk', mail='pako@gmail.com', number='+48 123001230',company='McDonalds', position='Menager', businessNum='+48 126653312')
staff_two = BusinessContact(name='Antoni', surname='Wolski', mail='anowol@.pl', number='+48 123332134', company='ITDev', position='Senior Developer', businessNum='+48 123433908')
staff_three = BusinessContact(name='Andrzej', surname='Nowacki', mail='nowa.a@mail.pl', number='+48 663445364', company='ITLog', position='Junior Specialist', businessNum='+48 122344566')
print(staff_one)
staff_one.contact()
staff_one.label_length
