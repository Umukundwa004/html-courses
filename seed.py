class Assignment:
    """
    Represents a single assignment in a course.

    Attributes:
        name (str): The name or identifier of the assignment (e.g., "Assignment 1", "Midterm").
        type (str): The category of the assignment, either "Formative" (FA) or "Summative" (SA).
        score (float): The student's score for this assignment, expressed as a percentage (out of 100).
        weight (float): The weight this assignment contributes to its respective group total (formative or summative).
    """

    def __init__(self, name, type, score, weight):
        """
        Initializes an Assignment object with the given attributes.

        Args:
            name (str): The name of the assignment.
            type (str): The category of the assignment ("Formative" or "Summative").
            score (float): The student's score as a percentage (0-100).
            weight (float): The weight of the assignment (percentage contribution).
        """
        self.name = name
        self.type = type
        self.score = score
        self.weight = weight

    def calculate_weighted_score(self):
        """
        Calculates the weighted score of the assignment based on its score and weight.

        Returns:
            float: The weighted score of the assignment (percentage).
        """
        return (self.score / 100) * self.weight


class Student:
    """
    Represents a student and their performance in a course.

    Attributes:
        assignments (list[Assignment]): A list of Assignment objects representing the student's assignments.
        formative_total (float): The total weighted score for all formative assignments.
        summative_total (float): The total weighted score for all summative assignments.
    """

    def __init__(self, assignments):
        """
        Initializes a Student object with the given list of assignments.

        Args:
            assignments (list[Assignment]): A list of Assignment objects.
        """
        self.assignments = assignments
        self.formative_total = 0
        self.summative_total = 0

    def calculate_scores(self):
        """
        Calculates the total weighted scores for formative and summative assignments.
        Also identifies formative assignments eligible for resubmission (score below 50%).

        Iterates through each assignment, calculates its weighted score, and accumulates
        the scores based on the assignment type. Prints messages for resubmission eligibility.
        """
        for assignment in self.assignments:
            weighted_score = assignment.calculate_weighted_score()
            if assignment.type == "Formative":
                self.formative_total += weighted_score
            else:
                self.summative_total += weighted_score

            if assignment.type == "Formative" and assignment.score < 50:
                print(f"Assignment '{assignment.name}' is eligible for resubmission.")

    def check_progression(self):
        """
        Evaluates the student's performance based on formative and summative score thresholds.

        Checks if the student's formative total score is >= 30% and summative total score is >= 20%.
        Prints congratulatory or failure messages depending on the outcome.
        """
        passed_formative = self.formative_total >= 30
        passed_summative = self.summative_total >= 20

        if passed_formative and passed_summative:
            print("Congratulations! You have passed the course and progressed to the next level.")
        else:
            print("Unfortunately, you have not met the minimum requirements.")
            if not passed_formative:
                print(f"Your formative score is below 30%.")
            if not passed_summative:
                print(f"Your summative score is below 20%.")

    def generate_transcript(self):
        """
        Generates a formatted transcript displaying individual assignment details and totals.

        Prints a header row with assignment information, followed by details for each assignment.
        Ten, presents the overall formative and summative totals with proper formatting.
        """
        print("scores in linux and IT tools")
        print("Assignment\tType\tScore(%)\tWeight(%)")
        print("-" * 40)
        for assignment in self.assignments:
            print(f"{assignment.name}\t{assignment.type}\t{assignment.score:.2f}\t{assignment.weight:.2f}")

        # Print the formative and summative totals with formatted scores (two decimal places)
        print("\nFormative Total: {:.2f}%" .format(self.formative_total))
        print("Summative Total: {:.2f}%"   .format(self.summative_total))


""""" Sample assignments (replace with actual data collection)
  This list defines a set of sample assignments for demonstration purposes.
  
  In a real-world application, you would typically replace this with a dynamic way to
  collect assignment data, such as reading from a file, database, or user input."""

    # Sample assignments (replace with actual data collection)
assignments = [
        Assignment("Assignment 1", "Formative", 90, 15),
        Assignment("Assignment 2", "Formative", 65, 10),
        Assignment("Assignment 3", "Formative", 100, 10),
        Assignment("Assignment 4", "Formative", 100, 15),
        Assignment("Midterm", "Summative", 77.5, 20),
        Assignment("Final Exam", "Summative", 97.5, 20), ]

# Validate total formative and summative weights

total_formative_weight = sum(assignment.weight for assignment in assignments if assignment.type == "Formative")
total_summative_weight = sum(assignment.weight for assignment in assignments if assignment.type == "Summative")
 # Check if total formative and summative weights exceed the allowed limits
if total_formative_weight > 60 or total_summative_weight > 40:
 print("Error: Formative or summative weights exceed the allowed limit.")
else:
 # Exit the program if the weights are invalid

 # Create a Student object with the given assignments
 student = Student(assignments)

 # Calculate the weighted scores for each assignment and update the total scores
 student.calculate_scores()

 # Check the student's progress based on the calculated formative and summative scores
 student.check_progression()
 #order to be used
 order = input("\nWould you like to see your transcript in ascending or descending order? (ascending/descending): ")
 # Generate a detailed transcript of the student's performance, including assignment details, scores, and weights
 student.generate_transcript()

