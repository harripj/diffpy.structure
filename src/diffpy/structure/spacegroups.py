#!/usr/bin/env python3
##############################################################################
#
# diffpy.structure  by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2011 Trustees of the Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE_DANSE.txt for license information.
#
##############################################################################

'''Space group classes and definitions from mmLib and sgtbx.
'''

from diffpy.structure.spacegroupmod import SymOp, SpaceGroup
from diffpy.structure.mmlibspacegroups import mmLibSpaceGroupList
from diffpy.structure.sgtbxspacegroups import sgtbxSpaceGroupList

# all spacegroup definitions
SpaceGroupList = mmLibSpaceGroupList + sgtbxSpaceGroupList


def GetSpaceGroup(sgid):
    """Returns the SpaceGroup instance for the given identifier.

    sgid -- space group symbol, either short_name or pdb_name,
            whatever it means in mmlib.  Can be also an integer.

    Return space group instance.
    Raise ValueError when not found.
    """
    if not _sg_lookup_table:
        _buildSGLookupTable()
    if sgid in _sg_lookup_table:
        return _sg_lookup_table[sgid]
    # Try different versions of sgid, first make sure it is a string
    emsg = "Unknown space group identifier %r" % sgid
    if not isinstance(sgid, str):
        raise ValueError(emsg)
    # short name case adjusted
    sgkey = sgid.strip()
    sgkey = sgkey[:1].upper() + sgkey[1:].lower()
    if sgkey in _sg_lookup_table:
        return _sg_lookup_table[sgkey]
    # long name all upper case
    sgkey = sgid.strip().upper()
    if sgkey in _sg_lookup_table:
        return _sg_lookup_table[sgkey]
    # try to remove any blanks
    sgkey = sgid.replace(' ', '')
    if sgkey in _sg_lookup_table:
        return _sg_lookup_table[sgkey]
    # nothing worked, sgid is unknown identifier
    raise ValueError(emsg)


def IsSpaceGroupIdentifier(sgid):
    """Check if identifier can be used as an argument to GetSpaceGroup.

    Return bool.
    """
    try:
        GetSpaceGroup(sgid)
        rv = True
    except ValueError:
        rv = False
    return rv


def _buildSGLookupTable():
    """Rebuild space group lookup table from the SpaceGroupList data.

    This routine updates the global _sg_lookup_table dictionary.
    No return value.
    """
    _sg_lookup_table.clear()
    for sg in SpaceGroupList:
        _sg_lookup_table.setdefault(sg.number, sg)
        _sg_lookup_table.setdefault(str(sg.number), sg)
        _sg_lookup_table.setdefault(sg.short_name, sg)
        _sg_lookup_table.setdefault(sg.pdb_name, sg)
        _sg_lookup_table.setdefault(sg.alt_name, sg)
    # make sure None does not sneak into the dictionary
    if None in _sg_lookup_table:
        del _sg_lookup_table[None]
    return
_sg_lookup_table = {}

# Import SpaceGroup objects --------------------------------------------------

