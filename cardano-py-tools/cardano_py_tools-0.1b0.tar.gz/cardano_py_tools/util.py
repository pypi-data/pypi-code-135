
def shortAddr(addr: str)-> str:
    return f"{addr[:12]}...{addr[-12:]}"

def shortUTXO(addr: str)-> str:
    return f"{addr[:7]}...{addr[-7:]}"

def shortSignature(addr: str)-> str:
    return f"{addr[:7]}...{addr[-7:]}"

def shortVKey(addr: str)-> str:
    return f"{addr[:7]}...{addr[-7:]}"

def lovelanceToAda(amount:int):
    return f"{amount/1000000} ₳"

def getNetworkFromAddr(addr:str)->str:
    networkTag=addr[1]
    return "Testnet" if networkTag == '0' else "Mainnet"


