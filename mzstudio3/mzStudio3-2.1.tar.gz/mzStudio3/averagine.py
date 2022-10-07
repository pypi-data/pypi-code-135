import numpy as np
#from brainpy import isotopic_variants
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
from scipy import signal


def returnIsotopeDistribution(peptides, mz, intensity_data, charge, trueMonoIsotopic):
    
    # Normalize data
    max_intensity = max(intensity_data)
    intensity_data = [i/max_intensity*100 for i in intensity_data]  
    mz = [i*charge+1 for i in mz]
    # Re-grid data to match averagine 
    f = interp1d(mz, intensity_data)    
    
    n_plots = len(peptides)
    fig, axs = plt.subplots(n_plots, 2,figsize = [12, 10], sharex = False)
    n_plot = 0;
    
    for peptide in peptides:
        print(peptide)
        theoretical_isotopic_cluster = isotopic_variants(peptide)
        
        ## Calculate the distribution of the averagine, but only with the number of peaks we see in the original data
        #peaks, _ = signal.find_peaks(intensity_data)
        #theoretical_isotopic_cluster = theoretical_isotopic_cluster[0:len(peaks)]
        
        # produce a theoretical profile using a gaussian peak shape
        delta_mz = 0.01
        mz_grid = np.arange(theoretical_isotopic_cluster[0].mz - 2,
                    theoretical_isotopic_cluster[-1].mz + 2, delta_mz)
        intensity_averagine = np.zeros_like(mz_grid)
        sigma = 0.002
        for peak in theoretical_isotopic_cluster:
            # Add gaussian peak shape centered around each theoretical peak
            intensity_averagine += peak.intensity * np.exp(-(mz_grid - peak.mz) ** 2 / (2 * sigma)
                                                 ) / (np.sqrt(2 * np.pi) * sigma)
        
        # Normalize profile to 0-100
        intensity_averagine = (intensity_averagine / intensity_averagine.max()) * 100
        
        
        # Interpolate onto common grid
        f1 = interp1d(mz,      intensity_data,        bounds_error = False, fill_value = 0, kind = 'quadratic')
        f2 = interp1d(mz_grid, intensity_averagine,bounds_error = False, fill_value = 0, kind = 'quadratic')

        delta_mz = 0.01
        
        mz_uniform = np.arange( np.floor(min(min(mz),min(mz_grid))) ,max(max(mz),max(mz_grid)),delta_mz)
        
        # Rename variables
        intensity_data = f1(mz_uniform)
        intensity_averagine = f2(mz_uniform)
        mz = mz_uniform
        


        # Calculate cross correlation
        corr = signal.correlate(intensity_data, intensity_averagine)
        corr = corr/max(corr)
        lags = signal.correlation_lags(len(intensity_data), len(intensity_averagine))
        ind_max = np.argmax(corr)
        Delta_mz = delta_mz * lags[ind_max]
        
        
        #Calculate monoisotopic peak
        monoisotopic_peak_averagine = theoretical_isotopic_cluster[0].mz
        monoisotopic_peak_averagine = monoisotopic_peak_averagine + Delta_mz
        guessMonoIsotopic = (monoisotopic_peak_averagine - 1)/charge
        
        
        
        # Graph data
        
        axs[n_plot, 0].plot(mz, intensity_data, '-',label = 'Original Data')
        axs[n_plot, 0].plot(mz, intensity_averagine, '-', label = 'Averagine')
        axs[n_plot, 0].legend()
        axs[n_plot,0].set_title('True monoisotopic: ' + str(trueMonoIsotopic))
        
        
                
        axs[n_plot, 1].plot(mz ,           intensity_data, '-',label = 'Interpolated Original')
        axs[n_plot, 1].plot(mz + Delta_mz, intensity_averagine, '-',label = 'Shifted Interpolated Averagine')
        #axs[n_plot, 0].set_xlim([3225, 3235])
        axs[n_plot, 1].legend()
        axs[n_plot,1].set_title('Guessed monoisotopic: ' + "{:.2f}".format(guessMonoIsotopic))        
        
        

        n_plot = n_plot + 1
    plt.show()    


def calculateIsotopeDistribution(peptide):
    theoretical_isotopic_cluster = isotopic_variants(peptide)
    max_intensity = 0
    for peak in theoretical_isotopic_cluster:
        #print(peak.mz, peak.intensity)
        if peak.intensity>max_intensity:
            max_intensity = peak.intensity
            most_abundant_peak = peak.mz
    monoisotopic_peak = theoretical_isotopic_cluster[0].mz
    delta_abundant_mono = most_abundant_peak - monoisotopic_peak
    
    
    return delta_abundant_mono

def graphIsotopicDistribution(peptides,charge, labels=None):
    plt.figure()

    for peptide in peptides:
        theoretical_isotopic_cluster = isotopic_variants(peptide)
        
        # produce a theoretical profile using a gaussian peak shape
        mz_grid = np.arange(theoretical_isotopic_cluster[0].mz - 1,
                            theoretical_isotopic_cluster[-1].mz + 1, 0.02)
        intensity = np.zeros_like(mz_grid)
        sigma = 0.002
        for peak in theoretical_isotopic_cluster:
            # Add gaussian peak shape centered around each theoretical peak
            intensity += peak.intensity * np.exp(-(mz_grid - peak.mz) ** 2 / (2 * sigma)
                                                 ) / (np.sqrt(2 * np.pi) * sigma)

        # Normalize profile to 0-100
        intensity = (intensity / intensity.max()) * 100

        # draw the profile

        plt.plot(mz_grid/charge, intensity)
        
    plt.xlabel("Molecular Weight")
    plt.ylabel("Relative intensity")  
    
    if labels:
        plt.legend(labels)
    plt.show()    

