##################### generated by xml-casa (v2) from componentlist.xml #############
##################### 7d4015e3f5fdef976d4ceff68d49aa7f ##############################
from __future__ import absolute_import 
from .__casac__ import componentlist as _componentlist

from .platform import str_encode as _str_ec
from .platform import str_decode as _str_dc
from .platform import dict_encode as _dict_ec
from .platform import dict_decode as _dict_dc
from .platform import dict_encode as _quant_ec
from .platform import dict_decode as _quant_dc
from .platform import encode as _any_ec
from .platform import decode as _any_dc
from .errors import create_error_string
from .typecheck import CasaValidator as _validator
_pc = _validator( )
from .coercetype import coerce as _coerce


class componentlist:
    _info_group_ = """components"""
    _info_desc_ = """A tool for the manipulation of groups of components"""
    ### self
    def __init__(self, *args, **kwargs):
        """Use this constructor to construct a componentlist tool that does not
        contain any components. Components can be appended to the list using
        the addcomponent or simulate functions,
        and the list can be stored to disk by giving it a name with cl.rename
        
        """
        self._swigobj = kwargs.get('swig_object',None)
        if self._swigobj is None:
            self._swigobj = _componentlist()

    def open(self, filename='', nomodify=False, log=True):
        """Use this constructor to construct a componentlist tool by reading
        the data from an table. To ensure that this table contains
        all the necessary columns and to allow the table format to be
        enhanced in the future, it is highly recommended that the table be
        created using a componentlist tool.
        
        The table that contains the componentlist may be opened read-only by
        setting the readonly flag to True. When this is done some of the
        functions in the componentlist tool cannot be used. These include
        the ``set'', ``convert'', ``remove'', ``replace'', ``purge'',
        ``recover'', and ``sort'' functions.
        
        """
        return self._swigobj.open(_str_ec(filename), nomodify, log)

    def asciitocomponentlist(self, filename, asciifile, refer='J2000', format='ST', direction={ }, spectrum={ }, flux={ }, log=True):
        """This constructor will allow conversion of a number of ascii-file-based
        formats to componentlists.
        
        """
        return self._swigobj.asciitocomponentlist(_str_ec(filename), _str_ec(asciifile), _str_ec(refer), _str_ec(format), _dict_ec(direction), _dict_ec(spectrum), _dict_ec(flux), log)

    def concatenate(self, list=[ ], which=[ int(-1) ], log=True):
        """The concatenate function copies the specified component(s), from
        the specified to list, to the end of the current list.  The
        components are specified by numbering them from one to the length
        of the list.  You cannot append components to a list that has been
        opened read only but the list you are copying from may be
        readonly.
        
        You use a vector of indices to copy a number of components at
        once. By default all components are copied.
        
        """
        return self._swigobj.concatenate(_any_ec(list), which, log)

    def fromrecord(self, record={ }):
        """This function allows the componentlist records that are returned
        by other functions (for e.g from imageanalysis tool) be converted
        to a tool to be manipulated or to be saved on disk
        
        
        """
        return self._swigobj.fromrecord(_dict_ec(record))

    def torecord(self):
        """This function allows the componentlist to be converted to a
        record. Usually useful to pass to other functions in image
        analysis for e.g
        
        
        """
        return _dict_dc(self._swigobj.torecord())

    def remove(self, which=[ int(-1) ], log=True):
        """The remove function removes the specified component(s) from the
        list. Components are specified by numbering them from one to the
        length of the list. So removing component one will remove the
        first component. After using this function all the
        remaining components will be shuffled down so that component two
        becomes component one.  You cannot remove components from a list
        that has been opened read only.
        
        You can specify a vector of indices to remove a number of
        components at once. For example in a five element list removing
        elements [1,3,5] will result in a two element list, now indexed as
        elements one and two, containing what was previously the second
        and fourth components.
        
        Components that have been deleted using this function are not
        lost. The recover function can be used to get them back unless the
        purge function has been executed. Then they are completely gone.
        
        
        """
        return self._swigobj.remove(which, log)

    def purge(self):
        """The remove function deletes components from the list but does not
        remove them from memory. They remain accessible and can be
        obtained with the recover function. The purge function frees up
        the memory occupied by the removed components. You cannot use the
        recover function to obtain the removed components after the purge
        function has been called.
        
        
        """
        return self._swigobj.purge()

    def recover(self, log=True):
        """The recover function appends components to the end of the list
        that have been deleted with the remove function. This does not
        include components that were removed before the purge function was
        last executed.
        
        """
        return self._swigobj.recover(log)

    def length(self):
        """The length function returns a non-negative integer that
        indicates how many components the list currently contains.
        
        """
        return self._swigobj.length()

    def indices(self):
        """The indices function will returns a vector of non-negative
        integers that can be used to index through the list. This vector
        always contains the integers starting at one and increasing
        sequentially to the length of the list. Its main use is in for
        loops as is illustrated in the example below.
        
        """
        return self._swigobj.indices()

    def sort(self, criteria='Flux', log=True):
        """The sort function can sort all the components in a list using a
        variety of criteria. Currently the following criteria are
        available:
        Flux: Sorts the list so that the brightest components,
        as defined by Stokes I, are at the beginning of the list.
        Position: Sorts the list so that components that are
        closest to a reference position, which is currently fixed at
        (ra,dec)=(0,0), are at the beginning of the list.
        Polarization: Sorts the list so that components with the
        largest fractional polarization, sqrt(Q**2+U**2+V**2)/I, are
        at the front of the list. Components where I=0 are placed at
        the end of the list.
        The parsing of the string containg the sorting criteria is case
        insensitive. You cannot sort a list that has been opened read only.
        
        """
        return self._swigobj.sort(_str_ec(criteria), log)

    def isphysical(self, which=[ int(-1) ]):
        """The isphysical function is used to check if the specified
        components meet a number of criteria that must be true if the
        component could be used to model a physical process. These
        criteria are:
        1. I >= sqrt(Q**2 + U**2 + V**2)
        2. That the flux, when represented using the Stokes
        representation, has a zero imaginary value.
        
        The ``Flux properties'' section of the ComponentModels module
        documentation describes how it is possible to generate a
        component which has non-zero imaginary value in the Stokes
        representation.
        
        It is possible to check a number of components at once by
        specifying the indicies of all the components. The returned value
        will only be True if all the specified components are physical.
        
        
        """
        return self._swigobj.isphysical(which)

    def sample(self, direction=[ ], pixellatsize=[ ], pixellongsize=[ ], frequency=[ ]):
        """The sample function will returns a vector containing the flux in
        Janskys/pixel of all the components in the list, in the specified
        direction, at the specified frequency. The returned vector always
        contains four elements corresponding to the Stokes parameters
        I,Q,U,V.
        
        
        """
        return self._swigobj.sample(_any_ec(direction), _any_ec(pixellatsize), _any_ec(pixellongsize), _any_ec(frequency))

    def rename(self, filename, log=True):
        """The rename function is used to specify the name of the table
        associated with this componentlist.
        
        When a componentlist is created it is not associated with an casa
        table. So when the componentlist is removed from memory its
        contents are lost. But if a name is attached to the componentlist,
        using the rename function, then its contents are saved in a table
        with the specified name when the componentlist is closed
        
        NOTE: that by just using rename the componentlist is not ensured
        to be on disk; to be sure use close after rename
        
        If the componentlist is created using the open() constructor then
        this function will rename the table associated with the list to
        the user specified name. You cannot rename a componentlist that
        has been opened read only.
        
        
        
        
        """
        return self._swigobj.rename(_str_ec(filename), log)

    def simulate(self, howmany=int(1), log=True):
        """The simulate function adds simulated components to the list. The
        simulation criterion is very simple, all the components added are
        identical! They are point sources at the J2000 north pole with a
        flux in Stokes I of 1~Jy, and zero in the other polarizations. The
        spectrum is constant. The 'set' functions (eg. setflux, setfreq)
        can be used to change these parameters to desired ones.
        
        The howmany argument indicates how many components to append to
        the list.
        
        """
        return self._swigobj.simulate(howmany, log)

    def addcomponent(self, flux=[ ], fluxunit='Jy', polarization='Stokes', dir=[ ], shape='point', majoraxis=[ ], minoraxis=[ ], positionangle=[ ], freq=[ ], spectrumtype='constant', index=[ ], optionalparms=[ float(0.0) ], label=''):
        """The addcomponent function is a convenience function that ties
        together the simulate function, and the various set
        functions. This function adds a component to the end of the
        list. For a description of the arguments see the following
        functions.
        [flux, fluxunit, polarization] See setflux
        [ra, raunit, dec, decunit] See setrefdir
        [dirframe] See setrefdirframe
        [shape, majoraxis, minoraxis, positionangle] See setshape
        [freq] A frequency quantity which is split into a value and
        units and passed to the setfreq function
        [freqframe] See setfreq
        [spectrumtype, index] The spectral index alpha such that flux density S
        as a function of frequency nu is: S~nu**alpha.
        See also the setspectrum or setstokesspectrum functions.
        [label] See setlabel
        
        """
        return self._swigobj.addcomponent(_any_ec(flux), _str_ec(fluxunit), _str_ec(polarization), _any_ec(dir), _str_ec(shape), _any_ec(majoraxis), _any_ec(minoraxis), _any_ec(positionangle), _any_ec(freq), _str_ec(spectrumtype), _any_ec(index), optionalparms, _str_ec(label))

    def close(self, log=True):
        """The close function resets the componentlist to its default state. In
        this state it contains no components and is not associated with
        any table.
        
        This function flushes all the components in memory to disk if the
        componentlist is associated with a table. The table is then
        closed, and the contents of the list deleted.
        
        If the list is not associated with a table its contents are still
        deleted and memory used by the list is released.
        
        """
        return self._swigobj.close(log)

    def edit(self, which, log=True):
        """
        """
        return self._swigobj.edit(which, log)

    def done(self):
        """The done function frees up all the memory associated with a
        componentlist tool. After calling this function the componentlist
        tool cannot be used, either to manipulate the current list, or
        to open a new one. This function does not delete the disk
        file associated with a componentlist, but it will shut down the
        server process if there are no other componentlist tools being used.
        
        """
        return self._swigobj.done()

    def select(self, which):
        """The select function is used to mark the specified components as
        ``selected''. This function will be used in conjunction with the
        planned graphical user interface. Other functions functions in the
        componentlist tool will behave no differently if a component is
        marked as ``selected''.
        
        Components are not selected when the list is initially read
        from disk or when a new component is added to the list using the
        simulate function.
        
        """
        return self._swigobj.select(which)

    def deselect(self, which):
        """The deselect function is used to remove the ``selected'' mark from
        specified components in the list. This function wiil be used in
        conjunction with the planned graphical user interface and no other
        functions in the componentlist will behave differently if a
        component is marked as ``selected'' or not.
        
        Components are not selected when the list is initially read from
        disk or when a new component is added to the list using the
        simulate function.  function. Deselecting a component that is
        already deselected is perfectly valid and results in no change.
        
        """
        return self._swigobj.deselect(which)

    def selected(self):
        """The selected function is used to determine which components in a
        list are selected. It returns a vector with indices that indicate
        which components are selected. A zero length vector is returned if
        no components are selected.
        
        Components are marked as selected using the
        select
        function. This function will be used in conjunction with the
        graphical user interface and other functions in the componentlist
        tool will behave no differently if a component is marked as
        ``selected'' or not.
        
        
        """
        return self._swigobj.selected()

    def getlabel(self, which):
        """The getlabel function returns the label associated with the specified
        component. The label is an arbitrary text string that can be used
        to tag a component.
        
        """
        return _str_dc(self._swigobj.getlabel(which))

    def setlabel(self, which, value, log=True):
        """The setlabel function is used to reassign the label (an arbitrary
        text string) of the specified components to
        a new value.
        
        """
        return self._swigobj.setlabel(which, _str_ec(value), log)

    def getfluxvalue(self, which):
        """The getfluxvalue function returns the value of the flux of the
        specified component using the current units and the current
        polarization representation. The functions
        getfluxunit &
        getfluxpol &
        can be used to get the units and polarization
        representation that corresponds to the supplied value.
        
        """
        return self._swigobj.getfluxvalue(which)

    def getfluxunit(self, which):
        """The getfluxunit function returns the units of the flux of the
        specified component. The actual values are obtained using the
        getfluxvalue function.
        
        """
        return _str_dc(self._swigobj.getfluxunit(which))

    def getfluxpol(self, which):
        """The getfluxunit function returns the polarization representation
        of the flux of the specified component. The actual values are
        obtained using the
        getfluxvalue
        function.
        
        """
        return _str_dc(self._swigobj.getfluxpol(which))

    def getfluxerror(self, which):
        """The getfluxerror function returns the error in the flux of the
        specified component using the current units and the current
        polarization representation. The functions
        getfluxvalue &
        getfluxunit &
        getfluxpol &
        can be used to get the value, units and polarization
        representation that corresponds to the specified error.
        
        No error calculations are done by this tool. The error can be
        stored and retreived and if any of the parameters of the flux
        change the user is responsible for updating the errors.
        
        """
        return self._swigobj.getfluxerror(which)

    def setflux(self, which, value=[ ], unit='Jy', polarization='Stokes', error=[ ], log=True):
        """The setflux function is used to reassign the flux of the
        specified components to a new value. The flux value, unit and
        polarization can be specified and any number of components can be
        set to the new value.  (Currently, the parameter, error is
        ignored.)
        
        """
        return self._swigobj.setflux(which, _any_ec(value), _str_ec(unit), _str_ec(polarization), _any_ec(error), log)

    def convertfluxunit(self, which, unit='Jy'):
        """The convertfluxunit function is used to convert the flux to another
        unit. The units emph{must} have the same dimensions as the Jansky.
        
        """
        return self._swigobj.convertfluxunit(which, _str_ec(unit))

    def convertfluxpol(self, which, polarization='Stokes'):
        """The convertfluxpol function is used to convert the flux to another
        polarization representation. There are are three representations
        used, namely , 'Stokes', 'linear' & 'circular'
        
        """
        return self._swigobj.convertfluxpol(which, _str_ec(polarization))

    def getrefdir(self, which):
        """The getrefdir function returns, as a direction measure, the
        reference direction for the specified component. The reference
        direction is for all the currently supported component shapes the
        direction of the centre of the component.
        
        """
        return _dict_dc(self._swigobj.getrefdir(which))

    def getrefdirra(self, which, unit='deg', precision=int(6)):
        """
        """
        return _str_dc(self._swigobj.getrefdirra(which, _str_ec(unit), precision))

    def getrefdirdec(self, which, unit='deg', precision=int(6)):
        """The getrefdirdec function returns the declination of the reference
        direction of the component as a formatted string. If the reference
        frame is something other than J2000 or B1950 the value returned is
        the longitude or the altitude.
        
        See the getrefdirra function for a description of the unit and
        precision arguments.
        
        
        """
        return _str_dc(self._swigobj.getrefdirdec(which, _str_ec(unit), precision))

    def getrefdirframe(self, which):
        """The getrefdirframe function returns the reference frame of the reference
        direction of the component as a string. The returned string is
        always in upper case. Common frames are, 'J2000', 'B1950' and 'GALACTIC'.
        
        
        """
        return _str_dc(self._swigobj.getrefdirframe(which))

    def setrefdir(self, which=int(1), ra=[ ], dec=[ ], log=True):
        """The setrefdir function sets the reference direction of the
        specified components to a new value. The direction is defined by
        separately specifying the right ascension and the declination.
        
        The right ascension is specified as a string or a real number
        
        Ra can be in standard angle units 'deg', 'rad', or time formatted as such 'HH:MM:SS.sss'
        eg., '19:34:63.8' or angle formatted as such  '+DDD.MM.SS.sss' eg.,
        '127.23.12.37'.
        
        Similarly the declination is specified as a string or a real
        number and the decunit can be any angular unit or 'angle' or
        'time'.
        
        """
        return self._swigobj.setrefdir(which, _any_ec(ra), _any_ec(dec), log)

    def setrefdirframe(self, which, frame, log=True):
        """The setrefdirframe function sets the reference frame for the
        reference direction of the specified components (what a mouthful)!
        
        Currently the reference frame does not include additional
        information like when and where the observation took place. Hence
        only reference frames that are independent of this information can be
        used. This includes the common ones of 'J2000', 'B1950', and
        'Galactic'. The measures module contains a
        complete listing of all possible reference frames. The parsing of
        the reference frame string is case-insensitive.
        
        
        """
        return self._swigobj.setrefdirframe(which, _str_ec(frame), log)

    def convertrefdir(self, which, frame):
        """The convertrefdir function changes the specified components to use a
        new direction reference frame. Using this function will change the
        right-ascension and declination of the component(s), unlike the
        setrefdirframe which does not.
        
        Please see the
        setrefdirframe
        function for a description of what frames are allowed.
        
        
        """
        return self._swigobj.convertrefdir(which, _str_ec(frame))

    def shapetype(self, which):
        """The shapetype function returns the current shape of the specified
        component. The shape defines how the flux of the component varies
        with direction on the sky. Currently there are three shapes
        available. These are 'Point', 'Gaussian', and 'Disk'. This
        function returns one of these four strings.
        
        
        """
        return _str_dc(self._swigobj.shapetype(which))

    def getshape(self, which):
        """The getshape function returns the shape parameters of a component
        in a record. As different shapes can have a differing number and
        type of parameters the shape parameters are returned in a record
        with fields that correspond to parameters relevant to the current
        shape.
        
        For a point shape there are only two fields; type and
        direction. These are the shape type, and the reference
        direction. These values are also returned by the
        shapetype and
        getrefdir
        functions.
        
        For both the Gaussian and disk shapes there are three additional
        fields; majoraxis, minoraxis, positionangle. These are angular
        quantities, and hence are records with a value
        and a unit.
        
        
        """
        return _dict_dc(self._swigobj.getshape(which))

    def setshape(self, which, type='Point', majoraxis=[ ], minoraxis=[ ], positionangle=[ ], majoraxiserror=[ ], minoraxiserror=[ ], positionangleerror=[ ], optionalparms=[ float(0.0) ], log=True):
        """The setshape function changes the shape of the specified components
        to the user specified shape.
        
        The type argument defines what the sort of new shape to use. This
        can be either 'point', 'Gaussian', or 'disk'.
        The parsing of this string is case insensitive.
        
        
        If the shape type is 'point' then the remaining arguments in this
        function are ignored. There are no other parameters needed to
        specify a point shape.
        
        But if the shape is 'Gaussian', or 'disk',
        the remaining arguments are needed to fully specify the shape.
        The majoraxis, minoraxis and positionangle arguments are quantities (see the
        quanta module for a definition of a
        quantity). Hence they can be specified either as with string eg.,
        '1arcsec' or with a record eg., [value=1, unit='deg'].
        
        The major axis is the width of the larger axis. For the Gaussian
        shape this is the full width at half maximum. And the minor axis
        is the width of the orthogonal axis. The positionangle is the
        specifies the rotation of these two axes with respect to a line
        connecting the poles of the current direction reference frame. If
        the angle is positive the the north point of the component moves
        in the eastern direction.
        
        
        """
        return self._swigobj.setshape(which, _str_ec(type), _any_ec(majoraxis), _any_ec(minoraxis), _any_ec(positionangle), _any_ec(majoraxiserror), _any_ec(minoraxiserror), _any_ec(positionangleerror), optionalparms, log)

    def convertshape(self, which, majoraxis='arcmin', minoraxis='arcmin', positionangle='deg'):
        """
        """
        return self._swigobj.convertshape(which, _str_ec(majoraxis), _str_ec(minoraxis), _str_ec(positionangle))

    def spectrumtype(self, which):
        """The spectrumtype function returns the current spectral shape of the
        specified component. The spectral shape defines how the flux of
        the component varies with frequency. Returns one of "Constant",
        "Spectral Index", "Tabular Spectrum", and "Power Logarithmic Polynomial".
        
        
        """
        return _str_dc(self._swigobj.spectrumtype(which))

    def getspectrum(self, which):
        """The getspectrum function returns the spectral parameters of a
        component in a record. As different spectral shapes can have a
        differing number and type of parameters the spectral parameters
        are returned in a record with fields that correspond to parameters
        relevant to the current spectral shape.
        
        For a constant spectrum there are only two fields; type and
        frequency. These are the spectral type, and the reference
        frequency. These values are also returned by the
        spectrumtype and
        getfreq
        functions.
        
        For the spectral index spectral shape there is also an index
        field.  This contains a vector with four numbers, these are the
        spectral indicies for the I,Q,U,V components of the flux.
        
        The dictionary associated with a power log polynomial spectrum has the following structure:
        
        {
        'coeffs': array([ 1.,  2.,  3.]),
        'frequency': {
        'type': 'frequency',
        'm0': {'value': 1.4200000000000002, 'unit': 'GHz'},
        'refer': 'LSRK'
        },
        'type': 'Power Logarithmic Polynomial',
        'error': array([ 0.,  0.,  0.])
        }
        
        The 'error' value is currently not used.
        
        
        
        """
        return _dict_dc(self._swigobj.getspectrum(which))

    def setstokesspectrum(self, which, type='spectral index', index=[ float(0.0) ], tabularfreqs=[ float(1.0e11) ], tabulari=[ float(1.0) ], tabularq=[ float(0.0) ], tabularu=[ float(0.0) ], tabularv=[ float(0.0) ], reffreq=[ ], frame='LSRK'):
        """The setstokesspectrum function changes the spectrum of the specified components
        to the user specified spectrum. This is different from setspectrum as it provides ways to control variation of all 4 Stokes parameters with frequency. If only I variation is needed please use setspectrum
        
        The type argument defines what the sort of new spectrum to use. This
        can be either 'constant' or 'spectral index' or 'tabular'. The parsing of this
        string is case insensitive.
        
        If the spectrum type is 'constant' then the remaining arguments in
        this function are ignored. There are no other parameters needed to
        specify a constant spectrum.
        
        But if the spectrum is 'spectral index', the 'index' argument is
        needed. It is a 4 element vector.
        
        The first element ($alpha_0$) is the spectral index of stokes I ($ I(nu)=I(nu_0)({{nu}over{nu_0}})^{alpha_0} $)
        
        The second element ($alpha_1$) is a spectral index for the fractional linear polarization ( $sqrt{{{(Q(nu)^2+U(nu)^2)}over{I(nu)^2}}} =   sqrt{{{(Q(nu_0)^2+U(nu_0)^2)}over{I(nu_0)^2}}}({{nu}over{nu_0}})^{alpha_1}$). $alpha_1=0$ implies constant fractional linear polarization w.r.t frequency.
        
        The third element is a "Rotation Measure" factor, i.e angle of rotation $theta= alpha_2 (lambda^2 - lambda_0^2)$ of the linear polarization at frequency $nu$ w.r.t  frequency $nu_0$.
        
        The fourth element  is a spectral index for the fractional spectral polarization ( $ {{V(nu)}over{I(nu)}} =   {{V(nu_0)}over{I(nu_0)}}({{nu}over{nu_0}})^{alpha_3}$
        
        If the spectrum is 'tabular', then {tt index} is ignored but the six parameters
        {tt tabularfreqs, tabulari, tabularq, tabularu, tabularv and tabularframe} are considered. {tt tabularfreqs} and {tt tabulari, tabularq, tabularu, tabularv} have to be list of same lengths and larger than 2. You need at least 2 samples to interpolate the spectral value in between.
        The Stokes parameters  of the source is interpolated from these values. Extrappolation outside the range given in {tt tabularfreqs} is not done.
        {tt tabularfreqs} should be float values in 'Hz'
        {tt tabulari, tabularq, tabularu, tabularv} should be float values in 'Jy'
        
        
        You should ensure that the reference
        frequency is set to the value you desire, using the
        setfreq
        function if you change to the spectral index shape.
        
        
        """
        return self._swigobj.setstokesspectrum(which, _str_ec(type), index, tabularfreqs, tabulari, tabularq, tabularu, tabularv, _any_ec(reffreq), _str_ec(frame))

    def setspectrum(self, which, type='spectral index', index=[ ], tabularfreqs=[ float(1.0e11) ], tabularflux=[ float(1.0) ], tabularframe='LSRK'):
        """The setspectrum function changes the spectrum of the specified components
        to the user specified spectrum.
        
        The type argument defines what the sort of new spectrum to use. This
        can be one of 'constant', 'tabular', 'plp', or 'spectral index'. Minimal
        match, case insensitive.
        
        If the spectrum type is 'constant' then the remaining arguments in
        this function are ignored. There are no other parameters needed to
        specify a constant spectrum. The reference frequency is set to be
        the same value as the component being replaced. Although this is
        unimportant for a constant spectrum, it may be important if
        the spectral model of the component in question is changed again
        later. See rules to how the reference frequencies of various spectral
        models are set in the description below.
        
        If the spectrum is 'spectral index', the 'index' argument is
        needed to fully specify the spectrum by using the index argument. The
        index parameter may be in the form of a single numerical value, or
        an array containing a numerical value. In the case of the array containing
        multiple values, the zeroth value is used as the value of index, while
        subsequent values are tacitly ignored. The functional form of this model
        is
        
        R = x^(alpha)
        
        where R = I_nu/I_nu0 is the ratio of the intensities at observed frequency nu
        and the reference frequency nu_0, x = nu/nu_0, and alpha is the specified
        spectral index. The reference frequency is tacitly set to that of the component
        being replaced. and can be changed by a subsequent call to setfreq().
        
        If spectrum = 'plp', then the spectral model is set to a power log polynomial.
        The functional form of this model is
        
        R = x^(c_0 + c_1*(ln(x)) + c_2*(ln(x))^2 + c_3*(ln(x))^3 + ... + c_n*(ln(x))^n)
        
        where R = I_nu/I_nu0 is the ratio of the intensities at observed frequency nu
        and the reference frequency nu_0, x = nu/nu_0, ln is the natural logarithm, and
        c_0 ... c_n are the coefficients specified by index. In this case, index should
        be an array of numerical values, and the array length is unconstrained. The
        reference frequency is tacitly set to that of the component being replaced, and
        can be changed by a subsequent call to setfreq().
        
        If the spectrum is 'tabular', then 'index' is ignored but the
        three parameters 'tabularfreqs', 'tabularflux' and 'tabularframe'
        are considered. 'tabularfreqs' and 'tabularflux' have to be list
        of same lengths and larger than 2. You need at least 2 samples to
        interpolate the spectral value in between.  The flux of the source
        is interpolated from these values. Extrapolation outside the range
        given in 'tabularfreqs' is not done.
        'tabularfreqs' should be float values in 'Hz'
        'tabularflux' should be float values in 'Jy'
        The reference frequency is chosen to be the zeroth element of tabularfreqs.
        
        
        
        You should ensure that the reference
        frequency is set to the value you desire, using the
        setfreq
        function if you change to the spectral index shape.
        
        
        """
        return self._swigobj.setspectrum(which, _str_ec(type), _any_ec(index), tabularfreqs, tabularflux, _str_ec(tabularframe))

    def getfreq(self, which):
        """
        """
        return _dict_dc(self._swigobj.getfreq(which))

    def getfreqvalue(self, which):
        """
        """
        return self._swigobj.getfreqvalue(which)

    def getfrequnit(self, which):
        """
        """
        return _str_dc(self._swigobj.getfrequnit(which))

    def getfreqframe(self, which):
        """
        """
        return _str_dc(self._swigobj.getfreqframe(which))

    def setfreq(self, which, value, unit='GHz', log=True):
        """The setfreq function sets the reference frequency of the specified
        components to a new value. The frequency is defined by separately
        specifying the value and its units. Use the
        setfreqframe
        function to set the frequency reference frame
        
        
        """
        return self._swigobj.setfreq(which, value, _str_ec(unit), log)

    def setfreqframe(self, which, frame='LSRK', log=True):
        """The setfreqframe function sets the reference frame for the
        reference frequency of the specified components.
        
        Currently the reference frame does not include additional
        information like when are where the observation took place. Hence
        no conversion between reference frames is available. In the
        interim I recommend you always use the same frame.
        
        
        """
        return self._swigobj.setfreqframe(which, _str_ec(frame), log)

    def convertfrequnit(self, which, unit='GHz'):
        """The convertfrequnit function changes the specified components to use
        a new unit for the reference frequency. Using this function will
        change the frequency value also so that the overall reference
        frequency is not changed. It will affect the values and units
        obtained with
        setfreqvalue
        function.
        
        Any unit can be used that has the same dimensions as the 'Hz'.
        
        
        """
        return self._swigobj.convertfrequnit(which, _str_ec(unit))

    def getcomponent(self, which, iknow=False):
        """The component function returns a record, showing the current state
        of the specified component in the list.
        
        Modifying the record that is returned by this function does not
        modify the component in the list. To do this you must remove the
        component from the list, using the
        remove function,
        and add the modified component using the
        add function, or use
        the replace object
        function.  This function will be removed in a future release of
        and you are urged to use the get functions to extract
        information about a component.
        
        
        """
        return _dict_dc(self._swigobj.getcomponent(which, iknow))

    def add(self, thecomponent, iknow=True):
        """The add function adds a component to the component
        list. You cannot add components to a list that has been opened
        read only. To use this function you need to know the details of
        the record format. however this has been deprecated and you are
        urged to use the set functions, in conjunction with the simulate
        function to add a component to the list.
        
        
        """
        return self._swigobj.add(_dict_ec(thecomponent), iknow)

    def replace(self, which, list, whichones=[ int(-1) ]):
        """The replace function replaces the components from the list with
        the specified components from another list. The source list can be
        opened readonly and the length of the vectors in the first and
        third arguments must the the name.
        
        You cannot replace components in a list that has been opened read
        only.
        
        
        """
        return self._swigobj.replace(which, _dict_ec(list), whichones)

    def summarize(self, which=int(-1)):
        """The summarize function summarizes the contents of the specified components to the logger.
        
        """
        return self._swigobj.summarize(which)

    def iscomponentlist(self, tool=[ ]):
        """This global function can be used to determine if the supplied
        argument is a componentlist tool. If so it returns True, otherwise
        it returns False.
        
        """
        return self._swigobj.iscomponentlist(_any_ec(tool))