from diffpy.structure.spacegroupmod import (
    Rot_X_Y_Z, Rot_mX_mY_mZ, Rot_mX_Y_mZ, Rot_X_mY_Z,
    Rot_mX_mY_Z, Rot_X_mY_mZ, Rot_mX_Y_Z, Rot_X_Y_mZ,
    Rot_mY_X_Z, Rot_Y_mX_Z, Rot_Y_mX_mZ, Rot_mY_X_mZ,
    Rot_Y_X_mZ, Rot_mY_mX_mZ, Rot_mY_mX_Z, Rot_Y_X_Z,
    Rot_mY_XmY_Z, Rot_mXY_mX_Z, Rot_Z_X_Y, Rot_Y_Z_X,
    Rot_Y_mXY_mZ, Rot_XmY_X_mZ, Rot_mZ_mX_mY, Rot_mY_mZ_mX,
    Rot_mXY_Y_mZ, Rot_X_XmY_mZ, Rot_XmY_mY_mZ, Rot_mX_mXY_mZ,
    Rot_mX_mZ_mY, Rot_mZ_mY_mX, Rot_mXY_Y_Z, Rot_X_XmY_Z,
    Rot_XmY_mY_Z, Rot_mX_mXY_Z, Rot_X_Z_Y, Rot_Z_Y_X,
    Rot_Y_mXY_Z, Rot_XmY_X_Z, Rot_mY_XmY_mZ, Rot_mXY_mX_mZ,
    Rot_Z_mX_mY, Rot_mZ_mX_Y, Rot_mZ_X_mY, Rot_mY_Z_mX,
    Rot_Y_mZ_mX, Rot_mY_mZ_X, Rot_mZ_X_Y, Rot_Z_X_mY,
    Rot_Z_mX_Y, Rot_Y_mZ_X, Rot_mY_Z_X, Rot_Y_Z_mX,
    Rot_X_Z_mY, Rot_mX_Z_Y, Rot_X_mZ_Y, Rot_Z_Y_mX,
    Rot_Z_mY_X, Rot_mZ_Y_X, Rot_mX_Z_mY, Rot_mX_mZ_Y,
    Rot_X_mZ_mY, Rot_Z_mY_mX, Rot_mZ_Y_mX, Rot_mZ_mY_X,
    Tr_0_0_0, Tr_0_12_0, Tr_12_12_0, Tr_0_0_12,
    Tr_12_12_12, Tr_0_12_12, Tr_12_0_12, Tr_12_0_0,
    Tr_14_14_14, Tr_14_34_34, Tr_34_14_34, Tr_34_34_14,
    Tr_0_0_14, Tr_0_0_34, Tr_0_12_14, Tr_12_0_34,
    Tr_12_12_14, Tr_12_12_34, Tr_0_12_34, Tr_12_0_14,
    Tr_0_0_13, Tr_0_0_23, Tr_23_13_13, Tr_13_23_23,
    Tr_23_13_56, Tr_13_23_16, Tr_0_0_56, Tr_0_0_16,
    Tr_34_14_14, Tr_34_34_34, Tr_14_14_34, Tr_14_34_14,
)

from diffpy.structure.mmlibspacegroups import (
    sg1, sg2, sg3, sg4, sg5, sg6, sg7, sg8,
    sg9, sg10, sg11, sg12, sg13, sg14, sg15, sg16,
    sg17, sg18, sg19, sg20, sg21, sg22, sg23, sg24,
    sg25, sg26, sg27, sg28, sg29, sg30, sg31, sg32,
    sg33, sg34, sg35, sg36, sg37, sg38, sg39, sg40,
    sg41, sg42, sg43, sg44, sg45, sg46, sg47, sg48,
    sg49, sg50, sg51, sg52, sg53, sg54, sg55, sg56,
    sg57, sg58, sg59, sg60, sg61, sg62, sg63, sg64,
    sg65, sg66, sg67, sg68, sg69, sg70, sg71, sg72,
    sg73, sg74, sg75, sg76, sg77, sg78, sg79, sg80,
    sg81, sg82, sg83, sg84, sg85, sg86, sg87, sg88,
    sg89, sg90, sg91, sg92, sg93, sg94, sg95, sg96,
    sg97, sg98, sg99, sg100, sg101, sg102, sg103, sg104,
    sg105, sg106, sg107, sg108, sg109, sg110, sg111, sg112,
    sg113, sg114, sg115, sg116, sg117, sg118, sg119, sg120,
    sg121, sg122, sg123, sg124, sg125, sg126, sg127, sg128,
    sg129, sg130, sg131, sg132, sg133, sg134, sg135, sg136,
    sg137, sg138, sg139, sg140, sg141, sg142, sg143, sg144,
    sg145, sg146, sg1146, sg147, sg148, sg1148, sg149, sg150,
    sg151, sg152, sg153, sg154, sg155, sg1155, sg156, sg157,
    sg158, sg159, sg160, sg1160, sg161, sg1161, sg162, sg163,
    sg164, sg165, sg166, sg1166, sg167, sg1167, sg168, sg169,
    sg170, sg171, sg172, sg173, sg174, sg175, sg176, sg177,
    sg178, sg179, sg180, sg181, sg182, sg183, sg184, sg185,
    sg186, sg187, sg188, sg189, sg190, sg191, sg192, sg193,
    sg194, sg195, sg196, sg197, sg198, sg199, sg200, sg201,
    sg202, sg203, sg204, sg205, sg206, sg207, sg208, sg209,
    sg210, sg211, sg212, sg213, sg214, sg215, sg216, sg217,
    sg218, sg219, sg220, sg221, sg222, sg223, sg224, sg225,
    sg226, sg227, sg228, sg229, sg230, sg1003, sg1004, sg3004,
    sg1005, sg2005, sg3005, sg1006, sg1007, sg1008, sg1009, sg1010,
    sg1011, sg1012, sg1013, sg1014, sg1015, sg1017, sg2017, sg1018,
    sg2018, sg3018, sg1020, sg1021, sg1022, sg1023, sg1059, sg1094,
    sg1197,
)

