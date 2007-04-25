# This module is imported from top level diffpy setup.py.
# It has to define the following variables:
#     name, description, diffpy_deps, other_deps, setup_args

"""Structure - objects for storage and manipulation of crystal structures.

Packages:   diffpy.Structure
Scripts:    transtry, anyeye
"""

# version
__id__ = "$Id$"

import os.path

thisfile = os.path.abspath(locals().get('__file__', 'setup_args.py'))
thisdir = os.path.dirname(thisfile)

# name of this subpackage
name = "diffpy.Structure"
description =  "Crystal structure container.",

# dependencies from diffpy
diffpy_deps = []

# third-party dependencies
other_deps = [
    "numpy",
    ]

# define distribution arguments for this subpackage
setup_args = {
    "name" : name,
    "description" : description,
    "packages" : [
        "diffpy.Structure",
        "diffpy.Structure.Parsers"
        ],
    "package_dir" : {
        "diffpy.Structure" : os.path.join(thisdir, "Structure")
        },
    "scripts" : [
        os.path.join(thisdir, "applications/anyeye"),
        os.path.join(thisdir, "applications/transtru")
        ],
}

# End of file 
