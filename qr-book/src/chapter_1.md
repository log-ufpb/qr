# Multiple-Choice Knapsack Problem (MCKP)

Consider that each item \\( i \in I \\) contains a set \\( N_i \\) of variants \\( j \\). In this case, the objective is to select one variant of each item in order to maximize value \\( v_{ij} \\). The mathematical formulation can be written as follows:

**Sets**

- \\( I = \{1, \dots, n\} \\): set of items
- \\( N_i = \{1, \dots, t\} \\): set of variants of item \\( i \in I \\)

**Parameters**

- \\( C \in \mathbb{R}_{>0} \\): maximum capacity of the knapsack
- \\( v_{ij} \in \mathbb{R}_{>0} \\): value of the variant \\( j \in N_i \\) of the item \\( i \in I \\)
- \\( w_{ij} \in \mathbb{R}_{>0} \\): weight of the variant \\( j \in N_i \\) of the item \\( i \in I \\)

**Decision Variables**

- \\( x_{ij} = \begin{cases}
1, & \text{if variant } j \in N_i \text{ of item } i \in I \text{ is selected} \\\\
0, & \text{otherwise}
\end{cases} \\)

**Mathematical Formulation**

\\[
\begin{aligned}
\text{maximize} \quad & \sum_{i \in I} \sum_{j \in N_i} v_{ij} x_{ij} \\\\
\text{subject to} \quad
& \sum_{i \in I} \sum_{j \in N_i} w_{ij} x_{ij} \leq C \\\\
& \sum_{j \in N_i} x_{ij} = 1 \quad && \forall i \in I \\\\
& x_{ij} \in \{0,1\} \quad && \forall i \in I,  j \in N_i
\end{aligned}
\\]
