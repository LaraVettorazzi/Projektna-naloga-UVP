def zdruzi_po_casu(niz:str):
    cas = int(niz)
    if cas <= 15:
        return '<15'
    elif cas <= 30:
        return '15-30'
    elif cas <= 45:
        return '30-45'
    elif cas <= 60:
        return '45-60'
    elif cas <= 75:
        return '60-75'
    elif cas <= 90:
        return '75-90'
    else:
        return '>90'
    
def zdruzi_po_kcal(niz:str):
    st = int(niz)
    return str(10 * (st // 10))
    