#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datasets import load_dataset

dataset = load_dataset("aclImdb_v1/aclImdb")

train_data = dataset["train"]
test_data = dataset["test"]

print(train_data)
print(test_data)

# In[7]:


from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")
train_data = dataset["train"]
test_data = dataset["test"]

print(dataset)
print(dataset["train"].column_names)
print(dataset["test"].column_names)

print(dataset["train"][0])

# In[8]:


import pandas as pd

train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

print(train_df.head())
print(test_df.head())

print(train_df["label"].value_counts())
print(test_df["label"].value_counts())

# In[9]:


X_train = train_df["text"].astype(str)
y_train = train_df["label"].astype(int)

X_test = test_df["text"].astype(str)
y_test = test_df["label"].astype(int)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# In[10]:


from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    (
        "vectorizer",
        TfidfVectorizer(
            sublinear_tf=True,
            lowercase=True,
            strip_accents="unicode",
            ngram_range=(1, 2),
            max_features=100000
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            C=2.0
        )
    )
])

# In[11]:


print("Training model...")

pipeline.fit(X_train, y_train)

print("Training complete!")

# In[12]:


from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

train_predictions = pipeline.predict(X_train)
test_predictions = pipeline.predict(X_test)

train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print(f"Training accuracy: {train_accuracy:.4f}")
print(f"Testing accuracy:  {test_accuracy:.4f}")

print("\nClassification report:")
print(classification_report(
    y_test,
    test_predictions,
    target_names=["Negative", "Positive"]
))

print("\nConfusion matrix:")
print(confusion_matrix(y_test, test_predictions))

# In[13]:


reviews = [
    "This movie was absolutely fantastic. I loved every minute of it.",
    "This was one of the worst movies I have ever watched.",
    "The acting was great and the story was very entertaining.",
    "Terrible movie. The plot was boring and the acting was awful."
]

predictions = pipeline.predict(reviews)

for review, prediction in zip(reviews, predictions):
    sentiment = "Positive (1)" if prediction == 1 else "Negative (0)"
    print(f"{sentiment}: {review}")

# In[14]:


probabilities = pipeline.predict_proba(reviews)

for review, prediction, probability in zip(
    reviews,
    predictions,
    probabilities
):
    print("\nReview:", review)
    print("Prediction:", prediction)
    print("Negative probability:", probability[0])
    print("Positive probability:", probability[1])

# In[15]:


import joblib

MODEL_FILE = "skills_assessment.joblib"

joblib.dump(pipeline, MODEL_FILE)

print(f"Model saved as: {MODEL_FILE}")

# In[16]:


loaded_model = joblib.load("skills_assessment.joblib")

test_reviews = [
    "I absolutely loved this movie!",
    "This movie was terrible and boring."
]

predictions = loaded_model.predict(test_reviews)

for review, prediction in zip(test_reviews, predictions):
    print(
        f"{prediction} -> {review}"
    )

# In[ ]:



