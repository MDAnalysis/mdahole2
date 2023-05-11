__all__ = [
    "DCD",
    "PDB_HOLE",
    "MULTIPDB_HOLE",
]

from pkg_resources import resource_filename

PDB_HOLE = resource_filename(__name__,
                             'data/1grm_single.pdb')
MULTIPDB_HOLE = resource_filename(__name__,
                                  'data/1grm_elNemo_mode7.pdb.bz2')
DCD = resource_filename(__name__,
                        'data/adk_dims.dcd')

del resource_filename