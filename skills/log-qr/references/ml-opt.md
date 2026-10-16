# Machine Learning Under a Modern Optimization Lens

## Summary
- Learning to make decisions directly from data
    - Optimal Policy Trees
    - Prescriptive Neural Networks
    - ROAD
- Multimodal data
    - TabText
- How to deal with missing data
    - Data Imputation
    - Matrix Completion
    - Tensor Completion

## Learning to make decisions directly from data

Description: This is useful when you want to make decisions based on historical data (observations).

Take a set of features per observation $\mathbf{x}$, a set of mutually-exclusive policy options, and, for each observation, a real-valued outcome resulting from applying a given treatment to this observation. Our end goal is to learn the treatment assignment that optimizes the outcome for a new observation $\mathbf{x}$. This is challenging to learn because in observational data, we only know the outcome for the prescription $t_i$ that patient $i$ actually received. We do not know what would have happened (counterfactuals) to patient $i$ under the alternative treatments.

To overcome this challenge, we apply causal inference techniques, developed to learn the true causal dependence between the treatment application and the outcome. We highlight three approaches:
1. Direct Method: Train a different model for each treatment. However, this method is susceptible to treatment assignment bias (e.g., a stronger treatment may be prescribed more often to sicker patients, who die with higher probability because they are sicker, not because the treatment is worse; and the model for the lighter treatment may estimate a better survival outcome for the sicker out-of-sample patient because its training data contained more healthier patients than sicker patients).
2. Inverse Propensity Weighting: This method tries to fix the treatment assignment bias by reweighing the population. For an observation (e.g., patient) with features $\mathbf{x}$, the propensity score measures how likely this observation was to receive the treatment observed in the data, as opposed to any other treatment. We can then reweigh the outcomes in the observed data to make it balanced. However, this method usually has high variance, because it is very sensitive to minor changes in the propensity score estimates.
3. Doubly Robust: Combines both in a joint reward expression.

For any of these approaches, we can now estimate the outcomes for the alternative treatments and train a model that prescribes the best treatment given the observed features (with trees or neural networks).

References: Lecture slides (Lecture 11, Recitation 6); Bertsimas and Dunn book (Chapters 13 and 14); paper on "Optimal Prescriptive Trees" by Bertsimas, Dunn, and Mundru.

### ROAD

Description: Combining some of the definitions above, ROAD is a framework for computing counterfactuals in prescriptive problems that involve a binary decision (treat / do not treat) in which one option is known to be generally beneficial, and where we learn from observational (non-randomized) data. Its purpose is to correct the confounding that arises because the decision in the data was not assigned at random, addressing both the observed confounding (differences in recorded features between the two groups) and the unobserved confounding (hidden differences the recorded features do not capture) before prescribing a policy. The medical setting (using observational data instead of clinical trials) is the motivating application, but the framework is general.

The pipeline has three steps. First, prognostic matching corrects the observed confounding: a baseline model trained only on the untreated observations estimates each observation's outcome under no treatment, observations are grouped into risk buckets, and within each bucket, treated and untreated observations are matched by feature similarity through optimization (optimal assignment), discarding non-comparable observations so the resulting cohort emulates a randomized trial. Second, weight tuning corrects residual unobserved confounding: two outcome estimators (one per option) produce the counterfactuals, and if their average outcomes contradict the known benefit of the treatment, a weight on the good-outcome treated observations is increased until they no longer do. Third, an Optimal Policy Tree is trained on the corrected counterfactuals to prescribe the option for each observation and reveal interpretable subgroups. Sensitivity and specificity are used to validate the prescriptions and to tune the weight.

Consider ROAD when the decision is binary, one option is known to be beneficial in general, the outcome is binary, and only observational (non-randomized) data are available.

References: Lecture slides (Lecture 18, Recitation 11); paper on "ROAD to precision medicine" by Bertsimas, Koulouras, and Margonis.

## Multimodal data: TabText

Description: For tabular data, machine learning models do not get contextual information from the column labels. For example, the model does not have the context that the column "Glucose" may have thresholds and correlations with other indicators already known in the literature. TabText converts tables into contextual language and applies pretrained large language models to generate enriched embeddings. Moreover, when we have unstructured data in addition to the tabular data (e.g., clinical notes), this allows us to convert everything into text and process the different kinds of information together.

Reference: paper on "TabText: Language-Based Representations of Tabular Health Data for Predictive Modelling" by Carballo et al.

## How to deal with missing data

### Data imputation

Description: Imputation methods in the literature may struggle to scale, lose accuracy when the percentage of missing data is large, or require strong assumptions about the underlying distribution of the missing data. This is an optimization-based alternative to data imputation.

We formulate the problem as a (non-convex, nonlinear) integer program, in which we minimize the sum of Euclidean distances from each imputed value to its $K$ nearest neighbors. To solve this problem, due to its non-convexity and nonlinearity, we use first-order methods with random warm starts (Block Coordinate Descent and Coordinate Descent). The method can be extended to handle categorical variables and imputation models other than KNN (e.g., decision trees, SVM).

References: Lecture slides (Lecture 19); Bertsimas and Dunn book (Chapter 19).

### Matrix Completion

Description: Here, we have a sparse matrix that records interactions between users (e.g., Netflix user) and products (e.g., movies). In principle, we do not have associated features to either the user or the product, but only some of their interactions.

We cannot fill the missing data without imposing any sort of structure on it. Thus, we impose the low-rank assumption, which carries two components:
1. Sparsity: The interaction between user $i$ and product $j$ (e.g., a movie) is affected by a small number of underlying factors (e.g., genre, director, cast). In other words, this component assumes that the users only look at $k$ factors when determining their (movie) preferences, but at varying weights for each user. However, in general, the features are in a latent space that is not interpretable, as you will see later that we are only decomposing our original matrix into a product of a user matrix (which learns the preferences - weights - of the user over the product features) and a product matrix (which learns the values each product should assume on the best latent space of $k$ features) to force it to be $k$-rank (i.e., the resulting matrix will have at most $k$ linearly independent rows).
2. Linearity: The effect of each of the factors is additive (i.e., we can write the interaction as a weighted sum of the $k$ factors for each user-product pair).

Under these assumptions, we can fit a completed low-rank matrix $\mathbf{X} = \mathbf{U} \mathbf{V}$, where $\mathbf{U} \in \mathbb{R}^{n \times k}$ is the user matrix and $\mathbf{V} \in \mathbb{R}^{k \times m}$ is the product matrix, while minimizing the squared loss of our imputed matrix with respect to the existing data. If interpretability is important in our case, we can set $\mathbf{V} = \mathbf{S} \mathbf{B}$, where $\mathbf{B}$ is a known feature matrix (e.g., genre, director, cast, Rotten Tomatoes rating, duration, awards, etc.), then each feature in $\mathbf{V}$ will be a linear combination of our known features. Since a general linear combination of known features is still not very interpretable, we could pose an additional sparsity assumption that chooses at most $k$ out of the $p$ known features. This problem can be formulated as a binary convex optimization problem, which can be solved by a cutting plane algorithm.

We can extend this method to tensors (arrays with 3 or more dimensions).

References: Lecture slides (Lectures 21 and 22, Recitation 13); Bertsimas and Dunn book (Chapters 24 and 25); paper on "Interpretable Matrix Completion: A Discrete Optimization Approach" by Bertsimas and Li; paper on "Tensor completion with noisy side information" by Bertsimas and Pawlowski.
