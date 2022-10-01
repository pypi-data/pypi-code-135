"""Helper to annotate metabolites and species."""

from cobra.core.formula import Formula
import pandas as pd
from micom import Community
import warnings


def flatten(d):
    """Flatten a dictionary into strings."""
    return {k: str(v) for k, v in d.items()}


def annotate(ids, community, what="reaction"):
    """Annotate a list of entities."""
    if what == "reaction":
        elems = community.reactions
    elif what == "metabolite":
        elems = community.metabolites
    else:
        raise ValueError("Invalid value for `what` :(")

    objs = elems.get_by_any(ids)
    attr = "global_id" if isinstance(community, Community) else "id"

    if what == "reaction":
        anns = [
            pd.Series({what: getattr(o, attr), "name": o.name, **flatten(o.annotation)})
            for o in objs
        ]
    else:
        anns = [
            pd.Series({
                what: getattr(o, attr),
                "name": o.name,
                "molecular_weight": Formula(o.formula).weight,
                "C_number": Formula(o.formula).elements.get("C", 0),
                "N_number": Formula(o.formula).elements.get("N", 0),
                **flatten(o.annotation)})
            for o in objs
        ]

    return pd.DataFrame.from_records(anns).drop_duplicates()


def annotate_metabolites_from_exchanges(com):
    """Annotate exchange reactions by their metabolite."""
    if isinstance(com, Community):
        exs = com.internal_exchanges + com.exchanges
        attr = "global_id"
    else:
        exs = com.exchanges
        attr = "id"
    mets = pd.DataFrame.from_records(
        [
            {
                "metabolite": r.reactants[0],
                "mid": getattr(r.reactants[0], attr),
                "rid": getattr(r, attr),
            }
            for r in exs
        ]
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        anns = annotate(mets.metabolite.tolist(), com, "metabolite")
    idmap = mets[["mid", "rid"]].drop_duplicates()
    idmap.index = idmap.mid
    anns["reaction"] = idmap.loc[anns.metabolite, "rid"].values
    return anns
