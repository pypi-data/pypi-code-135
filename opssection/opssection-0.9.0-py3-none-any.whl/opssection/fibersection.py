
import copy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import matplotlib.patches as matpach
import matplotlib.lines as matline
import math
import os
import webbrowser
import numpy as np

colors = [1, 'c', 2, 'm', 3, '0.8', 4, '0.8']
def setmatcolors(*args):
    global colors
    if len(args) % 2 != 0:
        raise ValueError("setmatcolors: Arguments must be matTag, color pairs")
    colors = list(args)
    pass

class FrameSection:
    def __init__(self, name, tag):
       self.secTag = tag
       self.Name = name

    def __get_tag(self):
            return self._secTag

    def __set_tag(self, tag):
        if (type(tag) != int):
            raise ValueError("Section tag must be positive integer value")
        if (tag <= 0):
            raise ValueError("Section tag must be positive integer value")

        self._secTag = tag

    def __del_tag(self):
        del self._secTag

    secTag = property(__get_tag, __set_tag, __del_tag)



    def __get_name(self):
            return self._Name

    def __set_name(self, name):
        self._Name = name

    def __del_name(self):
        del self._Name

    Name = property(__get_name, __set_name, __del_name)


## Tube Section
class Tube(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, tw, tf, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # w:       Flange Width
        # tw:      Web Thickness
        # tf:      Flange Thickness
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0)
        # zc:      z coordinate of the center of section(Optional, default = 0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)


        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.FlangeTh = tf
        self.WebTh = tw
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)


    # Width Validation
    def __get_width(self):
        return self._Width

    def __set_width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Width must be positive numeric value")

        self._Width = value

    def __del_width(self):
        del self._Width

    Width = property(__get_width, __set_width, __del_width)


    # Flange Thickness
    def __get_FlangeTh(self):
        return self._FlangeTh

    def __set_FlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._FlangeTh = value

    def __del_FlangeTh(self):
        del self._FlangeTh

    FlangeTh = property(__get_FlangeTh, __set_FlangeTh, __del_FlangeTh)

    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)


    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)


    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation


    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        patches = []
        # patch top flange
        yi, zi = h/2 -tf, w/2
        yj, zj = yi, -w/2
        yk, zk = h/2, zj
        yl, zl = yk, zi
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p1)

        # patch left web
        yi, zi = h / 2 - tf, w / 2
        yj, zj = -yi, zi
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p2)

        # patch bot flange
        yi, zi = -h / 2, w / 2
        yj, zj = yi, -w / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p3)

        # patch right web
        yi, zi = h / 2 - tf, -w / 2 + tw
        yj, zj = -yi, zi
        yk, zk = yj, -w / 2
        yl, zl = yi, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p4 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p4)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):

        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Total Width: " + str(self.Width))
        strprp.append("Flange Thickness: " + str(self.FlangeTh))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Tube")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
        ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Tube Section Parameters:")
        print("--------------------------------------------------")
        print("  Tube(name, sectag, mattag, h, w, tw, tf, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  w:       Flange Width")
        print("  tw:      Web Thickness")
        print("  tf:      Flange Thickness")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0)")


    ## End of PrintParams Function
################ End of Tube Class ########################

## I Section
class I(FrameSection):
    def __init__(self, name, sectag, mattag, h, wTop,wBot,tTop,tBot, tw, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0,yc=0.0, zc=0.0, rot=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # wTop:    Top Flange Width
        # tTop:    Top Flange Thickness
        # wBot:    Bottom Flange Width
        # tBot:    Bottom Flange Thickness
        # tw:      Web Thickness
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 1)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.TopWidth = wTop
        self.BotWidth = wBot
        self.TopFlangeTh = tTop
        self.BotFlangeTh = tBot
        self.WebTh = tw
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)



    # Width Validation
    def __get_TopWidth(self):
        return self._TopWidth

    def __set_TopWidth(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange width must be positive numeric value")

        self._TopWidth = value

    def __del_TopWidth(self):
        del self._TopWidth

    TopWidth = property(__get_TopWidth, __set_TopWidth, __del_TopWidth)

    def __get_BotWidth(self):
        return self._BotWidth

    def __set_BotWidth(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange width must be positive numeric value")

        self._BotWidth = value

    def __del_BotWidth(self):
        del self._BotWidth

    BotWidth = property(__get_BotWidth, __set_BotWidth, __del_BotWidth)



    # Flange Thickness
    def __get_TopFlangeTh(self):
        return self._TopFlangeTh

    def __set_TopFlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._TopFlangeTh = value

    def __del_TopFlangeTh(self):
        del self._TopFlangeTh

    TopFlangeTh = property(__get_TopFlangeTh, __set_TopFlangeTh, __del_TopFlangeTh)


    def __get_BotFlangeTh(self):
        return self._BotFlangeTh

    def __set_BotFlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._BotFlangeTh = value

    def __del_BotFlangeTh(self):
        del self._BotFlangeTh

    BotFlangeTh = property(__get_BotFlangeTh, __set_BotFlangeTh, __del_BotFlangeTh)


    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)


    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation

    def __Center(self):
        h = self.Height
        wTop = self.TopWidth
        wBot = self.BotWidth
        tTop = self.TopFlangeTh
        tBot = self.BotFlangeTh
        tw = self.WebTh
        A = wTop * tTop + wBot * tBot + (h - tTop - tBot)*tw
        QT = wTop * tTop * (h - tTop / 2)
        QB = wBot * tBot * tBot / 2
        Qw = (h - tTop - tBot)*tw * ((h - tTop - tBot)/2 + tBot)
        cy = (QT + QB + Qw) / A
        cz = 0.0
        return cy, cz

    ###### Create Patch Objects ########################
    def CreatePatches(self):

        h = self.Height
        wTop = self.TopWidth
        wBot = self.BotWidth
        tTop = self.TopFlangeTh
        tBot = self.BotFlangeTh
        tw = self.WebTh
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation

        patches = []
        # patch top flange
        cy, cz = self.__Center()
        ht = h - cy

        yi, zi = ht -tTop, wTop/2
        yj, zj = yi, -wTop/2
        yk, zk = ht, zj
        yl, zl = yk, zi
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p1)

        # patch web
        yi, zi = ht -tTop, tw / 2
        yj, zj = tBot - cy, zi
        yk, zk = yj, -tw/2
        yl, zl = yi, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p2)

        # patch bot flange
        yi, zi = -cy, wBot / 2
        yj, zj = yi, -wBot / 2
        yk, zk = yj + tBot, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p3)

        return patches
        ## End of CreatePatches Function



    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Top Flange Width: " + str(self.TopWidth))
        strprp.append("Top Flange Thickness: " + str(self.TopFlangeTh))
        strprp.append("Bottom Flange Width: " + str(self.BotWidth))
        strprp.append("Bottom Flange Thickness: " + str(self.BotFlangeTh))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: I")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("I Section Parameters:")
        print("--------------------------------------------------")
        print("  I(name, sectag, mattag, h, wTop,wBot,tTop,tBot, tw, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0,yc=0.0, zc=0.0, rot=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  wTop:    Top Flange Width")
        print("  tTop:    Top Flange Thickness")
        print("  wBot:    Bottom Flange Width")
        print("  tBot:    Bottom Flange Thickness")
        print("  tw:      Web Thickness")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of I Class ########################

## Angle Section
class Angle(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, tw, tf, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # w:       Total Width
        # tw:      Web Thickness
        # tf:      Flange Thickness
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 1)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.FlangeTh = tf
        self.WebTh = tw
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)


    # Width Validation
    def __get_width(self):
        return self._Width

    def __set_width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Width must be positive numeric value")

        self._Width = value

    def __del_width(self):
        del self._Width

    Width = property(__get_width, __set_width, __del_width)


    # Flange Thickness
    def __get_FlangeTh(self):
        return self._FlangeTh

    def __set_FlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._FlangeTh = value

    def __del_FlangeTh(self):
        del self._FlangeTh

    FlangeTh = property(__get_FlangeTh, __set_FlangeTh, __del_FlangeTh)

    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)


    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation

    def __Center(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh

        A = tw * h + (w - tw) * tf
        Qwy = tw * h * h /2
        Qfy = (w - tw) * tf * tf /2
        cy = (Qwy + Qfy ) / A
        Qwz = tw * h * ( w - tw /2)
        Qfz = (w - tw) * tf * (w - tw) / 2
        cz = (Qwz + Qfz ) / A

        return cy, cz
    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        cy, cz = self.__Center()
        patches = []

        # patch web
        yi, zi = h - cy, w - cz
        yj, zj = -cy, w - cz
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p1)

        # patch flange
        yi, zi = -cy, w - cz - tw
        yj, zj = -cy, -cz
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p2)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ

        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Total Width: " + str(self.Width))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Flange Thickness: " + str(self.FlangeTh))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Angle")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Angle Section Parameters:")
        print("--------------------------------------------------")
        print("  Angle(name, sectag, mattag, h, w, tw, tf, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  w:       Total Width")
        print("  tw:      Web Thickness")
        print("  tf:      Flange Thickness")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")


    ## End of PrintParams Function

################ End of Angle Class ########################



## Double Angle (Back to Back) Section
class DoubleAngle(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, tw, tf, db, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot =0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # w:       Total Width
        # tw:      Web Thickness
        # tf:      Flange Thickness
        # db:      Back to Back Distance
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.FlangeTh = tf
        self.WebTh = tw
        self.BDist = db
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)


    # Width Validation
    def __get_width(self):
        return self._Width

    def __set_width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Width must be positive numeric value")

        self._Width = value

    def __del_width(self):
        del self._Width

    Width = property(__get_width, __set_width, __del_width)


    # Flange Thickness
    def __get_FlangeTh(self):
        return self._FlangeTh

    def __set_FlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._FlangeTh = value

    def __del_FlangeTh(self):
        del self._FlangeTh

    FlangeTh = property(__get_FlangeTh, __set_FlangeTh, __del_FlangeTh)

    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)

    # Back to Back Distance
    def __get_BDist(self):
        return self._BDist

    def __set_BDist(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Back to Back Distance must be positive numeric value")

        if (value < 0):
            raise ValueError("Back to Back Distance must be positive numeric value")

        self._BDist = value

    def __del_BDist(self):
        del self._BDist

    BDist = property(__get_BDist, __set_BDist, __del_BDist)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)


    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation

    def __Center(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        A = tw * h + (w - tw) * tf
        Qwy = tw * h * h /2
        Qfy = (w - tw) * tf * tf /2
        cy = (Qwy + Qfy ) / A
        cz = 0

        return cy, cz
    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        db = self.BDist
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        cy, cz = self.__Center()
        patches = []

        # patch web 1
        yi, zi = h - cy, tw + db / 2
        yj, zj = -cy, zi
        yk, zk = yj, db / 2
        yl, zl = yi, zk
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p1)

        # patch web 2
        yi, zi = h - cy, -db /2
        yj, zj = -cy, zi
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p2)

        # patch flange 1
        yi, zi = -cy, w + db / 2
        yj, zj = -cy, tw + db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p3)

        # patch flange 2
        yi, zi = -cy, -1 * (tw + db / 2)
        yj, zj = -cy, -1 * (w + db / 2)
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p4 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p4)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion = 0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Flange Width: " + str(self.Width))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Flange Thickness: " + str(self.FlangeTh))
        strprp.append("Back to Back Distance: " + str(self.BDist))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Double Angle")
            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Double Angle Section Parameters:")
        print("--------------------------------------------------")
        print("  DoubleAngle(name, sectag, mattag, h, w, tw, tf, db, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot =0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  w:       Total Width")
        print("  tw:      Web Thickness")
        print("  tf:      Flange Thickness")
        print("  db:      Back to Back Distance")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")


    ## End of PrintParams Function

################ End of DoubleAngle Class ########################


## Channel Section
class Channel(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, tw, tf, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot =0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # w:       Total Width
        # tw:      Web Thickness
        # tf:      Flange Thickness
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.FlangeTh = tf
        self.WebTh = tw
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)


    # Width Validation
    def __get_width(self):
        return self._Width

    def __set_width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Width must be positive numeric value")

        self._Width = value

    def __del_width(self):
        del self._Width

    Width = property(__get_width, __set_width, __del_width)


    # Flange Thickness
    def __get_FlangeTh(self):
        return self._FlangeTh

    def __set_FlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._FlangeTh = value

    def __del_FlangeTh(self):
        del self._FlangeTh

    FlangeTh = property(__get_FlangeTh, __set_FlangeTh, __del_FlangeTh)

    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)


    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation

    def __Center(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        A = tw * h + (w - tw) * tf * 2
        cy = h / 2
        Qwz = tw * h * (w - tw / 2)
        Qfz = (w - tw) * tf * (w - tw)
        cz = (Qwz + Qfz ) / A

        return cy, cz
    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        cy, cz = self.__Center()
        patches = []

        # patch web
        yi, zi = h - cy , w - cz
        yj, zj = -cy, w - cz
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p1)

        # patch flange 1
        yi, zi = h - cy - tf, w - cz - tw
        yj, zj = yi, -cz
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p2)

        # patch flange 2
        yi, zi = -cy, w - cz - tw
        yj, zj = yi, -cz
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p3)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ

        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Total Width: " + str(self.Width))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Flange Thickness: " + str(self.FlangeTh))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Channel")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Channel Section Parameters:")
        print("--------------------------------------------------")
        print("  Channel(name, sectag, mattag, h, w, tw, tf, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot =0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  w:       Flange Width")
        print("  tw:      Web Thickness")
        print("  tf:      Flange Thickness")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")


    ## End of PrintParams Function

