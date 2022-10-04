from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition, TermTermType

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.dataCompleteness import _is_term_type_complete
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.cycle import get_organic_fertilizer_N_total, get_ecoClimateZone
from .utils import get_FracLEACH_H
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "dataCompleteness.fertilizer": "True",
        "dataCompleteness.water": "True",
        "inputs": [
            {
                "@type": "Input",
                "value": "",
                "term.termType": "organicFertilizer",
                "optional": {
                    "properties": [{"@type": "Property", "value": "", "term.@id": "nitrogenContent"}]
                }
            }
        ],
        "site": {
            "@type": "Site",
            "measurements": [{"@type": "Measurement", "value": "", "term.@id": "ecoClimateZone"}]
        },
        "optional": {
            "practices": [{"@type": "Practice", "value": "", "term.termType": "waterRegime"}]
        }
    }
}
RETURNS = {
    "Emission": [{
        "value": "",
        "sd": "",
        "min": "",
        "max": "",
        "methodTier": "tier 1",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'no3ToGroundwaterOrganicFertilizer'
TIER = EmissionMethodTier.TIER_1.value


def _emission(value: float, sd: float, min: float, max: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['sd'] = [sd]
    emission['min'] = [min]
    emission['max'] = [max]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _run(cycle: dict):
    N_total = get_organic_fertilizer_N_total(cycle)
    value, min, max, sd = get_FracLEACH_H(cycle, TERM_ID)
    converted_N_total = N_total * get_atomic_conversion(Units.KG_NO3, Units.TO_N)
    return [_emission(
        converted_N_total * value,
        converted_N_total * sd,
        converted_N_total * min,
        converted_N_total * max
    )]


def _should_run(cycle: dict):
    N_total = get_organic_fertilizer_N_total(cycle)
    ecoClimateZone = get_ecoClimateZone(cycle)
    fertilizer_complete = _is_term_type_complete(cycle, {'termType': 'fertilizer'})
    water_complete = _is_term_type_complete(cycle, {'termType': TermTermType.WATER.value})

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    N_total=N_total,
                    ecoClimateZone=ecoClimateZone,
                    fertilizer_complete=fertilizer_complete,
                    water_complete=water_complete)

    should_run = all([N_total > 0, ecoClimateZone, fertilizer_complete, water_complete])
    logShouldRun(cycle, MODEL, TERM_ID, should_run)
    return should_run


def run(cycle: dict): return _run(cycle) if _should_run(cycle) else []
