class Employe:
    Company = "Ace"
    Sallary = 100

    def address(self):
        print(f"live in {self.city}")


Shivam = Employe()
Nilesh = Employe()

Shivam.Sallary = 200
Shivam.city = "Surat"

print(Shivam.Sallary)
Shivam.address()
print(Nilesh.Sallary)
# Nilesh.address()