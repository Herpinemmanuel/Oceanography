# Case 6 : Southatlgyre6

In this case we choose to :

-> Replace harmonic diffusion/viscosity model by a schema of LEITH 

Documentation : http://mitgcm.org/public/r2_manual/latest/online_documents/node86.html#SECTION003211400000000000000

-> Change advection schema for Temperature : less diffusive than the three first cases

-> Edit advection schema in moment equations : centered differences to a schema which keeps Kinetic energy during more time

-> 60 vertical levels

-> Creation of 'etan' which is the data of ETA with a gap of time of 2 days

-> Scale : 14km between 2 points of the mesh
