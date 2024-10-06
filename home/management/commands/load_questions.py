from django.core.management.base import BaseCommand
from home.models import Question, Answer, Types  # Ensure to import your models

class Command(BaseCommand):
    help = 'Load quiz questions into the database'

    def handle(self, *args, **kwargs):
        questions_data = [
            {
                "type": "High School",
                "question": "What is the 'transit method' in exoplanet discovery?",
                "answers": [
                    {"answer": "Sending a probe to a planet", "is_correct": False},
                    {"answer": "Looking for changes in a star’s brightness", "is_correct": True},
                    {"answer": "Measuring a planet’s temperature", "is_correct": False},
                    {"answer": "Listening to radio signals from space", "is_correct": False}
                ],
                "explanation": "The transit method involves observing the dip in a star's brightness when an exoplanet passes in front of it.",
                "fun_fact": "This method has helped scientists discover more than 2,000 exoplanets!"
            },
            {
                "type": "High School",
                "question": "What makes an exoplanet potentially habitable?",
                "answers": [
                    {"answer": "Its size", "is_correct": False},
                    {"answer": "Its distance from Earth", "is_correct": False},
                    {"answer": "Being in the 'Goldilocks Zone'", "is_correct": True},
                    {"answer": "Having moons", "is_correct": False}
                ],
                "explanation": "The 'Goldilocks Zone' is the area around a star where a planet might have liquid water, making it a potential place for life.",
                "fun_fact": "Earth is in the Goldilocks Zone of our Sun, which is why life can exist here!"
            },
            {
                "type": "High School",
                "question": "Which space telescope discovered the most exoplanets?",
                "answers": [
                    {"answer": "Hubble Space Telescope", "is_correct": False},
                    {"answer": "James Webb Space Telescope", "is_correct": False},
                    {"answer": "Kepler Space Telescope", "is_correct": True},
                    {"answer": "Spitzer Space Telescope", "is_correct": False}
                ],
                "explanation": "The Kepler Space Telescope discovered over 2,600 exoplanets before it retired in 2018.",
                "fun_fact": "Kepler’s discoveries have changed the way scientists think about planets and solar systems!"
            },
            {
                "type": "High School",
                "question": "What is a 'super-Earth'?",
                "answers": [
                    {"answer": "A planet made of gas", "is_correct": False},
                    {"answer": "A planet smaller than Earth", "is_correct": False},
                    {"answer": "A planet bigger than Earth but smaller than gas giants", "is_correct": True},
                    {"answer": "A planet made entirely of water", "is_correct": False}
                ],
                "explanation": "Super-Earths are rocky planets larger than Earth but smaller than gas giants like Jupiter.",
                "fun_fact": "Super-Earths may have the right conditions to support life!"
            },
            {
                "type": "High School",
                "question": "How does the 'radial velocity' method help discover exoplanets?",
                "answers": [
                    {"answer": "By measuring changes in a star’s position due to the pull of a planet", "is_correct": True},
                    {"answer": "By directly imaging planets", "is_correct": False},
                    {"answer": "By detecting radio signals from planets", "is_correct": False},
                    {"answer": "By measuring the planet’s temperature", "is_correct": False}
                ],
                "explanation": "The radial velocity method detects the slight wobble of a star caused by the gravitational pull of an orbiting planet.",
                "fun_fact": "This method helped discover the first-ever exoplanet in 1995!"
            },
            {
                "type": "High School",
                "question": "What is the closest exoplanet to Earth?",
                "answers": [
                    {"answer": "Proxima Centauri b", "is_correct": True},
                    {"answer": "Kepler-22b", "is_correct": False},
                    {"answer": "Jupiter", "is_correct": False},
                    {"answer": "Mars", "is_correct": False}
                ],
                "explanation": "Proxima Centauri b is just 4.2 light-years away from Earth, orbiting our nearest star neighbor, Proxima Centauri.",
                "fun_fact": "If we could travel at the speed of light, it would still take over 4 years to reach Proxima Centauri b!"
            },
            {
                "type": "High School",
                "question": "What type of exoplanet is most commonly found?",
                "answers": [
                    {"answer": "Ice giants", "is_correct": False},
                    {"answer": "Rocky planets", "is_correct": False},
                    {"answer": "Gas giants", "is_correct": True},
                    {"answer": "Water worlds", "is_correct": False}
                ],
                "explanation": "Gas giants like Jupiter and Saturn are the most commonly discovered exoplanets because their large size makes them easier to detect.",
                "fun_fact": "Some gas giants orbit very close to their stars and are called 'Hot Jupiters' because they are extremely hot!"
            },
        ]

        for q in questions_data:
            # Create the Types instance if it doesn't exist
            type_instance, created = Types.objects.get_or_create(
                gfg_name=q["type"])

            # Create the Question instance
            question_instance = Question.objects.create(
                gfg=type_instance,
                question=q["question"],
                marks=5  # You can customize the marks if needed
            )

            # Create the Answer instances
            for answer in q["answers"]:
                Answer.objects.create(
                    question=question_instance,
                    answer=answer["answer"],
                    is_correct=answer["is_correct"]
                )

            # Optionally, if you want to store explanations and fun facts, you can create separate models or fields for that
            # e.g. question_instance.explanation = q["explanation"]
            # e.g. question_instance.fun_fact = q["fun_fact"]

        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded questions into the database'))
