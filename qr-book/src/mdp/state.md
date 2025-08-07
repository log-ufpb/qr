# State

At each decision point \\(k\\), the state of the system is represented by \\(s_k \in \mathcal{S}\\), which encapsulates the current situation of the system.

## Dynamic routing example

In a dynanimc vehicle routing problem, a state can be modeled as a four-tuple:

\\[s_k = (t_k, r_k, l_k, \theta_k)\\]

In which, \\(t_k)\\) is the current system time, \\(r_k\\) is the new request, \\(l_k\\) is the last visited location of each vehicle \\(v \in \mathcal{V}\\) and \\(\theta_k\\) is the route plan.
