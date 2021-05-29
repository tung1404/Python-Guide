
# **[Testing in Python](https://testdriven.io/blog/testing-python/)**
Automated testing has always been a hot topic in software development, but in the era of continuous integration and microservices, it's talked about even more.

# pytest

When compared to unittest, from the Python standard library, pytest:

1. Requires less boilerplate code so your test suites will be more readable.
2. Supports the plain `assert` statement, which is far more readable and easier to remember compared to the `assertSomething` methods -- like `assertEquals`, `assertTrue`, and `assertContains` -- in unittest.
3. Is updated more frequently since it's not part of the Python standard library.
4. Simplifies setting up and tearing down test state with its fixture system.
5. Uses a functional approach.

# Mocking

Automated tests should be fast, isolated/independent, and deterministic/repeatable.

Mocking is the practice of replacing real objects with mocked objects, which mimic their behavior, at runtime. So, instead of a sending a real HTTP request over the network, we just return an expected response when the mocked method is called.

For example:

```python
import requests


def get_my_ip():
    response = requests.get(
        'http://ipinfo.io/json'
    )
    return response.json()['ip']


def test_get_my_ip(monkeypatch):
    my_ip = '123.123.123.123'

    class MockResponse:

        def __init__(self, json_body):
            self.json_body = json_body

        def json(self):
            return self.json_body

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse({'ip': my_ip})
    )

    assert get_my_ip() == my_ip
```

Although pytest recommends the monkeypatch approach for mocking, the pytest-mock extension and the vanilla unittest.mock library from the standard library are fine approaches as well.

# Code Coverage

Another important aspect of tests is code coverage. It's a metric which tells you the ratio between the number of lines executed during test runs and the total number of all lines in your code base. We can use the [pytest-cov](https://pypi.org/project/pytest-cov/) plugin for this, which integrates [Coverage.py](https://coverage.readthedocs.io/) with pytest.

Once installed, to run tests with coverage reporting, add the --cov option like so:

```bash
python -m pytest --cov=.
```

# Mutation Testing

Mutation Testing helps ensure that your tests actually cover the full behavior of your code. Put another way, it analyzes the effectiveness or robustness of your test suite. During mutation testing, a tool iterates through each line of your source code, making small changes (called mutations) that should break your code. After each mutation, the tool runs your unit tests and checks whether your tests fail or not. If your tests still pass, then your code didn't survive the mutation test.

For example, say you have the following code:

```python
if x > y:
    z = 50
else:
    z = 100
```
The mutation tool may change the operator from `>` to `>=` like so:

```python
if x >= y:
    z = 50
else:
    z = 100
```

# Hypothesis

Hypothesis is a library for conducting property-based testing in Python. Rather than having to write different test cases for every argument you want to test, property-based testing generates a wide-range of random test data that's dependent on previous tests runs. This helps increase the robustness of your test suite while decreasing test redundancy. In short, your test code will be cleaner, more DRY, and overall more efficient while still covering a wide range of test data.

For example, say you have to write tests for the following function:

```python
# increment.py
def increment(num: int) -> int:
    return num + 1
```

```python
# test_hypotesis.py
from hypothesis import given
import hypothesis.strategies as st

from .increment import increment


@given(st.integers())
def test_increment(number):
    assert increment(number) == number + 1
```

```bash
pytest Hypothesis/test_hypotesis.py --hypothesis-show-statistics
...
Hypothesis/test_hypotesis.py::test_increment:

  - during reuse phase (0.01 seconds):
    - Typical runtimes: ~ 1ms, ~ 35% in data generation
    - 1 passing examples, 0 failing examples, 0 invalid examples

  - during generate phase (0.18 seconds):
    - Typical runtimes: 0-1 ms, ~ 46% in data generation
    - 99 passing examples, 0 failing examples, 0 invalid examples

  - Stopped because settings.max_examples=100
```

# Type Checking

Runtime (or dynamic) type checkers, like Typeguard and pydantic, can help to minimize the number of tests. Let's take a look at an example of this with pydantic.

# Conclusion

 Your tests should also be fast, isolated/independent, and deterministic/repeatable. In the end, having confidence in your test suite will help you deploy to production more often and, more importantly, help you sleep at night.