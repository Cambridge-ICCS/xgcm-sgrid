# Helpful links
* https://web.archive.org/web/20160417032300/http://pycomodo.forge.imag.fr/norm.html
* https://xgcm.readthedocs.io/en/latest/grids.html
* https://sgrid.github.io/sgrid/
* https://github.com/xgcm/xgcm

XGCM discussions on SGRID:

* https://github.com/xgcm/xgcm/issues/109

Sample S-Grid Data Sources
* https://dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/YKM4LQ
* https://drive.google.com/file/d/1MH1b5vt3Cu-Hg0I2tdGUA3CxiLU3T9Za/view?usp=sharing
* https://opendap.deltares.nl/thredds/catalog/opendap/deltares/Delft3D/netcdf_example_files/catalog.html?dataset=varopendap/deltares/Delft3D/netcdf_example_files/trim-westernscheldt_sph.nc

## Pseudocode & discussion
### Analysing `grid.face_dimensions`
  * List of `FACE_NAME: NODE_NAME (padding: PADDING)`
  * Each entry becomes an axis in xGCM

e.g.

```
node_dimensions: MC NC
face_dimensions: M:MC (padding: low) N:NC (padding: low)
```

### Mapping SGRID `padding` to `position`
Given that SGRID face centre corresponds to an xGCM cell centre:

  * `none` -> `outer`
  * `both` -> `inner`
  * `low`  -> `right`
  * `high` -> `left`

Compare:

  * https://sgrid.github.io/sgrid/#2d-grid
  * https://xgcm.readthedocs.io/en/latest/grids.html#axes-and-positions
