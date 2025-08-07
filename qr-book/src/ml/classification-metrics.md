# Classification Metrics

In classification models, the output is discrete (labels) and model is supposed to predict the label of a certain instance.
With that, given a classification model \\(f\\), the following metrics can be used to evaluate its performance:

- Accuracy
- Confusion Matrix
- Precision and Recall
- F1-score
- AU-ROC

## Error and Accuracy

The **error** \\(err(f) \in [0,1]\\) is defined as:

\\[err(f) = \frac{\text{Incorrect classifications}}{\text{Total classifications}}\\]

The **accuracy** is defined as the complement of the error \\(err(f)\\):

\\[acc(f) = 1 - err(f)\\]

or simply:

\\[acc(f) = \frac{\text{Correct classifications}}{\text{Total classifications}}\\]

Therefore, is desirable to have \\(acc(f)\\) close to \\(1\\) and \\(err(f)\\) close to \\(0\\).

### Implementation

Here is a simple binary classification (considering that the predictions were made by classification model):

```python
from sklearn.metrics import accuracy_score

y_test = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1] # Ground truth
y_pred = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1] # Model output

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2f}")
```

Output:

```bash
Accuracy: 0.80
```

### Confusion Matrix

A **confusion matrix** \\(M\\) is a visualization of the number of correct and incorrect predictions in each label \\(i \in L\\), in which \\(M_{i,j}\\) represents the number

**True positives** \\(TP = \sum_{i \in L}M_{i,i}\\) are the cases where the model predicted correctly, representing the main diagonal of \\(M\\).
