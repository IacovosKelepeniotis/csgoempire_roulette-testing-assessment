# CSGOEmpire Roulette Testing Assessment
QA Engineer assessment project for testing the roulette features on CSGOEmpire.
This repository contains my test plans, scripts, and reports for the QA Engineer assessment focused on testing the roulette feature at https://csgoempire.com/roulette. 

## Testing Approach

Brief overview of testing strategy, tools used, and how to run the test scripts.
The testing strategy encompasses a multi-faceted approach to thoroughly evaluate the roulette feature. Utilizing a blend of automated and manual testing methodologies, I aim to cover every aspect of the feature, from user interface interactions to backend logic validations.

Check the docs for full overview and testing approach/strategy
Check reports to view test cases designs and future plans

## Tools Used
Selenium WebDriver: For automating browser interactions and validating UI elements and user journeys.
Python: The programming language of choice for writing our test scripts, chosen for its readability and the powerful Selenium bindings it offers.

## Running the Test Scripts
Setup Environment: Ensure Python, Selenium,chrome webdriver and any other dependencies are installed on your system.
A requirements.txt file is provided to facilitate easy setup with the command pip install -r requirements.txt.
Navigate to Test Scripts: The test scripts are located in the scripts/ directory. Each script is named according to the specific part of the feature it tests.
Execute Tests: Run the tests using a Python interpreter. For Selenium tests, ensure you have the WebDriver for your browser installed and correctly pathed. Example: python scripts/test_roulette_wheel_presence.py.
