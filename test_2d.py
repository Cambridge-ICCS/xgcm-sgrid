import xarray as xr
import numpy as np
#Input Information
time= UNLIMITED
inode=10
jnode=20
icell=9
jcell=19
topology_dimension=2
node_dimensions= "inode jnode"
face_dimension= "icell: inode (padding: none) jcell: jnode (padding: none)" ;


#Comodo Output Information
axes={"I","J"]
coords={
  "i" : (("i",),np.arange(9), {"axis": "I"}),
  "i1" : (("i1",),np.arange(10)-0.5,
           {"axis": "i", "c_grid_axis_shift":-0.5}),
  "j" : (("j",),np.arange(19), {"axis": "J"}),
  "j1" : (("j1",),np.arange(20)-0.5,
           {"axis": "j", "c_grid_axis_shift":-0.5}), 
}
      
comodo_output_ds=xr.Dataset(
  coords=coords,)
      
      
#Xgcm Output Info
axes={"I","J"]
coords={
  "i" : (("i",),np.arange(9)),
  "i1" : (("i1",),np.arange(10)-0.5),
  "j" : (("j",),np.arange(19)),
  "j1" : (("j1",),np.arange(20)-0.5), 
}
grid_coords={"I": {"center":"i", "outer":"i1"},"J": {"center":"j", "outer":"j1"}}
      
      
