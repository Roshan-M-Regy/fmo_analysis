def output_parser(line, lno):
    if 'Fragment statistics' in line:
        value = "Fragment stats"
        return lno+4,value,'Fragment statistics'
    elif 'Total energy of the molecule: Euncorr(2)=' in line:
        value = float(line.split()[-1])
        return lno, value, 'Euncorr(2)'
    elif 'Total energy of the molecule: Eunc_es(2)=' in line:
        value = float(line.split()[-1])
        return lno, value, 'Eunc_es(2)'
    elif 'Total energy of the molecule: Eunc_es(1)=' in line:
        value = float(line.split()[-1])
        return lno, value, 'Eunc_es(1)'
    elif 'Total energy of the molecule: Eunc+so(1)=' in line:
        value = float(line.split()[-1])
        return lno, value, 'Eunc+so(1)'
    elif 'Electrostatic (PL state, incl. EPLs)  EES' in line:
        value = float(line.split()[-1])
        return lno,value,'EES'
    elif ' 0-th order DFTB energy (PL state)      E0' in line:
        value = float(line.split()[-1])
        return lno,value,'E0'
    elif ' Charge transfer coupled to ES (PL) E(CT*ES)' in line:
        value = float(line.split()[-1])
        return lno,value,'E(CT*ES)'
    elif 'Dispersion (PL state)                 EDI' in line:
        value = float(line.split()[-1])
        return lno,value,'EDI'
    elif 'Solvent screening (PL state)          ESOLV' in line:
        value = float(line.split()[-1])
        return lno, value, 'ESOLV'
    elif 'Total interaction (PL state)         Eint' in line:
        value = float(line.split()[-1])
        return lno, value, 'Eint'
    elif 'The 0-th order, P and REP energy =' in line:
        value = float(line.split()[-1])
        return lno, value, 'Oth_P_REP_energy'
    elif "Electrostatic (PL state, incl. EPLs)  E'ES" in line:
        value = float(line.split()[-1])
        return lno, value, "E'ES"
    elif "Exchange (PL state)                   E'EX" in line:
        value = float(line.split()[-1])
        return lno,  value, "E'EX"
    elif "Charge transfer (PL state)      E'(CT+mix)" in line:
        value = float(line.split()[-1])
        return lno, value, "E'(CT+mix)"
    elif "Dispersion (PL state)                 E'DI" in line:
        value = float(line.split()[-1])
        return lno, value, "E'DI"
    elif '   I    J DL  Z    R   Q(I->J)  EIJ-EI-EJ dDIJ*VIJ    total     Ees       E0     Ect*es    Edisp    Gsol' in line:
        return lno+2,line, 'PIEDA'
    elif '   I    J DL  Z    R   Q(I->J)  EIJ-EI-EJ dDIJ*VIJ    total     Ees      Eex    Ect+mix    Edisp    Gsol' in line:
        return lno+2,line, "Two-body FMO properties"

def input_parser(line,lno):
    if "INDAT(1)=" in line:
        return lno+1,line,"INDAT"