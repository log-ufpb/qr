# Houd-Out

**Hold-Out** is a sampling technique used to split a dataset into two disjoint subsets: the **training set** and the **test set**.
The model is trained solely on the training set, and its performance is then evaluated on the unseen test set.

Given a proportion \\( P \\) for training, the test set will have a proportion \\( 1 - P \\).
A common choice is \\( P = 2/3\\), but other splits like \\(70/30\\) or \\(80/20\\) are also widely used, depending on the dataset and the problem.

The Hold-Out method is most appropriate when the dataset is large enough to ensure that both the training and test sets are representative of the overall data distribution.

## Example

Steps:

1. Copy the target column, which is the column we want to predict.

2. Remove the target column from the dataset.

3. Split the dataset.

This results in four subsets:

- `X_train`: Training data without the labels

- `X_test`: Testing data without the labels

- `y_train`: Labels for the training data

- `y_test`: Labels for the testing data

The model is trained on X_train and evaluated by comparing its predictions on X_test with the actual labels in y_test.

```python
from sklearn.model_selection import train_test_split

df_target = df.target.copy()
df_data = df.drop("target", axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    df_data,
    df_target,
    random_state=21,
    test_size=0.25
)
```

## Limitations

The Hold-Out method may result in the training and test sets having different class distributions, especially in datasets with class imbalance.
This can cause the model to perform poorly on certain classes if they are **underrepresented** in the training set or **overrepresented** in the test set.

To mitigate this issue, **stratified sampling** can be used when splitting the data.
Stratification ensures that the proportion of each class is preserved in both the training and test sets, making the evaluation more reliable and representative of the overall dataset.

#### Example with Stratification

```python
from sklearn.model_selection import train_test_split

df_target = df.target.copy()
df_data = df.drop("target", axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    df_data,
    df_target,
    test_size=0.25,
    random_state=21,
    stratify=df_target  # Ensures class distribution is preserved
)
```

This way, the training and test sets will each have approximately the same class proportions as the original dataset, leading to more stable and fair model evaluation.

Another limitation is that it does not evaluate the model’s performance across different combinations of training and test instances.
Because the split is done only once, the results may depend heavily on how the data was partitioned.

To address this, **random subsampling** (also known as repeated hold-out) can be used.
In this approach, the dataset is split multiple times using random partitions, and the model is evaluated on each split.
The final performance is then averaged across the runs, providing a more reliable estimate.
