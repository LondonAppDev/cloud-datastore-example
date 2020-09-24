"""
Demonstrate issue with race condition.
"""
import random

from google.cloud import ndb
from google.auth.credentials import AnonymousCredentials


client = ndb.Client(
    credentials=AnonymousCredentials(),
    project='local-dev',
)


class SampleModel(ndb.Model):
    """Sample model."""
    some_val = ndb.StringProperty()

for x in range(1, 1000):
    print(f'Attempt {x}')
    with client.context():
        random_text = str(random.randint(0, 9999999999))
        new_model = SampleModel(some_val=random_text)
        new_model.put()

        retrieved_model = SampleModel.query().filter(
            SampleModel.some_val == random_text
        ).get()
        print(f'Model Text: {retrieved_model.some_val}')
