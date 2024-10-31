import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        self.assertEqual(hw2.create_rectangle(data.Point(2, 2), data.Point(10, 10)),
                         data.Rectangle(data.Point(2, 10), data.Point(10, 2)))
        self.assertEqual(hw2.create_rectangle(data.Point(5, 5), data.Point(5, 5)),
                         data.Rectangle(data.Point(5, 5), data.Point(5, 5)))

    def test_create_rectangle_2(self):
        self.assertEqual(hw2.create_rectangle(data.Point(-3, 1), data.Point(2, -4)),
                         data.Rectangle(data.Point(-3, 1), data.Point(2, -4)))
        self.assertEqual(hw2.create_rectangle(data.Point(10, 5), data.Point(5, 10)),
                         data.Rectangle(data.Point(5, 10), data.Point(10, 5)))

    # Part 2
    def test_shorter_duration_than_1(self):
        self.assertTrue(hw2.shorter_duration_than(data.Duration(3, 20),
                                                  data.Duration(4, 0)))
        self.assertFalse(hw2.shorter_duration_than(data.Duration(5, 0),
                                                   data.Duration(5, 0)))

    def test_shorter_duration_than_2(self):
        self.assertTrue(hw2.shorter_duration_than(data.Duration(2, 30),
                                                  data.Duration(3, 30)))
        self.assertFalse(hw2.shorter_duration_than(data.Duration(7, 15),
                                                   data.Duration(6, 59)))

    # Part 3
    def test_songs_shorter_than_1(self):
        song1 = data.Song("Song1", "Artist1", data.Duration(3, 30))
        song2 = data.Song("Song2", "Artist2", data.Duration(2, 45))
        self.assertEqual(hw2.songs_shorter_than([song1, song2],
                                                data.Duration(3, 0)), [song2])

    def test_songs_shorter_than_2(self):
        song1 = data.Song("Song1", "Artist1", data.Duration(2, 30))
        song2 = data.Song("Song2", "Artist2", data.Duration(4, 10))
        song3 = data.Song("Song3", "Artist3", data.Duration(5, 5))
        self.assertEqual(hw2.songs_shorter_than([song1, song2, song3],
                                                data.Duration(4, 0)), [song1])

    # Part 4
    def test_running_time_1(self):
        song1 = data.Song("Song1", "Artist1", data.Duration(3, 30))
        song2 = data.Song("Song2", "Artist2", data.Duration(2, 45))
        song3 = data.Song("Song3", "Artist3", data.Duration(4, 20))
        self.assertEqual(hw2.running_time([song1, song2, song3],
                                          [0, 2, 1]), data.Duration(10, 35))

    def test_running_time_2(self):
        song1 = data.Song("Song1", "Artist1", data.Duration(1, 45))
        song2 = data.Song("Song2", "Artist2", data.Duration(2, 30))
        song3 = data.Song("Song3", "Artist3", data.Duration(3, 20))
        self.assertEqual(hw2.running_time([song1, song2, song3],
                                          [0, 1, 1, 2]), data.Duration(10, 5))

    # Part 5
    def test_validate_route_1(self):
        city_links = [['city1', 'city2'], ['city2', 'city3'], ['city3', 'city4']]
        self.assertTrue(hw2.validate_route(city_links, ['city1', 'city2', 'city3', 'city4']))
        self.assertFalse(hw2.validate_route(city_links, ['city1', 'city3', 'city4']))

    def test_validate_route_2(self):
        city_links = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']]
        self.assertTrue(hw2.validate_route(city_links, ['a', 'b', 'c', 'd', 'e']))
        self.assertFalse(hw2.validate_route(city_links, ['a', 'e', 'd']))

    # Part 6
    def test_longest_repetition_1(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 2, 3, 3]), 2)
        self.assertIsNone(hw2.longest_repetition([]))

    def test_longest_repetition_2(self):
        self.assertEqual(hw2.longest_repetition([4, 4, 4, 5, 5, 5, 5, 3, 3, 3]), 3)
        self.assertEqual(hw2.longest_repetition([7, 7, 7, 8, 9, 9, 9, 9, 6]), 4)

if __name__ == '__main__':
    unittest.main()
