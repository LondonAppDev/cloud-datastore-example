# Cloud Datastore Example

## Issue

When creating and retrieving entities, occasionally there is a delay on the entity being available.

## Steps to re-produce

 1. Run `docker-compose build`
 2. Run `docker-compose run app`

The script will run and fail with the following error:

```
Traceback (most recent call last):
  File "datastore.py", line 30, in <module>
    print(f'Model Text: {retrieved_model.some_val}')
AttributeError: 'NoneType' object has no attribute 'some_val'
```

It happens after a random number of attempts (occasionally the 1st).