weight_builtin = {
    "proton": 1.00727646677,
    "electron": 0.00054857990924,
    "neutron": 1.00866491588,
    "H":  1.007825,
    "He": 4.002602,
    "Li": 6.941,
    "Be": 9.012182,
    "B":  10.811,
    "C":  12.0107,
    "N":  14.00674,
    "O":  15.9994,
    "F":  18.9984032,
    "Ne": 20.1797,
    "Na": 22.989768,
    "Mg": 24.3050,
    "Al": 26.981539,
    "Si": 28.0855,
    "P":  30.973762,
    "S":  32.066,
    "Cl": 35.4527,
    "Ar": 39.948,
    "K":  39.0983,
    "Ca": 40.078,
    "Sc": 44.955910,
    "Ti": 47.88,
    "V":  50.9415,
    "Cr": 51.9961,
    "Mn": 54.93805,
    "Fe": 55.847,
    "Co": 58.93320,
    "Ni": 58.6934,
    "Cu": 63.546,
    "Zn": 65.39,
    "Ga": 69.723,
    "Ge": 72.61,
    "As": 74.92159,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.80,
    "Rb": 85.4678,
    "Sr": 87.62,
    "Y":  88.90585,
    "Zr": 91.224,
    "Nb": 92.90638,
    "Mo": 95.94,
    "Tc": 98.0,
    "Ru": 101.07,
    "Rh": 102.90550,
    "Pd": 106.42,
    "Ag": 107.8682,
    "Cd": 112.411,
    "In": 114.82,
    "Sn": 118.710,
    "Sb": 121.757,
    "Te": 127.60,
    "I":  126.90447,
    "Xe": 131.29,
    "Cs": 132.90543,
    "Ba": 137.327,
    "La": 138.9055,
    "Ce": 140.115,
    "Pr": 140.90765,
    "Nd": 144.24,
    "Pm": 145.0,
    "Sm": 150.36,
    "Eu": 151.965,
    "Gd": 157.25,
    "Tb": 158.92534,
    "Dy": 162.50,
    "Ho": 164.93032,
    "Er": 167.26,
    "Tm": 168.93421,
    "Yb": 173.04,
    "Lu": 174.967,
    "Hf": 178.49,
    "Ta": 180.9479,
    "W":  183.85,
    "Re": 186.207,
    "Os": 190.2,
    "Ir": 192.22,
    "Pt": 195.08,
    "Au": 196.96654,
    "Hg": 200.59,
    "Tl": 204.3833,
    "Pb": 207.2,
    "Bi": 208.98037,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226.0254,
    "Ac": 227,
    "Th": 232.0381,
    "Pa": 213.0359,
    "U":  238.0289,
    "Np": 237.0482,
    "Pu": 244,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 252,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "Lr": 260,
    "Rf": 261,
    "Db": 262,
    "Sg": 263,
    "Bh": 262,
    "Hs": 265,
    "Mt": 266,
}

def calculatePolyAveragine(mz, charge):
    test_mass = (mz*charge)
    
    averagine = {'H': 7.7583,'C' : 4.9384, 'N': 1.3577, 'O':1.4773,'S':0.0417}
    mass_elements = {'H': 1.00727646677, 'C' : 12.0107, 'N': 14.00674, 'O':15.9994,'S':32.066}
    averagine_mass = 0 #111.1254 #Da
    for element in averagine:
        averagine_mass = averagine_mass + averagine[element]*weight_builtin[element]
    
    
    
    n_averagine = test_mass / averagine_mass
    #print("Number of averagine molecules: " + str(n_averagine))
    
    poly_averagine = {}
    for element in averagine:
    
        #print(element + ": " + str(averagine[element] * n_averagine))
        poly_averagine[element] = int(np.floor(averagine[element] * n_averagine))
        added_hydrogen_mass = mass_elements[element] * ((averagine[element] * n_averagine) - np.floor(averagine[element] * n_averagine))
        added_n_hydrogen = np.round(added_hydrogen_mass / mass_elements['H'])
        poly_averagine['H'] = int(poly_averagine['H'] + added_n_hydrogen)
    


    #print(poly_averagine)  
    poly_averagine_mass = 0;
    for element in poly_averagine:
        poly_averagine_mass = poly_averagine_mass + poly_averagine[element]*mass_elements[element]
    
    return poly_averagine
    

def calculateMonoIsotopicMass(mz, charge):
    
    test_mass = mz*charge
    poly_averagine = calculatePolyAveragine(mz, charge)
    delta_abundant_mono = calculateIsotopeDistribution(poly_averagine)
    print(delta_abundant_mono)
    true_monoisotopic = test_mass - delta_abundant_mono
    
    print('Monoisotopic Mass: ' + str(true_monoisotopic/charge))
    #print('Most Abundant Mass: ' + str(test_mass/charge))
    
