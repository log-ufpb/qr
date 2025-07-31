# Duplicate Data

Duplicate data refers to rows that are repeated partially or fully in a dataset. These duplicates can lead to biased analyses, incorrect statistics, and misleading results.

---

## What Is It?

Duplicates are records in your dataset that are identical (complete duplicates) or share key identifying information (incomplete duplicates).

* **Complete duplicate:** Every column in a row matches exactly with another row.
* **Incomplete duplicate:** Only some columns match (e.g., name and address), while others may differ (e.g., height, timestamp).


## Why Do They Happen?

Common causes of duplicate data:

* **Human error:** Manual data entry mistakes or form re-submissions.
* **Merges/joins:** Joining datasets without specifying appropriate keys can create repeated rows.
* **Bugs in data pipelines:** Errors in scripts, APIs, or scraping logic.
* **Design flaws:** Systems that don't enforce unique constraints or primary keys.


## How to Find Duplicate Values?

### 1. Complete Duplicates

Find rows that are **exact copies**:

```python
duplicates = df.duplicated()
print(df[duplicates])
```

This flags rows that match all column values of a previous row. To include the first occurrence:

```python
df[df.duplicated(keep=False)]
```

### Example Output:

| first\_name | last\_name | address     | height | weight |
| ----------- | ---------- | ----------- | ------ | ------ |
| Alice       | Smith      | 123 Main St | 165    | 60     |
| Alice       | Smith      | 123 Main St | 165    | 60     |


### 2. Incomplete Duplicates

Find duplicates based on **subset of columns**:

```python
column_names = ["first_name", "last_name", "address"]
duplicates = df.duplicated(subset=column_names, keep=False)
print(df[duplicates])
```

### Example Output:

| first\_name | last\_name | address     | height | weight |
| ----------- | ---------- | ----------- | ------ | ------ |
| John        | Doe        | 456 Elm Ave | 180    | 80     |
| John        | Doe        | 456 Elm Ave | 179    | 82     |


## How to Treat Duplicate Values?

### 1. Removing Complete Duplicates

```python
df.drop_duplicates(inplace=True)
```

This keeps only the **first occurrence** of each duplicate row.

You can customize:

* `keep='last'`: keeps the **last** occurrence.
* `keep=False`: drops **all** duplicates.


### 2. Resolving Incomplete Duplicates with Aggregation

If some attributes differ, you may want to merge them using summary statistics:

```python
column_names = ["first_name", "last_name", "address"]
summaries = {"height": "max", "weight": "mean"}
df_cleaned = df.groupby(by=column_names).agg(summaries).reset_index()
```

### Example Transformation:

**Original:**

| first\_name | last\_name | address     | height | weight |
| ----------- | ---------- | ----------- | ------ | ------ |
| John        | Doe        | 456 Elm Ave | 180    | 80     |
| John        | Doe        | 456 Elm Ave | 179    | 82     |

**After aggregation:**

| first\_name | last\_name | address     | height | weight |
| ----------- | ---------- | ----------- | ------ | ------ |
| John        | Doe        | 456 Elm Ave | 180    | 81.0   |

---

## Best Practices

* Always inspect duplicates **before** removing them.
* Understand **why** duplicates occur — fixing the root cause is better than patching.
* Consider if duplicates contain **additional information** worth preserving (e.g., timestamps, different measurements).

## Bonus: Count of Duplicates

To check how often each duplicate appears:

```python
df[column_names].value_counts()
```
