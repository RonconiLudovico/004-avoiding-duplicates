
import unittest

from main import arrizer
class Test_arrizer(unittest.TestCase):
    def test_arrizer(self):
        '''
        test that creates a list eliminating duplicates
        '''
        data = 'one two three four four five five'
        result = arrizer(data)
        self.assertEqual(['one', 'two', 'three', 'four', 'five'], result)


class Test_arrizer2(unittest.TestCase):
    def test_arrizer(self):
        '''
        test that creates a list eliminating duplicates
        '''
        data = '1 2 3 4 five 5 five six 7'
        result = arrizer(data)
        self.assertEqual(['1', '2', '3', '4', 'five', '5', 'six', '7'], result)


class Test_arrizer3(unittest.TestCase):
    def test_arrizer(self):
        '''
        test that creates a list eliminating duplicates
        '''
        data = 'one one two two three 4 4 five 5'
        result = arrizer(data)
        self.assertEqual(['one', 'two', 'three', '4', 'five', '5'], result)


class Test_arrizer4(unittest.TestCase):
    def test_arrizer(self):
        '''
        test that creates a list eliminating duplicates
        '''
        data = 'oashfaoi7q30 dlkfaounva dlkfaounva 29098y8b jjjkapog99 jjjkapog99 jjjkapog99 fhahsahf888 fhahsahf888'
        result = arrizer(data)
        self.assertEqual(['oashfaoi7q30', 'dlkfaounva', '29098y8b', 'jjjkapog99', 'fhahsahf888'], result)


class Test_arrizer5(unittest.TestCase):
    def test_arrizer(self):
        '''
        test that creates a list eliminating duplicates
        '''
        data = '00000000000000000 000000000001000000000 000000000001000000000 0000000000900000090 0000000010101009 0000000010101009 0000000010101009 000000002020203'
        result = arrizer(data)
        self.assertEqual(['00000000000000000', '000000000001000000000', '0000000000900000090', '0000000010101009', '000000002020203'], result)
