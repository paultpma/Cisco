import sys
sys.path.insert(0, './script/')

import fileParser
import io
import unittest

from unittest.mock import patch

class TestFileParser(unittest.TestCase):
    def test_getFileNameList(self):
        testJson = """{"nm":"a.txt","ts":1551140352,"pt":55,"si":"3380fb19-0bdb-46ab-8781-e4c5cd448074","uu":"0dd24034-36d6-4b1e-a6c1-a52cc984f105","bg":"77e28e28-745a-474b-a496-3c0e086eaec0","sha":"abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52","ph":"/efvrfutgp/expgh/phkkrw","dp":2}
                      {"nm":"b.pdf","ts":1551140352,"pt":55,"si":"3380fb19-0bdb-46ab-8781-e4c5cd448074","uu":"0dd24034-36d6-4b1e-a6c1-a52cc984f105","bg":"77e28e28-745a-474b-a496-3c0e086eaec0","sha":"abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52","ph":"/efvrfutgp/expgh/phkkrw","dp":2}
                      {"nm":"b.pdf","ts":1551140352,"pt":55,"si":"3380fb19-0bdb-46ab-8781-e4c5cd448074","uu":"0dd24034-36d6-4b1e-a6c1-a52cc984f105","bg":"77e28e28-745a-474b-a496-3c0e086eaec0","sha":"abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52","ph":"/efvrfutgp/expgh/phkkrw","dp":2}
                      {"nm":"invalidJsonLine".pdf","ts":1551140352,"pt":55,"si":"3380fb19-0bdb-46ab-8781-e4c5cd448074","uu":"0dd24034-36d6-4b1e-a6c1-a52cc984f105","bg":"77e28e28-745a-474b-a496-3c0e086eaec0","sha":"abb3ec1b8174043d5cd21d21fbe3c3fb3e9a11c7ceff3314a3222404feedda52","ph":"/efvrfutgp/expgh/phkkrw","dp":2}"""
        expectedData = {"a.txt", "b.pdf"}

        #mock file open to return testJson 
        with patch("builtins.open", return_value=io.StringIO(testJson)):
             result = fileParser.getFileNameList('placeHolder.json')

        self.assertSetEqual(expectedData, result)

    def test_countExtensions(self):
        inputList = ("a.txt","b.pdf","c.txt","d.docx","e.txt")
        expectedData = {"txt":3,"pdf":1,"docx":1}

        result = fileParser.countExtensions(inputList)

        self.assertDictEqual(expectedData,result)

    def test_printResults(self):
        dataToPrint = {"txt":3,"pdf":1,"docx":1}

        with patch('sys.stdout', new = io.StringIO()) as outputString:
            fileParser.printResults(dataToPrint)
            self.assertTrue("txt:3" in outputString.getvalue())
            self.assertTrue("pdf:1" in outputString.getvalue())
            self.assertTrue("docx:1" in outputString.getvalue())

if __name__ == '__main__':
    unittest.main()
