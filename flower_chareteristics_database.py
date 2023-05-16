import sqlite3

connection = sqlite3.connect('Flowers.db')

connection.execute('''
    CREATE TABLE Daisy
    (id INTEGER PRIMARY KEY,
    Orgins TEXT,
    Danger TEXT,
    Feature TEXT,
    WildLife TEXT)
''')

connection.execute('''
    CREATE TABLE Dandelion
    (id INTEGER PRIMARY KEY,
    Orgins TEXT,
    Danger TEXT,
    Feature TEXT,
    WildLife TEXT)
''')

connection.execute('''
    CREATE TABLE Rose
    (id INTEGER PRIMARY KEY,
    Orgins TEXT,
    Danger TEXT,
    Feature TEXT,
    WildLife TEXT)
''')

connection.execute('''
    CREATE TABLE Sunflower
    (id INTEGER PRIMARY KEY,
    Orgins TEXT,
    Danger TEXT,
    Feature TEXT,
    WildLife TEXT)
''')

connection.execute('''
    CREATE TABLE Tulip
    (id INTEGER PRIMARY KEY,
    Orgins TEXT,
    Danger TEXT,
    Feature TEXT,
    WildLife TEXT)
''')


connection.execute("INSERT INTO Daisy (Orgins, Danger, Feature, WildLife) VALUES('Are a european species', NULL, 'Opens up at dawn and closes at dusk', 'Bees')")

connection.execute("INSERT INTO Dandelion (Orgins, Danger, Feature, WildLife) VALUES('A large genus of plants belonging to the Asteraceae family', 'low', 'Posses antioidant properties', 'Bees/Butterflies/Beetles')")

connection.execute("INSERT INTO Rose (Orgins, Danger, Feature, WildLife) VALUES('They are in the Rosaceae Family', 'Can cut if handled' ,'Stems are covered in sharp thorns', 'Bees/Butterflies/Beetles')")

connection.execute("INSERT INTO Sunflower (Orgins, Danger, Feature, WildLife) VALUES('Commonly grown as a crop for its edible seeds and useful for feed vvarious animals ', 'small amount of toxicty' , 'They track the Sun', 'Bees/birds/insects')")

connection.execute("INSERT INTO Tulip (Orgins, Danger, Feature, WildLife) VALUES('Belong to thhe Plantae family and come in a variety of colours', 'low', 'Orginally created from a virus and come in a variety of colours', 'Bees')")


connection.commit()
connection.close()