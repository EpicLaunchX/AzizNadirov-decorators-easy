from dataclasses import dataclass


@dataclass
class Movie:
    """movie class"""

    name: str
    customer_age: int


def movie_factory(name: str, customer_age: int) -> Movie:
    """movie factory"""
    return Movie(name=name, customer_age=customer_age)
