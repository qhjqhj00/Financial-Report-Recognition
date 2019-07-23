from typing import Dict

def verticle(base,nominator:dict,name=None):
    for key in nominator:
        nominator[key] /= base
    return {"name": name, "common_size":nominator}


def horizontal(balance_sheet_data:Dict):
    for key in balance_sheet_data:
        tmp = balance_sheet_data[key]
        balance_sheet_data = [value / min(tmp) for value in tmp]
    return balance_sheet_data

