from django.test import TestCase

# Create your tests here.


d = { "hello":"world"}

for value, key in enumerate(d):
    print(value, key)