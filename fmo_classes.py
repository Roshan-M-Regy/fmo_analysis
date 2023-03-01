class FMOFragment():
    def __init__(self, index, name, q, nat0, natb, na, nao, lay, mul, scftyp, nop, mol, conv):
        self.index = str(index)
        self.name = str(name)
        self.q = int(q)
        self.nat0 = int(nat0)
        self.natb = int(natb)
        self.na = int(na)
        self.nao = int(nao)
        self.lay = int(lay)
        self.mul = int(mul)
        self.scftyp = str(scftyp)
        self.nop = int(nop)
        self.mol = int(mol)
        self.conv = int(conv)
        self.atoms = None
    
    def to_list(self):
        return [self.index, self.name, self.atoms,self.q, self.nat0, self.natb, self.na, 
                self.nao, self.lay, self.mul, self.scftyp, self.nop, self.mol, self.conv]
    
    def add_atoms(self,indat_string):
        self.atoms = indat_string


class FMODimer():
    def __init__(self, fragi, fragj, dl, z, r, qi2j, eij_ei_ej, dDijmulVij, total, Ees, Eex, Ectplusmix, Edisp, Gsol):
        self.ij = f"{fragi.index}-{fragj.index}"
        self.fragi = fragi
        self.fragj = fragj
        self.dl = str(dl)
        self.z = int(z)
        self.r = float(r)
        self.qi2j = float(qi2j)
        self.eij_ei_ej = float(eij_ei_ej)
        self.dDijmulVij = float(dDijmulVij)
        self.total = float(total)
        self.Ees = float(Ees)
        self.Eex = float(Eex)
        self.Ectplusmix = float(Ectplusmix)
        self.Edisp = float(Edisp)
        self.Gsol = float(Gsol)
    
    def to_list(self,fragdata=False):
        if fragdata==True:
            return [self.ij, self.fragi.get_list(), self.fragj.get_list(),self.dl, self.z, self.r, self.qi2j,
                self.eij_ei_ej,self.dDijmulVij, self.total, self.Ees, self.Eex, self.Ectplusmix, self.Edisp, self.Gsol]
        else:
            return [f"{self.fragi.name}",f"{self.fragj.name}",self.dl, self.z, self.r, self.qi2j,
                self.eij_ei_ej,self.dDijmulVij, self.total, self.Ees, self.Eex, self.Ectplusmix, self.Edisp, self.Gsol]
