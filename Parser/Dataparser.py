
import pandas as pd
import numpy as np
import xlrd
import re
import json


def data_reader(level):
    '''Data reader takes level as an input, for now we have parsed the undergraduate classes only, and takes the Separetedfile.xlsx file and stores it as a dataframe df'''
    df = pd.read_excel('Parser/Separetedfile.xlsx', sheet_name="PreReqText Courses")
    df = df[df['CourseLevel'] == level.title()]
    return df



''' The functions named manually cleaned below, are used to get the last 1.7 % on parsing success rate. These classes are manually parsed due to their extreme complications'''
def math_manually_cleaned(column, df):
    df[column] = df[column].apply(lambda x: re.sub("\s+", " ", x))
    df[column] = df[column].apply(lambda x: re.sub(' \(MATH 354, STATS 354, MATH 455 or STAT 455\) and MATH 223',
                                  '( MATH 354 or STATS 354 or MATH 455 or STAT 455 ) and MATH 223', x))
    return df




def ANTH_manually_cleaned(column, df):
    df[column] = df[column].replace(
        "GEOG 101, ANTH 210; Students are strongly encouraged to take Geog 315 or 4/515 before enrolling. Geol 121 can be substituted for Geog 101 with instructor permission.", "GEOG 101, ANTH 210")
    return df




def BIO_manually_cleaned(column, df):
    df[column] = df[column].apply(lambda x: x.strip())
    df[column] = df[column].replace("One BIOL course and one semester of chemistry from among CHEM 104, CHEM 106, CHEM 111, or CHEM 201",
                                    "BIO COURSE, CHEM 104 OR CHEM 106 OR CHEM 111 OR CHEM 201")
    return df



def CHEM_manually_cleaned(column, df):
    df[column] = df[column].replace(
        "Student must demonstrate math placement requirements at or above MATH 112 in the placement chart. See Mathematics for details.", "")
    df[column] = df[column].replace(
        'High school chemistry or “C” (2.0) or higher in CHEM 104. Student must demonstrate math placement requirements at or above MATH 115 in the placement chart. See Mathematics for details.', 'CHEM 104')
    df[column] = df[column].str.replace(
    r'\bBIOL 106,\s+CHEM 324\.\s*BIOL 106 or permission “C” \(2\.0\) or higher in all prerequisites\.', 
    'BIOL 106, CHEM 324', regex=True)
    df[column] = df[column].replace(
    r'\bConcurrent registration in CHEM 460 or completion of CHEM 460 with “C” or higher\. CHEM 305 is highly recommended\. ',
    '', regex=True)
    return df





def CS_manually_cleaned(column, df):
    df[column] = df[column].replace("CS 491 and (CS 306, CS 401, CS 403, CS 406, CS 410, CS 420, CS 435, CS 440, CS 445, CS 450, CS 465, CS 470, CS 480, or CS 485)",
                                    "CS 491 and CS 306 or CS 401 or CS 403 or CS 406 or CS 410 or CS 420 or CS 435 or CS 440 or CS 445 or CS 450 or CS 465 or CS 470 or CS 480 or CS 485 )")
    df[column] = df[column].replace("CS 491W and (CS 306, CS 401, CS 403, CS 406, CS 410, CS 420, CS 435, CS 440, CS 445, CS 450, CS 465, CS 470, CS 480, or CS 485)",
                                    "CS 491W and CS 306 or CS 401 or CS 403 or CS 406 or CS 410 or CS 420 or CS 435 or CS 440 or CS 445 or CS 450 or CS 465 or CS 470 or CS 480 or CS 485 )")
    return df



def CDIS_manually_cleaned(column, df):
    df[column] = df[column].replace("3 of the following: 402, 417, 438. CDIS 416 is recommended.",
                                    "CDIS 402 and CDIS 417 and CDIS 438")
    return df



def EE_manually_cleaned(column, df):
    df[column] = df[column].replace("EE, 230, EE 231, EE 240",
                                    "EE 230, EE 231, EE 240")
    return df


