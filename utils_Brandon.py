'''

My First Python Project

'''

# Import the statistics module to calculate mean and standard deviation
import statistics

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
######################################

# Boolean variable to indicate if the company is privately held
is_privately_held: bool = True

# Integer variable for the number of employees
number_of_employees: int = 50

# List of strings representing the technologies used
technologies_used: list = ["Python", "Pandas", "NumPy", "SQL"]

# List of floats representing client satisfaction scores
client_satisfaction_scores: list = [88.5, 92.7, 85.0, 94.3]

# List of floats representing the recent scores
recent_scores: list = [92.22, 99.2, 95.3, 91.2]

#####################################
# Calculate statistics for client satisfaction scores
#####################################

min_client_score = min(client_satisfaction_scores)  # Smallest score
max_client_score = max(client_satisfaction_scores)  # Highest score
mean_client_score = statistics.mean(client_satisfaction_scores)  # Average score
stdev_client_score = statistics.stdev(client_satisfaction_scores)  # Standard deviation

#####################################
# Calculate statistics for recent scores
#####################################

min_recent_score = min(recent_scores)  # Smallest recent score
max_recent_score = max(recent_scores)  # Highest recent score
mean_recent_score = statistics.mean(recent_scores)  # Average recent score
stdev_recent_score = statistics.stdev(recent_scores)  # Standard deviation of recent scores

#####################################
# Update the byline to include additional information and statistics.
#####################################

# Multiline f-string for the byline that includes all relevant information and key statistics
byline: str = f"""

--------------------------
My First Python Project
--------------------------

Is Privately Held: {is_privately_held}
Number of Employees: {number_of_employees}
Technologies Used: {', '.join(technologies_used)}

Client Satisfaction Scores:
  - Min Client Score: {min_client_score}
  - Max Client Score: {max_client_score}
  - Mean Client Score: {mean_client_score:.2f}
  - Client Score Standard Deviation: {stdev_client_score:.2f}

Recent Performance Scores:
  - Min Recent Score: {min_recent_score}
  - Max Recent Score: {max_recent_score}
  - Mean Recent Score: {mean_recent_score:.2f}
  - Recent Score Standard Deviation: {stdev_recent_score:.2f}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
