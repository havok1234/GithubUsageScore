# This code checks the Github Usage stats and generates a usage score.
# Scoring criteria: {"PullRequestEvent": 5, "PushEvent": 4, "IssueCommentEvent": 3, "CreateEvent": 2, "Other": 1}
#TODO: Add Validation for correct user value
#TODO: Add Logging
#TODO: Add requirements.txt
#TODO: Add Testing framework

import requests
import sys

class GithubUsageScore:
    ## Variables
    eventScores = {"PullRequestEvent": 5, "PushEvent": 4, "IssueCommentEvent": 3, "CreateEvent": 2, "Other": 1} # Scores for different event types.
    baseUrl = "https://api.github.com/users/"
    scores = []

    def __init__(self):
        # Test calculate function
        self.testCalculateScore()
        
    # Read user(s) from input.txt
    def getUsers(self):
        try:
            f = open("./input.txt", "r")
            users = f.read().split(",")
        except OSError:
            print("Could not open/read file: input.txt")
            sys.exit()
        
        if not users:
            raise Exception("No Input provided")
        return users
        

    # Call github api to retrieve user event usage metadata
    def getEvents(self, user):
        try: 
            response = requests.get(f"{self.baseUrl}{user}/events")
            events = []
            try:
                data = response.json()
                for obj in data:
                    events.append(obj["type"])
            except requests.JSONDecodeError:
                self.scores.append(f"Unexpected error while fetching Event Data for {user}")
        except requests.RequestException as e:
            self.scores.append(f"Unexpected error while fetching Event Data for {user}")
            
        return events
            
    # Calculate github usage score for a user by fetching their events
    def calculateScore(self, user, events):
        score = 0
        #iterate over events to calculate score
        for event in events:
            if event in self.eventScores:
                score += self.eventScores[event]
            else:
                score += self.eventScores["Other"]
        self.scores.append(f"{user}'s github usage score is {score}")
    
    # Print github usage score(s) for a user(s)
    def printScores(self):
        for score in self.scores:
            print(score)
        
    # Check github usage score(s) for a user(s)
    def checkScore(self):
        # Get users
        users = self.getUsers()
            
        # Calculate Score for each user
        for user in users:
            user = user.strip()
            if user:
                events = self.getEvents(user)
                self.calculateScore(user, events)
        
        # Print Score(s)
        self.printScores()
    
    # Testcase to validate accuracy of Calculations
    def testCalculateScore(self):
        events = ['PushEvent', 'PushEvent', 'PushEvent', 'PushEvent', 'CreateEvent', 'CreateEvent']
        self.calculateScore("Test", events)
        assert self.scores[0] == "Test's github usage score is 20"
        self.scores = []
    
def main():
    g = GithubUsageScore()
    g.checkScore()
    
if __name__ == '__main__':
    main()