def GEOG_manually_cleaned(column, df):
    df[column] = df[column].replace("Prerequisite: GEOG 373, or 473/573, or permission of instructor.",
                                    "Prerequisite: GEOG 373, or GEOG 473 or GEOG 573, or permission of instructor.")
    df[column] = df[column].replace("Either Geog 101 or Geol 121 and Geog 315 or 415 are recommended. Or instructor consent.",
                                    "Either Geog 101 or Geol 121 and Geog 315 or Geog 415 are recommended. Or instructor consent.")
    df[column] = df[column].replace(
        "Either GEOG 101 or ANTH 210; We strongly encourage students to take GEOG 315 before enrolling. Geol 121 can be substituted for GEOG 101 with instructor permission.", "Either GEOG 101 or ANTH 210")
    return df




def GEOL_manually_cleaned(column, df):
    df[column] = df[column].replace("CHEM 191, CHEM 201, GEOL/BIOL 104 or instructor permission.",
                                    "CHEM 191, CHEM 201, GEOL 104 or BIOL 104 or instructor permission.")
    return df




def MATH_manually_cleaned(column, df):
    df[column] = df[column].replace(
        "Three years high school algebra/geometry or MATH 098", "MATH 098")
    return df




def MET_manually_cleaned(column, df):
    df[column] = df[column].replace(
        "ENG 271W, MET 275, MET 425, 10 AET or MET 300/400 level credits", "ENG 271W, MET 275, MET 425")
    return df




def STAT_manually_cleaned(column, df):
    df[column] = df[column].str.replace(
        "MATH/STAT 354", "MATH 354 or STAT 354")
    df[column] = df[column].str.replace(
        "MATH 354 or STAT 354 or both MATH 121 and STAT 154", "MATH 354 or STAT 354 or both STAT 154 and MATH 121")
    df[column] = df[column].str.replace(
        "MATH 354 or STAT 354 or both MATH 121 adn STAT 154", "MATH 354 or STAT 354 or both STAT 154 adn MATH 121")

    return df




def RPLS_manually_cleaned(column, df):
    df[column] = df[column].str.replace("RPLS 272 RPLS 282 RPLS 341W, or with instructor permission. Upper division prerequisites can be taken concurrently with instructor permission.",
                                        "RPLS 272, RPLS 282, RPLS 341W, or with instructor permission. Upper division prerequisites can be taken concurrently with instructor permission.", regex=True)

    return df


def PSYC_manually_cleaned(column, df):
    df[column] = df[column].str.replace("Complete one course: MATH 112, MATH 113, MATH 115, MATH 121, MATH 130, or STAT 154",
                                        "MATH 112 or MATH 113 or MATH 115 or MATH 121 or MATH 130 or STAT 154")

    return df




def choose_two_manually_cleaned(column, df):
    df[column] = df[column].str.replace("Two of the following: MATH 316, MATH 321, MATH 345, MATH 375 and senior standing \(or permission of the instructor\). Course can also be taken independent study with permission of a cooperating faculty member.",
                                        "MATH 316 or MATH 321 or MATH 345 or MATH 375 AND MATH 316 or MATH 321 or MATH 345 or MATH 375", regex=True)
    df[column] = df[column].str.replace("STAT 457, STAT 458, STAT 459, STAT 450 \(at least two of these\)",
                                        "STAT 457 or STAT 458 or STAT 459 or STAT 450 AND STAT 457 or STAT 458 or STAT 459 or STAT 450", regex=True)
    df[column] = df[column].str.replace("IBUS 428, IBUS 448, IBUS 469 \(select 2 out of the 3 courses\)",
                                        "IBUS 428 or IBUS 448 or IBUS 469 AND IBUS 428 or IBUS 448 or IBUS 469", regex=True)
    return df





def or_formatter(column, df):
    '''Takes the data frame and works on the PreReqText column, focusing on the ORs to have a consistent structure '''
    df[column] = df[column].str.replace(' / |/', ' or ', regex=True)
    df[column] = df[column].str.replace(', or', ' or')
    df[column] = df[column].str.replace('OR "C"', 'or C')
    df[column] = df[column].str.replace(', with ', ' with ')
    df[column] = df[column].str.replace(', and', ' and')
    df[column] = df[column].str.replace('\(or ', '( or ', regex=True)
    df[column] = df[column].str.replace('OR', 'or')
    df[column] = df[column].str.replace('or better', '', regex=True)

    return df





