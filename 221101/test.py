from rdkit import Chem
suppl = Chem.SDMolSupplier('Chemdiv_500.sdf',removeHs = False)
mol = suppl[0]

