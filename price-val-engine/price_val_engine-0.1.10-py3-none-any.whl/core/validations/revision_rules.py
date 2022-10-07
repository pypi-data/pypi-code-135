from price_val_engine.core.validations.base_rules import BaseRule
from price_val_engine.conf import settings


class AbsoluteDeltaPercentageRangeValidationRule(BaseRule):
    name = "revised-vs-listing-price-delta"
    # REPIVISED VS LISTING PRICE DELTA
    severity = None
    message = "{} Vs {} delta greater than ({}, {})%. Actual is {}%"
    
    PREV_VALUE_FIELD = settings.DEFAULT_PREV_DAY_LP_FIELD or 'lp'
    CUR_VALUE_FIELD = settings.DEFAULT_LP_FIELD or 'final_liquidation_price'
    
    SEVERITY_CATEGORY = { "DEFAULT": [-5, 5], "LOW": [-7, 7], "MEDIUM": [-10, 10]}
    
    def __init__(self) -> None:
        super().__init__()
        
        if hasattr(settings, 'DELTA_PCT_VAL_DEFAULT') and  settings.DELTA_PCT_VAL_DEFAULT:
            self.SEVERITY_CATEGORY['DEFAULT'] = settings.DELTA_PCT_VAL_DEFAULT 
        
        if hasattr(settings, 'DELTA_PCT_VAL_LOW') and  settings.DELTA_PCT_VAL_LOW:
            self.SEVERITY_CATEGORY['LOW'] = settings.DELTA_PCT_VAL_LOW 
        
        if hasattr(settings, 'DELTA_PCT_VAL_MEDIUM') and  settings.DELTA_PCT_VAL_MEDIUM:
            self.SEVERITY_CATEGORY['MEDIUM'] = settings.DELTA_PCT_VAL_MEDIUM 
    
    def get_current_value_field(self, default_field=None):
        if self.CUR_VALUE_FIELD is None:
            return default_field
        return self.CUR_VALUE_FIELD
    
    def get_previous_value_field(self, default_field=None):
        if self.PREV_VALUE_FIELD is None:
            return default_field
        return self.PREV_VALUE_FIELD
        
    def is_valid(self, item, target_field="final_liquidation_price"):
        current_field = self.get_current_value_field(target_field)
        prev_field = self.get_previous_value_field('lp')
        
        current_value = float(item[current_field])
        prev_value = float(item[prev_field])
        
        delta = current_value - prev_value
        delta_pct = round(100 * delta / (prev_value or 0.000001) ,0)    
        
        if  self.SEVERITY_CATEGORY['DEFAULT'][0] <= delta_pct  <= self.SEVERITY_CATEGORY['DEFAULT'][1]:
            return True
        
        elif self.SEVERITY_CATEGORY['LOW'][0] <= delta_pct  <= self.SEVERITY_CATEGORY['LOW'][1]:
            self.severity = 'LOW'
            self.message = self.message.format(self.PREV_VALUE_FIELD, self.CUR_VALUE_FIELD, self.SEVERITY_CATEGORY['LOW'][0], self.SEVERITY_CATEGORY['LOW'][1], delta_pct)
            self.message= self.message.format("7%", delta_pct) 
            return False
        
        elif  self.SEVERITY_CATEGORY['MEDIUM'][0] <= delta_pct  <= self.SEVERITY_CATEGORY['MEDIUM'][1]:
            self.severity = 'MEDIUM'
            #self.message = self.message.format("10%", delta_pct) 
            self.message = self.message.format(self.PREV_VALUE_FIELD, self.CUR_VALUE_FIELD, self.SEVERITY_CATEGORY['LOW'][0], self.SEVERITY_CATEGORY['LOW'][1], delta_pct)
            return False
        
        else:
            self.severity = 'HIGH'
            self.message = self.message.format(self.PREV_VALUE_FIELD, self.CUR_VALUE_FIELD, self.SEVERITY_CATEGORY['LOW'][0], self.SEVERITY_CATEGORY['LOW'][1], delta_pct)
            #self.message= "Revised Vs Listing price delta more than 10%. Actual is {}%".format(delta_pct) 
            return False 

    
class DeltaPercentageValidationRule(BaseRule):
    name = 'absolute-delta-percentage-validation'
    message = "absolute delta percentage should not more than +(-) {}%. Actual is {}%"
    severity = 'HIGH'

    absolute_allowed_delta_pct = 100
    
    def get_delta(self, item):
        return self.absolute_allowed_delta_pct

    def is_valid(self, item):
        delta = round(self.get_delta(item),2)
        if delta > self.absolute_allowed_delta_pct:
            self.message = self.message.format(self.absolute_allowed_delta_pct, delta)
            return False
        return True

class DeltaValidationRule(BaseRule):
    name = 'final-lp-greater-than-price-after-onroad'
    message = "Invalid Value"
    severity = 'MEDIUM'
    
    high_value_field = "final_liquidation_price"
    low_value_field = "price_after_onroad"

    HIGH_DELTA = 10000
    MEDIUM_DELTA = 5000
    LOW_DELTA = 1000
    
    def is_valid(self, item):
        if item[self.high_value_field] - item['tcs_addition'] - item['tcs_addition'] - self.HIGH_DELTA  > item[self.low_value_field]:
            self.message = f"{self.high_value_field} [{item[self.high_value_field]}] is greater than {self.low_value_field} [{item[self.low_value_field]}]"
            self.severity = 'HIGH'
            return False

        elif item[self.high_value_field] - item['tcs_addition'] - self.MEDIUM_DELTA  > item[self.low_value_field]:
            self.message = f"{self.high_value_field} [{item[self.high_value_field]}] is greater than {self.low_value_field} [{item[self.low_value_field]}]"
            self.severity = 'MEDIUM'
            return False
        
        elif item[self.high_value_field] - item['tcs_addition'] - self.LOW_DELTA  > item[self.low_value_field]:
            self.message = f"{self.high_value_field} [{item[self.high_value_field]}] is greater than {self.low_value_field} [{item[self.low_value_field]}]"
            self.severity = 'LOW'
            return False

        return True
