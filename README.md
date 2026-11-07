#  Sprint Project — Urban Grocers and Introduction to Automated Testing.

## Project Description

The goal of this project is to develop and run automated tests to validate the functionality of the Urban Grocers API, specifically the process of creating product kits and the validation rules for the `name` field.

The automation is based on a checklist that includes nine test scenarios, designed to verify the system’s behavior in response to valid and invalid inputs. The evaluation covers name length limits, empty fields, special characters, spaces, numeric values represented as text, the absence of a required parameter, and the submission of incorrect data types.

## Objectives

- Automate the nine test cases defined in the project requirements.
- Validate HTTP response codes and the correspondence between sent and received data.
- Verify the acceptance limits for the `name` field.
- Implement reusable functions for sending HTTP requests and managing authentication.
- Organize the code into independent modules to facilitate maintenance, readability, and reuse.
- Use Pytest to run the tests and analyze the results.
- Manage the source code using Git and GitHub, following an organized and documented workflow.


## Main Files
````
configuraCion.py:
Contains the service URL and the
configuration parameters required for API requests.
````

````
create_kit_name_test.py:
Contains the automated test cases used to
validate the kit name creation requirements
and the expected responses.
````

````
data.py:
Stores the request payloads, test data, and
expected values used during test execution.
````

````
sender_stand_request.py:
Contains the methods responsible for sending
API requests to the application’s endpoints.
````


## Technologies and Tools

- **Python:** language used to develop automated tests.
- **Pytest:** framework for organizing and running test cases.
- **Requests:** library for sending HTTP requests to the API.
- **Git:** version control system.
- **GitHub:** a platform for hosting and deploying the repository.
- **Urban Grocers API:** the service being tested.



## Project Structure

- `configuration.py`: centralizes the server URL and endpoint routes.
- `data.py`: contains test data and request bodies.
- `sender_stand_request.py`: implements functions to create users, obtain the authentication token, and send kit creation requests.
- `create_kit_name_kit_test.py`: contains the nine automated test cases for the `name` field.
- `README.md`: documents the project’s purpose, its requirements, and the steps to run the tests.
- `.gitignore`: excludes temporary files, caches, and other items that should not be included in version control.



## Validation Criteria

Positive tests verify that the API responds with HTTP status code `201` and that the returned name matches the one sent in the request. Negative tests verify that invalid inputs result in HTTP status code `400`, in accordance with the established requirements.

## Execution

Once the current Urban Grocers server URL has been configured and the necessary dependencies have been installed, the tests are run using:

`pytest -v create_kit_name_kit_test.py`

The results allow you to identify compliant behavior and potential discrepancies between the API response and the expected results.

## Expected Result

To have an organized, reusable, and documented automated test suite that evaluates the validation rules for the `name` field during the creation of product kits, facilitating error detection and contributing to the quality and reliability of the service.

Prepared by:
Camilo Andrés Tiuzo 
Quality Assurance Engineer
