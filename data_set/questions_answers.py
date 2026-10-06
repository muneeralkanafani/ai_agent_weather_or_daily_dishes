class QuestionsAnswers:
    """
    the dataset of the resturant
    we use it for the daily dishes agent
    """
    def __init__(self):
        self.questions = [
            "What are your opening hours?",
            "Do you take reservations?",
            "What type of cuisine do you serve?",
            "Do you have vegetarian options?",
            "Where are you located?",
            "Do you offer delivery?",
            "What is your phone number?",
            "Do you have gluten-free options?"
        ]
        self.answers = [
            "We're open Monday-Thursday 11am-10pm, Friday-Saturday 11am-11pm, Sunday 10am-9pm.",
            "Yes, we accept reservations. Call us at (555) 123-4567 or book online.",
            "We serve contemporary American cuisine with seasonal ingredients.",
            "Yes, we have several vegetarian and vegan options on our menu.",
            "We're located at 123 Main Street, Downtown.",
            "Yes, we partner with major delivery services including DoorDash and Uber Eats.",
            "You can reach us at (555) 123-4567.",
            "Yes, we offer gluten-free bread and pasta options."
        ]
