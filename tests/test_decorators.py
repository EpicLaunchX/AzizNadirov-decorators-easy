from unittest import TestCase

from src.pytemplate.domain.models import Movie, movie_factory


class TestMovie(TestCase):
    def test_movie(self):
        movie = Movie(name="The Godfather", customer_age="18")
        self.assertEqual(movie.name, "The Godfather")
        self.assertEqual(movie.customer_age, "18")

    def test_movie_factory(self):
        movie = movie_factory(name="The Godfather", customer_age="18")
        self.assertIsInstance(movie, Movie)
        self.assertEqual(movie.name, "The Godfather")
        self.assertEqual(movie.customer_age, "18")


if __name__ == "__main__":
    import unittest

    unittest.main()