from diffpy.structure.sgtbxspacegroups import (
    sg2003, sg2004, sg4005, sg5005, sg6005, sg7005, sg8005, sg9005,
    sg10005, sg2006, sg2007, sg3007, sg4007, sg5007, sg6007, sg7007,
    sg8007, sg2008, sg3008, sg4008, sg5008, sg6008, sg7008, sg8008,
    sg2009, sg3009, sg4009, sg5009, sg6009, sg7009, sg8009, sg9009,
    sg10009, sg11009, sg12009, sg13009, sg14009, sg15009, sg16009,
    sg17009, sg2010, sg2011, sg2012, sg3012, sg4012, sg5012, sg6012,
    sg7012, sg8012, sg2013, sg3013, sg4013, sg5013, sg6013, sg7013,
    sg8013, sg2014, sg3014, sg4014, sg5014, sg6014, sg7014, sg8014,
    sg2015, sg3015, sg4015, sg5015, sg6015, sg7015, sg8015, sg9015,
    sg10015, sg11015, sg12015, sg13015, sg14015, sg15015, sg16015,
    sg17015, sg2020, sg3020, sg2021, sg3021, sg1025, sg2025, sg1026,
    sg2026, sg3026, sg4026, sg5026, sg1027, sg2027, sg1028, sg2028,
    sg3028, sg4028, sg5028, sg1029, sg2029, sg3029, sg4029, sg5029,
    sg1030, sg2030, sg3030, sg4030, sg5030, sg1031, sg2031, sg3031,
    sg4031, sg5031, sg1032, sg2032, sg1033, sg2033, sg3033, sg4033,
    sg5033, sg1034, sg2034, sg1035, sg2035, sg1036, sg2036, sg3036,
    sg4036, sg5036, sg1037, sg2037, sg1038, sg2038, sg3038, sg4038,
    sg5038, sg1039, sg2039, sg3039, sg4039, sg5039, sg1040, sg2040,
    sg3040, sg4040, sg5040, sg1041, sg2041, sg3041, sg4041, sg5041,
    sg1042, sg2042, sg1043, sg2043, sg1044, sg2044, sg1045, sg2045,
    sg1046, sg2046, sg3046, sg4046, sg5046, sg1049, sg2049, sg1050,
    sg2050, sg3050, sg4050, sg1051, sg2051, sg3051, sg4051, sg5051,
    sg1052, sg2052, sg3052, sg4052, sg5052, sg1053, sg2053, sg3053,
    sg4053, sg5053, sg1054, sg2054, sg3054, sg4054, sg5054, sg1055,
    sg2055, sg1056, sg2056, sg1057, sg2057, sg3057, sg4057, sg5057,
    sg1058, sg2058, sg2059, sg3059, sg4059, sg5059, sg1060, sg2060,
    sg3060, sg4060, sg5060, sg1061, sg1062, sg2062, sg3062, sg4062,
    sg5062, sg1063, sg2063, sg3063, sg4063, sg5063, sg1064, sg2064,
    sg3064, sg4064, sg5064, sg1065, sg2065, sg1066, sg2066, sg1067,
    sg2067, sg3067, sg4067, sg5067, sg1068, sg2068, sg3068, sg4068,
    sg5068, sg6068, sg7068, sg1072, sg2072, sg1073, sg1074, sg2074,
    sg3074, sg4074, sg5074,
)