################ End of Channel Class ########################


## Double Channel ( Back to Back) Section
class DoubleChannelB(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, tw, tf, db, Nwl=6, Nfl=6, Nwt=1, Nft=1,gj=0, yc=0.0, zc=0.0, rot=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # w:       Flange Width
        # tw:      Web Thickness
        # tf:      Flange Thickness
        # db:      Back to Back Distance
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.FlangeTh = tf
        self.WebTh = tw
        self.BDist = db
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)


    # Width Validation
    def __get_width(self):
        return self._Width

    def __set_width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Width must be positive numeric value")

        self._Width = value

    def __del_width(self):
        del self._Width

    Width = property(__get_width, __set_width, __del_width)


    # Flange Thickness
    def __get_FlangeTh(self):
        return self._FlangeTh

    def __set_FlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._FlangeTh = value

    def __del_FlangeTh(self):
        del self._FlangeTh

    FlangeTh = property(__get_FlangeTh, __set_FlangeTh, __del_FlangeTh)

    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)

    # Back to Back Distance
    def __get_BDist(self):
        return self._BDist

    def __set_BDist(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Back to Back Distance must be positive numeric value")

        if (value < 0):
            raise ValueError("Back to Back Distance must be positive numeric value")

        self._BDist = value

    def __del_BDist(self):
        del self._BDist

    BDist = property(__get_BDist, __set_BDist, __del_BDist)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)


    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        db = self.BDist
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        patches = []

        # patch web 1
        yi, zi = h / 2, tw + db / 2
        yj, zj = -h / 2, zi
        yk, zk = yj, db / 2
        yl, zl = yi, zk
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p1)

        # patch web 2
        yi, zi = h / 2, -db /2
        yj, zj = -h / 2, zi
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p2)

        # patch flange 1
        yi, zi = h / 2 - tf, w + db / 2
        yj, zj = yi, tw + db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p3)

        # patch flange 2
        yi, zi = -h / 2 , w + db / 2
        yj, zj = yi, tw + db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p4 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p4)

        # patch flange 3
        yi, zi = h / 2 - tf, -tw - db / 2
        yj, zj = yi, -w - db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p5 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p5)

        # patch flange 4
        yi, zi = -h / 2, -tw - db / 2
        yj, zj = yi, -w - db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p6 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p6)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion = 0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Flange Width: " + str(self.Width))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Flange Thickness: " + str(self.FlangeTh))
        strprp.append("Back to Back Distance: " + str(self.BDist))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Double Channel (Back to Back)")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Double Channel (Back to Back) Section Parameters:")
        print("--------------------------------------------------")
        print("  DoubleChannelB(name, sectag, mattag, h, w, tw, tf, db, Nwl=6, Nfl=6, Nwt=1, Nft=1,gj=0, yc=0.0, zc=0.0, rot=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  w:       Flange Width")
        print("  tw:      Web Thickness")
        print("  tf:      Flange Thickness")
        print("  db:      Back to Back Distance")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")


    ## End of PrintParams Function

################ End of DoubleChannelB Class ########################


## Double Channel ( Face to Face) Section
class DoubleChannelF(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, tw, tf, df, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Total Height
        # w:       Total Width
        # tw:      Web Thickness
        # tf:      Flange Thickness
        # df:      Back to Back Distance
        # Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)
        # Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)
        # Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)
        # Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.FlangeTh = tf
        self.WebTh = tw
        self.FDist = df
        self.FlangeDivLength = Nfl
        self.FlangeDivTh = Nft
        self.WebDivLength = Nwl
        self.WebDivTh = Nwt
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)


    # Width Validation
    def __get_width(self):
        return self._Width

    def __set_width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Width must be positive numeric value")

        self._Width = value

    def __del_width(self):
        del self._Width

    Width = property(__get_width, __set_width, __del_width)


    # Flange Thickness
    def __get_FlangeTh(self):
        return self._FlangeTh

    def __set_FlangeTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange thickness must be positive numeric value")

        self._FlangeTh = value

    def __del_FlangeTh(self):
        del self._FlangeTh

    FlangeTh = property(__get_FlangeTh, __set_FlangeTh, __del_FlangeTh)

    # Web Thickness
    def __get_WebTh(self):
        return self._WebTh

    def __set_WebTh(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Web thickness must be positive numeric value")

        if (value <= 0):
            raise ValueError("Web thickness must be positive numeric value")

        self._WebTh = value

    def __del_WebTh(self):
        del self._WebTh

    WebTh = property(__get_WebTh, __set_WebTh, __del_WebTh)

    # Face to Face  Distance
    def __get_FDist(self):
        return self._FDist

    def __set_FDist(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Face to Face Distance must be positive numeric value")

        if (value < 0):
            raise ValueError("Face to Face Distance must be positive numeric value")

        self._FDist = value

    def __del_FDist(self):
        del self._FDist

    FDist = property(__get_FDist, __set_FDist, __del_FDist)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_FlangeDivLength(self):
        return self._FlangeDivLength

    def __set_FlangeDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivLength = val

    def __del_FlangeDivLength(self):
        del self._FlangeDivLength

    FlangeDivLength = property(__get_FlangeDivLength, __set_FlangeDivLength, __del_FlangeDivLength)


    # Subdivision Validation
    def __get_FlangeDivTh(self):
        return self._FlangeDivTh

    def __set_FlangeDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._FlangeDivTh = val

    def __del_FlangeDivTh(self):
        del self._FlangeDivTh

    FlangeDivTh = property(__get_FlangeDivTh, __set_FlangeDivTh, __del_FlangeDivTh)

    # Subdivision Validation
    def __get_WebDivLength(self):
        return self._WebDivLength

    def __set_WebDivLength(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivLength = val

    def __del_WebDivLength(self):
        del self._WebDivLength

    WebDivLength = property(__get_WebDivLength, __set_WebDivLength, __del_WebDivLength)

    # Subdivision Validation
    def __get_WebDivTh(self):
        return self._WebDivTh

    def __set_WebDivTh(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._WebDivTh = val

    def __del_WebDivTh(self):
        del self._WebDivTh

    WebDivTh = property(__get_WebDivTh, __set_WebDivTh, __del_WebDivTh)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation


    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        tf = self.FlangeTh
        tw = self.WebTh
        db = self.FDist
        Nfl = self.FlangeDivLength
        Nft = self.FlangeDivTh
        Nwl = self.WebDivLength
        Nwt = self.WebDivTh
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        patches = []

        # patch web 1
        yi, zi = h / 2, w + db / 2
        yj, zj = -h / 2, zi
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi,zi] = rotate([yi,zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p1)

        # patch web 2
        yi, zi = h / 2, -w - db /2 + tw
        yj, zj = -h / 2, zi
        yk, zk = yj, zj - tw
        yl, zl = yi, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Nwl, Nwt, self.matTag)
        patches.append(p2)

        # patch flange 1
        yi, zi = h / 2 - tf, w + db / 2 -tw
        yj, zj = yi, db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p3)

        # patch flange 2
        yi, zi = -h / 2 , w + db / 2 - tw
        yj, zj = yi, db / 2
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p4 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p4)

        # patch flange 3
        yi, zi = h / 2 - tf, -db / 2
        yj, zj = yi, -w - db / 2 + tw
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p5 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p5)

        # patch flange 4
        yi, zi = -h / 2, -db / 2
        yj, zj = yi, -w - db / 2 + tw
        yk, zk = yj + tf, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p6 = quad(y, z, Nfl, Nft, self.matTag)
        patches.append(p6)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion = 0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Total Height: " + str(self.Height))
        strprp.append("Flange Width: " + str(self.Width))
        strprp.append("Web Thickness: " + str(self.WebTh))
        strprp.append("Flange Thickness: " + str(self.FlangeTh))
        strprp.append("Face to Face Distance: " + str(self.FDist))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Double Channel (Face to Face)")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp

    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Double Channel (Face to Face) Section Parameters:")
        print("--------------------------------------------------")
        print("  DoubleChannelF(name, sectag, mattag, h, w, tw, tf, df, Nwl=6, Nfl=6, Nwt=1, Nft=1, gj=0, yc=0.0, zc=0.0, rot=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Total Height")
        print("  w:       Flange Width")
        print("  tw:      Web Thickness")
        print("  tf:      Flange Thickness")
        print("  df:      Face to Face Distance")
        print("  Nwl:     Number of subdivisions in the web along the length(Optional, default = 6)")
        print("  Nfl:     Number of subdivisions in the flange along the length(Optional, default = 6)")
        print("  Nwt:     Number of subdivisions in the web along the thickness(Optional, default = 1)")
        print("  Nft:     Number of subdivisions in the flange along the thickness(Optional, default = 1)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")


    ## End of PrintParams Function

################ End of DoubleChannelF Class ########################