def or_and_formatter_2(column, df):
    '''Focuses on the ANDs to have a consistent structure '''

    df[column] = df[column].str.replace('Select One:|Select 1:','and',  flags=re.IGNORECASE, regex=True)
    df[column] = df[column].str.replace('.', ' and ', regex=True)
    df[column] = df[column].str.replace('&', ' and ')
    df[column] = df[column].str.replace(';', ' and ')
    df[column] = df[column].str.replace(' AND ', ' and ', regex=True)
    df[column] = df[column].str.replace(' adn ', ' and ')
    df[column] = df[column].str.replace(',| , ', ' and ', regex=True)
    df[column] = df[column].str.replace('(', '(  ', regex=True)
    df[column] = df[column].str.replace(')', ' )', regex=True)




    return df





def typo_fixer(column, df):
    ''' Fixes Typos in the data-frame'''
    df[column] = df[column].str.replace("ATHN", "ETHN")
    df[column] = df[column].str.replace("DANC120W", "DANC 120W")
    df[column] = df[column].str.replace("STATS", "STAT")
    df[column] = df[column].str.replace("CDS", "CDIS")
    df[column] = df[column].str.replace("ACT", "ACCT")
    df[column] = df[column].str.replace("MUS ", "MUSC ")
    df[column] = df[column].str.replace("Psy ", "PSYC ")
    df[column] = df[column].str.replace("SPC ", "SOC ")




    return df





def remove_before_strongly_recommended(column):
    '''temporarily: We are removing all non class PreReqs '''
    pattern = re.compile(r'(?:[A-Z]+\s\d+\W*\s*,\s*)*([A-Z]+\s\d+\W*)*\W*(strongly recommended|recommended|is strongly recommended|advisory)', flags=re.IGNORECASE)
    return column.apply(lambda x: re.sub(pattern, '', x, count=1))



def remove_after_point(column, point):
    ''' Some classes which are supposed to be in the concurrent sheet are listed under PreReq, so we are removing them here'''
    class_lists = column.apply(lambda x: x.upper().split(" "))
    new_lists = []
    pattern = re.compile(r'\b(CONCURRENT|CURRENTLY)\w*\b', flags=re.IGNORECASE)
    for class_list in class_lists:
        new_class_list = []
        for word in class_list:
            if pattern.search(word):
                new_class_list.append('CO-REQUISITE:')
            else:
                new_class_list.append(word)
        if point in new_class_list:
            index = new_class_list.index(point)
            new_class_list = new_class_list[:index-1]
        new_lists.append(new_class_list)
    new_column = []
    for new_list in new_lists:
        new_column.append(" ".join(new_list))
    return new_column




def clean_class_list(class_list, sub):
    ''' This function comes after the parser function, it cleans the data from trailing or leading extra words'''
    i = 0
    while i < len(class_list):
        if class_list[i] == 'OR':
            # Remove non-class elements following "OR"
            j = i + 1
            while j < len(class_list) and class_list[j] not in sub:
                class_list.pop(j)
            if j < len(class_list):
                i = j
            else:
                break
        elif class_list[i] in sub and (i == len(class_list) - 1 or not (len(class_list[i+1]) == 3 and class_list[i+1].isdigit() or len(class_list[i+1]) == 4 and class_list[i+1][:3].isdigit() and class_list[i+1][3] == 'W')):
            class_list.pop(i)
        else:
            i += 1
    # Remove leading and trailing "or" and "and" conjunctions
    while class_list and class_list[0] in ["OR","AND"," OR "," AND "]:
        class_list = class_list[1:]
    while class_list and class_list[-1] in ["OR","AND"," OR "," AND "]:
        class_list = class_list[:-1]
    # Remove classes that are not followed by numbers
    return class_list


