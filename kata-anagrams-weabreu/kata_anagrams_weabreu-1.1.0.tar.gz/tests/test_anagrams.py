import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from unittest import TestCase, main
from time import time
from src.kata_anagrams_weabreu.anagrams import search_anagrams, search_anagrams_advanced, AnagramsAnalyzer

input_data = [
    "crepitus", "piecrust", "spate", "tapes", "tepas", "punctilio", 
    "unpolitic", "paste", "pates", "peats", "septa", "sunders", "undress", 
    "cuprites", "pictures", "sort", "a"
]
input_data_all_anagrams = [
    "kinship", "pinkish", "enlist", "inlets", "listen", "silent", 
    "boaster", "boaters", "borates", "fresher", "refresh", "sinks", 
    "skins", "knits", "stink", "rots", "sort"
]

expected_data = [
    "crepitus piecrust cuprites pictures",
    "spate tapes tepas paste pates peats septa",
    "punctilio unpolitic", "sunders undress"
]
expected_data_all_anagrams = [
    "kinship pinkish", "enlist inlets listen silent", 
    "boaster boaters borates", "fresher refresh", 
    "sinks skins", "knits stink", "rots sort"
]

class TestSearchAnagrams(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_should_return_expected_data(self):
        result = search_anagrams( input_data )
        self.assertEqual(result, (expected_data, 15))

    def test_should_return_empty_list_and_0_if_receive_empty_list(self):
        result = search_anagrams([])
        self.assertEqual(result, ([], 0))

    def test_should_return_expected_data_all_anagrams_if_receive_a_list_of_anagrams(self):
        result = search_anagrams( input_data_all_anagrams )
        self.assertEqual(result, (expected_data_all_anagrams, 17))

    def test_should_return_empty_list_and_0_if_receive_list_without_anagrams(self):
        result = search_anagrams(["sort", "a"])
        self.assertEqual(result, ([], 0))

    def test_should_be_executed_in_less_than_1_8_seconds(self):
        start_time = time()
        search_anagrams( input_data )
        end_time = time()

        self.assertTrue( (end_time - start_time) < 1.8 )

    def test_should_return_type_exception_if_receive_None(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams(None)

    def test_should_return_type_exception_if_receive_string(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams("")

    def test_should_return_type_exception_if_receive_number(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams(0)

    def test_should_return_type_exception_if_receive_number_list(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams([0])
    
    def test_should_return_type_exception_if_receive_dict(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams({ "a": "b" })

class TestSearchAnagramsAdvanced(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_should_return_expected_data(self):
        result = search_anagrams_advanced( input_data )
        self.assertEqual(result, 
            (
                expected_data, 15, 
                "punctilio unpolitic", 
                "spate tapes tepas paste pates peats septa"
            )
        )
    
    def test_should_return_empty_values_if_receive_empty_list(self):
        result = search_anagrams_advanced([])
        self.assertEqual(result, ([], 0, "", ""))

    def test_should_return_empty_values_if_receive_list_without_anagrams(self):
        result = search_anagrams_advanced(["sort", "a"])
        self.assertEqual(result, ([], 0, "", ""))

    def test_should_return_empty_values_if_receive_list_with_a(self):
        result = search_anagrams_advanced(["a"])
        self.assertEqual(result, ([], 0, "", ""))

    def test_should_return_expected_data_all_anagrams_if_receive_a_list_of_anagrams(self):
        result = search_anagrams_advanced( input_data_all_anagrams )
        self.assertEqual(result,
            (
                expected_data_all_anagrams, 17,
                "kinship pinkish",
                "enlist inlets listen silent"
            )
        )

    def test_should_be_executed_in_less_than_1_8_seconds(self):
        start_time = time()
        search_anagrams_advanced( input_data )
        end_time = time()

        self.assertTrue( (end_time - start_time) < 1.8 )

    def test_should_return_type_exception_if_receive_None(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams_advanced(None)

    def test_should_return_type_exception_if_receive_string(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams_advanced("")
    
    def test_should_return_type_exception_if_receive_number(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams_advanced(0)

    def test_should_return_type_exception_if_receive_number_list(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams_advanced([0])

    def test_should_return_type_exception_if_receive_dict(self):
        with self.assertRaises(TypeError) as context:
            search_anagrams({ "a": "b" })

class TestAnagramsAnalyzer(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_load_word_does_not_throw_error(self):
        analyzer = AnagramsAnalyzer()
        analyzer.load_word( input_data[0] )

    def test_load_word_throw_type_error_if_receive_int(self):
        analyzer = AnagramsAnalyzer()
        with self.assertRaises(TypeError) as context:
            analyzer.load_word( 1 )

    def test_get_anagrams_return_empty_list_if_does_not_load_word(self):
        analyzer = AnagramsAnalyzer()
        self.assertEqual( analyzer.get_anagrams(), [] )

    def test_get_anagrams_return_expected_data_if_load_every_word_on_input_data(self):
        analyzer = AnagramsAnalyzer()
        
        for word in input_data:
            analyzer.load_word( word )
        
        self.assertEqual( analyzer.get_anagrams(), expected_data )
    
    def test_get_anagrams_words_count_return_0_if_does_not_load_word(self):
        analyzer = AnagramsAnalyzer()
        self.assertEqual( analyzer.get_anagrams_words_count(), 0 )

    def test_get_anagrams_words_count_return_15_if_load_every_word_on_input_data(self):
        analyzer = AnagramsAnalyzer()

        for word in input_data:
            analyzer.load_word( word )

        self.assertEqual( analyzer.get_anagrams_words_count(), 15 )

    def test_get_longest_word_set_should_return_empty_if_does_not_load_word(self):
        analyzer = AnagramsAnalyzer()
        self.assertEqual( analyzer.get_longest_word_set(), "" )

    def test_get_longest_word_set_should_return_longest_word_if_load_every_word_on_input_data(self):
        analyzer = AnagramsAnalyzer()

        for word in input_data:
            analyzer.load_word( word )

        self.assertEqual( analyzer.get_longest_word_set(), "punctilio unpolitic" )

    def test_get_most_words_set_should_return_empty_if_does_not_load_word(self):
        analyzer = AnagramsAnalyzer()
        self.assertEqual( analyzer.get_most_words_set(), "" )

    def test_get_most_words_set_should_return_most_words_set_if_load_every_word_on_input_data(self):
        analyzer = AnagramsAnalyzer()

        for word in input_data:
            analyzer.load_word( word )

        self.assertEqual( analyzer.get_most_words_set(), "spate tapes tepas paste pates peats septa" )

    def test_get_set_count_should_return_0_if_does_not_load_word(self):
        analyzer = AnagramsAnalyzer()
        self.assertEqual( analyzer.get_set_count(), 0 )

    def test_get_set_count_should_return_4_if_load_every_word_on_input_data(self):
        analyzer = AnagramsAnalyzer()

        for word in input_data:
            analyzer.load_word( word )

        self.assertEqual( analyzer.get_set_count(), 4 )

    def test_get_set_count_should_return_0_if_not_anagrams_words_loaded(self):
        analyzer = AnagramsAnalyzer()

        analyzer.load_word("sort")
        analyzer.load_word("word")

        self.assertEqual( analyzer.get_set_count(), 0 )

if __name__ == "__main__":
    main()