def print_hi(name):
    print(f'Hi, {name}')



if __name__ == '__main__':
    print_hi('PyCharm')



def emailIsValid():
    return True


class Guide:
    wordbook = {}

    # ['email'] = ['имя','фамилия','телефон','город']

    def addNote(self, email, name, secName, number, city):
        if email not in self.wordbook.keys():
            if (emailIsValid):
                self.wordbook[email] = [name, secName, number, city]

    def change(self, email, name, secName, number, city):
        if email not in self.wordbook.keys():
            return
        if len(str(name)):
            self.wordbook[email][0] = name
        if len(str(secName)):
            self.wordbook[email][1] = secName
        if len(str(number)):
            self.wordbook[email][2] = number
        if len(str(city)):
            self.wordbook[email][3] = city

    def find(self, email):
        if email not in self.wordbook.keys():
            return
        return self.wordbook[email]

    def delete(self, email):
        if email not in self.wordbook.keys():
            return
        self.wordbook.pop(email)


guide = Guide()

guide.addNote('whewisa@mail.com', 'Иван', 'Иванович', '1234567890', 'Москва')
guide.addNote('abc@mail.com', 'Кирилл', 'Васькин', '+78521416563', 'Екатеринбург')
print(guide.wordbook)
guide.change('abc@mail.com', '', 'Lalala', '', '')
print(guide.wordbook)

print(guide.find('abc@mail.com'))
print(guide.find('qabc@mail.com'))

guide.delete('abc@mail.com')
print(guide.wordbook)

guide.delete('abc@mail.com')
print(guide.wordbook)