def parser_function(column, df):
    '''This is the main part of the algorithm, it removes every word that isn't an instance of the class or our conjunction points'''
    df[column] = df[column].str.replace('\.\s*$', '', regex=True)
    df[column] = df[column].apply(lambda x: x.upper().split(" "))
    conjunction=["OR","AND"," OR "," AND "]
    sub=df["SubjectAbbreviation"].tolist()
    sub.extend(["IT","ISYS", "CJ"])

    for index, row in df.iterrows():
        new_list = []
        for i in row[column]:
            if i in sub or i in conjunction or (isinstance(i, str) and ((len(i) == 3 and i.isdigit()) or (len(i) == 4 and i[:3].isdigit() and i[3] == 'W'))):
                new_list.append(i)
            else:
                continue
        new_list = clean_class_list(new_list, sub)
        df.at[index, column] = " ".join(new_list)
    return df




def And_formatter_for_separation(column, df):
    '''This function formats AND to comma for our separation to begin'''
    df[column] = df[column].str.replace(" AND ", " , ")
    return df

def credit_300(column, df):
    '''We have a couple of words that say 300 credit level which aren't need within our algorithm for now, so this removes the number 300 that is left off from our parser function'''
    df[column] = df[column].apply(lambda x: x.upper().split(" "))
    sub = df["SubjectAbbreviation"].tolist()
    sub.extend(["IT","ISYS", "CJ"])
    for index, row in df.iterrows():
        new_list = []
        for i in range(len(row[column])):
            if row[column][i] == "300" and (row[column][i-1] not in sub):
                continue
            else:
                new_list.append(row[column][i])
        df.at[index, column] = " ".join(new_list)
    return df





def largest_comma_count(df):
    ''' The two functions below creates new columns based on how much is needed to make ready for our next step which is splitting the prerequisites into separate columns from the PreReqText column.
        The first function creates the columns by taking the largest number of prereqs from the second function. 
        The second function determines how many new columns are needed by counting the number of prereqs in each cell of the column and storing the value of prereqs for the cell with the largest number of prereqs. It does this by counting the commas, (commas are the separator of prereqs.)'''
    prereqs = 0
    for i in df["PreReqText"]:
        count = 0
        x=","
        for j in i:
            if j == x:
                count+=1
        if count>prereqs:
            prereqs=count
    return prereqs+1


def create_new_columns(df, prereqs):
    for i in range(prereqs):
        df["Prereq " + str(i + 1)] = ""
    return df



def split_values_into_columns(df, y):
    '''The code below will split the values into the newly created columns.'''
    last_y_columns = df.columns[-y:]
    for i, row in df.iterrows():
        split_values = row["PreReqText"].split(",")
        for j in range(y):
            if j < len(split_values):
                df.at[i, last_y_columns[j]] = split_values[j]
    return df



def inner_array_split(df):
    '''The code below removes unsolved instance of AND due to duplication, and creates the inner OR array'''
    subjects= df['SubjectAbbreviation'].drop_duplicates().tolist()
    columns_to_replace = df.columns[df.columns.get_loc("CourseLevel") + 1:]  
    df.loc[:, columns_to_replace] = df.loc[:, columns_to_replace].apply(lambda x: x.str.replace(r'^OR\s*', '', regex=True))
    df.loc[:, columns_to_replace] = df.loc[:, columns_to_replace].apply(lambda x: x.str.replace('AND', '', regex=True))
    df.loc[:, columns_to_replace] = df.loc[:, columns_to_replace].apply(lambda x: x.str.strip())  

    for col in columns_to_replace:
        df[col] = df[col].apply(lambda x: x.split(" OR ") if isinstance(x, str) and " OR " in x else x)

    return df  



