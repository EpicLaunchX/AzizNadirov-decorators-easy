from unittest import TestCase
from src.pytemplate.domain.models import Movie

class TestMovie(TestCase):
    def test_movie(self):
        movie = Movie(name="The Godfather", customer_age="18")
        self.assertEqual(movie.name, "The Godfather")
        self.assertEqual(movie.customer_age, "18")
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()