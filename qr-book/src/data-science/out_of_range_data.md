# How to Deal with Out-of-Range Data

Out-of-range data refers to values that fall outside the expected or acceptable range for a given feature. These values can occur due to data entry errors, system glitches, or real but rare events. Handling such values appropriately is critical for ensuring robust and accurate models or analyses.

---

### 1. Dropping Data

Removing rows that contain out-of-range values.

**Pros:**

* Simple and effective if few data points are affected.
* Ensures only valid data is used in analysis.

**Cons:**

* May lead to information loss, especially if the affected proportion is high.
* Can introduce bias if the removed data is not missing at random.

**Rule of Thumb:**
Only drop rows when a **small proportion** (e.g., < 5%) of your dataset contains out-of-range values.

**Example:**

```python
df = df[df['age'] <= 100]  # Remove entries with age > 100
```


### 2. Setting Custom Minimums and Maximums (Capping or Clipping)

Cap values at predefined minimum and maximum thresholds.

**Pros:**

* Preserves all data points while limiting the influence of outliers.
* Useful for models sensitive to extreme values (e.g., linear regression).

**Cons:**

* Can distort the data distribution.
* Requires domain knowledge to set appropriate thresholds.

**Example:**

```python
df['income'] = df['income'].clip(lower=0, upper=200_000)
```


### 3. Treat as Missing and Impute

Convert out-of-range values to `NaN` and handle them using imputation techniques.

**Pros:**

* Flexible and model-friendly.
* Allows for advanced imputation strategies (e.g., KNN, regression).

**Cons:**

* Introduces complexity.
* Risk of incorrect imputation if assumptions are wrong.

**Example:**

```python
df.loc[df['temperature'] < -50, 'temperature'] = np.nan
df['temperature'].fillna(df['temperature'].mean(), inplace=True)
```


### 4. Setting Custom Values Based on Business Rules

Replace out-of-range values with specific values that reflect domain-specific assumptions.

**Pros:**

* Makes data consistent with business logic.
* Can enhance interpretability of results.

**Cons:**

* Requires clear and justifiable domain rules.
* May oversimplify real-world complexity.

**Example:**

```python
# Set to 0 if below minimum viable production
df.loc[df['production'] < 0, 'production'] = 0
```


### 5. Binning or Categorization

Convert continuous out-of-range values into categorical bins.

**Pros:**

* Useful for decision trees or models that handle categories well.
* Can handle extreme values gracefully.

**Cons:**

* Loss of numeric precision.
* Choice of bins affects model performance.

**Example:**

```python
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 65, 100], labels=['child', 'adult', 'senior'])
```


### 6. Log or Other Transformations

Apply transformations to reduce the effect of extreme values rather than removing or capping them.

**Pros:**

* Useful for skewed distributions.
* Retains the structure of the data.

**Cons:**

* May not be interpretable in business terms.
* Zero or negative values can cause issues.

**Example:**

```python
df['log_income'] = np.log1p(df['income'])  # log(1 + income)
```

---

### Final Thoughts

Choosing the right strategy depends on:

* The proportion of out-of-range values.
* Domain knowledge and business constraints.
* The sensitivity of downstream models or analyses to extreme values.

When in doubt, **visualize your data**, consult domain experts, and test different approaches to ensure robustness.
