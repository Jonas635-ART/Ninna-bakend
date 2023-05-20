# factory                         

from faker import Faker
from faker.providers import internet, person, emoji

fake = Faker()
fake.add_provider({internet, person, emoji}), 

# Como crear varios usuarios:


for producto in range(20):
        nombre = fake.first_name()
        color = fake.color()
        precio = fake.bothify(text='##')
        imagen = fake.emoji()
        #Apellido = fake.last_name()
        #Telefono = fake.bothify(text='9########')
        # version comun ->
        sql= ''' INSERT INTO producto (nombre,color,precio,imagen) VALUES
                    ('%s','%s','%s',%s');''' % (nombre,color,precio,imagen)
        #version moderna -c
        sql2= ''' INSERT INTO producto (nombre,color,precio,imagen) VALUES
                ('{}','{}','{}','{}')''' .format (nombre,color,precio,imagen)

        print(sql)
#Fin
















































