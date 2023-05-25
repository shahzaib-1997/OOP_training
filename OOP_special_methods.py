# __init__()
# __str__()
# __del__()
# __len__()

class Book():
    def __init__(self, title, author, pages):
        print('Book is created.')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        A = f"title: {self.title}, author: {self.author}, pages: {self.pages}"
        return A
        
    def __len__(self):
        return int(self.pages)

    def __del__(self):
        pass

b1 = Book('Mind your Code', 'Shahzaib Ali', 150)
b2 = Book('Coding the Brains', 'Awais Mazahir', 200)

print(b1)
print(len(b1))
print(b2)

del b2

print(b2)
