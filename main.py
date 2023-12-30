from models.keeping import keeping
from models.materials import materials
from models.suppliers import suppliers

suppliers = suppliers()
materials = materials()
keeping = keeping()

for row, list in enumerate(suppliers.countAboutBanks()):
    print(row, ')', list)