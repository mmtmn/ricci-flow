import numpy as np
import matplotlib.pyplot as plt

gs=[]
def ricci_flow(g, t_max, dt):
  # Initialize the time and the Ricci curvature
  t = 0
  ricci = np.zeros_like(g)

  # Compute the Ricci curvature at the initial time
  for i in range(g.shape[0]):
    for j in range(g.shape[1]):
      for k in range(g.shape[2]):
        ricci[i, j, k] = g[i, j, k] + g[i, k, j] - g[j, k, i]

  # Iterate over time steps until we reach the maximum time
  while t < t_max:
    # Update the metric using the Ricci flow equation
    g += dt * (-2 * ricci)

    # Recompute the Ricci curvature at the new time
    for i in range(g.shape[0]):
      for j in range(g.shape[1]):
        for k in range(g.shape[2]):
          ricci[i, j, k] = g[i, j, k] + g[i, k, j] - g[j, k, i]

    # print(g)
    gs.append(g)
    # Update the time
    t += dt

# Example usage
g = np.ones((10, 10, 10)) # Initialize the metric to be the identity matrix

ricci_flow(g, t_max=1.0, dt=0.01) # Evolve the metric for 1 second with a time step of 0.01

# print(gs)

xs = [x for x in range(len(gs))]
# plt.plot(xs, gs)
# plt.show()
# # Make sure to close the plt object once done
# plt.close()

import pandas
df = pandas.DataFrame(data={"col1": xs, "col2": gs})
df.to_csv("./file.csv", sep=',',index=False)