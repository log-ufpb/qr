## When to use it

A significance test relies on two hypotheses: the null hypothesis (H<sub>0</sub>) and the alternative hypothesis (H<sub>a</sub>). It can be applied, for instance, to formally confirm if the average gaps found by two algorithms are statistically different. In such a case, H<sub>0</sub> states that **there are no differences between the average gaps**, and H<sub>a</sub> states the logical opposite, i.e., that **there are differences between the average gaps**.

## A few tips

### Building the distribution of the differences

Suppose the samples, namely the average gaps found by algorithms A and B, are a = [250, 500, ..., 300], and b = [251, 480, ..., 350], respectively. Then, the distribution of the differences is a - b = [-1, 20, ..., -50].

### Normality test

Depending on the type of test one wishes to perform, a [normality test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html) might be required. That is the case for parametric tests like the t-test. For nonparametric tests, such as the [Wilcoxon signed-rank test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html), **no assumptions are made on the samples**, and the normality test is not necessary. The following diagram shows the type of test one must use based on a few characteristics of the data.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*620UIGQx3RVbZUsF76-Img.jpeg)

Although not strictly necessary, one can apply a normality test on a - b to confirm that it is not normally distributed and justify the choice of employing a nonparametric test.

## Wilcoxon signed-rank test

The Wilcoxon signed-rank test can either reject the null hypothesis in favor of the alternative hypothesis, or fail to reject H<sub>0</sub>. **The latter does not mean that the null hypothesis is accepted**.

## Example of an article with significance tests

[Generating guitar solos by integer programming](https://doi.org/10.1080/01605682.2017.1390528)
