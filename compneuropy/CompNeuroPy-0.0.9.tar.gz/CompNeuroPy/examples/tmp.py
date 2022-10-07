from ANNarchy import Neuron, Population, compile, Monitor, simulate, setup, get_time, dt
from CompNeuroPy import my_raster_plot, get_pop_rate
import numpy as np

period = 11
timestep = 4
actual_period = int(period / timestep) * timestep
start = 17
stop = start + 140

setup(dt=timestep)

n = Neuron(equations="a=t", spike="a>0")
p = Population(1, n)

compile()

m = Monitor(p, ["a", "spike"], start=False, period=period)

simulate(start)
m.start()
start_time = get_time()
simulate(stop - start)  #
m.pause()
stop_time = get_time()
simulate(100)
# m.resume()
# simulate(1000)  #
# m.pause()
# simulate(1000)

r = m.get("a")
data = m.get("spike")
print(f"data: {data}")

t, n = my_raster_plot(data)
t = t * dt()  # convert time steps into ms
mask = ((t >= start_time).astype(int) * (t <= stop_time).astype(int)).astype(bool)
print(f"mask: {mask}")
print(f"mask.size: {mask.size}")

time_arr, firing_rate = get_pop_rate(
    data,
    stop_time - start_time,
    dt=dt(),
    t_start=start_time,
)
print(firing_rate.shape)
print(time_arr.shape)
print(np.arange(start_time, stop_time, dt()).shape)

print(r.shape)
print(r[0], r[-1])

# print(f"start_time: {start_time}")
# print(f"stop_time: {stop_time}")
# print(f"period: {period}")
# print(f"timestep: {timestep}")
# print("calculated")
# print(f"actual_period: {actual_period}")
start_time = np.array([start_time, 56])
stop_time = np.array([stop_time, 1501])

actual_start_time = np.ceil(start_time / actual_period) * actual_period
print(f"actual_start_time: {actual_start_time}")

actual_stop_time = np.ceil(stop_time / actual_period - 1) * actual_period
print(f"actual_stop_time: {actual_stop_time}")

nr_rec_vals = (
    1 + (actual_stop_time - actual_start_time) / actual_period
)  # np.arange(actual_start_time, actual_stop_time + 1, actual_period)
print(nr_rec_vals)
