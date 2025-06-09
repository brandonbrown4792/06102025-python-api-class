# Getting Remote Data Lab

## The Scenario 
It is time to practice building out your own class for retrieving remote data. In this lab, you are tasked with building a generic GetRequester class. This class will be able to take in a URL on initialization and send an HTTP GET request on command. You will also need to build a method for dealing with requests that return JSON.

## Tools and Resources 
- [GitHub Repo](https://github.com/learn-co-curriculum/flask-getting-remote-data-lab)
- [GET - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [HTTP methods - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [requests](https://requests.readthedocs.io/en/latest/)
- [Python JSON](https://docs.python.org/3/library/json.html)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 

* Fork and Clone
  * For this lesson, you will need the following GitHub Repo:
  * Go to the provided GitHub repository link.
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Open and Run File
  * Open the project in VSCode.
  * Run pipenv install to install all necessary dependencies.
  * Run pipenv shell to open instance of python shell

### Task 1: Define the Problem

* Build a class to interact with api
* Get the data
* Convert to json data

### Task 2: Determine the Design

* Endpoint: https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json.
  * ```get_response_body```
    * Query endpoint
  * ```load_json```
    * Convert to json data

#### Task 3: Develop, Test, and Refine the Code

* Create feature branch
* Build get_response_body to query endpoint
* Convert endpoint data to json and return the data
* Push feature branch and open a PR on GitHub
* Merge to main

#### Task 4: Document and Maintain

Best Practice documentation steps:
* Add comments to code to explain purpose and logic, clarifying intent / functionality of code to other developers.
* Add screenshot of completed work included in Markdown in README.
* Update README text to reflect the functionality of the application following https://makeareadme.com.
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Submission

Once all tests are passing and working code is pushed to the GitHub main branch, submit your GitHub repo through Canvas using CodeGrade.

## Grading Criteria

The application passes all test suites.
* Get json data
* Convert to Json
