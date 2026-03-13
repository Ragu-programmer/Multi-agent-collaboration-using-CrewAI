from dotenv import load_dotenv
load_dotenv()

from Crew.product_dev_crew import product_dev_crew

if __name__ == "__main__":

    client_request = """
    Build a food delivery web application.

    Requirements:
    - restaurant browsing
    - search by city
    - cart management
    - order checkout
    """

    result = product_dev_crew.kickoff(
        inputs={
            "client_request": client_request
        }
    )

    print(result)