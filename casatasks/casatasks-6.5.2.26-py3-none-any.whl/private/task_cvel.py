from __future__ import absolute_import
import os
import shutil

# get is_CASA6 and is_python3
from casatasks.private.casa_transition import *
if is_CASA6:
    from casatools import table, quanta
    from casatools import ms as mstool
    from casatasks import casalog
    from .mstools import write_history

    qa = quanta()
else:
    from taskinit import *
    from mstools import write_history

    mstool = casac.ms
    table = casac.table

def cvel(vis, outputvis,
         passall, field, spw, selectdata, antenna, timerange, scan, array,
         mode, nchan, start, width, interpolation,
         phasecenter, restfreq, outframe, veltype, hanning):

    """ regrid an MS to a new spectral window / channel structure or frame
    
         vis -- Name of input visibility file
               default: none; example: vis='ngc5921.ms'    
    
         outputvis -- Name of output measurement set (required)
                 default: none; example: vis='ngc5921-regridded.ms'    

         passall --  if False, data not meeting the selection on field or spw 
                 is omitted; if True, data not meeting the selection 
                 is passed through without modification
                 default: False; example: 
                 field='NGC5921'
                 passall=False : only data from NGC5921 is included in output MS, 
                           no data from other fields (e.g. 1331+305) is included
                 passall=True : data from NGC5921 is transformed by cvel, all other 
                           fields are passed through unchanged 
    
         field -- Select fields in MS.  Use field id(s) or field name(s).
                    ['go listobs' to obtain the list id's or names]
                default: ''= all fields
                If field string is a non-negative integer, it is assumed to
                    be a field index otherwise, it is assumed to be a 
                    field name
                field='0~2'; field ids 0,1,2
                field='0,4,5~7'; field ids 0,4,5,6,7
                field='3C286,3C295'; field named 3C286 and 3C295
                field = '3,4C*'; field id 3, all names starting with 4C
    
         spw --Select spectral window/channels
                NOTE: This selects the data passed as the INPUT to mode
                default: ''=all spectral windows and channels
                  spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                  spw='0:5~61'; spw 0, channels 5 to 61
                  spw='<2';   spectral windows less than 2 (i.e. 0,1)
                  spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, 
                                     channels 3 to 45.
                  spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                  spw='0:0~10;15~60'; spectral window 0 with channels 
                                      0-10,15-60
                  spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
                        spw 1, channels 20-30, and spw 2, channels, 1,2 and 3
    
         selectdata -- Other data selection parameters
                default: True
    
         selectdata=True expandable parameters
    
                antenna -- Select data based on antenna/baseline
                    default: '' (all)
                    If antenna string is a non-negative integer, it is 
                      assumed to be an antenna index, otherwise, it is
                      considered an antenna name.
                    antenna='5&6'; baseline between antenna index 5 and 
                                   index 6.
                    antenna='VA05&VA06'; baseline between VLA antenna 5 
                                         and 6.
                    antenna='5&6;7&8'; baselines 5-6 and 7-8
                    antenna='5'; all baselines with antenna index 5
                    antenna='05'; all baselines with antenna number 05 
                                  (VLA old name)
                    antenna='5,6,9'; all baselines with antennas 5,6,9 
                                     index numbers
    
                timerange  -- Select data based on time range:
                   default = '' (all); examples,
                    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                    Note: if YYYY/MM/DD is missing date defaults to first 
                          day in data set
                    timerange='09:14:0~09:54:0' picks 40 min on first day
                    timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 
                               30min on NEXT day
                    timerange='09:44:00' pick data within one integration 
                               of time
                    timerange='>10:24:00' data after this time
    
                scan -- Scan number range.
                    default: '' (all)
                    example: scan='1~5'
                    Check 'go listobs' to insure the scan numbers are in 
                          order.
    
                array -- Select data by (sub)array indices
                    default: '' (all); example:
                    array='0~2'; arrays 0 to 2 
    
          mode -- Frequency Specification:
                 NOTE: See examples below:
                 default: 'channel'
                   mode = 'channel'; Use with nchan, start, width to specify
                           output spw.  See examples below
                   mode = 'velocity', means channels are specified in 
                        velocity.
                   mode = 'frequency', means channels are specified in 
                        frequency.
    
          mode expandable parameters 
                 Start, width are given in units of channels, frequency 
                    or velocity as indicated by mode 
                 nchan -- Number of channels in output spw
                   default: -1 = all channels; example: nchan=3
                 start -- Start input channel (relative-0)
                   default=0; example: start=5
                 width -- Output channel width in units of the input
                       channel width (>1 indicates channel averaging)
                   default=1; example: width=4
                 interpolation -- Interpolation method
                   default = 'linear'

             examples:
                 spw = '0,1'; mode = 'channel'
                    will produce a single spw containing all channels in spw 
                         0 and 1
                 spw='0:5~28^2'; mode = 'channel'
                    will produce a single spw made with channels 
                         (5,7,9,...,25,27)
                 spw = '0'; mode = 'channel': nchan=3; start=5; width=4
                    will produce an spw with 3 output channels
                    new channel 1 contains data from channels (5+6+7+8)
                    new channel 2 contains data from channels (9+10+11+12)
                    new channel 3 contains data from channels (13+14+15+16)
                 spw = '0:0~63^3'; mode='channel'; nchan=21; start = 0; 
                     width = 1
                    will produce an spw with 21 channels
                    new channel 1 contains data from channel 0
                    new channel 2 contains data from channel 2
                    new channel 21 contains data from channel 61
                 spw = '0:0~40^2'; mode = 'channel'; nchan = 3; start = 
                     5; width = 4
                    will produce an spw with three output channels
                    new channel 1 contains channels (5,7)
                    new channel 2 contains channels (13,15)
                    new channel 3 contains channels (21,23)
    
          phasecenter -- direction measure  or fieldid for the mosaic center
                 default: '' => first field selected ; example: phasecenter=6
                 or phasecenter='J2000 19h30m00 -40d00m00'
    
          restfreq -- Specify rest frequency to use for output image
                 default='' Occasionally it is necessary to set this (for
                 example some VLA spectral line data).  For example for
                 NH_3 (1,1) put restfreq='23.694496GHz'
    
          outframe -- output reference frame (not case-sensitive)
               possible values: LSRK, LSRD, BARY, GALACTO, LGROUP, CMB, GEO, TOPO or SOURCE
               default='' (keep original reference frame) ; example: outframe='BARY' 
    
          veltype -- definition of velocity (in mode)
                 default = 'radio'
    
          hanning -- if true, Hanning smooth frequency channel data before regridding
                 to remove Gibbs ringing
                 default = False
    
    """

    # Note: this is duplicated in task_cvel, and really needing CASA-wide harmonization
    # (CAS-12871)
    def copy_ms(src, dest):
        """ This is a MMS-safe copy of an MMS tree directory.
        :param src: path to the source MS
        :param dest: path to the destination MS
        """
        shutil.copytree(src, dest, symlinks=True)

    #Python script

    # make ms, table tools local
    _ms = mstool()
    _tb = table()

    try:
        casalog.origin('cvel')

        if not ((type(vis)==str) & (os.path.exists(vis))):
            raise ValueError('Visibility data set not found - please verify the name')

        assert outputvis != '', "Must provide output data set name in parameter outputvis."
        assert not os.path.exists(outputvis), "Output MS %s already exists - will not overwrite." % outputvis
        assert not os.path.exists(outputvis+".flagversions"), \
            "The flagversions \"%s.flagversions\" for the output MS already exist. Please delete." % outputvis
                            
        # Handle selectdata explicitly
        #  (avoid hidden globals)
        if (selectdata==False):
            timerange=''
            array=''
            antenna=''
            scan=''

        if(type(antenna) == list):
            antenna = ', '.join([str(ant) for ant in antenna])

        if (field == ''):
            field = '*'

        if (spw == ''):
            spw = '*'

        if(passall and spw=='*' and field=='*'):
            # all spws and fields selected, nothing to pass through
            passall = False

        doselection = True
        if(field=='*' and spw=='*' and
           (not selectdata or (selectdata and antenna=='' and timerange=='' and scan=='' and array==''))
            ):
            doselection = False

        # open input MS
        _ms.open(vis)

        if(type(phasecenter)==str):
            ### blank means take field 0
            if (phasecenter==''):
                phasecenter=_ms.msseltoindex(vis,field=field)['field'][0]
            else:
                tmppc=phasecenter
                try:
                    if(len(_ms.msseltoindex(vis, field=phasecenter)['field']) > 0):
                        tmppc=_ms.msseltoindex(vis, field=phasecenter)['field'][0]
                        ##succesful must be string like '0' or 'NGC*'
                except Exception:
                    ##failed must be a string 'J2000 18h00m00 10d00m00'
                    tmppc=phasecenter
                phasecenter=tmppc

        newphasecenter = phasecenter
        phasecentername = phasecenter
        if not (type(phasecenter)==str):
            # first check that this field will be in the output MS
            if not (phasecenter in _ms.msseltoindex(vis,field=field)['field']):
                message = "Field id " + str(phasecenter)
                message += " was selected as phasecenter but is not among the fields selected for output: "
                message += str(_ms.msseltoindex(vis,field=field)['field'])
                _ms.close()
                raise RuntimeError(message)

            _tb.open(vis+"/FIELD")
            try:
                # get the name for later display
                phasecentername = _tb.getcell('NAME', phasecenter) + " (original field " + str(phasecenter)
                _tb.close()
                # phase center id will change if we select on fields,
                # the name column is only optionally filled and not necessarily unique.
                # But _ms.msseltoindex(vis,field=field)['field'] returns the old field ids
                # in the order in which they will occur in the new field table.
                # => need to get index from there as new phase center ID
                newphasecenter = (_ms.msseltoindex(vis,field=field)['field']).tolist().index(phasecenter)
                phasecentername += ", new field " + str(newphasecenter) + ")"
            except:
                _tb.close()
                message = "phasecenter field id " + str(phasecenter) + " is not valid"
                _ms.close()
                raise RuntimeError(message)

        if(mode=='frequency'):
            ## reset the default values
            if(start==0):
                start = ""
            if(width==1):
                width = ""
            ##check that start and width have units if they are non-empty
            if not(start==""):
                if (qa.quantity(start)['unit'].find('Hz') < 0):
                    _ms.close()
                    raise TypeError("start parameter is not a valid frequency quantity " %start)
            if(not(width=="") and (qa.quantity(width)['unit'].find('Hz') < 0)):
                _ms.close()
                raise TypeError("width parameter %s is not a valid frequency quantity " %width)
            
        elif(mode=='velocity'):
            ## reset the default values
            if(start==0):
                start = ""
            if(width==1):
                width = ""
            ##check that start and width have units if they are non-empty
            if not(start==""):
                if (qa.quantity(start)['unit'].find('m/s') < 0):
                    _ms.close()
                    raise TypeError("start parameter %s is not a valid velocity quantity " %start)
            if(not(width=="") and (qa.quantity(width)['unit'].find('m/s') < 0)):
                _ms.close()
                raise TypeError("width parameter %s is not a valid velocity quantity " %width)

        elif(mode=='channel' or mode=='channel_b'):
            if((type(width) != int) or (type(start) != int)):
                _ms.close()
                raise TypeError("start and width have to be integers with mode = %s" %mode)


        ## check if preaveraging is necessary
        dopreaverage=False
        preavwidth = [1]        

        thespwsel = _ms.msseltoindex(vis=vis, spw=spw)['spw']
        thefieldsel = _ms.msseltoindex(vis=vis, field=field)['field']
        outgrid =  _ms.cvelfreqs(spwids=thespwsel, fieldids=thefieldsel,
                                 mode=mode, nchan=nchan, start=start, width=width,
                                 phasec=newphasecenter, restfreq=restfreq,
                                 outframe=outframe, veltype=veltype, verbose=False)
        if(len(outgrid)>1):
            tmpavwidth = []
            for thespw in thespwsel:
                outgridw1 =  _ms.cvelfreqs(spwids=[thespw], fieldids=thefieldsel,
                                           mode='channel', nchan=-1, start=0, width=1, # native width
                                           phasec=newphasecenter, restfreq=restfreq,
                                           outframe=outframe, veltype=veltype, verbose=False)
                if(len(outgridw1)>1):
                    widthratio = abs((outgrid[1]-outgrid[0])/(outgridw1[1]-outgridw1[0]))                    
                    if(widthratio>=2.0): # do preaverage
                        tmpavwidth.append( int(widthratio+0.001) )
                        dopreaverage=True
                else:
                    tmpavwidth.append(1)

            if dopreaverage:
                preavwidth = tmpavwidth

        _ms.close()

        # if in channel mode and preaveraging, 
        if(dopreaverage and (mode=='channel' or mode=='channel_b')):
            if(max(preavwidth)==1):
                dopreaverage = False
            else:
                # switch to frequency mode
                mode = 'frequency'
                if(width>0):
                    start = str(outgrid[0]/1E6)+'MHz'
                    width = str((outgrid[1]-outgrid[0]))+'Hz'
                else:
                    start = str(outgrid[len(outgrid)-1]/1E6)+'MHz'
                    width = str(-(outgrid[1]-outgrid[0]))+'Hz'
                casalog.post("After pre-averaging, will switch to frequency mode with start="+start+", width = "+width, 'INFO')

        if(dopreaverage and hanning and max(preavwidth)>2):
            casalog.post("NOTE: You have requested Hanning smoothing and at the same time you have chosen\n"
                         +"a large width parameter which makes pre-averaging necessary.\n"
                         +"The Hanning-smoothing may be redundant in this context.\n", 'WARN')

        if dopreaverage:
            # Past this point we know we are going to 'dopreaverage'
            # CAS-9798
            raise RuntimeError('ERROR: cvel does not regrid properly for channel '
                               'widths > or = 2x the native channel width, please use '
                               'mstransform, clean, or tclean for larger regridding. '
                               'All earlier versions of CASA also have this issue.')
            
        # determine parameter "datacolumn"
        _tb.open(vis)
        allcols = _tb.colnames()
        _tb.close()
        dpresent = ('DATA' in allcols)
        mpresent = ('MODEL_DATA' in allcols)
        cpresent = ('CORRECTED_DATA' in allcols)
        if (dpresent and cpresent):
            datacolumn = 'all'
        elif (dpresent and not cpresent):
            datacolumn = 'data'
        elif (cpresent and not dpresent):
            datacolumn = 'corrected_data'
        elif (mpresent and not cpresent and not dpresent):
            datacolumn = 'model_data'
        else:
            raise RuntimeError("Neither DATA nor CORRECTED_DATA nor MODEL_DATA column present. Cannot proceed.")

        if(doselection and not dopreaverage):
            casalog.post("Creating selected SubMS ...", 'INFO')
            _ms.open(vis)
            _ms.split(outputms=outputvis, field=field,
                      spw=spw,            step=[1],
                      baseline=antenna,   subarray=array,
                      timebin='-1s',      time=timerange,
                      whichcol=datacolumn,
                      scan=scan,          uvrange="")
            _ms.close()

        elif(dopreaverage and not doselection):
            if(hanning):
                casalog.post("Creating working copy for Hanning-smoothing ...", 'INFO')
                shutil.rmtree(outputvis+'TMP',ignore_errors=True)
                copy_ms(vis, outputvis+'TMP')
                _ms.open(outputvis+'TMP', nomodify=False)
                _ms.hanningsmooth(datacolumn=datacolumn)
                _ms.close()
                hanning = False
                _ms.open(outputvis+'TMP')
            else:
                _ms.open(vis)
                
            casalog.post("Creating preaveraged SubMS using widths "+str(preavwidth), 'INFO')
            _ms.split(outputms=outputvis, 
                      whichcol=datacolumn, step=preavwidth)
            _ms.close()

        elif(doselection and dopreaverage):
            if(hanning):
                casalog.post("Creating selected working copy for Hanning-smoothing ...", 'INFO')
                shutil.rmtree(outputvis+'TMP',ignore_errors=True)
                _ms.open(vis)
                _ms.split(outputms=outputvis+'TMP', field=field,
                          spw=spw,            step=[1],
                          baseline=antenna,   subarray=array,
                          timebin='-1s',      time=timerange,
                          whichcol=datacolumn,
                          scan=scan,          uvrange="")
                _ms.close()
                _ms.open(outputvis+'TMP', nomodify=False)
                _ms.hanningsmooth(datacolumn=datacolumn)
                _ms.close()
                hanning = False
                _ms.open(outputvis+'TMP')
                casalog.post("Creating preaveraged SubMS using widths "+str(preavwidth), 'INFO')
                _ms.split(outputms=outputvis, 
                          whichcol=datacolumn, step=preavwidth)
                _ms.close()
            else:
                casalog.post("Creating selected, preaveraged SubMS using widths "+str(preavwidth), 'INFO')
                _ms.open(vis)
                _ms.split(outputms=outputvis, field=field,
                          spw=spw,            step=preavwidth,
                          baseline=antenna,   subarray=array,
                          timebin='-1s',      time=timerange,
                          whichcol=datacolumn,
                          scan=scan,          uvrange="")
                _ms.close()
                
        else:
            # no selection or preaveraging necessary, just copy
            casalog.post("Creating working copy ...", 'INFO')
            shutil.rmtree(outputvis,ignore_errors=True)
            copy_ms(vis, outputvis)

        # Combine and if necessary regrid it
        _ms.open(outputvis, nomodify=False)

        message = "Using " + phasecentername + " as common direction for the output reference frame."
        casalog.post(message, 'INFO')

        if not _ms.cvel(mode=mode, nchan=nchan, start=start, width=width,
                        interp=interpolation,
                        phasec=newphasecenter, restfreq=restfreq,
                        outframe=outframe, veltype=veltype, hanning=hanning):
            _ms.close()
            raise RuntimeError("Error in regridding step ...")
        _ms.close()

        # deal with the passall option
        temp_suffix = ".deselected"
        if (passall):
            # determine range of fields
            fieldsel = _ms.msseltoindex(vis=vis, field=field)['field']
            _tb.open(vis+"/FIELD")
            nfields = _tb.nrows()
            _tb.close()
            fielddesel = ""
            for i in range(0,nfields):
                if not (i in fieldsel):
                    if not (fielddesel == ""):
                        fielddesel += ","
                    fielddesel += str(i)

            # determine range of SPWs
            spwsel = _ms.msseltoindex(vis=vis, spw=spw)['spw']
            _tb.open(vis+"/SPECTRAL_WINDOW")
            nspws = _tb.nrows()
            _tb.close()
            spwdesel = ""
            for i in range(0,nspws):
                if not (i in spwsel):
                    if not (spwdesel == ""):
                        spwdesel += ","
                    spwdesel += str(i)

            if not (fielddesel == "" and spwdesel == ""):        
                # split out the data not selected by the conditions on field and spw
                # from the original MS and join it to the output MS 

                # need to do this in two steps
                # I) field == "*" and deselected spws
                if not (spwdesel == ""):
                    _ms.open(vis)
                    casalog.post("Passing through data with", 'INFO')
                    casalog.post("      spws:   " + spwdesel, 'INFO')

                    _ms.split(outputms=outputvis+temp_suffix, field='*',
                              spw=spwdesel,            step=[1],
                              baseline=antenna,   subarray=array,
                              timebin='-1s',    time=timerange,
                              whichcol=datacolumn,
                              scan=scan,          uvrange="")
                    _ms.close()

                    # join with the deselected part
                    _ms.open(outputvis, nomodify=False)
                    rval = _ms.concatenate(msfile = outputvis+temp_suffix)
                    _ms.close()
                    shutil.rmtree(outputvis+temp_suffix)
                    if not rval:
                        raise RuntimeError("Error in attaching passed-through data ...")

                # II) deselected fields and selected spws
                if not (fielddesel == ""):
                    _ms.open(vis)
                    casalog.post("Passing through data with", 'INFO')
                    casalog.post("    fields: " + fielddesel, 'INFO')
                    casalog.post("      spws: " + spw, 'INFO')

                    _ms.split(outputms=outputvis+temp_suffix, field=fielddesel,
                              spw=spw,            step=[1],
                              baseline=antenna,   subarray=array,
                              timebin='-1s',    time=timerange,
                              whichcol=datacolumn,
                              scan=scan,          uvrange="")
                    _ms.close()
                    
                    # join with the deselected part
                    _ms.open(outputvis, nomodify=False)
                    rval = _ms.concatenate(msfile = outputvis+temp_suffix)
                    _ms.close()
                    shutil.rmtree(outputvis+temp_suffix)
                    if not rval:
                        raise RuntimeError("Error in attaching passed-through data ...")

        # Write history to output MS
        try:
            param_names = cvel.__code__.co_varnames[:cvel.__code__.co_argcount]
            if is_python3:
                vars = locals()
                param_vals = [vars[p] for p in param_names]
            else:
                param_vals = [eval(p) for p in param_names]
            write_history(mstool(), outputvis, 'cvel', param_names,
                          param_vals, casalog)
        except Exception as instance:
            casalog.post("*** Error \'%s\' updating HISTORY" % (instance),
                         'WARN')

    finally:
        # delete temp output (comment out for debugging)
        if os.path.exists(outputvis+".spwCombined"):
            casalog.post("Deleting temporary output files ...", 'INFO')
            shutil.rmtree(outputvis+".spwCombined")
