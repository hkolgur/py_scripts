"""Module providing a function printing grades from scores."""


class Score:
    """ "Initiate student scores"""

    def __init__(self, score: int) -> None:
        self.score = score

    def show_score(self) -> None:
        """Display scores"""
        print("Inside Show")
        print(f"Score is :{self.score}")


def execute():
    """Logic"""
    print("inside Execute")
    john = Score(85)
    john.show_score()


if __name__ == "__main__":
    execute()

# scores = [80, 91, 77]

# for score in scores:
#     if score > 90:
#         print("Distinction")
#     elif score > 80:
#         print("First Grade")
#     else:
#         print("others")

# print("Done")


