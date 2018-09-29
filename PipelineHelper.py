from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import Imputer, StandardScaler, LabelEncoder, LabelBinarizer


class CustomLabelBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self, unseen):
        self.le = LabelEncoder()
        self.lb = LabelBinarizer()
        self.imputer = Imputer(strategy='most_frequent')
        self.seen_labels = set()
        self.unseen = unseen

    def fit(self, x, y=None, **fit_params):
        self.seen_labels = set(x)
        self.seen_labels.add(self.unseen)

        # add 'unseen' to X
        x_new = list(x)
        x_new.append(self.unseen)
        label_encoded = self.le.fit_transform(x_new)
        label_encoded_imputed = self.imputer.fit_transform(label_encoded.reshape(1, -1))
        self.lb.fit(label_encoded)
        return self

    def transform(self, x):
        x_new = map(lambda label: label if label in self.seen_labels else self.unseen, list(x))
        label_encoded = self.le.transform(list(x_new))
        return self.lb.transform(label_encoded)


class ItemSelector(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, df):
        return df[self.key]


class MultiItemSelector(BaseEstimator, TransformerMixin):
    def __init__(self, key_list):
        self.key_list = key_list

    def fit(self, x, y=None):
        return self

    def transform(self, df):
        return df[self.key_list]