## Recatngle Section
class Recatngle(FrameSection):
    def __init__(self, name, sectag, mattag, h, w, Nh=15, Nw=15, gj=0, yc=0.0,zc=0.0, rot=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # h:       Height
        # w:       Width
        # Nh:      Number of subdivisions along the height(Optional, default = 15)
        # Nw:      Number of subdivisions along the width(Optional, default = 15)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Height = h
        self.Width = w
        self.Ycenter = yc
        self.Zcenter = zc
        self.DivHeight = Nh
        self.DivWidth = Nw
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)



    # Width Validation
    def __get_Width(self):
        return self._Width

    def __set_Width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange width must be positive numeric value")

        self._Width = value

    def __del_Width(self):
        del self._Width

    Width = property(__get_Width, __set_Width, __del_Width)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivHeight(self):
        return self._DivHeight

    def __set_DivHeight(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivHeight = val

    def __del_DivHeight(self):
        del self._DivHeight

    DivHeight = property(__get_DivHeight, __set_DivHeight, __del_DivHeight)


    # Subdivision Validation
    def __get_DivWidth(self):
        return self._DivWidth

    def __set_DivWidth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivWidth = val

    def __del_DivWidth(self):
        del self._DivWidth

    DivWidth = property(__get_DivWidth, __set_DivWidth, __del_DivWidth)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        w = self.Width
        yc = self.Ycenter
        zc = self.Zcenter
        Nh = self.DivHeight
        Nw = self.DivWidth
        h = self.Height
        rot = self.Rotation

        patches = []
        yi, zi = -h / 2 + yc, w / 2 + zc
        yj, zj = yi, -w/2 + zc
        yk, zk = h / 2 + yc, zj
        yl, zl = yk, zi
        [yi,zi] = rotate([yi,zi], rot, (yc,zc))
        [yj, zj] = rotate([yj, zj], rot, (yc,zc))
        [yk, zk] = rotate([yk, zk], rot, (yc,zc))
        [yl, zl] = rotate([yl, zl], rot, (yc,zc))
        z = [zi, zj, zk, zl]
        y = [yi, yj, yk, yl]
        p1 = quad(y, z, Nw, Nh, self.matTag)
        patches.append(p1)

        return patches
        ## End of CreatePatches Function



    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Height: " + str(self.Height))
        strprp.append("Width: " + str(self.Width))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Rectangle")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Rectangle Section Parameters:")
        print("--------------------------------------------------")
        print("  Rectangle(name, sectag, mattag, h, w, Nh=15, Nw=15, gj=0, yc=0.0,zc=0.0, rot=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  h:       Height")
        print("  w:       Width")
        print("  Nh:      Number of subdivisions along the height(Optional, default = 15)")
        print("  Nw:      Number of subdivisions along the width(Optional, default = 15)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of Recatngle Class ########################


## Circle Section
class Circle(FrameSection):
    def __init__(self, name, sectag, mattag, r, Nc=15, Nr=8, gj=0, yc=0.0,zc=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # r:       Radius
        # Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)
        # Nr:      Number of subdivisions in the radial direction(Optional, default = 8)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Radius = r
        self.Ycenter = yc
        self.Zcenter = zc
        self.DivRad = Nr
        self.DivCirc = Nc
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Radius Validation
    def __get_Radius(self):
        return self._Radius

    def __set_Radius(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Radius must be positive numeric value")

        if (value <= 0):
            raise ValueError("Radius must be positive numeric value")

        self._Radius = value

    def __del_Radius(self):
        del self._Radius

    Radius = property(__get_Radius, __set_Radius, __del_Radius)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivRad(self):
        return self._DivRad

    def __set_DivRad(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivRad = val

    def __del_DivRad(self):
        del self._DivRad

    DivRad = property(__get_DivRad, __set_DivRad, __del_DivRad)


    # Subdivision Validation
    def __get_DivCirc(self):
        return self._DivCirc

    def __set_DivCirc(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCirc = val

    def __del_DivCirc(self):
        del self._DivCirc

    DivCirc = property(__get_DivCirc, __set_DivCirc, __del_DivCirc)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        r = self.Radius
        yc = self.Ycenter
        zc = self.Zcenter
        Nr = self.DivRad
        Nc = self.DivCirc
        mattag = self.matTag
        patches = []
        p1 = circle([yc, zc], r, Nc, Nr, mattag)
        patches.append(p1)

        return patches
        ## End of CreatePatches Function



    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function

    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Radius: " + str(self.Radius))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Circle")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Circle Section Parameters:")
        print("--------------------------------------------------")
        print("  Circle(name, sectag, mattag, r, Nc=15, Nr=8, gj=0, yc=0.0,zc=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  r:       Radius")
        print("  Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)")
        print("  Nr:      Number of subdivisions in the radial direction(Optional, default = 8)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of Circle Class ########################


## SemiCircle Section
class SemiCircle(FrameSection):
    def __init__(self, name, sectag, mattag, r, stAng, endAng, Nc=15, Nr=8, gj=0, yc=0.0,zc=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # r:       Radius
        # Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)
        # Nr:      Number of subdivisions in the radial direction(Optional, default = 8)
        # stAng:   starting angle
        # endAng:  ending angle
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Radius = r
        self.Ycenter = yc
        self.Zcenter = zc
        self.StAng = stAng
        self.EndAng = endAng
        self.DivRad = Nr
        self.DivCirc = Nc
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Radius Validation
    def __get_Radius(self):
        return self._Radius

    def __set_Radius(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Radius must be positive numeric value")

        if (value <= 0):
            raise ValueError("Radius must be positive numeric value")

        self._Radius = value

    def __del_Radius(self):
        del self._Radius

    Radius = property(__get_Radius, __set_Radius, __del_Radius)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Angles validation
    def __get_StAng(self):
        return self._StAng

    def __set_StAng(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        if (value < 0 or value > 360):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        self._StAng = value

    def __del_StAng(self):
        del self._StAng

    StAng = property(__get_StAng, __set_StAng, __del_StAng)

    def __get_EndAng(self):
        return self._EndAng

    def __set_EndAng(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        if (value < 0 or value > 360):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        self._EndAng = value

    def __del_EndAng(self):
        del self._EndAng

    EndAng = property(__get_EndAng, __set_EndAng, __del_EndAng)

    # Subdivision Validation
    def __get_DivRad(self):
        return self._DivRad

    def __set_DivRad(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivRad = val

    def __del_DivRad(self):
        del self._DivRad

    DivRad = property(__get_DivRad, __set_DivRad, __del_DivRad)


    # Subdivision Validation
    def __get_DivCirc(self):
        return self._DivCirc

    def __set_DivCirc(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCirc = val

    def __del_DivCirc(self):
        del self._DivCirc

    DivCirc = property(__get_DivCirc, __set_DivCirc, __del_DivCirc)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        r = self.Radius
        stAng = self.StAng
        endAng = self.EndAng
        yc = self.Ycenter
        zc = self.Zcenter
        Nr = self.DivRad
        Nc = self.DivCirc
        mattag = self.matTag
        patches = []
        p1 = circ([yc, zc],0,r,stAng,endAng,Nc,Nr,mattag)
        patches.append(p1)

        return patches
        ## End of CreatePatches Function



    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function

    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Radius: " + str(self.Radius))
        strprp.append("Starting angle: " + str(self.StAng))
        strprp.append("Ending angle: " + str(self.EndAng))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: SemiCircle")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("SemiCircle Section Parameters:")
        print("--------------------------------------------------")
        print("  SemiCircle(name, sectag, mattag, r, stAng, endAng, Nc=15, Nr=8, gj=0, yc=0.0,zc=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  r:       Radius")
        print("  stAng:   starting angle ( between 0 and 360 )")
        print("  endAng:  ending angle ( between 0 and 360 )")
        print("  Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)")
        print("  Nr:      Number of subdivisions in the radial direction(Optional, default = 8)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of SemiCircle Class ########################


## Pipe Section
class Pipe(FrameSection):
    def __init__(self, name, sectag, mattag, r,th, Nc=15, Nr=2, gj=0, yc=0.0, zc=0.0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # matTag:  Material tag associated with this fiber
        # th:      Thickness
        # r:       Outer Radius
        # Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)
        # Nr:      Number of subdivisions in the radial direction(Optional, default = 2)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)

        self.matTag = mattag
        self.Radius = r
        self.Ycenter = yc
        self.Zcenter = zc
        self.DivRad = Nr
        self.DivCirc = Nc
        self.Thickness = th
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_mattag(self):
            return self._matTag


    def __set_mattag(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._matTag = val

    def __del_mattag(self):
        del self._matTag

    matTag = property(__get_mattag, __set_mattag, __del_mattag)

    # Radius Validation
    def __get_Radius(self):
        return self._Radius

    def __set_Radius(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Radius must be positive numeric value")

        if (value <= 0):
            raise ValueError("Radius must be positive numeric value")

        self._Radius = value

    def __del_Radius(self):
        del self._Radius

    Radius = property(__get_Radius, __set_Radius, __del_Radius)

    # Thickness Validation
    def __get_Thickness(self):
        return self._Thickness

    def __set_Thickness(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Radius must be positive numeric value")

        if (value <= 0):
            raise ValueError("Radius must be positive numeric value")

        self._Thickness = value

    def __del_Thickness(self):
        del self._Thickness

    Thickness = property(__get_Thickness, __set_Thickness, __del_Thickness)


    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivRad(self):
        return self._DivRad

    def __set_DivRad(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivRad = val

    def __del_DivRad(self):
        del self._DivRad

    DivRad = property(__get_DivRad, __set_DivRad, __del_DivRad)


    # Subdivision Validation
    def __get_DivCirc(self):
        return self._DivCirc

    def __set_DivCirc(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCirc = val

    def __del_DivCirc(self):
        del self._DivCirc

    DivCirc = property(__get_DivCirc, __set_DivCirc, __del_DivCirc)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        r = self.Radius
        th = self.Thickness
        yc = self.Ycenter
        zc = self.Zcenter
        Nr = self.DivRad
        Nc = self.DivCirc
        mattag = self.matTag
        patches = []
        p1 = circ([yc, zc],r - th,r,0,360,Nc,Nr,mattag)
        patches.append(p1)

        return patches
        ## End of CreatePatches Function



    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Material Tag: " + str(self.matTag))
        strprp.append("Outer Radius: " + str(self.Radius))
        strprp.append("Thickness: " + str(self.Thickness))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Pipe")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Pipe Section Parameters:")
        print("--------------------------------------------------")
        print("  Pipe(name, sectag, mattag, r,th, Nc=15, Nr=2, gj=0, yc=0.0,zc=0.0)")
        print("  name:    Name of section")
        print("  secTag:  Unique section tag")
        print("  matTag:  Material tag associated with section")
        print("  r:       Outer Radius")
        print("  th:      Thickness")
        print("  Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)")
        print("  Nr:      Number of subdivisions in the radial direction(Optional, default = 2)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of Pipe Class ########################


## RcRectBeam Section
class RcRectBeam(FrameSection):
    def __init__(self, name, sectag, coremat, covermat, barmat, h, w, cover, topbard, topbarnum,
                 botbard, botbarnum, Nh=15, Nw=15, gj=0,yc=0.0, zc=0.0, rot=0.0, Nch=0, Ncw=0, Nct=2, toplayernum = 1, botlayernum = 1):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # coremat: Material tag associated with core
        # covermat:Material tag associated with cover
        # barmat:  Material tag associated with bars
        # h:       Height
        # w:       Width
        # cover:   Cover
        # topbard: Top reinforcing bar diameter
        # topbarnum: Number of top reinforcing bars at each layer
        # toplayernum: Number of top reinforcing bar layers(Optional, default = 1)
        # botbard: Bottom reinforcing bar diameter
        # botbarnum: Number of bottom reinforcing bars at each layer
        # botlayernum: Number of bottom reinforcing bar layers(Optional, default = 1)
        # Nh:      Number of subdivisions along the height in the core(Optional, default = 15)
        # Nw:      Number of subdivisions along the width in the core(Optional, default = 15)
        # Nch:     Number of subdivisions along the height in the cover(Optional, default = Nh)
        # Ncw:     Number of subdivisions along the width in the cover(Optional, default = Nw)
        # Nct:     Number of subdivisions along the thickness in the cover(Optional, default = 2)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.coreMat = coremat
        self.barMat = barmat
        self.coverMat = covermat
        self.Height = h
        self.Width = w
        self.Cover = cover
        self.BarDiTop = topbard
        self.BarDiBot = botbard
        self.BarNumTop = topbarnum
        self.BarNumBot = botbarnum
        self.NumLayerTop = toplayernum
        self.NumLayerBot = botlayernum
        self.DivHeight = Nh
        self.DivWidth = Nw
        self.DivCoverH = Nch
        self.DivCoverW = Ncw
        self.DivCoverth = Nct
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_coreMat(self):
            return self._coreMat


    def __set_coreMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coreMat = val

    def __del_coreMat(self):
        del self._coreMat

    coreMat = property(__get_coreMat, __set_coreMat, __del_coreMat)


    def __get_barMat(self):
            return self._barMat


    def __set_barMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._barMat = val

    def __del_barMat(self):
        del self._barMat

    barMat = property(__get_barMat, __set_barMat, __del_barMat)


    def __get_coverMat(self):
            return self._coverMat


    def __set_coverMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coverMat = val

    def __del_coverMat(self):
        del self._coverMat

    coverMat = property(__get_coverMat, __set_coverMat, __del_coverMat)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)



    # Width Validation
    def __get_Width(self):
        return self._Width

    def __set_Width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange width must be positive numeric value")

        self._Width = value

    def __del_Width(self):
        del self._Width

    Width = property(__get_Width, __set_Width, __del_Width)

    # Cover
    def __get_Cover(self):
        return self._Cover

    def __set_Cover(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Cover must be positive numeric value")

        if (value <= 0):
            raise ValueError("Cover must be positive numeric value")

        self._Cover = value

    def __del_Cover(self):
        del self._Cover

    Cover = property(__get_Cover, __set_Cover, __del_Cover)



    # Bar Dameter
    def __get_BarDiTop(self):
        return self._BarDiTop

    def __set_BarDiTop(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDiTop = value

    def __del_BarDiTop(self):
        del self._BarDiTop

    BarDiTop = property(__get_BarDiTop, __set_BarDiTop, __del_BarDiTop)


    def __get_BarDiBot(self):
        return self._BarDiBot

    def __set_BarDiBot(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDiBot = value

    def __del_BarDiBot(self):
        del self._BarDiBot

    BarDiBot = property(__get_BarDiBot, __set_BarDiBot, __del_BarDiBot)

   # Number of Bars
    def __get_BarNumTop(self):
        return self._BarNumTop

    def __set_BarNumTop(self, val):
        if (type(val) != int):
            raise ValueError("Number of bars must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bars must be positive integer value")

        self._BarNumTop = val

    def __del_BarNumTop(self):
        del self._BarNumTop

    BarNumTop = property(__get_BarNumTop, __set_BarNumTop, __del_BarNumTop)

    def __get_BarNumBot(self):
        return self._BarNumBot

    def __set_BarNumBot(self, val):
        if (type(val) != int):
            raise ValueError("Number of bars must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bars must be positive integer value")

        self._BarNumBot = val

    def __del_BarNumBot(self):
        del self._BarNumBot

    BarNumBot = property(__get_BarNumBot, __set_BarNumBot, __del_BarNumBot)

    # Number of bar layers
    def __get_NumLayerTop(self):
        return self._NumLayerTop

    def __set_NumLayerTop(self, val):
        if (type(val) != int):
            raise ValueError("Number of bar layers must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bar layers must be positive integer value")

        self._NumLayerTop = val

    def __del_NumLayerTop(self):
        del self._NumLayerTop

    NumLayerTop = property(__get_NumLayerTop, __set_NumLayerTop, __del_NumLayerTop)

    def __get_NumLayerBot(self):
        return self._NumLayerBot

    def __set_NumLayerBot(self, val):
        if (type(val) != int):
            raise ValueError("Number of bar layers must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bar layers must be positive integer value")

        self._NumLayerBot = val

    def __del_NumLayerBot(self):
        del self._NumLayerBot

    NumLayerBot = property(__get_NumLayerBot, __set_NumLayerBot, __del_NumLayerBot)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivHeight(self):
        return self._DivHeight

    def __set_DivHeight(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivHeight = val

    def __del_DivHeight(self):
        del self._DivHeight

    DivHeight = property(__get_DivHeight, __set_DivHeight, __del_DivHeight)


    # Subdivision Validation
    def __get_DivWidth(self):
        return self._DivWidth

    def __set_DivWidth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivWidth = val

    def __del_DivWidth(self):
        del self._DivWidth

    DivWidth = property(__get_DivWidth, __set_DivWidth, __del_DivWidth)

    def __get_DivCoverH(self):
        return self._DivCoverH

    def __set_DivCoverH(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val < 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val == 0):
            val = self.DivHeight

        self._DivCoverH = val

    def __del_DivCoverH(self):
        del self._DivCoverH

    DivCoverH = property(__get_DivCoverH, __set_DivCoverH, __del_DivCoverH)

    def __get_DivCoverW(self):
        return self._DivCoverW

    def __set_DivCoverW(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val < 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val == 0):
            val = self.DivWidth

        self._DivCoverW = val

    def __del_DivCoverW(self):
        del self._DivCoverW

    DivCoverW = property(__get_DivCoverW, __set_DivCoverW, __del_DivCoverW)

    def __get_DivCoverth(self):
        return self._DivCoverth

    def __set_DivCoverth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCoverth = val

    def __del_DivCoverth(self):
        del self._DivCoverth

    DivCoverth = property(__get_DivCoverth, __set_DivCoverth, __del_DivCoverth)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation= value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation


    ###### Create Patch Objects ########################
    def CreatePatches(self):

        h = self.Height
        w = self.Width
        cover = self.Cover
        topbard = self.BarDiTop
        botbard = self.BarDiBot
        topbarnum = self.BarNumTop
        botbarnum = self.BarNumBot
        toplayernum = self.NumLayerTop
        botlayernum = self.NumLayerBot
        Nh = self.DivHeight
        Nw = self.DivWidth
        Nch = self.DivCoverH
        Ncw = self.DivCoverW
        Nct = self.DivCoverth
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation

        patches = []

        # Core
        hc, wc = h - 2 * cover, w - 2 * cover
        yi, zi = -hc / 2, wc / 2
        yj, zj = yi, -wc / 2
        yk, zk = hc / 2, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nw, Nh, self.coreMat)
        patches.append(p1)

        # Covers
        # Top
        yi, zi = h / 2 - cover, w / 2 - cover
        yj, zj = yi, -w / 2 + cover
        yk, zk = h / 2, -w / 2
        yl, zl = yk, w / 2
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Ncw, Nct, self.coverMat)
        patches.append(p2)
        # Bot
        yi, zi = -h / 2, w / 2
        yj, zj = yi, -w / 2
        yk, zk = -h / 2 + cover, -w / 2 + cover
        yl, zl = yk, w / 2 - cover
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Ncw, Nct, self.coverMat)
        patches.append(p3)
        # Left
        yi, zi = h / 2, w / 2
        yj, zj = -h / 2, w / 2
        yk, zk = -h / 2 + cover, w / 2 - cover
        yl, zl = -yk, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p4 = quad(y, z, Nch, Nct, self.coverMat)
        patches.append(p4)

        # Right
        yi, zi = h / 2 - cover, -w / 2 + cover
        yj, zj = -h / 2 + cover, -w / 2 + cover
        yk, zk = -h / 2 , -w / 2
        yl, zl = -yk, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p5 = quad(y, z, Nch, Nct, self.coverMat)
        patches.append(p5)

        # Top Bars
        d = cover + topbard / 2
        areaf = math.pi * topbard * topbard /4
        for i in range(toplayernum):
            zi, zj = w / 2 - d, -w / 2 + d
            yi, yj = h / 2 - d - i*topbard, h / 2 - d - i*topbard
            [yi, zi] = rotate([yi, zi], rot)
            [yj, zj] = rotate([yj, zj], rot)
            p6 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, topbarnum, self.barMat)
            patches.append(p6)

        # Bot Bars
        d = cover + botbard / 2
        areaf = math.pi * botbard * botbard / 4
        for i in range(botlayernum):
            zi, zj = w / 2 - d, -w / 2 + d
            yi, yj = -h / 2 + d + i * botbard, -h / 2 + d + i * botbard
            [yi, zi] = rotate([yi, zi], rot)
            [yj, zj] = rotate([yj, zj], rot)
            p6 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, botbarnum, self.barMat)
            patches.append(p6)



        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function
    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Core Material Tag: " + str(self.coreMat))
        strprp.append("Cover Material Tag: " + str(self.coverMat))
        strprp.append("Bar Material Tag: " + str(self.barMat))
        strprp.append("Height: " + str(self.Height))
        strprp.append("Width: " + str(self.Width))
        strprp.append("Cover thickness: " + str(self.Cover))
        strprp.append("Top bar diameter: " + str(self.BarDiTop))
        strprp.append("Number of top bars at each layer: " + str(self.BarNumTop))
        strprp.append("Number of top bar layers: " + str(self.NumLayerTop))
        strprp.append("Bottom bar diameter: " + str(self.BarDiBot))
        strprp.append("Number of bottom bars at each layer: " + str(self.BarNumBot))
        strprp.append("Number of bottom bar layers: " + str(self.NumLayerBot))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))

        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: RC Rectangular Beam")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("RcRectBeam Section Parameters:")
        print("--------------------------------------------------")
        print("  RcRectBeam(name, sectag, coremat, covermat, barmat, h, w, cover, topbard, topbarnum,")
        print("                 botbard, botbarnum, Nh=15, Nw=15, gj=0, yc=0.0, zc=0.0, rot=0.0, Nch=0, Ncw=0, Nct=2, toplayernum = 1, botlayernum = 1)")
        print("  name:        Name of section")
        print("  secTag:      Unique section tag")
        print("  coremat:     Material tag associated with core")
        print("  covermat:    Material tag associated with cover")
        print("  barmat:      Material tag associated with bars")
        print("  h:           Height")
        print("  w:           Width")
        print("  cover:       Cover")
        print("  topbard:     Top reinforcing bar diameter")
        print("  topbarnum:   Number of top reinforcing bars at each layer")
        print("  toplayernum: Number of top reinforcing bar layers(Optional, default = 1)")
        print("  botbard:     Bottom reinforcing bar diameter")
        print("  botbarnum:   Number of bottom reinforcing bars at each layer")
        print("  botlayernum: Number of bottom reinforcing bar layers(Optional, default = 1)")
        print("  Nh:          Number of subdivisions along the height in the core(Optional, default = 15)")
        print("  Nw:          Number of subdivisions along the width in the core(Optional, default = 15)")
        print("  Nch:         Number of subdivisions along the height in the cover(Optional, default = 0, if Nch == 0 --> Nch = Nh)")
        print("  Ncw:         Number of subdivisions along the width in the cover(Optional, default = 0, if Ncw == 0 --> Ncw = Nw)")
        print("  Nct:         Number of subdivisions along the thickness in the cover(Optional, default = 2)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of RcRectBeam Class ########################

## RcRectColumn Section
class RcRectColumn(FrameSection):
    def __init__(self, name, sectag, coremat, covermat, barmat, h, w, cover, ybard, ybarnum,
                 zbard, zbarnum, cbard, Nh=15, Nw=15, gj=0, yc=0.0, zc=0.0, rot=0.0, Nch=0, Ncw=0, Nct=2):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # coremat: Material tag associated with core
        # covermat:Material tag associated with cover
        # barmat:  Material tag associated with bars
        # h:       Height
        # w:       Width
        # cover:   Cover
        # ybard:   reinforcing bar diameter along y direction face
        # ybarnum: Number of reinforcing bars along y direction face
        # zbard:   reinforcing bar diameter along z direction face
        # zbarnum: Number of reinforcing bars along z direction face
        # cbard:   corner bar diameter
        # Nh:      Number of subdivisions along the height in the core(Optional, default = 15)
        # Nw:      Number of subdivisions along the width in the core(Optional, default = 15)
        # Nch:      Number of subdivisions along the height in the cover(Optional, default = Nh)
        # Ncw:      Number of subdivisions along the width in the cover(Optional, default = Nw)
        # Nct:      Number of subdivisions along the thickness in the cover(Optional, default = 2)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)
        # rot:     Rotation about center point of section(Optional, default = 0.0)

        self.coreMat = coremat
        self.barMat = barmat
        self.coverMat = covermat
        self.Height = h
        self.Width = w
        self.Cover = cover
        self.BarDiY = ybard
        self.BarDiZ = zbard
        self.BarDiC = cbard
        self.BarNumY = ybarnum
        self.BarNumZ = zbarnum
        self.DivHeight = Nh
        self.DivWidth = Nw
        self.DivCoverH = Nch
        self.DivCoverW = Ncw
        self.DivCoverth = Nct
        self.Ycenter = yc
        self.Zcenter = zc
        self.Rotation = rot
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_coreMat(self):
        return self._coreMat

    def __set_coreMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coreMat = val

    def __del_coreMat(self):
        del self._coreMat

    coreMat = property(__get_coreMat, __set_coreMat, __del_coreMat)

    def __get_barMat(self):
        return self._barMat

    def __set_barMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._barMat = val

    def __del_barMat(self):
        del self._barMat

    barMat = property(__get_barMat, __set_barMat, __del_barMat)

    def __get_coverMat(self):
        return self._coverMat

    def __set_coverMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coverMat = val

    def __del_coverMat(self):
        del self._coverMat

    coverMat = property(__get_coverMat, __set_coverMat, __del_coverMat)

    # Height Validation
    def __get_height(self):
        return self._Height

    def __set_height(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Height must be positive numeric value")

        if (value <= 0):
            raise ValueError("Height must be positive numeric value")

        self._Height = value

    def __del_height(self):
        del self._Height

    Height = property(__get_height, __set_height, __del_height)

    # Width Validation
    def __get_Width(self):
        return self._Width

    def __set_Width(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Flange width must be positive numeric value")

        if (value <= 0):
            raise ValueError("Flange width must be positive numeric value")

        self._Width = value

    def __del_Width(self):
        del self._Width

    Width = property(__get_Width, __set_Width, __del_Width)

    # Cover
    def __get_Cover(self):
        return self._Cover

    def __set_Cover(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Cover must be positive numeric value")

        if (value <= 0):
            raise ValueError("Cover must be positive numeric value")

        self._Cover = value

    def __del_Cover(self):
        del self._Cover

    Cover = property(__get_Cover, __set_Cover, __del_Cover)

    # Bar Dameter
    def __get_BarDiY(self):
        return self._BarDiY

    def __set_BarDiY(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDiY = value

    def __del_BarDiY(self):
        del self._BarDiY

    BarDiY = property(__get_BarDiY, __set_BarDiY, __del_BarDiY)

    def __get_BarDiZ(self):
        return self._BarDiZ

    def __set_BarDiZ(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDiZ = value

    def __del_BarDiZ(self):
        del self._BarDiZ

    BarDiZ = property(__get_BarDiZ, __set_BarDiZ, __del_BarDiZ)

    def __get_BarDiC(self):
        return self._BarDiC

    def __set_BarDiC(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDiC = value

    def __del_BarDiC(self):
        del self._BarDiC

    BarDiC = property(__get_BarDiC, __set_BarDiC, __del_BarDiC)

    # Number of Bars
    def __get_BarNumY(self):
        return self._BarNumY

    def __set_BarNumY(self, val):
        if (type(val) != int):
            raise ValueError("Number of bars must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bars must be positive integer value")

        self._BarNumY = val

    def __del_BarNumY(self):
        del self._BarNumY

    BarNumY = property(__get_BarNumY, __set_BarNumY, __del_BarNumY)

    def __get_BarNumZ(self):
        return self._BarNumZ

    def __set_BarNumZ(self, val):
        if (type(val) != int):
            raise ValueError("Number of bars must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bars must be positive integer value")

        self._BarNumZ = val

    def __del_BarNumZ(self):
        del self._BarNumZ

    BarNumZ = property(__get_BarNumZ, __set_BarNumZ, __del_BarNumZ)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivHeight(self):
        return self._DivHeight

    def __set_DivHeight(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivHeight = val

    def __del_DivHeight(self):
        del self._DivHeight

    DivHeight = property(__get_DivHeight, __set_DivHeight, __del_DivHeight)

    # Subdivision Validation
    def __get_DivWidth(self):
        return self._DivWidth

    def __set_DivWidth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivWidth = val

    def __del_DivWidth(self):
        del self._DivWidth

    DivWidth = property(__get_DivWidth, __set_DivWidth, __del_DivWidth)

    def __get_DivCoverH(self):
        return self._DivCoverH

    def __set_DivCoverH(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val < 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val == 0):
            val = self.DivHeight

        self._DivCoverH = val

    def __del_DivCoverH(self):
        del self._DivCoverH

    DivCoverH = property(__get_DivCoverH, __set_DivCoverH, __del_DivCoverH)

    def __get_DivCoverW(self):
        return self._DivCoverW

    def __set_DivCoverW(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val < 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val == 0):
            val = self.DivWidth

        self._DivCoverW = val

    def __del_DivCoverW(self):
        del self._DivCoverW

    DivCoverW = property(__get_DivCoverW, __set_DivCoverW, __del_DivCoverW)

    def __get_DivCoverth(self):
        return self._DivCoverth

    def __set_DivCoverth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCoverth = val

    def __del_DivCoverth(self):
        del self._DivCoverth

    DivCoverth = property(__get_DivCoverth, __set_DivCoverth, __del_DivCoverth)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    # Rotation
    def __get_Rotation(self):
        return self._Rotation

    def __set_Rotation(self, value):
        if type(value) == int:
            value = float(value)
            self._Rotation = value
        elif (type(value) == float):
            self._Rotation = value
        else:
            raise ValueError("Rotation must be numeric value")

    def __del_Rotation(self):
        del self._Rotation

    Rotation = property(__get_Rotation, __set_Rotation, __del_Rotation)

    ## End of validation


    ###### Create Patch Objects ########################
    def CreatePatches(self):
        h = self.Height
        w = self.Width
        cover = self.Cover
        ybard = self.BarDiY
        zbard = self.BarDiZ
        cbard = self.BarDiC
        ybarnum = self.BarNumY
        zbarnum = self.BarNumZ
        Nh = self.DivHeight
        Nw = self.DivWidth
        Nch = self.DivCoverH
        Ncw = self.DivCoverW
        Nct = self.DivCoverth
        yc = self.Ycenter
        zc = self.Zcenter
        rot = self.Rotation
        patches = []
        # Core
        hc, wc = h - 2 * cover, w - 2 * cover
        yi, zi = -hc / 2, wc / 2
        yj, zj = yi, -wc / 2
        yk, zk = hc / 2, zj
        yl, zl = yk, zi
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p1 = quad(y, z, Nw, Nh, self.coreMat)
        patches.append(p1)

        # Covers
        # Top
        yi, zi = h / 2 - cover, w / 2 - cover
        yj, zj = yi, -w / 2 + cover
        yk, zk = h / 2, -w / 2
        yl, zl = yk, w / 2
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p2 = quad(y, z, Ncw, Nct, self.coverMat)
        patches.append(p2)
        # Bot
        yi, zi = -h / 2, w / 2
        yj, zj = yi, -w / 2
        yk, zk = -h / 2 + cover, -w / 2 + cover
        yl, zl = yk, w / 2 - cover
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p3 = quad(y, z, Ncw, Nct, self.coverMat)
        patches.append(p3)
        # Left
        yi, zi = h / 2, w / 2
        yj, zj = -h / 2, w / 2
        yk, zk = -h / 2 + cover, w / 2 - cover
        yl, zl = -yk, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p4 = quad(y, z, Nch, Nct, self.coverMat)
        patches.append(p4)

        # Right
        yi, zi = h / 2 - cover, -w / 2 + cover
        yj, zj = -h / 2 + cover, -w / 2 + cover
        yk, zk = -h / 2, -w / 2
        yl, zl = -yk, zk
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        [yk, zk] = rotate([yk, zk], rot)
        [yl, zl] = rotate([yl, zl], rot)
        z = [zi + zc, zj + zc, zk + zc, zl + zc]
        y = [yi + yc, yj + yc, yk + yc, yl + yc]
        p5 = quad(y, z, Nch, Nct, self.coverMat)
        patches.append(p5)

        # Corner Bars
        d = cover + cbard / 2
        areaf = math.pi * cbard * cbard / 4
        zi, zj = w / 2 - d, -w / 2 + d
        yi, yj = h / 2 - d , h / 2 - d
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        p6 = layerstraight([yi, yj], [zi, zj], areaf, 2, self.barMat)
        patches.append(p6)

        zi, zj = w / 2 - d, -w / 2 + d
        yi, yj = -h / 2 + d, -h / 2 + d
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        p7 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, 2, self.barMat)
        patches.append(p7)

        # Y Bars
        d1 = cover + cbard / 2
        d2 = (h - 2 * d1) / (ybarnum + 1)
        d3 = cover + ybard / 2
        areaf = math.pi * ybard * ybard / 4

        zi, zj = w / 2 - d3,  w / 2 - d3
        yi, yj = h / 2 - d1 - d2, -h / 2 + d1 + d2
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        p8 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, ybarnum, self.barMat)
        patches.append(p8)

        zi, zj = -w / 2 + d3, -w / 2 + d3
        yi, yj = h / 2 - d1 - d2, -h / 2 + d1 + d2
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        p9 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, ybarnum, self.barMat)
        patches.append(p9)

        # Z Bars
        d1 = cover + cbard / 2
        d2 = (w - 2 * d1) / (zbarnum + 1)
        d3 = cover + zbard / 2
        areaf = math.pi * zbard * zbard / 4

        zi, zj = w / 2 - d1 - d2, -w / 2 + d1 + d2
        yi, yj = h / 2 - d3, h / 2 - d3
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        p10 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, zbarnum, self.barMat)
        patches.append(p10)

        zi, zj = w / 2 - d1 - d2, -w / 2 + d1 + d2
        yi, yj = -h / 2 + d3, -h / 2 + d3
        [yi, zi] = rotate([yi, zi], rot)
        [yj, zj] = rotate([yj, zj], rot)
        p11 = layerstraight([yi+ yc, yj+ yc], [zi+ zc, zj+ zc], areaf, zbarnum, self.barMat)
        patches.append(p11)

        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', " + str(secTag) + ", '-GJ', " + str(GJ) + ")")

            else:
                print("ops.section('Fiber', " + str(secTag) + ")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', " + str(secTag) + ", '-torsion', " + str(GJ) + ")")

            else:
                print("ops.section('Fiber', " + str(secTag) + ")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function

    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Core Material Tag: " + str(self.coreMat))
        strprp.append("Cover Material Tag: " + str(self.coverMat))
        strprp.append("Bar Material Tag: " + str(self.barMat))
        strprp.append("Height: " + str(self.Height))
        strprp.append("Width: " + str(self.Width))
        strprp.append("Cover thickness: " + str(self.Cover))
        strprp.append("Bar diameter along y direction face: " + str(self.BarDiY))
        strprp.append("Number of bars along y direction face: " + str(self.BarNumY))
        strprp.append("Bar diameter along z direction face: " + str(self.BarDiZ))
        strprp.append("Number of bars along z direction face: " + str(self.BarNumZ))
        strprp.append("Corner bar diameter: " + str(self.BarDiC))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))
        strprp.append("Rotation about center point of section: " + str(self.Rotation))

        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: RC Rectangular Column")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("RcRectColumn Section Parameters:")
        print("--------------------------------------------------")
        print("  RcRectColumn(name, sectag, coremat, covermat, barmat, h, w, cover, ybard, ybarnum,")
        print(
            "                 zbard, zbarnum, cbard, Nh=15, Nw=15, gj=0, yc=0.0, zc=0.0, rot=0.0, Nch=0, Ncw=0, Nct=2)")
        print("  name:        Name of section")
        print("  secTag:      Unique section tag")
        print("  coremat:     Material tag associated with core")
        print("  covermat:    Material tag associated with cover")
        print("  barmat:      Material tag associated with bars")
        print("  h:           Height")
        print("  w:           Width")
        print("  cover:       Cover")
        print("  ybard:       Reinforcing bar diameter along y direction face")
        print("  ybarnum:     Number of reinforcing bars along y direction face")
        print("  zbard:       Reinforcing bar diameter along z direction face")
        print("  zbarnum:     Number of reinforcing bars along z direction face")
        print("  cbard:       Corner bar diameter")
        print("  Nh:          Number of subdivisions along the height in the core(Optional, default = 15)")
        print("  Nw:          Number of subdivisions along the width in the core(Optional, default = 15)")
        print(
            "  Nch:         Number of subdivisions along the height in the cover(Optional, default = 0, if Nch == 0 --> Nch = Nh)")
        print(
            "  Ncw:         Number of subdivisions along the width in the cover(Optional, default = 0, if Ncw == 0 --> Ncw = Nw)")
        print("  Nct:         Number of subdivisions along the thickness in the cover(Optional, default = 2)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")
        print("  rot:     Rotation about center point of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of RcRectColumn Class ########################


## RcCirColumn Section
class RcCirColumn(FrameSection):
    def __init__(self, name, sectag, coremat, covermat, barmat, r, cover, bard, barnum,
                  Nc=15, Nr=8, gj=0,yc=0.0,zc=0.0, Nct=2):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # coremat: Material tag associated with core
        # covermat:Material tag associated with cover
        # barmat:  Material tag associated with bars
        # r:       Radius
        # cover:   Cover
        # bard:    reinforcing bar diameter
        # barnum:  Number of reinforcing bars
        # Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)
        # Nr:      Number of subdivisions in the radial direction(Optional, default = 8)
        # Nct:     Number of subdivisions along the thickness in the cover(Optional, default = 2)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)

        self.coreMat = coremat
        self.barMat = barmat
        self.coverMat = covermat
        self.Radius = r
        self.Cover = cover
        self.BarDi = bard
        self.BarNum = barnum
        self.DivRad = Nr
        self.DivCirc = Nc
        self.DivCoverth = Nct
        self.Ycenter = yc
        self.Zcenter = zc
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_coreMat(self):
        return self._coreMat

    def __set_coreMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coreMat = val

    def __del_coreMat(self):
        del self._coreMat

    coreMat = property(__get_coreMat, __set_coreMat, __del_coreMat)

    def __get_barMat(self):
        return self._barMat

    def __set_barMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._barMat = val

    def __del_barMat(self):
        del self._barMat

    barMat = property(__get_barMat, __set_barMat, __del_barMat)

    def __get_coverMat(self):
        return self._coverMat

    def __set_coverMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coverMat = val

    def __del_coverMat(self):
        del self._coverMat

    coverMat = property(__get_coverMat, __set_coverMat, __del_coverMat)

    # Radius Validation
    def __get_Radius(self):
        return self._Radius

    def __set_Radius(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Radius must be positive numeric value")

        if (value <= 0):
            raise ValueError("Radius must be positive numeric value")

        self._Radius = value

    def __del_Radius(self):
        del self._Radius

    Radius = property(__get_Radius, __set_Radius, __del_Radius)

    # Cover
    def __get_Cover(self):
        return self._Cover

    def __set_Cover(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Cover must be positive numeric value")

        if (value <= 0):
            raise ValueError("Cover must be positive numeric value")

        self._Cover = value

    def __del_Cover(self):
        del self._Cover

    Cover = property(__get_Cover, __set_Cover, __del_Cover)

    # Bar Dameter
    def __get_BarDi(self):
        return self._BarDi

    def __set_BarDi(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDi = value

    def __del_BarDi(self):
        del self._BarDi

    BarDi = property(__get_BarDi, __set_BarDi, __del_BarDi)


    # Number of Bars
    def __get_BarNum(self):
        return self._BarNum

    def __set_BarNum(self, val):
        if (type(val) != int):
            raise ValueError("Number of bars must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bars must be positive integer value")

        self._BarNum = val

    def __del_BarNum(self):
        del self._BarNum

    BarNum = property(__get_BarNum, __set_BarNum, __del_BarNum)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivRad(self):
        return self._DivRad

    def __set_DivRad(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivRad = val

    def __del_DivRad(self):
        del self._DivRad

    DivRad = property(__get_DivRad, __set_DivRad, __del_DivRad)

    # Subdivision Validation
    def __get_DivCirc(self):
        return self._DivCirc

    def __set_DivCirc(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCirc = val

    def __del_DivCirc(self):
        del self._DivCirc

    DivCirc = property(__get_DivCirc, __set_DivCirc, __del_DivCirc)


    def __get_DivCoverth(self):
        return self._DivCoverth

    def __set_DivCoverth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCoverth = val

    def __del_DivCoverth(self):
        del self._DivCoverth

    DivCoverth = property(__get_DivCoverth, __set_DivCoverth, __del_DivCoverth)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        r = self.Radius
        cover = self.Cover
        bard = self.BarDi
        barnum = self.BarNum
        Nr = self.DivRad
        Nc = self.DivCirc
        Nct = self.DivCoverth
        yc = self.Ycenter
        zc = self.Zcenter

        patches = []
        # Core
        p1 = circle([yc, zc],r - cover,Nc,Nr,self.coreMat)
        patches.append(p1)

        # Cover
        p2 = circ([yc, zc], r - cover, r, 0, 360, Nc, Nct, self.coverMat)
        patches.append(p2)

        # Bars
        d = r - cover - bard / 2
        areaf = math.pi * bard * bard / 4

        p3 = layercirc([yc, zc],0,360,d,areaf,barnum, self.barMat)
        patches.append(p3)


        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', " + str(secTag) + ", '-GJ', " + str(GJ) + ")")

            else:
                print("ops.section('Fiber', " + str(secTag) + ")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', " + str(secTag) + ", '-torsion', " + str(GJ) + ")")

            else:
                print("ops.section('Fiber', " + str(secTag) + ")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function

    def PrintProps(self, doprint = "yes"):
        strprp=[]
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Core Material Tag: " + str(self.coreMat))
        strprp.append("Cover Material Tag: " + str(self.coverMat))
        strprp.append("Bar Material Tag: " + str(self.barMat))
        strprp.append("Radius: " + str(self.Radius))
        strprp.append("Cover thickness: " + str(self.Cover))
        strprp.append("Bar diameter: " + str(self.BarDi))
        strprp.append("Number of bars: " + str(self.BarNum))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))

        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: RC Circular Column")

            for i in range(len(strprp)):
                 print(strprp[i])

        return strprp

    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("RcCirColumn Section Parameters:")
        print("--------------------------------------------------")
        print("  RcCirColumn(name, sectag, coremat, covermat, barmat, r, cover, bard, barnum, Nc=15, Nr=8, gj=0, yc=0.0, zc=0.0, Nct=2)")
        print("  name:        Name of section")
        print("  secTag:      Unique section tag")
        print("  coremat:     Material tag associated with core")
        print("  covermat:    Material tag associated with cover")
        print("  barmat:      Material tag associated with bars")
        print("  r:           Radius")
        print("  cover:       Cover")
        print("  bard:       Reinforcing bar diameter")
        print("  barnum:     Number of reinforcing bars")
        print("  Nc:         Number of subdivisions in the circumferential direction(Optional, default = 15)")
        print("  Nr:         Number of subdivisions in the radial direction(Optional, default = 8)")
        print("  Nct:        Number of subdivisions along the thickness in the cover(Optional, default = 2)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of RcCirColumn Class ########################


## RcSemiCirColumn Section
class RcSemiCirColumn(FrameSection):
    def __init__(self, name, sectag, coremat, covermat, barmat, r,stAng, endAng, cover, bard, barnum,
                  Nc=15, Nr=8, gj=0,yc=0.0,zc=0.0, Nct=2):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # coremat: Material tag associated with core
        # covermat:Material tag associated with cover
        # barmat:  Material tag associated with bars
        # r:       Radius
        # stAng:   starting angle
        # endAng:  ending angle
        # cover:   Cover
        # bard:    reinforcing bar diameter
        # barnum:  Number of reinforcing bars
        # Nc:      Number of subdivisions in the circumferential direction(Optional, default = 15)
        # Nr:      Number of subdivisions in the radial direction(Optional, default = 8)
        # Nct:      Number of subdivisions along the thickness in the cover(Optional, default = 2)
        # gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)
        # yc:      y coordinate of the center of section(Optional, default = 0.0)
        # zc:      z coordinate of the center of section(Optional, default = 0.0)

        self.coreMat = coremat
        self.barMat = barmat
        self.coverMat = covermat
        self.Radius = r
        self.StAng = stAng
        self.EndAng = endAng
        self.Cover = cover
        self.BarDi = bard
        self.BarNum = barnum
        self.DivRad = Nr
        self.DivCirc = Nc
        self.DivCoverth = Nct
        self.Ycenter = yc
        self.Zcenter = zc
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_coreMat(self):
        return self._coreMat

    def __set_coreMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coreMat = val

    def __del_coreMat(self):
        del self._coreMat

    coreMat = property(__get_coreMat, __set_coreMat, __del_coreMat)

    def __get_barMat(self):
        return self._barMat

    def __set_barMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._barMat = val

    def __del_barMat(self):
        del self._barMat

    barMat = property(__get_barMat, __set_barMat, __del_barMat)

    def __get_coverMat(self):
        return self._coverMat

    def __set_coverMat(self, val):
        if (type(val) != int):
            raise ValueError("Material tag must be positive integer value")

        if (val <= 0):
            raise ValueError("Material tag must be positive integer value")

        self._coverMat = val

    def __del_coverMat(self):
        del self._coverMat

    coverMat = property(__get_coverMat, __set_coverMat, __del_coverMat)

    # Radius Validation
    def __get_Radius(self):
        return self._Radius

    def __set_Radius(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Radius must be positive numeric value")

        if (value <= 0):
            raise ValueError("Radius must be positive numeric value")

        self._Radius = value

    def __del_Radius(self):
        del self._Radius

    Radius = property(__get_Radius, __set_Radius, __del_Radius)

    # Angles validation
    def __get_StAng(self):
        return self._StAng

    def __set_StAng(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        if (value < 0 or value > 360):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        self._StAng = value

    def __del_StAng(self):
        del self._StAng

    StAng = property(__get_StAng, __set_StAng, __del_StAng)

    def __get_EndAng(self):
        return self._EndAng

    def __set_EndAng(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        if (value < 0 or value > 360):
            raise ValueError("Starting and ending angles must be numeric values between 0 and 360")

        self._EndAng = value

    def __del_EndAng(self):
        del self._EndAng

    EndAng = property(__get_EndAng, __set_EndAng, __del_EndAng)

    # Cover
    def __get_Cover(self):
        return self._Cover

    def __set_Cover(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Cover must be positive numeric value")

        if (value <= 0):
            raise ValueError("Cover must be positive numeric value")

        self._Cover = value

    def __del_Cover(self):
        del self._Cover

    Cover = property(__get_Cover, __set_Cover, __del_Cover)

    # Bar Dameter
    def __get_BarDi(self):
        return self._BarDi

    def __set_BarDi(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Bar diameter must be positive numeric value")

        if (value <= 0):
            raise ValueError("Bar diameter must be positive numeric value")

        self._BarDi = value

    def __del_BarDi(self):
        del self._BarDi

    BarDi = property(__get_BarDi, __set_BarDi, __del_BarDi)


    # Number of Bars
    def __get_BarNum(self):
        return self._BarNum

    def __set_BarNum(self, val):
        if (type(val) != int):
            raise ValueError("Number of bars must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of bars must be positive integer value")

        self._BarNum = val

    def __del_BarNum(self):
        del self._BarNum

    BarNum = property(__get_BarNum, __set_BarNum, __del_BarNum)

    # Center Validation
    def __get_Ycenter(self):
        return self._Ycenter

    def __set_Ycenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Ycenter must be numeric value")

        self._Ycenter = value

    def __del_Ycenter(self):
        del self._Ycenter

    Ycenter = property(__get_Ycenter, __set_Ycenter, __del_Ycenter)

    # Center Validation
    def __get_Zcenter(self):
        return self._Zcenter

    def __set_Zcenter(self, value):
        if type(value) == int:
            value = float(value)

        if (type(value) != float):
            raise ValueError("Zcenter must be numeric value")

        self._Zcenter = value

    def __del_Zcenter(self):
        del self._Zcenter

    Zcenter = property(__get_Zcenter, __set_Zcenter, __del_Zcenter)

    # Subdivision Validation
    def __get_DivRad(self):
        return self._DivRad

    def __set_DivRad(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivRad = val

    def __del_DivRad(self):
        del self._DivRad

    DivRad = property(__get_DivRad, __set_DivRad, __del_DivRad)

    # Subdivision Validation
    def __get_DivCirc(self):
        return self._DivCirc

    def __set_DivCirc(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCirc = val

    def __del_DivCirc(self):
        del self._DivCirc

    DivCirc = property(__get_DivCirc, __set_DivCirc, __del_DivCirc)


    def __get_DivCoverth(self):
        return self._DivCoverth

    def __set_DivCoverth(self, val):
        if (type(val) != int):
            raise ValueError("Number of subdivisions must be positive integer value")

        if (val <= 0):
            raise ValueError("Number of subdivisions must be positive integer value")

        self._DivCoverth = val

    def __del_DivCoverth(self):
        del self._DivCoverth

    DivCoverth = property(__get_DivCoverth, __set_DivCoverth, __del_DivCoverth)

    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)

    ## End of validation

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        r = self.Radius
        stAng = self.StAng
        enAng = self.EndAng
        cover = self.Cover
        bard = self.BarDi
        barnum = self.BarNum
        Nr = self.DivRad
        Nc = self.DivCirc
        Nct = self.DivCoverth
        yc = self.Ycenter
        zc = self.Zcenter

        patches = []
        # Core
        p1 = circ([yc, zc], 0, r - cover, stAng, enAng, Nc, Nr, self.coreMat)
        patches.append(p1)

        # Cover
        p2 = circ([yc, zc], r - cover, r, stAng, enAng, Nc, Nct, self.coverMat)
        patches.append(p2)

        # Bars
        d = r - cover - bard / 2
        areaf = math.pi * bard * bard / 4

        p3 = layercirc([yc, zc], stAng, enAng,d,areaf,barnum, self.barMat)
        patches.append(p3)


        return patches
        ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', " + str(secTag) + ", '-GJ', " + str(GJ) + ")")

            else:
                print("ops.section('Fiber', " + str(secTag) + ")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', " + str(secTag) + ", '-torsion', " + str(GJ) + ")")

            else:
                print("ops.section('Fiber', " + str(secTag) + ")")
        else:
            raise ValueError(
                "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function

    def PrintProps(self, doprint = "yes"):
        strprp=[]
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Core Material Tag: " + str(self.coreMat))
        strprp.append("Cover Material Tag: " + str(self.coverMat))
        strprp.append("Bar Material Tag: " + str(self.barMat))
        strprp.append("Radius: " + str(self.Radius))
        strprp.append("Starting angle: " + str(self.StAng))
        strprp.append("Ending angle: " + str(self.EndAng))
        strprp.append("Cover thickness: " + str(self.Cover))
        strprp.append("Bar diameter: " + str(self.BarDi))
        strprp.append("Number of bars: " + str(self.BarNum))
        strprp.append("Section Y Center: " + str(self.Ycenter))
        strprp.append("Section Z Center: " + str(self.Zcenter))

        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: RC Semi Circular Column")

            for i in range(len(strprp)):
                 print(strprp[i])

        return strprp

    ###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("RcSemiCirColumn Section Parameters:")
        print("--------------------------------------------------")
        print("  RcSemiCirColumn(name, sectag, coremat, covermat, barmat, r, stAng, endAng, cover, bard, barnum, Nc=15, Nr=8, gj=0, yc=0.0, zc=0.0, Nct=2)")
        print("  name:        Name of section")
        print("  secTag:      Unique section tag")
        print("  coremat:     Material tag associated with core")
        print("  covermat:    Material tag associated with cover")
        print("  barmat:      Material tag associated with bars")
        print("  r:           Radius")
        print("  stAng:       Starting Angle")
        print("  endAng:      Ending Angle")
        print("  cover:       Cover")
        print("  bard:       Reinforcing bar diameter")
        print("  barnum:     Number of reinforcing bars")
        print("  Nc:         Number of subdivisions in the circumferential direction(Optional, default = 15)")
        print("  Nr:         Number of subdivisions in the radial direction(Optional, default = 8)")
        print("  Nct:        Number of subdivisions along the thickness in the cover(Optional, default = 2)")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")
        print("  yc:      y coordinate of the center of section(Optional, default = 0.0)")
        print("  zc:      z coordinate of the center of section(Optional, default = 0.0)")

    ## End of PrintParams Function

################ End of RcSemiCirColumn Class ########################


## Composite Section
class Composite(FrameSection):
    def __init__(self, name, sectag, sections, gj=0):
        FrameSection.__init__(self, name, sectag)
        # name:    Name of Section
        # secTag:  Unique section tag
        # sections:  A list of previously defined sections

        self.Sections = sections
        self.GJ = gj

    ###### alidation VBlock ( Set and Get Properties ) ########################
    # Material Tag Validation
    def __get_Sections(self):
            return self._Sections


    def __set_Sections(self, val):
        if len(val) == 0:
            raise ValueError("empty section list")
        # print(type(val[1]) == 'FrameSections.I')
        # if (type(val) != Section.FrameSection):
        #     raise ValueError("sectios must be FrameSection object")

        self._Sections = val

    def __del_Sections(self):
        del self._Sections

    Sections = property(__get_Sections, __set_Sections, __del_Sections)


    # GJ
    def __get_GJ(self):
        return self._GJ

    def __set_GJ(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            value = float(value)
            self._GJ = value
        elif (type(value) == float):
            if value < 0:
                raise ValueError("GJ must be positive numeric value")
            self._GJ = value
        else:
            raise ValueError("GJ must be positive numeric value")

    def __del_GJ(self):
        del self._GJ

    GJ = property(__get_GJ, __set_GJ, __del_GJ)


    ## End of validation


    def AddSection(self, sec):
        sections = self.Sections
        if sec not in sections:
            sections.append(sec)

    def RemoveSection(self,sec):
        sections = self.Sections
        if sec in sections:
            sections.remove(sec)

    ###### Create Patch Objects ########################
    def CreatePatches(self):
        sections = self.Sections
        patches = []
        for sec in sections:
            patches.extend(sec.CreatePatches())

        return patches
    ## End of CreatePatches Function

    ###### Print Cammand ########################
    def PrintCommand(self, torsion=0):
        print("#-----------------------------------")
        print("# Section Openseespy Commands: " + str(self.Name))
        print("#-----------------------------------")
        patches = self.CreatePatches()
        secTag = self.secTag
        GJ = self.GJ
        if torsion == 0:
            if GJ != 0:
                print("ops.section('Fiber', "+str(secTag) + ", '-GJ', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        elif torsion == 1:
            if GJ != 0:
                GJ = int(GJ)
                print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + self.Name + "\'")
                print("ops.section('Fiber', "+str(secTag) + ", '-torsion', " +str(GJ) +")")

            else:
                print("ops.section('Fiber', " + str(secTag) +")")
        else:
            raise ValueError(
                "torsion = 0: section('Fiber', secTag, '-GJ', GJ) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

        for pa in patches:
            pa.PrintCommand()

    ## End of PrintCommand Function

    def PrintProps(self, doprint="yes"):
        strprp = []
         
        strprp.append("Section Tag: " + str(self.secTag))
        strprp.append("Sections: ")
        for sec in self.Sections:
            strprp.append("   " + sec.Name)

        if doprint == "yes":
            strprp.insert(0, "-----------------------------------")
            strprp.insert(1, "Section Properties: " + str(self.Name))
            strprp.insert(2, "-----------------------------------")
            strprp.insert(3, "Type: Composite")

            for i in range(len(strprp)):
                print(strprp[i])

        return strprp
###### Print Parameter Description ########################
    @staticmethod
    def PrintParams():
        print("--------------------------------------------------")
        print("Composite Section Parameters:")
        print("--------------------------------------------------")
        print("  Composite(name, sectag, sections, gj=0)")
        print("  name:        Name of section")
        print("  secTag:      Unique section tag")
        print("  sections:    A list of previously defined sections")
        print(
            "  gj:      Linear-elastic torsional stiffness or uniaxialMaterial tag assigned to the section for torsional response(Optional, default = 0)")


    ## End of PrintParams Function
################ End of Composite Class ########################




######## some functios
def rotate(point, angle = 90.0,origin = (0,0)):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in degrees.
    """
    ang_rad = math.pi * angle / 180
    oy, oz = origin
    py, pz = point

    qy = oy + math.cos(ang_rad) * (py - oy) - math.sin(ang_rad) * (pz - oz)
    qz = oz + math.sin(ang_rad) * (py - oy) + math.cos(ang_rad) * (pz - oz)
    return [qy, qz]

def drawarrow(xyA,xyB,txt,ha,va,ax):

    coordsA = "data"
    coordsB = "data"

    con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                          arrowstyle="-|>", shrinkA=2, shrinkB=2,
                          mutation_scale=15, lw = 1.5, fc="w")

    ax.text(xyB[0],xyB[1], txt,dict(size=12),
            horizontalalignment=ha,
            verticalalignment=va)
    ax.axhline(0, alpha = 0.4,lw = 1, linestyle=":", color='g')
    ax.axvline(0, alpha=0.4, lw = 1, linestyle=":", color='g')
    ax.add_artist(con)

def DrawSection(sec, properties = 'y', subdivisions = 'y', edgelines = 'n', grids = 'n', shadow = 'n', dir=""):
    name = sec.Name
    tag = sec.secTag

    if shadow in ['yes', 'y', 'no', 'n']:
        pass
    else:
        raise ValueError("shadow can be \"yes\", \"y\",  \"no\" or \"n\" ")

    if properties in ['yes', 'y']:
        fig, (ax, axt) = plt.subplots(ncols=2)
    elif properties in ['no', 'n']:
        fig, ax = plt.subplots()
    else:
        raise ValueError("properties can be \"yes\", \"y\",  \"no\" or \"n\" ")


    if grids in ['yes', 'y']:
        ax.grid(color='gray', linestyle=':', linewidth=0.5)
    elif grids in ['no', 'n']:
        pass
    else:
        raise ValueError("grids can be \"yes\", \"y\",  \"no\" or \"n\" ")


    if properties in ['yes', 'y']:
        props = sec.PrintProps(doprint="no")
        for i in range(len(props)):
            x = 0.0
            y = i * 0.07  + 0.0
            t = axt.text(x, y, props[i],dict(size=11),va = "top")
            axt.add_artist(t)

        axt.invert_yaxis()
        axt.axis("off")

    axpatches =[]

    if isinstance(sec,Composite):
        sections = sec.Sections
        for s in sections:
            cedge, cdiv = 'b', 'gray'
            patches = s.CreatePatches()
            for p in patches:
                if p.matTag in colors:
                    cindex = colors.index(p.matTag)
                    cface = colors[cindex + 1]
                else:
                    cface = '0.8'

                if isinstance(p, layerstraight)  or isinstance(p, layercirc):
                    drawings = p.Draw(cface, cface, ax)
                else:
                    drawings = p.Draw(cface, cedge, cdiv,subdivisions,edgelines, ax)
                    axpatches.extend(drawings)
    else:
        patches = sec.CreatePatches()
        cedge, cdiv =  'b', 'gray'
        for p in patches:
            if p.matTag in colors:
                cindex = colors.index(p.matTag)
                cface = colors[cindex + 1]
            else:
                cface = '0.8'
            if isinstance(p, layerstraight) or isinstance(p, layercirc):
                drawings = p.Draw(cface, cface, ax)
            else:
                drawings = p.Draw(cface, cedge, cdiv, subdivisions,edgelines, ax)
                axpatches.extend(drawings)



    ax.spines["bottom"].set_color("gray")
    ax.spines["bottom"].set_alpha(0.3)
    ax.spines["left"].set_color("gray")
    ax.spines["left"].set_alpha(0.3)
    ax.spines["top"].set_color("gray")
    ax.spines["top"].set_alpha(0.3)
    ax.spines["right"].set_color("gray")
    ax.spines["right"].set_alpha(0.3)



    ax.set_title(" Section: " + name + " [" + str(tag) + "]",fontsize=11)
    ax.axis('equal')
    # plt.tight_layout()
    xl = ax.get_xlim()
    yl = ax.get_ylim()
    dx = xl[1] - xl[0]
    dy = yl[1] - yl[0]
    h = min((dx,dy))

    if shadow in ['yes', 'y']:
        for patch in axpatches:
            if type(patch) != matline.Line2D:
                w = matpach.Shadow(patch, -h/80, -h/80)
                # w.set_gid(s.get_gid() + "_shadow")
                w.set_zorder(patch.get_zorder() - 0.1)
                ax.add_patch(w)

    drawarrow((0, 0), (h / 6, 0), 'Z', 'right', 'center', ax)
    drawarrow((0, 0), (0, h / 6), 'Y', 'center', 'bottom', ax)

    ax.invert_xaxis()

    fig.tight_layout()

    if type(dir) == str:
        if len(dir) != 0:
            if os.path.isdir(dir):
                pass
            else:
                os.mkdir(dir)

            filename = dir + sec.Name + ".png"
            sav = plt.savefig(filename, dpi=150)
            print("figure was saved to " + filename)
    # plt.show()
###### Create Opnseespy Fiber Section ########################
def CreateOpsSection(sec,ops, torsion=0):
    patches = sec.CreatePatches()
    secTag = sec.secTag
    GJ = sec.GJ
    if torsion == 0:
        if GJ != 0:
            ops.section('Fiber', secTag, '-GJ', GJ)
        else:
            ops.section('Fiber', secTag)
    elif torsion == 1:
        if GJ != 0:
            GJ = int(GJ)
            print("# Note: torsionMatTag was set to " + str(GJ) + " for \'" + sec.Name + "\'")
            ops.section('Fiber', secTag, '-torsion', GJ)
        else:
            ops.section('Fiber', secTag)
    else:
        raise ValueError(
            "torsion = 0: (section('Fiber', secTag, '-GJ', GJ)) or 1: section('Fiber', secTag, '-torsion', torsionMatTag)")

    for pa in patches:
        pa.CreateFibers(ops)

    print("Section: " + sec.Name + '  was created.' )
    ## End of CreateSection Function

###### Make a Deep Copy of object ########################
def CopySection(sec, newname, newtag):
    newsec = copy.deepcopy(sec)
    newsec.Name = newname
    newsec.secTag = newtag
    return newsec

def getDoc():
   webbrowser.open('https://drive.google.com/file/d/14YjLMHoF9C2b_RddTJqhrB6e6OWlx4Yt/view?usp=sharing')


##### fibers classes


class fiber:
    def __init__(self, yloc, zloc, Area, matatg):
        self.Yloc = yloc
        self.Zloc = zloc
        self.A = Area
        self.matTag = matatg

    def Draw(self,cface,cedge, ax):
        r = math.sqrt(self.A / math.pi)
        s = matpach.Circle((self.Zloc,self.Yloc),r)
        s.set_facecolor(cface)
        s.set_edgecolor(cedge)
        s.set_alpha(0.6)
        ax.add_patch(s)
        return s

    # End of Draw Function

    ###### Create Opnseespy fiber ########################
    def CreateFibers(self, ops):
        Y = self.Yloc
        Z = self.Zloc
        A = self.A
        mattag = self.matTag
        pa = ops.fiber(Y, Z, A, mattag)
        return pa
    # End of CreateFibers Function

   ###### Print Opnseespy Command ########################
    def PrintCommand(self):
        Y = self.Yloc
        Z = self.Zloc
        A = self.A
        mattag = self.matTag
        print("ops.fiber(" + str(Y) + ", " + str(Z) + ", "  + str(A) + ", "  +
              str(mattag) +")")

    # End of PrintCommand Function
################ End of fiber Class ########################



class quad:
    def __init__(self, Y, Z, divIJ, divJK, mattag):
        self.Y = Y
        self.Z = Z
        self.divIJ = divIJ
        self.divJK = divJK
        self.matTag = mattag

    ###### Draw Patch ########################
    def Draw(self,cface,cedge,cdiv,subdivisions,edgelines, ax):
        if subdivisions in ['yes', 'y', 'no', 'n']:
            pass
        else:
            raise ValueError("subdivisions can be \"yes\", \"y\",  \"no\" or \"n\" ")

        if edgelines in ['yes', 'y', 'no', 'n']:
            pass
        else:
            raise ValueError("edgelines can be \"yes\", \"y\",  \"no\" or \"n\" ")

        drawings =[]
        y = np.array(self.Y)
        z = np.array(self.Z)
        yz = np.array([[z[0],y[0]],[z[1],y[1]],[z[2],y[2]],[z[3],y[3]]])
        s = matpach.Polygon(yz)
        s.set_facecolor(cface)
        s.set_edgecolor(cedge)
        s.set_linewidth(0.4)
        if edgelines in ['no', 'n']:
            s.set_linestyle('none')
        s.set_alpha(1)
        ax.add_patch(s)
        drawings.append(s)

        if subdivisions in ['yes', 'y']:
            # Draw Sub Diisions
            dy_ij, dy_jk, dy_lk, dy_il = (y[1] - y[0]) / self.divIJ,(y[2] - y[1]) / self.divJK, (y[2] - y[3]) / self.divIJ ,(y[3] - y[0]) / self.divJK

            dz_ij, dz_jk, dz_lk, dz_il = (z[1] - z[0]) / self.divIJ,(z[2] - z[1]) / self.divJK, (z[2] - z[3]) / self.divIJ,(z[3] - z[0]) / self.divJK

            count = 1
            for i in np.arange(self.divIJ - 1):
                y1, y2 = dy_ij * count + y[0], dy_lk * count + y[3]
                z1, z2 = dz_ij * count + z[0], dz_lk * count + z[3]
                l = matline.Line2D([z1, z2],[y1, y2])
                l.set_color(cdiv)
                l.set_linestyle('--')
                l.set_alpha(0.6)
                l.set_linewidth(0.5)
                drawings.append(l)
                ax.add_line(l)
                count += 1

            count = 1
            for i in np.arange(self.divJK - 1):
                y1, y2 = dy_jk * count + y[1], dy_il * count + y[0]
                z1, z2 = dz_jk * count + z[1], dz_il * count + z[0]
                l = matline.Line2D([z1, z2], [y1, y2])
                l.set_color(cdiv)
                l.set_linestyle('--')
                l.set_alpha(0.6)
                l.set_linewidth(0.5)
                drawings.append(l)
                ax.add_line(l)
                count += 1

        return drawings
    # End of Draw Function

    ###### Create Opnseespy quad Patch ########################
    def CreateFibers(self, ops):
        Y = self.Y
        Z = self.Z
        divIJ = self.divIJ
        divJK = self.divJK
        mattag = self.matTag
        pa = ops.patch('quad', mattag, divIJ, divJK, Y[0], Z[0], Y[1], Z[1], Y[2], Z[2], Y[3], Z[3])
        return pa
    # End of CreateFibers Function

    ###### Print Opnseespy Command ########################
    def PrintCommand(self):
        Y = self.Y
        Z = self.Z
        divIJ = self.divIJ
        divJK = self.divJK
        mattag = self.matTag
        print("ops.patch('quad' ," + str(mattag) + ", " + str(divIJ) + ", "  + str(divJK) + ", "  +
              str(Y[0]) + ", "  + str(Z[0]) + ", "  +str(Y[1]) + ", "  +str(Z[1]) + ", "
              +str(Y[2]) + ", "  +str(Z[2]) + ", "  +str(Y[3]) + ", "  +str(Z[3]) +")")

    # End of PrintCommand Function
################ End of quad Class ########################



class circle:
    def __init__(self, center,rad, divCirc, divRad, mattag):
        self.Center = center
        self.Rad = rad
        self.divCirc = divCirc
        self.divRad = divRad
        self.matTag = mattag

    ###### Draw Patch ########################
    def Draw(self,cface,cedge,cdiv,subdivisions,edgelines, ax):
        if subdivisions in ['yes', 'y', 'no', 'n']:
            pass
        else:
            raise ValueError("subdivisions can be \"yes\", \"y\",  \"no\" or \"n\" ")

        if edgelines in ['yes', 'y', 'no', 'n']:
            pass
        else:
            raise ValueError("edgelines can be \"yes\", \"y\",  \"no\" or \"n\" ")

        yc = self.Center[0]
        zc = self.Center[1]
        r = self.Rad
        drawings = []
        s = matpach.Circle((zc, yc), r)
        s.set_facecolor(cface)
        s.set_edgecolor(cedge)
        s.set_linewidth(0.4)
        if edgelines in ['no', 'n']:
            s.set_linestyle('none')
        s.set_alpha(1)
        ax.add_patch(s)
        drawings.append(s)

        # Draw Sub Diisions
        if subdivisions in ['yes', 'y']:
            angsub = 360 / self.divCirc
            count = 0
            for i in np.arange(self.divCirc):
                angl = angsub * count
                zj = r * np.cos(np.deg2rad(angl)) + zc
                yj = r * np.sin(np.deg2rad(angl)) + yc
                l = matline.Line2D([yc, yj],[zc, zj])
                l.set_color(cdiv)
                l.set_linestyle('--')
                l.set_alpha(0.6)
                l.set_linewidth(0.5)
                drawings.append(l)
                ax.add_line(l)
                count += 1

            dr = r / self.divRad
            count = 1
            for i in np.arange(self.divRad - 1):
                ri = count * dr
                l = plt.Circle((zc,yc),ri, color=cdiv, fill=False)
                l.set_color(cdiv)
                l.set_linestyle('--')
                l.set_alpha(0.6)
                l.set_linewidth(0.5)
                drawings.append(l)
                ax.add_artist(l)
                count += 1

        return drawings
    # End of Draw Function

    ###### Create Opnseespy circ Patch ########################
    def CreateFibers(self, ops):
        yc = self.Center[0]
        zc = self.Center[1]
        r = self.Rad
        divCirc = self.divCirc
        divRad = self.divRad
        mattag = self.matTag
        pa = ops.patch('circ', mattag, divCirc, divRad,yc, zc,0, r,0, 360)
        return pa
    # End of CreateFibers Function

    ###### Print Opnseespy Command ########################
    def PrintCommand(self):
        yc = self.Center[0]
        zc = self.Center[1]
        r = self.Rad
        divCirc = self.divCirc
        divRad = self.divRad
        mattag = self.matTag
        print("ops.patch('circ' ," + str(mattag) + ", " + str(divCirc) + ", "  + str(divRad) + ", " +
              str(yc) + ", "  + str(zc) + ", " + str(0) + ", "  +str(r) + ", " + "0, 360)")

    # End of PrintCommand Function
################ End of circle Class ########################

class circ:
    def __init__(self, center,inRad,exRad,stAng,endAng, divCirc, divRad, mattag):
        self.Center = center
        self.inRad = inRad
        self.exRad = exRad
        self.stAng = stAng
        self.endAng = endAng
        self.divCirc = divCirc
        self.divRad = divRad
        self.matTag = mattag

    ###### Draw Patch ########################
    def Draw(self,cface,cedge,cdiv,subdivisions,edgelines, ax):
        if subdivisions in ['yes', 'y', 'no', 'n']:
            pass
        else:
            raise ValueError("subdivisions can be \"yes\", \"y\",  \"no\" or \"n\" ")

        if edgelines in ['yes', 'y', 'no', 'n']:
            pass
        else:
            raise ValueError("edgelines can be \"yes\", \"y\",  \"no\" or \"n\" ")

        yc = self.Center[0]
        zc = self.Center[1]
        ri = self.inRad
        re = self.exRad
        angs = self.stAng
        ange = self.endAng
        drawings =[]
        yin, zin = polycoords(yc,zc,ri,angs,ange,self.divCirc)
        yex, zex = polycoords(yc,zc,re,angs,ange,self.divCirc)
        yex.reverse()
        zex.reverse()
        z = zin
        z.extend(zex)
        y = yin
        y.extend(yex)
        z.append(zin[0])
        y.append(yin[0])
        yz =[]
        for i in np.arange(len(z)):
            yz.append([z[i],y[i]])

        s = matpach.Polygon(yz)
        s.set_facecolor(cface)
        s.set_edgecolor(cedge)
        s.set_linewidth(0.2)
        if edgelines in ['no', 'n']:
            s.set_linestyle('none')
        s.set_alpha(1)
        drawings.append(s)
        ax.add_patch(s)

        # Draw Sub Diisions
        if subdivisions in ['yes', 'y']:
            yex, zex = polycoords(yc, zc, re, angs, ange, self.divCirc)
            for i in np.arange(self.divCirc):
                l = matline.Line2D([zin[i], zex[i]], [yin[i], yex[i]])
                l.set_color(cdiv)
                l.set_linestyle('--')
                l.set_alpha(0.6)
                l.set_linewidth(0.5)
                drawings.append(l)
                ax.add_line(l)

            dr = (re - ri ) / self.divRad
            count = 1
            for i in np.arange(self.divRad - 1):
                r = count * dr + ri
                yin, zin = polycoords(yc, zc, r, angs, ange, self.divCirc)
                l = matline.Line2D(zin, yin)
                l.set_color(cdiv)
                l.set_linestyle('--')
                l.set_alpha(0.6)
                l.set_linewidth(0.5)
                drawings.append(l)
                ax.add_line(l)
                count += 1

        return drawings
    # End of Draw Function

    ###### Create Opnseespy circ Patch ########################
    def CreateFibers(self, ops):
        yc = self.Center[0]
        zc = self.Center[1]
        ri = self.inRad
        re = self.exRad
        angs = self.stAng
        ange = self.endAng
        divCirc = self.divCirc
        divRad = self.divRad
        mattag = self.matTag
        pa = ops.patch('circ', mattag, divCirc, divRad,yc, zc,ri, re,angs, ange)
        return pa
    # End of CreateFibers Function

    ###### Print Opnseespy Command ########################
    def PrintCommand(self):
        yc = self.Center[0]
        zc = self.Center[1]
        ri = self.inRad
        re = self.exRad
        angs = self.stAng
        ange = self.endAng
        divCirc = self.divCirc
        divRad = self.divRad
        mattag = self.matTag
        print("ops.patch('circ' ," + str(mattag) + ", " + str(divCirc) + ", "  + str(divRad) + ", " +
              str(yc) + ", "  + str(zc) + ", " + str(ri) + ", "  +str(re) +  ", " +str(angs) +  ", " +str(ange) + ")")

    # End of PrintCommand Function
################ End of circ Class ########################


# layer('straight', matTag, numFiber, areaFiber, *start, *end)
class layerstraight:
    def __init__(self, Y, Z, areaf, numf, mattag):
        self.Y = Y
        self.Z = Z
        self.areaF = areaf
        self.numF = numf
        self.matTag = mattag

    ###### Draw Patch ########################
    def Draw(self, cface, cedge, ax):
        yi, zi = self.Y[0], self.Z[0]
        yj, zj = self.Y[1], self.Z[1]
        rb = math.sqrt(self.areaF / math.pi)
        dy, dz = (yj - yi) / (self.numF - 1), (zj - zi) / (self.numF - 1)
        drawings = []
        for i in np.arange(self.numF):
            zc, yc = i * dz + zi, i * dy + yi
            s = matpach.Circle((zc, yc), rb)
            s.set_facecolor(cface)
            s.set_edgecolor(cedge)
            s.set_alpha(0.7)
            drawings.append(s)
            ax.add_patch(s)

        return drawings
    # End of Draw Function

    ###### Create Opnseespy layer straight Patch ########################
    def CreateFibers(self, ops):
        # layer('straight', matTag, numFiber, areaFiber, *start, *end)
        yi, zi = self.Y[0], self.Z[0]
        yj, zj = self.Y[1], self.Z[1]
        mattag = self.matTag
        pa = ops.layer('straight', mattag, self.numF, self.areaF, yi, zi, yj, zj)
        return pa
    # End of CreateFibers Function

    ###### Print Opnseespy Command ########################
    def PrintCommand(self):
        yi, zi = self.Y[0], self.Z[0]
        yj, zj = self.Y[1], self.Z[1]
        mattag = self.matTag
        print("ops.layer('straight' ," + str(mattag) + ", " + str(self.numF) + ", "  + str(self.areaF) + ", " +
              str(yi) + ", "  + str(zi) + ", " + str(yj) + ", "  +str(zj) + ")")

    # End of PrintCommand Function
################ End of layer straight Class ########################


# layer('circ', matTag,numFiber,areaFiber,*center,radius,*ang=[0.0,360.0-360/numFiber])
class layercirc:
    def __init__(self,center,stAng,endAng,rad, areaf, numf, mattag):
        self.Center = center
        self.stAng = stAng
        self.endAng = endAng
        self.Radius = rad
        self.areaF = areaf
        self.numF = numf
        self.matTag = mattag

    ###### Draw Patch ########################
    def Draw(self, cface, cedge, ax):
        yc, zc = self.Center[0], self.Center[1]
        rb = math.sqrt(self.areaF / math.pi)
        drawings = []
        if self.endAng - self.stAng == 360:
            ycoords, zcoords = polycoords(yc, zc, self.Radius, self.stAng, self.endAng, self.numF)
        else:
             ycoords, zcoords = polycoords(yc, zc, self.Radius, self.stAng, self.endAng, self.numF - 1)
        for i in np.arange(len(ycoords)):
            y, z = ycoords[i], zcoords[i]
            s = matpach.Circle((z, y), rb)
            s.set_facecolor(cface)
            s.set_edgecolor(cedge)
            s.set_alpha(0.7)
            drawings.append(s)
            ax.add_patch(s)

        return drawings
    # End of Draw Function

    ###### Create Opnseespy layer circ Patch ########################
    def CreateFibers(self, ops):
        # layer('circ', matTag,numFiber,areaFiber,*center,radius,*ang=[0.0,360.0-360/numFiber])
        yc, zc = self.Center[0], self.Center[1]
        mattag = self.matTag
        pa = ops.layer('circ', mattag, self.numF, self.areaF, yc, zc, self.Radius, self.stAng, self.endAng)
        return pa
    # End of CreateFibers Function

    ###### Print Opnseespy Command ########################
    def PrintCommand(self):
        yc, zc = self.Center[0], self.Center[1]
        mattag = self.matTag
        print("ops.layer('circ' ," + str(mattag) + ", " + str(self.numF) + ", "  + str(self.areaF) + ", " +
              str(yc) + ", " + str(zc) + ", " + str(self.Radius) + ", "  + str(self.stAng) + ", "  + str(self.endAng) + ")")

    # End of PrintCommand Function
################ End of layer circ Class ########################


################ other functions ########################
def polycoords(yc,zc,r,angs,ange,numsubdiv):
    dangle = (ange - angs)/numsubdiv
    count = 0
    zcoords = []
    ycoords = []
    for i in np.arange(numsubdiv+1):
        angl = dangle * count + angs
        y = r * np.cos(np.deg2rad(angl)) + yc
        z = r * np.sin(np.deg2rad(angl)) + zc
        zcoords.append(z)
        ycoords.append(y)
        count += 1
    return ycoords, zcoords
