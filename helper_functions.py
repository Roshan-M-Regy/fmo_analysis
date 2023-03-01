from fmo_classes import *
import pandas as pd 
import numpy as np 

def get_frag_stats(lno, lines):
    fragments = []
    flag = 0
    while flag==0:
        index, name, q, nat0, natb, na,nao, lay, mul,mulg, scftyp, nop, mol, conv = lines[lno].split()
        try:
            fragments.append(FMOFragment(index,name,q,nat0,natb,na,nao,lay,mul,scftyp,nop,mol,conv))
        except:
            print(f"Can't make a fragment from this line no. {lno}") 
            print(lines[lno])
            continue
        lno += 1
        if len(lines[lno].split())<14:
            flag = 1
    return fragments


def get_dimer_data(lno, lines, fragments):
    dimers = []
    flag = 0
    while flag==0:
        i,j,dl,z,r,qi2j,eij_ei_ej, dDijmulVij, total, Ees, Eex, Ectplusmix, Edisp, Gsol = lines[lno].split()
        try:
            dimers.append(FMODimer(fragments[int(i)-1],fragments[int(j)-1],dl,z,r,qi2j,eij_ei_ej, dDijmulVij, total,Ees,Eex,Ectplusmix, Edisp,Gsol))
        except:
            print(f"Can't make a dimer from this line no. {lno}") 
            print(lines[lno])
            continue
        lno += 1
        if len(lines[lno].split())<14:
            flag = 1
    return dimers

def add_atoms2frags(fragments,lno,inputlines):
    indatlines = []
    flag = 0
    while flag == 0:
        nextfrag = 'n'
        line  = ''
        while nextfrag == 'n':
            line += ' '.join(inputlines[lno].split())
            if line[-1] != '0':
                lno += 1
                line += ' '
            else:
                line = line[:-1]
                nextfrag = 'y'
        indatlines.append(line)
        lno += 1
        if "END" in inputlines[lno]:
            flag = 1
    if len(indatlines) != len(fragments):
        raise Exception(f"Mismatch between number of fragments {len(fragments)} and INDAT lines {len(indatlines)}!")
    else:
        for fragment,indatline in zip(fragments,indatlines):
            fragment.add_atoms(indatline)
    return fragments


def dimers_to_csv(dimers, fragdata=False, filename="dimer_data.csv"):
    dimerdata = []
    for d,dimer in enumerate(dimers):
        dimerdata.append(dimer.to_list(fragdata))
    dimerdata = pd.DataFrame(dimerdata,columns=['I','J', 'dl', 'z', 'r', 'qi2j', 'eij_ei_ej', 
                                                'dDijmulVij', 'total', 'Ees', 'Eex', 'Ectplusmix', 'Edisp', 'Gsol'])
    dimerdata.to_csv(filename,index=False)

def fragments_to_csv(fragments, filename="fragment_data.csv"):
    fragment_data = []
    for f,fragment in enumerate(fragments):
        fragment_data.append(fragment.to_list())
    fragment_data = pd.DataFrame(fragment_data, columns=['index', 'name','atoms', 'q', 'nat0', 'natb', 
                                                         'na','nao', 'lay', 'mul', 'scftyp', 'nop', 'mol', 'conv'])
    fragment_data.to_csv(filename,index=False)

def convert_atomstring(atmstring):
    """
    Takes the indat atom string and converts it 
    into a list for atom selection in nglview.
    """
    pieces = atmstring.split()
    atmlist = []
    for i,piece in enumerate(pieces):
        if piece[0] == '-':
            for i in np.arange(atmlist[-1]+1,int(piece[1:])+1):
                atmlist.append(i-1)
        else:
            atmlist.append(int(piece)-1)
    return atmlist