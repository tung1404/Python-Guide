# **[Modern Test-Driven Development in Python](https://testdriven.io/blog/modern-tdd/)**

This guide will take you through the development of an application using Test-Driven-Development (TDD). We'll look how and what you should test. We'll use pytest for testing, pydantic to validate data and reduce the number of tests required, and Flask to provide an interface for our clients via a RESTful API. By the end, you will have a solid pattern that you can use for any Python project so that you can have confidence that passing tests actually mean working software.

# Objectives

By the end of this article, you should be able to:

1. Explain how you should test your software
2. Configure pytest amd set up project structure for testing
3. Define database models with pydantic
4. Use pytest fixtures for managing test state and performing side effects
5. Verify JSON responses against JSON Schema definitions
6. Organize database operations with commands (modify state, have side effects) and queries (read-only, no side effects)
7. Write unit, integrations, and end-to-end tests with pytest
8. Explain why it's important to focus your testing efforts on testing behavior rather than implementation details

# How Should I Test My Software?

Let's look at three guidelines that most agree with that will help you write _valuable_ tests:

1. Tests should tell you the expected behavior of the unit under test. Therefore, it's advisable to keep them short and to the point. The [GIVEN, WHEN, THEN](https://martinfowler.com/bliki/GivenWhenThen.html) structure can help with this:

- GIVEN - what are the initial conditions for the test?
- WHEN - what is occurring that needs to be tested?
- THEN - what is the expected response?

2. Each piece of behavior should be tested once -- and only once.

3. Each test must be independent from other tests.

~ flask-tdd
