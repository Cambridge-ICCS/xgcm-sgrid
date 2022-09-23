import xarray as xr
output_ds = xr.Dataset(
        coords={
            "x_c": (
                ["x_c"],
                np.arange(1, 10),
                {"axis": "X"},
            ),
           "x_g": (
                ["x_g"],
                np.arange(0.5, 9),
                {"axis": "X", "c_grid_axis_shift": -0.5},
            ),
        }
    )
    
  
  
time=unlimited
inode=9
icell=9
padding="low"
topology_dimension=1
node_dimensions="inode"
edge_dimensions="icell: inode (padding: low)"
input_ds=xr.Dataset(
