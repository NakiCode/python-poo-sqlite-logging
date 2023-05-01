from main import data

db = data()

# response = db.sql_request()
# print(response)

###### INSER #########"
# donnees = [("Apprendre Python", 'Développement desktop avec PySide6'), ('Decouvrir React Js', 'Les Hooks')]
# response = db.insert(donnees)
# print(response)

######### SELECT ########
# response = db.select()
# print(response[0][2])
########### SELECT BY ID ######
# response = db.select_id(id=(2,))
# for data in response:
#     print(data)
#######""" UPDATE"
# response = db.update(donnees=('Django Signals', 1))
# print(response)
##############" DELETE"
response = db.delete(id=(3,))
print(response)