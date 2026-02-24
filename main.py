import sunpy.map
import sunpy.data.sample
import matplotlib.pyplot as plt

# 1. Data Ingestion: Loading a metadata-rich FITS file
aia_map = sunpy.map.Map(sunpy.data.sample.AIA_171_IMAGE)

# 2. Metadata Inspection: Accessing telescope telemetry
print(aia_map) 

# 3. Scientific Visualization
plt.figure(figsize=(6, 6))
aia_map.plot()
plt.title("Solar Corona at 171 Å (Extreme Ultraviolet)")
plt.colorbar(label="Intensity")
plt.show()
