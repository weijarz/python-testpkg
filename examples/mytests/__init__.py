db = []

def setUpPackage():
    db.extend((1, 2, 3))

def tearDownPackage():
    db.clear()
