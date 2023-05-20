from DataParser import *
import pandas as pd
import numpy as np
import json
from pandas.testing import assert_frame_equal
import unittest

class TestMathManuallyCleaned(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.DataFrame({'PreReqText': ['MATH 101 (or equivalent) and MATH 102 (or equivalent)', 'MATH 354, STATS 354, MATH 455 or STAT 455 and MATH 223', 'MATH 223 and (MATH 101 or MATH 221)']})
    
    def test_cleaned_column(self):
        
        cleaned_df = math_manually_cleaned('PreReqText', self.df)
        cleaned_df1 = ANTH_manually_cleaned('PreReqText', self.df)
        cleaned_df2 = BIO_manually_cleaned('PreReqText', self.df)
        cleaned_df3 = CHEM_manually_cleaned('PreReqText', self.df)
        cleaned_df4 = CS_manually_cleaned('PreReqText', self.df)
        cleaned_df5 = CDIS_manually_cleaned('PreReqText', self.df)
        cleaned_df6 = EE_manually_cleaned('PreReqText', self.df)
        cleaned_df7 = GEOG_manually_cleaned('PreReqText', self.df)
        cleaned_df8 = GEOL_manually_cleaned('PreReqText', self.df)
        cleaned_df9 = MATH_manually_cleaned('PreReqText', self.df)
        cleaned_df10 = MET_manually_cleaned('PreReqText', self.df)
        cleaned_df11 = STAT_manually_cleaned('PreReqText', self.df)
        cleaned_df12 = RPLS_manually_cleaned('PreReqText', self.df)
        cleaned_df13 = PSYC_manually_cleaned('PreReqText', self.df)
        cleaned_df14 = choose_two_manually_cleaned('PreReqText', self.df)

        
    
    def test_return_type(self):
       
        cleaned_df = math_manually_cleaned('PreReqText', self.df)
        cleaned_df1 = ANTH_manually_cleaned('PreReqText', self.df)
        cleaned_df2 = BIO_manually_cleaned('PreReqText', self.df)
        cleaned_df3 = CHEM_manually_cleaned('PreReqText', self.df)
        cleaned_df4 = CS_manually_cleaned('PreReqText', self.df)
        cleaned_df5 = CDIS_manually_cleaned('PreReqText', self.df)
        cleaned_df6 = EE_manually_cleaned('PreReqText', self.df)
        cleaned_df7 = GEOG_manually_cleaned('PreReqText', self.df)
        cleaned_df8 = GEOL_manually_cleaned('PreReqText', self.df)
        cleaned_df9 = MATH_manually_cleaned('PreReqText', self.df)
        cleaned_df10 = MET_manually_cleaned('PreReqText', self.df)
        cleaned_df11 = STAT_manually_cleaned('PreReqText', self.df)
        cleaned_df12 = RPLS_manually_cleaned('PreReqText', self.df)
        cleaned_df13 = PSYC_manually_cleaned('PreReqText', self.df)
        cleaned_df14 = choose_two_manually_cleaned('PreReqText', self.df)
        self.assertIsInstance(cleaned_df, pd.DataFrame)
        self.assertIsInstance(cleaned_df1, pd.DataFrame)
        self.assertIsInstance(cleaned_df2, pd.DataFrame)
        self.assertIsInstance(cleaned_df3, pd.DataFrame)
        self.assertIsInstance(cleaned_df4, pd.DataFrame)
        self.assertIsInstance(cleaned_df5, pd.DataFrame)
        self.assertIsInstance(cleaned_df6, pd.DataFrame)
        self.assertIsInstance(cleaned_df7, pd.DataFrame)
        self.assertIsInstance(cleaned_df8, pd.DataFrame)
        self.assertIsInstance(cleaned_df9, pd.DataFrame)
        self.assertIsInstance(cleaned_df10, pd.DataFrame)
        self.assertIsInstance(cleaned_df11, pd.DataFrame)
        self.assertIsInstance(cleaned_df12, pd.DataFrame)
        self.assertIsInstance(cleaned_df13, pd.DataFrame)
        self.assertIsInstance(cleaned_df14, pd.DataFrame)
    
    def test_missing_column(self):
        # test if the function raises an error when given a non-existent column name
        with self.assertRaises(KeyError):
            math_manually_cleaned('NonExistentColumn', self.df)
            
            ANTH_manually_cleaned('NonExistentColumn', self.df)
            BIO_manually_cleaned('NonExistentColumn', self.df)
            CHEM_manually_cleaned('NonExistentColumn', self.df)
            CS_manually_cleaned('NonExistentColumn', self.df)
            CDIS_manually_cleaned('NonExistentColumn', self.df)
            EE_manually_cleaned('NonExistentColumn', self.df)
            GEOG_manually_cleaned('NonExistentColumn', self.df)
            GEOL_manually_cleaned('NonExistentColumn', self.df)
            MATH_manually_cleaned('NonExistentColumn', self.df)
            MET_manually_cleaned('NonExistentColumn', self.df)
            STAT_manually_cleaned('NonExistentColumn', self.df)
            RPLS_manually_cleaned('NonExistentColumn', self.df)
            PSYC_manually_cleaned('NonExistentColumn', self.df)
            choose_two_manually_cleaned('NonExistentColumn', self.df)



    
    def test_empty_dataframe(self):
        # test if the function returns an empty DataFrame when given an empty DataFrame
        empty_df = pd.DataFrame(columns=['PreReqText'])
        cleaned_df = math_manually_cleaned('PreReqText', empty_df)
        cleaned_df1 = ANTH_manually_cleaned('PreReqText', empty_df)
        cleaned_df2 = BIO_manually_cleaned('PreReqText', empty_df)
        cleaned_df3 = CHEM_manually_cleaned('PreReqText', empty_df)
        cleaned_df4 = CS_manually_cleaned('PreReqText', empty_df)
        cleaned_df5 = CDIS_manually_cleaned('PreReqText', empty_df)
        cleaned_df6 = EE_manually_cleaned('PreReqText', empty_df)
        cleaned_df7 = GEOG_manually_cleaned('PreReqText', empty_df)
        cleaned_df8 = GEOL_manually_cleaned('PreReqText', empty_df)
        cleaned_df9 = MATH_manually_cleaned('PreReqText', empty_df)
        cleaned_df10 = MET_manually_cleaned('PreReqText', empty_df)
        cleaned_df11 = STAT_manually_cleaned('PreReqText', empty_df)
        cleaned_df12 = RPLS_manually_cleaned('PreReqText', empty_df)
        cleaned_df13 = PSYC_manually_cleaned('PreReqText', empty_df)
        cleaned_df14 = choose_two_manually_cleaned('PreReqText', empty_df)
        self.assertTrue(cleaned_df.empty)
        self.assertTrue(cleaned_df1.empty)
        self.assertTrue(cleaned_df2.empty)
        self.assertTrue(cleaned_df3.empty)
        self.assertTrue(cleaned_df4.empty)
        self.assertTrue(cleaned_df5.empty)
        self.assertTrue(cleaned_df6.empty)
        self.assertTrue(cleaned_df7.empty)
        self.assertTrue(cleaned_df8.empty)
        self.assertTrue(cleaned_df9.empty)
        self.assertTrue(cleaned_df10.empty)
        self.assertTrue(cleaned_df11.empty)
        self.assertTrue(cleaned_df12.empty)
        self.assertTrue(cleaned_df13.empty)
        self.assertTrue(cleaned_df14.empty)


    #Testing 2nd function

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame(columns=["PreReqText"])
        result = largest_comma_count(df)
        self.assertEqual(result, 1)

    def test_single_value(self):
        # Test with a DataFrame containing a single value
        df = pd.DataFrame({"PreReqText": ["MATH 101, MATH 102"]})
        result = largest_comma_count(df)
        self.assertEqual(result, 2)

    def test_multiple_values(self):
        # Test with a DataFrame containing multiple values
        df = pd.DataFrame({"PreReqText": ["MATH 101, MATH 102, MATH 103", "STAT 101", "MATH 201, MATH 202"]})
        result = largest_comma_count(df)
        self.assertEqual(result, 3)

    def test_no_commas(self):
        # Test with a DataFrame containing values with no commas
        df = pd.DataFrame({"PreReqText": ["MATH 101", "STAT 101", "MATH 201"]})
        result = largest_comma_count(df)
        self.assertEqual(result, 1)

   

    def setUp(self):
        # Set up a sample DataFrame
        self.df = pd.DataFrame({
            "PreReqText": ["MATH 101, MATH 102", "STAT 101, MATH 201", "MATH 201, MATH 202, STAT 101"],
            "Col1": [1, 2, 3],
            "Col2": [4, 5, 6],
            "Col3": [7, 8, 9]
        })

    def test_split_into_columns(self):
        # Test that the function correctly splits values into columns
        result = split_values_into_columns(self.df, 2)

    def test_insufficient_columns(self):
        # Test that the function does not modify the DataFrame if there are insufficient columns
        result = split_values_into_columns(self.df, 4)
        self.assertEqual(result.columns.tolist(), ["PreReqText", "Col1", "Col2", "Col3"])

    def test_cleaner(self):
        # Create a sample DataFrame with a PreReqText column
        data = {
            'PreReqText': [
                'COMPSCI 101 or higher',
                'MATH 101 with a grade of C or better',
                'STATS 201, with a grade of C or better, or instructor consent',
                'Two of the following: COMPSCI 201, 202, 203',
                'MATH 201 or equivalent, or instructor permission',
                'Either COMPSCI 210 or COMPSCI 220, with a grade of C or better',
            ]
        }
        df = pd.DataFrame(data)
        
        
        

        def run(self, result=None):
            self.currentResult = result # Remember result for use in tearDown
            unittest.TestCase.run(self, result) # call superclass run method


        def warp_test_suite(testcase_class):
            """Load tests from a specific set of TestCase classes."""
            suite = self.TestSuite()
            tests = unittest.defaultTestLoader.loadTestsFromTestCase(testcase_class)
            suite.addTest(tests)
            return suite

    def testing_parser(self):
        # Read the excel file into a dataframe
        
        output_df = pd.read_excel("Jsoncolumn.xlsx", sheet_name="Sheet1")
        # Loop through each row in the dataframe
        pass_counter = 0
        fail_counter = 0
        not_counter = 0

        with open('ParsedData.json') as user_file:
            file_contents = user_file.read()
            

        parsed_json = json.loads(file_contents)

        for (index, row) in output_df.iterrows():
            word = str(row['SubjectAbbreviation']) + " " + str(row['CourseNumber'])
            if word not in parsed_json :
                #print(word, "has no prerequisites")
                not_counter +=1
            elif str(parsed_json [word]) == str(row['Json format']):
                pass_counter+=1
            else:
                print(str(parsed_json [word]) + " " +str(row['Json format']))
                fail_counter +=1

        print("Pass", pass_counter)
        print("Fail", fail_counter)
        print("No prereq", not_counter)

       
if __name__ == '__main__':
    unittest.main()


