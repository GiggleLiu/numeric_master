#!/usr/bin/env python
# ****************************************************************************
# 
# ALPS Project: Algorithms and Libraries for Physics Simulations
# 
# ALPS Libraries
# 
# Copyright (C) 2010 by Jan Gukelberger <gukelberger@phys.ethz.ch> 
# 
# This software is part of the ALPS libraries, published under the ALPS
# Library License; you can use, redistribute it and/or modify it under
# the terms of the license, either version 1 or (at your option) any later
# version.
#  
# You should have received a copy of the ALPS Library License along with
# the ALPS Libraries; see the file LICENSE.txt. If not, the license is also
# available from http://alps.comp-phys.org/.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT 
# SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE 
# FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.
# 
# ****************************************************************************

import pyalps
import numpy as np

def run_dmrg(nsite, J2):
    #prepare the input parameters
    parms=[{ 
        'LATTICE_LIBRARY'           : 'j1j2_%d.xml'%nsite,
        'LATTICE'                   : 'J1J2',
        'MODEL'                     : 'spin',
        'local_S0'                  : '0.5',  # local_S0 means type 0 site, right?
        'CONSERVED_QUANTUMNUMBERS'  : 'N,Sz',
        'Sz_total'                  : 0,
        'J0'                        : 1,
        'J1'                        : J2,
        'SWEEPS'                    : 4,
        'NUMBER_EIGENVALUES'        : 1,
        'MAXSTATES'                 : 400
       }]

    #write the input file and run the simulation
    prefix = 'data/j1j2_%dJ2%s'%(nsite,J2)
    input_file = pyalps.writeInputFiles(prefix,parms)
    res = pyalps.runApplication('dmrg',input_file,writexml=True)

    #load all measurements for all states
    data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=prefix))

    # print properties of the eigenvector for each run:
    for run in data:
        for s in run:
            print('%s : %s'%(s.props['observable'], s.y[0]))

if __name__ == '__main__':
    import sys, os
    nsite, J2 = sys.argv[1:]
    nsite = int(nsite)
    lattice_file = 'lattices/j1j2_%d.xml'%nsite
    if not os.path.isfile(lattice_file):
        from build_lattice import build_j1j2
        build_j1j2(nsite, lattice_file)
    run_dmrg(nsite, float(J2))
