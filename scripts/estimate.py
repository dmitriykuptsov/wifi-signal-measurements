import matplotlib.pyplot as plt
import numpy as np

import gstools as gs

timestamp, signal, x, y, z, lat, lng = np.loadtxt("dataset.csv").T

bin_center, vario = gs.vario_estimate(
    (lat, lng), signal, latlon=True, geo_scale=gs.KM_SCALE
)

model = gs.Spherical(latlon=True, geo_scale=gs.KM_SCALE)
model.fit_variogram(bin_center, vario, nugget=False)
#ax = model.plot("vario_yadrenko", x_max=max(bin_center))
#ax.scatter(bin_center, vario)
print(model)

ok = gs.krige.Ordinary(
    model=model,
    cond_pos=(lat, lng),
    cond_val=signal
)

g_lat = np.arange(41.126, 41.129, 0.0005)
g_lon = np.arange(69.66, 69.67, 0.0005)

ok.set_pos((g_lat, g_lon), mesh_type="structured")
ok(return_var=False, store="signal_field")
#ok(only_mean=True, store="mean_field")

levels = np.linspace(-100, -30, 70)
#levels = np.linspace(5, 25, 64)
fig, ax = plt.subplots(1, 2, figsize=[10, 5], sharey=True)

print(len(g_lat))
print(len(g_lon))
print(ok["signal_field"])

sca = ax[0].scatter(lng, lat, c=signal, vmin=-100, vmax=-30, cmap="coolwarm")
co1 = ax[1].contourf(g_lon, g_lat, ok["signal_field"], levels, cmap="coolwarm")

[ax[i].set_xlim([69.66, 69.67]) for i in range(2)]
[ax[i].set_xlabel("Lon in deg") for i in range(2)]
ax[0].set_ylabel("Lat in deg")

ax[0].set_title("WiFi signal real-data")
ax[1].set_title("Interpolated signal")

fmt = dict(orientation="horizontal", shrink=0.5, fraction=0.1, pad=0.2)
fig.colorbar(co1, ax=ax, **fmt).set_label("Signal in [dBm]")
fig.savefig("estimate.pdf")
