#ENERGY GENERATED CALCULATION
def check_energy_generated(data_site, date, is_clear_sky_day, tripping_curt_energy):
    """Get the amount of energy generated in a certain site in a certain day, unit kWh.
    energy_generated, energy_generated_expected, estimation_method = check_energy_generated(data_site, date, is_clear_sky_day)

    Args:
        data_site (df): Cleaned D-PV time-series data, output of site_orgaize function
        date (str): date in focus
        is_clear_sky_day (bool): whether the date is a clear sky day or not
        tripping_curt_energy (float): the amount of energy curtailed due to tripping response

    Returns:
        energy_generated (float): Single value of the total energy generated in that day
        data_site (df): D-PV time series data with updated 'power_expected' column if the there is tripping in a non clear sky day.
    """
    
    #sh_idx = (data_site.index.hour>= 7) & (data_site.index.hour <= 17)
    #hour filter should not be necessary since outside of that hour, the power is zero anyway.
    
    date_dt = dt.datetime.strptime(date, '%Y-%m-%d').date()
    date_idx = data_site.index.date == date_dt
    energy_generated = data_site.loc[date_idx, 'power'].resample('h').mean().sum()/1000
    
    if not is_clear_sky_day:
        data_site['power_expected'] = data_site['power_expected_linear']
        
    return energy_generated, data_site

def check_energy_expected_generated(data_site, date):
    """Get the amount of expected energy generated in a certain site in a certain day, unit kWh.

    Args:
        data_site (df): Cleaned D-PV time-series data, with power_expected column
        date (str): date in focus

    Returns:
        energy_generated_expected (float): Single value of the total expected energy generated in that day
    """
    
    #sh_idx = (data_site.index.hour>= 7) & (data_site.index.hour <= 17)
    #hour filter should not be necessary since outside of that hour, the power is zero anyway.
    
    date_dt = dt.datetime.strptime(date, '%Y-%m-%d').date()
    date_idx = data_site.index.date == date_dt
    energy_generated_expected = data_site.loc[date_idx, 'power_expected'].resample('h').mean().sum()/1000
    return energy_generated_expected

def check_energy_expected(energy_generated, tripping_curt_energy, vvar_curt_energy, vwatt_curt_energy, is_clear_sky_day):
    ''' Calculate the expected energy generation without curtailment and the estimation method
    
    Args:
        energy_generated (float): the actual energy generated with curtailment
        tripping_curt_energy (float) : energy curtailed due to tripping. Can't be n/a
        vvar_curt_energy (float) :energy curtailed due to VVAr. Can be n/a in a non clear sky day
        vwatt_curt_energy (float) : energy curtailed due to VWatt. Can be n/a in a non clear sky day
        is_clear_sky_day (bool) : yes if the day is a clear sky day

    Returns:
        energy_generated_expected (float) : the estimated energy generated without curtailment
        estimation_method (str) : the method of estimating the previous value
    '''
    
    if is_clear_sky_day:
        estimation_method = 'Polyfit'
        energy_generated_expected = energy_generated + tripping_curt_energy + vvar_curt_energy + vwatt_curt_energy
    elif tripping_curt_energy > 0:
        estimation_method = 'Linear'
        if math.isnan(vvar_curt_energy):
            vvar_curt_energy = 0
        if math.isnan(vwatt_curt_energy):
            vwatt_curt_energy = 0
        energy_generated_expected = energy_generated + tripping_curt_energy + vvar_curt_energy + vwatt_curt_energy
    else:
        estimation_method = 'n/a'
        energy_generated_expected = 'n/a'
    
    return energy_generated_expected, estimation_method
