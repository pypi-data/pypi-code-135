def Res (V,I):
    R=V/I
    print ("Rds_on mΩ :",R)
    return Res
def Idss (Im):
    DLC=Im
    print ("Idss in mA :",DLC)
def Mos_Leakage_I(psu,dm3_I,V=5, I=1,VoV=5.5,VoC=0.5,ch=1) :
    def set_channel(psu, ch, V, I, internalVov, internalVoC) :
        psu.write('set_channel{0},Voltage{1},Current{2}'.format(ch, V, I))
        psu.write('set max_volt{0},set_max_current{1}'.format(internalVov, internalVoC))

    def turn_on(psu, ch) :
        psu.write('Channel_Turn_on{0}'.format(ch))

    def I_measure(dmm_Im) :
        I = float(dmm_Im.query(':MEASure:CURRent:DC?'))
        return I

    set_channel(psu, 1,V, I, VoV, VoC,ch)
    turn_on(psu, 1)

    curr = I_measure(dm3_I)

    print("The leakage current is ", curr)

    return curr

#Mos_Leakage_I(psu,dm3_I)
def Gm_vt(psu,dm3_I,dm4,V=5,I=1,VoV=5.5,VoC=0.5,ch=1) :
    def set_channel(psu, ch, V, I, internalVov, internalVoC) :
        psu.write('set_channel{0},Voltage{1},Current{2}'.format(ch, V, I))
        psu.write('set max_volt{0},set_max_current{1}'.format(internalVov, internalVoC))

    def turn_on(psu, ch) :
        psu.write('Channel_Turn_on{0}'.format(ch))

    def I_measure(dmm_Im) :
        I = float(dmm_Im.query(':MEASure:CURRent:DC?'))
        return I
    def V_measure(dmm_Vm) :
        Volt = float(dmm_Vm.query(':MEASure:VOLTage:DC?'))
        return Volt

    set_channel(psu, 1,V, I, VoV, VoC,ch)
    turn_on(psu, 1)



    curr = I_measure(dm3_I)
    return curr

    Volt = V_measure(dm4)
    return Volt