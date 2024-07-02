import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy.time import Time
from astropy.visualization import astropy_mpl_style
from astropy import units as u
plt.style.use(astropy_mpl_style)
# Sample star coordinates (RA, Dec) in degrees
stars = [
    {"name": "Sirius", "ra": 101.2875, "dec": -16.7161},
    {"name": "Betelgeuse", "ra": 88.7929, "dec": 7.4071},
    {"name": "Rigel", "ra": 78.6345, "dec": -8.2016},
    # Add more stars as needed
]
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.grid(True)
for star in stars:
    coord = SkyCoord(ra=star["ra"]*u.deg, dec=star["dec"]*u.deg, frame='icrs')
    ax.scatter(coord.ra.rad, coord.dec.deg, s=50, label=star["name"])
ax.legend()
plt.title("Star Chart")
plt.show()

