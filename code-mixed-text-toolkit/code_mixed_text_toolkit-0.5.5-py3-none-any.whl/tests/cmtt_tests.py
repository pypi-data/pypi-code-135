import unittest
import code_mixed_text_toolkit.data as cmtt_data
import code_mixed_text_toolkit.preprocessing as cmtt_pp

class CMTTTestCase(unittest.TestCase):
  def setUp(self):
    self.load_url = cmtt_data.load_url
    self.Word_T = cmtt_pp.tokenizer.WordTokenizer(); 
    # self.word_tokenize = cmtt_pp.tokenizer.word_tokenize

  def test_data_load_url_1(self):
    """Test data load_urling function 1"""
    result = self.load_url('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')
    self.assertEqual(result['code'], "5060292302201")

  def test_data_load_url_2(self):
    """Test data load_urling function 2"""
    result = self.load_url('https://gist.githubusercontent.com/rnirmal/e01acfdaf54a6f9b24e91ba4cae63518/raw/6b589a5c5a851711e20c5eb28f9d54742d1fe2dc/datasets.csv')
    self.assertEqual(result['about'][20], "Tate Collection metadata")
    self.assertEqual(len(result['about']), 61)

  def test_word_tokenize(self):
    """Test word tokenize function"""
    text = "This Python interpreter is in a conda environment, but the environment has not been activated.  Libraries may fail to load.  To activate this environment"
    result  = self.Word_T.tokenize(text)
    self.assertEqual(len(result), 27)
  
if __name__ == '__main__':
  unittest.main()