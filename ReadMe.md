## Description
This script calculates the Github Usage Scores for single or multiple users.

## Pre-requisites
- Python 3
- requests module

## Usage
You can execute this script via 
- Updating the input.txt and pushing the code back to the repository. This will trigger the Github Action that will trigger the code (Look at the 'Build' Job and 'Run Python Script' Step)
- Downloading the script and input.txt file and running it locally

## Input
Provide a comma-separated user values using the input.txt file to test the script. 
- E.g. advait, evan

## Output
The script output's each user's score on a single line. E.g.
- advait's github usage score is 0
- evan's github usage score is 24