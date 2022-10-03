"""Predict novel links in a Knowledge Graph from lists of heads/relations/tails.
"""
# imports
from pandas import DataFrame, concat
from pykeen.pipeline import pipeline
from pykeen.models import predict
from pandas import read_csv

def names2hetionet(names, hetionet_path):
    """Convert common names (genes, diseases etc.) to Hetionet node IDs.

    Parameters
    ----------
    names: list
        List of common names.
    hetionet_path: string
        A path to hetionet nodes file.

    Returns
    -------
    hetionet: list
        List of Hetionet IDs.
    """

    hetionet_nodes_df = read_csv(hetionet_path + 'hetionet-v1.0-nodes.tsv', sep="\t")
    hetionet = hetionet_nodes_df.loc[hetionet_nodes_df['name'].isin(names), 'id'].tolist()

    return(hetionet)

def pykeen_hetionet2names(pykeen_prediction, hetionet_path):
    """Convert Hetionet node IDs in the pykeen prediction DataFrame to common names.

    Parameters
    ----------
    pykeen_prediction: pandas DataFrame
        A pandas DataFrame containing pykeen prediciton results plus two extra columns: either head/tail, head/relation or relation/tail, depending on what was provided as an input.
    hetionet_path: string
        A path to hetionet nodes file.

    Returns
    -------
    pykeen_prediction: pandas DataFrame
        The same pandas DataFrame as the input DataFrame with items in the `heads` and `tails` columns renamed from hetionet IDs to common names.
    """

    hetionet_nodes_df = read_csv(hetionet_path + 'hetionet-v1.0-nodes.tsv', sep="\t")

    # rename heads
    pykeen_prediction = pykeen_prediction.rename(columns = {'head': 'id'})
    pykeen_prediction = pykeen_prediction.merge(hetionet_nodes_df)
    pykeen_prediction = pykeen_prediction.rename(columns = {'name': 'head'})
    pykeen_prediction = pykeen_prediction.drop(columns = ['id', 'kind'])

    # rename tails
    pykeen_prediction = pykeen_prediction.rename(columns = {'tail': 'id'})
    pykeen_prediction = pykeen_prediction.merge(hetionet_nodes_df)
    pykeen_prediction = pykeen_prediction.rename(columns = {'name': 'tail'})
    pykeen_prediction = pykeen_prediction.drop(columns = ['id', 'kind'])

    return(pykeen_prediction)

def pykeen(model, training, heads = None, relations = None, tails = None):
    """Predict novel links in a Knowledge Graph from lists of heads/relations/tails. The main difference from pykeen.models.predict.get_prediction_df is that this function can work with lists.

    Parameters
    ----------
    model: object of pykeen.models class
        Embedding model used when running a pykeen pipeline.
    training: object of pykeen.triples.triples_factory.TriplesFactory class
        An object containing a training set corpredictionsponding to a dataset on which a model was trained.
    heads: list of strings
        List of graph heads.
    relations: list of strings
        List of graph relations.
    tails: list of strings
        List of graph tails.

    Returns
    -------
    predictions_all: pandas DataFrame
        A pandas DataFrame containing pykeen prediciton results plus two extra columns: either head/tail, head/relation or relation/tail, depending on what was provided as an input.
    """

    # Predict tails
    if heads and relations:
        if tails:
            print("Only two (not all three) of heads/relations/tails must be defined!")
            return(None)
        predictions_all = DataFrame()
        for h in heads:
            for r in relations:
                predictions = predict.get_prediction_df(
                    model = model, 
                    head_label = h, 
                    relation_label = r, 
                    triples_factory = training
                )
                predictions['head'] = h
                predictions['relation'] = r
                predictions_all = concat([predictions_all, predictions])
        
    
    # Predict relations
    if heads and tails:
        if relations:
            print("Only two (not all three) of heads/relations/tails must be defined!")
            return(None)
        predictions_all = DataFrame()
        for h in heads:
            for t in tails:
                predictions = predict.get_prediction_df(
                    model = model, 
                    head_label = h, 
                    tail_label = t, 
                    triples_factory = training
                )
                predictions['head'] = h
                predictions['tail'] = t
                predictions_all = concat([predictions_all, predictions])

    # Predict heads
    if relations and tails:
        if heads:
            print("Only two (not all three) of heads/relations/tails must be defined!")
            return(None)
        predictions_all = DataFrame()
        for r in relations:
            for t in tails:
                predictions = predict.get_prediction_df(
                    model = model, 
                    relation_label = r, 
                    tail_label = t, 
                    triples_factory = training
                )
                predictions['relation'] = r
                predictions['tail'] = t
                predictions_all = concat([predictions_all, predictions])

    return(predictions_all)

# run when file is directly executed
if __name__ == '__main__':

    # run examples with the Nations dataset
    result = pipeline(
        model='TransE',
        dataset='Nations',
    )

    predictions = pykeen(result.model, result.training, heads = ['brazil'], tails = ['china'])
    print(predictions)
    predictions = pykeen(result.model, result.training, heads = ['brazil', 'uk'], tails = ['china', 'india'])
    print(predictions)
    predictions = pykeen(result.model, result.training, heads = ['brazil'], relations = ['relintergovorgs'])
    print(predictions.head())
    predictions = pykeen(result.model, result.training, relations = ['relintergovorgs'], tails = ['uk'])
    print(predictions.head())
    predictions = pykeen(result.model, result.training, heads = ['brazil'], relations = ['relintergovorgs'], tails = ['uk'])
    print(predictions)