# silence pyflakes checker
assert all(o is not None for o in (SpaceGroup, SymOp,
    Rot_X_Y_Z, Rot_mX_mY_mZ, Rot_mX_Y_mZ, Rot_X_mY_Z,
    Rot_mX_mY_Z, Rot_X_mY_mZ, Rot_mX_Y_Z, Rot_X_Y_mZ,
    Rot_mY_X_Z, Rot_Y_mX_Z, Rot_Y_mX_mZ, Rot_mY_X_mZ,
    Rot_Y_X_mZ, Rot_mY_mX_mZ, Rot_mY_mX_Z, Rot_Y_X_Z,
    Rot_mY_XmY_Z, Rot_mXY_mX_Z, Rot_Z_X_Y, Rot_Y_Z_X,
    Rot_Y_mXY_mZ, Rot_XmY_X_mZ, Rot_mZ_mX_mY, Rot_mY_mZ_mX,
    Rot_mXY_Y_mZ, Rot_X_XmY_mZ, Rot_XmY_mY_mZ, Rot_mX_mXY_mZ,
    Rot_mX_mZ_mY, Rot_mZ_mY_mX, Rot_mXY_Y_Z, Rot_X_XmY_Z,
    Rot_XmY_mY_Z, Rot_mX_mXY_Z, Rot_X_Z_Y, Rot_Z_Y_X,
    Rot_Y_mXY_Z, Rot_XmY_X_Z, Rot_mY_XmY_mZ, Rot_mXY_mX_mZ,
    Rot_Z_mX_mY, Rot_mZ_mX_Y, Rot_mZ_X_mY, Rot_mY_Z_mX,
    Rot_Y_mZ_mX, Rot_mY_mZ_X, Rot_mZ_X_Y, Rot_Z_X_mY,
    Rot_Z_mX_Y, Rot_Y_mZ_X, Rot_mY_Z_X, Rot_Y_Z_mX,
    Rot_X_Z_mY, Rot_mX_Z_Y, Rot_X_mZ_Y, Rot_Z_Y_mX,
    Rot_Z_mY_X, Rot_mZ_Y_X, Rot_mX_Z_mY, Rot_mX_mZ_Y,
    Rot_X_mZ_mY, Rot_Z_mY_mX, Rot_mZ_Y_mX, Rot_mZ_mY_X,
    Tr_0_0_0, Tr_0_12_0, Tr_12_12_0, Tr_0_0_12,
    Tr_12_12_12, Tr_0_12_12, Tr_12_0_12, Tr_12_0_0,
    Tr_14_14_14, Tr_14_34_34, Tr_34_14_34, Tr_34_34_14,
    Tr_0_0_14, Tr_0_0_34, Tr_0_12_14, Tr_12_0_34,
    Tr_12_12_14, Tr_12_12_34, Tr_0_12_34, Tr_12_0_14,
    Tr_0_0_13, Tr_0_0_23, Tr_23_13_13, Tr_13_23_23,
    Tr_23_13_56, Tr_13_23_16, Tr_0_0_56, Tr_0_0_16,
    Tr_34_14_14, Tr_34_34_34, Tr_14_14_34, Tr_14_34_14,
    sg1, sg2, sg3, sg4, sg5, sg6, sg7, sg8,
    sg9, sg10, sg11, sg12, sg13, sg14, sg15, sg16,
    sg17, sg18, sg19, sg20, sg21, sg22, sg23, sg24,
    sg25, sg26, sg27, sg28, sg29, sg30, sg31, sg32,
    sg33, sg34, sg35, sg36, sg37, sg38, sg39, sg40,
    sg41, sg42, sg43, sg44, sg45, sg46, sg47, sg48,
    sg49, sg50, sg51, sg52, sg53, sg54, sg55, sg56,
    sg57, sg58, sg59, sg60, sg61, sg62, sg63, sg64,
    sg65, sg66, sg67, sg68, sg69, sg70, sg71, sg72,
    sg73, sg74, sg75, sg76, sg77, sg78, sg79, sg80,
    sg81, sg82, sg83, sg84, sg85, sg86, sg87, sg88,
    sg89, sg90, sg91, sg92, sg93, sg94, sg95, sg96,
    sg97, sg98, sg99, sg100, sg101, sg102, sg103, sg104,
    sg105, sg106, sg107, sg108, sg109, sg110, sg111, sg112,
    sg113, sg114, sg115, sg116, sg117, sg118, sg119, sg120,
    sg121, sg122, sg123, sg124, sg125, sg126, sg127, sg128,
    sg129, sg130, sg131, sg132, sg133, sg134, sg135, sg136,
    sg137, sg138, sg139, sg140, sg141, sg142, sg143, sg144,
    sg145, sg146, sg1146, sg147, sg148, sg1148, sg149, sg150,
    sg151, sg152, sg153, sg154, sg155, sg1155, sg156, sg157,
    sg158, sg159, sg160, sg1160, sg161, sg1161, sg162, sg163,
    sg164, sg165, sg166, sg1166, sg167, sg1167, sg168, sg169,
    sg170, sg171, sg172, sg173, sg174, sg175, sg176, sg177,
    sg178, sg179, sg180, sg181, sg182, sg183, sg184, sg185,
    sg186, sg187, sg188, sg189, sg190, sg191, sg192, sg193,
    sg194, sg195, sg196, sg197, sg198, sg199, sg200, sg201,
    sg202, sg203, sg204, sg205, sg206, sg207, sg208, sg209,
    sg210, sg211, sg212, sg213, sg214, sg215, sg216, sg217,
    sg218, sg219, sg220, sg221, sg222, sg223, sg224, sg225,
    sg226, sg227, sg228, sg229, sg230, sg1003, sg1004, sg3004,
    sg1005, sg2005, sg3005, sg1006, sg1007, sg1008, sg1009, sg1010,
    sg1011, sg1012, sg1013, sg1014, sg1015, sg1017, sg2017, sg1018,
    sg2018, sg3018, sg1020, sg1021, sg1022, sg1023, sg1059, sg1094,
    sg1197,
    sg2003, sg2004, sg4005, sg5005, sg6005, sg7005, sg8005, sg9005,
    sg10005, sg2006, sg2007, sg3007, sg4007, sg5007, sg6007, sg7007,
    sg8007, sg2008, sg3008, sg4008, sg5008, sg6008, sg7008, sg8008,
    sg2009, sg3009, sg4009, sg5009, sg6009, sg7009, sg8009, sg9009,
    sg10009, sg11009, sg12009, sg13009, sg14009, sg15009, sg16009,
    sg17009, sg2010, sg2011, sg2012, sg3012, sg4012, sg5012, sg6012,
    sg7012, sg8012, sg2013, sg3013, sg4013, sg5013, sg6013, sg7013,
    sg8013, sg2014, sg3014, sg4014, sg5014, sg6014, sg7014, sg8014,
    sg2015, sg3015, sg4015, sg5015, sg6015, sg7015, sg8015, sg9015,
    sg10015, sg11015, sg12015, sg13015, sg14015, sg15015, sg16015,
    sg17015, sg2020, sg3020, sg2021, sg3021, sg1025, sg2025, sg1026,
    sg2026, sg3026, sg4026, sg5026, sg1027, sg2027, sg1028, sg2028,
    sg3028, sg4028, sg5028, sg1029, sg2029, sg3029, sg4029, sg5029,
    sg1030, sg2030, sg3030, sg4030, sg5030, sg1031, sg2031, sg3031,
    sg4031, sg5031, sg1032, sg2032, sg1033, sg2033, sg3033, sg4033,
    sg5033, sg1034, sg2034, sg1035, sg2035, sg1036, sg2036, sg3036,
    sg4036, sg5036, sg1037, sg2037, sg1038, sg2038, sg3038, sg4038,
    sg5038, sg1039, sg2039, sg3039, sg4039, sg5039, sg1040, sg2040,
    sg3040, sg4040, sg5040, sg1041, sg2041, sg3041, sg4041, sg5041,
    sg1042, sg2042, sg1043, sg2043, sg1044, sg2044, sg1045, sg2045,
    sg1046, sg2046, sg3046, sg4046, sg5046, sg1049, sg2049, sg1050,
    sg2050, sg3050, sg4050, sg1051, sg2051, sg3051, sg4051, sg5051,
    sg1052, sg2052, sg3052, sg4052, sg5052, sg1053, sg2053, sg3053,
    sg4053, sg5053, sg1054, sg2054, sg3054, sg4054, sg5054, sg1055,
    sg2055, sg1056, sg2056, sg1057, sg2057, sg3057, sg4057, sg5057,
    sg1058, sg2058, sg2059, sg3059, sg4059, sg5059, sg1060, sg2060,
    sg3060, sg4060, sg5060, sg1061, sg1062, sg2062, sg3062, sg4062,
    sg5062, sg1063, sg2063, sg3063, sg4063, sg5063, sg1064, sg2064,
    sg3064, sg4064, sg5064, sg1065, sg2065, sg1066, sg2066, sg1067,
    sg2067, sg3067, sg4067, sg5067, sg1068, sg2068, sg3068, sg4068,
    sg5068, sg6068, sg7068, sg1072, sg2072, sg1073, sg1074, sg2074,
    sg3074, sg4074, sg5074,
))
