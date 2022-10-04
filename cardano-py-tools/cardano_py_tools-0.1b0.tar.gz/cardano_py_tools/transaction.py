
import json
import cbor2
import pydot
from cardano_py_tools.util import *

def decodeCborHex(txFile:str=None, cborStr:str=None)->dict:
    if cborStr:  
        return formatTxData(cbor2.loads(bytes.fromhex(cborStr)))

    elif txFile: 
        with open(txFile, 'r') as file:
            data = file.read()
            return formatTxData(cbor2.loads(bytes.fromhex(json.loads(data)['cborHex'])))
    else:
        raise Exception("[ERROR] The path for the transaction signed file or the cborHex string is not definied in the parameter of the function decodeCborHex.")


def formatTxData(decodedCbor:dict)->dict:
        # Input and Output data (Addresses, amount, Fees, UTXO IN)  
        ioData  = decodedCbor[0]
        # Verification key and Signature
        witness = decodedCbor[1]
        
        # Format the data
        inputs  = [f"{txHash.hex()}#{txIx}" for txHash, txIx in ioData[0]]
        outputs = [{"address":addr.hex(), "amount":lovelance} for addr, lovelance in ioData[1]]
        witnesses  = [{"vKey":vKey.hex(), "signature":signature.hex()} for vKey, signature in witness[0]] 
        
        return {"inputs":inputs,
                "outputs":outputs,
                "fees":ioData[2],
                "network":getNetworkFromAddr(outputs[0]['address']),
                "witnesses":witnesses,
                "metadata":decodedCbor[3] if len(decodedCbor) >= 3 else None}


def vizualisation(txFile:str=None, cborStr:str=None, saveTo="txViz.png"):
    if txFile:
        txData = decodeCborHex(txFile=txFile)
    elif cborStr:
        txData = decodeCborHex(cborStr=cborStr)
    else:
        raise Exception("[ERROR] You have to select a signed transaction or the cbor string.")

    # Init the graph
    dot_graph = pydot.Dot(graph_type='digraph')

    # Get the data from the transaction
    amountOutputs = [output["amount"] for output in txData["outputs"]]
    utxoIn = [utxo for utxo in txData["inputs"]]
    fee = txData["fees"]
    amountTXUTXO  = sum(amountOutputs) + fee
    witnesses = txData["witnesses"]
    metadata = txData["metadata"]
   
    if metadata:
        metadata = str(list(txData["metadata"].value[0].values())[0]).replace("{", "\n")
        metadata = metadata.replace(",", "\n")
        metadata = metadata.replace("}", "")
        metadata = metadata.replace("'", "")
        metadataID = list(txData["metadata"].value[0].keys())[0]
   
    # Create the box label
    feeLabel      = f"TX_FEES \n{lovelanceToAda(fee)}"
    inputLabel    =[ f"UTXO_IN_{index+1} \n {shortUTXO(txData['inputs'][index])}" for index, _ in enumerate(utxoIn)]
    outputLabel   =[ f"ADDR_{index+1} \n {shortAddr(txData['outputs'][index]['address'])}" for index, _ in enumerate(amountOutputs)]

    # Generate the inputs transaction shape
    for label in inputLabel:
        dot_graph.add_node(pydot.Node(label, shape='box'))
        
    # Generate the outputs transaction shape
    for index, title in enumerate(outputLabel):
        dot_graph.add_node(pydot.Node(title, shape='plaintext'))
        
    # Generate the shape for the fees
    dot_graph.add_node(pydot.Node(feeLabel,style='filled', fillcolor="lightblue"))

    # Generate the shape for the transaction and witness on the same rank
    txFloor = pydot.Subgraph(rank='same')

    # Generate the transaction shape
    metadataLabel = f"\n\n • Metadata (ID: {metadataID}): {metadata}" if metadata else metadata
    txLabel = '"TRANSACTION \n \n • Network: {} \n  • UTXO amount: {} {} \n\n"'.format(txData["network"],lovelanceToAda(amountTXUTXO), metadataLabel)
    txFloor.add_node(pydot.Node(txLabel, shape='box3d'))

    # Generate witness shape
    for index, witness in enumerate(witnesses):
        signature = shortSignature(witness["signature"])
        vKey      = shortVKey(witness["vKey"])
        txFloor.add_node(pydot.Node(f"\n WITNESS_{index+1} \n Signature = {signature} \n vKey = {vKey} \n\n", shape='signature', style='filled', fillcolor="lightgreen"))
    
    # Add the witness shape and transaction on the same rank
    dot_graph.add_subgraph(txFloor)

    # Generate the edge from the inputs shape to the transaction shape 
    for label in inputLabel: 
        dot_graph.add_edge(pydot.Edge(label, txLabel))

    # Generate the edge from the transaction shape to the outputs shape
    for index, label in enumerate(outputLabel): 
        amount = lovelanceToAda(txData["outputs"][index]["amount"])
        dot_graph.add_edge(pydot.Edge(txLabel, label, label=amount))
        
    # Generate the edge from the transaction to the fee label
    dot_graph.add_edge(pydot.Edge(txLabel, feeLabel))

    # Save the graph
    if ".svg" in saveTo:
        dot_graph.write_svg(saveTo)
    elif ".png" in saveTo:
        dot_graph.write_png(saveTo)
    else:
         raise Exception("[ERROR] You have to specified the format of the graph (CVG | PNG).")
  

    



    