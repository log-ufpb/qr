## Instance space analysis

According to Smith-Miles and Muñoz (2023),

> "Instance Space Analysis (ISA) is a recently developed methodology to (a) support objective testing of algorithms and (b) assess the diversity of test instances. Representing test instances as feature vectors, the ISA methodology extends Rice’s 1976 Algorithm Selection Problem framework to enable visualization of the entire space of possible test instances, and gain insights into how algorithm performance is affected by instance properties. Rather than reporting algorithm performance on average across a chosen set of test problems, as is standard practice, the ISA methodology offers a more nuanced understanding of the unique strengths and weaknesses of algorithms across different regions of the instance space that may otherwise be hidden on average. It also facilitates objective assessment of any bias in the chosen test instances and provides guidance about the adequacy of benchmark test suites."

An ISA is capable of generating a plot of instances based on the projection of various features into a 2D space. It may be necessary to analyze multiple graphs simultaneously in order to obtain meaningful conclusions when interpreting an ISA. For example, the following plot suggests that the analyzed algorithm performs worse for the instances projected in the lower right half of the 2D space, as the gap is higher in that section.

<img src="https://github.com/log-ufpb/qr/blob/main/docs/src/instance-space-analysis/graphs/performance-h.png" width="70%" height="70%">

Concurrently, the following plot shows the value of the feature `max-utilization` in each instance. By comparing both graphs, we can infer a positive correlation tendency between the feature `max-utilization` and the instance difficulty. In other words, the higher the `max-utilization`, the harder the instance tends to be for the analyzed algorithm to solve.

<img src="https://github.com/log-ufpb/qr/blob/main/docs/src/instance-space-analysis/graphs/feature-max-utilization.png" width="70%" height="70%">

Finally, some algorithms perform better in certain instance sets, and an ISA is also capable of providing this valuable insight. As already observed, the algorithm `H` performs well in instances with a low `max-utilization`. However, with the increase of `max-utilization`, `F1_i` becomes the best choice.

<img src="https://github.com/log-ufpb/qr/blob/main/docs/src/instance-space-analysis/graphs/SVM-Selection.png" width="70%" height="70%">

Making a legible projection of the instances into the 2D space is a challenging task since each instance is represented by a vector of features whose length is usually greater than 2. Fortunately, the Melbourne Algorithm Test Instance Library with Data Analytics (Matilda) takes care of everything.

## Using Matilda

Matilda is an intuitive tool. Using the online version is recommended over downloading the code locally, as the former is much simpler.

For the input data, follow the instructions on their [GitHub repository](https://github.com/andremun/InstanceSpace?tab=readme-ov-file#the-metadata-file).

There is a complete tutorial available [here](https://matilda.unimelb.edu.au/matilda/matildadata/tutorials/matilda-technical-details.mp4). Start watching at time 33:32 if you want to use the online version.

## References

Kate Smith-Miles and Mario Andrés Muñoz. 2023. Instance Space Analysis for Algorithm Testing: Methodology and Software Tools. ACM Comput. Surv. 55, 12, Article 255 (December 2023), 31 pages. https://doi.org/10.1145/3572895