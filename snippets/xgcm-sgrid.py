import xarray as xr

def extract_xgcm_meta_from_sgrid_data(ds):
    """
    Analyse an xarray Dataset using SGRID conventions
    """



# comments are approximations to the original SGRID concept

    { "X": # XZ coord?
        { "center": "MC" # SGRID node
        , "left":   "M"  # SGRID face
        }
} , { "Y": # YZ coord?
        { "center": "NC" # SGRID node
        , "left":   "N"  # SGRID face
        }
  }

"""
* inspect ds.grid
  * inspect face_dimensions
"""