def json_creator(df, filename):
    '''The code below converts the values into a dictionary and exports them as a json file, so we could be able to use it for our tree algorithm.'''
    columns_to_replace = df.columns[df.columns.get_loc("CourseLevel") + 1:]    
    df["key"] = df["SubjectAbbreviation"] + " " + df["CourseNumber"].map(str)
    columns_to_include = ['key']
    columns_to_include.extend(columns_to_replace)
    df=df[columns_to_include]
    d={}
    for i, row in df.iterrows():
            class_name=row['key']
            values = []
            for cell_value in row[columns_to_include[1:]]:
                if cell_value not in ['', None]:
                    values.append(cell_value)
            if values:
                d[class_name] = values

    json_string = json.dumps(d, ensure_ascii=False, separators=(',', ': '))
    json_string = json_string.replace('],"', '],\n"').replace('{', '{\n').replace('}', '\n}')
    with open(filename, "w") as f:
        f.write(json_string)



def json_column(df, json_file):
    '''The function creates a Json column for testing purposes'''
    with open(json_file, 'r') as f:
        json_data = f.read()
    data = json.loads(json_data)
    
    json_col = []
    for i, row in df.iterrows():
        key = row['SubjectAbbreviation'] + ' ' + str(row['CourseNumber'])
        if key in data:
            json_col.append(data[key])
        else:
            json_col.append([])
    df['Json format'] = json_col
    return df



def parse_data(json_file_path, df):
    '''The function calculates how many percent of the data was successfully parsed'''
    code_pattern = re.compile(r"^[A-Z]{1,4}\s\d{3}W?\s?$")
    subjects = df['SubjectAbbreviation'].drop_duplicates().tolist()
    subjects.extend(["IT","ISYS", "CJ"])

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    num_successful = 0
    num_unsuccessful = 0
    unsuccess = []

    def is_successful_value(value):
        if isinstance(value, list):
            for element in value:
                if isinstance(element, list):
                    if not all(is_successful_value(nested_element) for nested_element in element):
                        return False
                else:
                    if not any(subject in element for subject in subjects) or not code_pattern.match(element):
                        return False
            return True
        else:
            return any(subject in value for subject in subjects) and code_pattern.match(value)

    for value in data.values():
        if is_successful_value(value):
            num_successful += 1
        else:
            num_unsuccessful += 1
            unsuccess.append(value)


    total_rows = num_successful + num_unsuccessful
    success_rate = num_successful / total_rows * 100
    x = "{:.2f}".format(success_rate)
    #print(unsuccess) -> uncomment for debugging 
    return x +" percent successfully parsed"




def main():
    df = data_reader("undergraduate")

    # Call the functions to clean the data manually
    df = math_manually_cleaned('PreReqText', df)
    df = ANTH_manually_cleaned('PreReqText', df)
    df = BIO_manually_cleaned('PreReqText', df)
    df = CHEM_manually_cleaned('PreReqText', df)
    df = CS_manually_cleaned('PreReqText', df)
    df = CDIS_manually_cleaned('PreReqText', df)
    df = EE_manually_cleaned('PreReqText', df)
    df = GEOG_manually_cleaned('PreReqText', df)
    df = GEOL_manually_cleaned('PreReqText', df)
    df = MATH_manually_cleaned('PreReqText', df)
    df = MET_manually_cleaned('PreReqText', df)
    df = STAT_manually_cleaned('PreReqText', df)
    df = RPLS_manually_cleaned('PreReqText', df)
    df = PSYC_manually_cleaned('PreReqText', df)
    df = choose_two_manually_cleaned('PreReqText', df)




    df = or_formatter('PreReqText', df)
    df = or_and_formatter_2('PreReqText', df)
    df = typo_fixer('PreReqText', df)
    df['PreReqText'] = remove_before_strongly_recommended(df['PreReqText'])
    df['PreReqText'] = remove_after_point(df['PreReqText'], 'CO-REQUISITE:')
    df = parser_function('PreReqText', df)
    df = And_formatter_for_separation('PreReqText', df)
    df = credit_300('PreReqText', df)
    df = create_new_columns(df, largest_comma_count(df))
    df = split_values_into_columns(df,largest_comma_count(df))
    df = inner_array_split(df)
    json_creator(df, "Parser/ParsedData.json")
    json_column(df, "Parser/ParsedData.json")
    df.insert(3, "Json format", df.pop("Json format"))
    df.to_excel("Parser/Jsoncolumn.xlsx")
    print(parse_data("Parser/ParsedData.json",df))

main()





