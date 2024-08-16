import pandas as pd
from openpyxl import Workbook
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def split_lang(text):
    result = []
    current_language = None
    current_word = ""
    print(text  )
    for char in text:
        if char.isalpha():
            if char.isascii():
                language = "english"
            else:
                language = "korean"
        else:
            language = current_language
        
        if current_language is None:
            current_language = language
        elif current_language != language:
            result.append(current_word)
            current_word = ""
            current_language = language
        
        current_word += char
    
    if current_word:
        result.append(current_word)
    
    return result

def split_syn_ant(text):
    syn_start = "syn.)"
    ant_start = "ant.)"
    
    synonym_list = []
    antonym_list = []
    
    if syn_start in text and ant_start in text:
        parts = text.split(ant_start)
        syn_text = parts[0].replace(syn_start, "")
        ant_text = parts[1].replace(ant_start, "")
        
        synonym_list = [word.strip().replace("…", "") for word in syn_text.split(",")]
        antonym_list = [word.strip().replace("…", "") for word in ant_text.split(",")]
        
    elif syn_start in text:
        syn_text = text.replace(syn_start, "")
        synonym_list = [word.strip().replace("…", "") for word in syn_text.split(",")]
        
    elif ant_start in text:
        ant_text = text.replace(ant_start, "")
        antonym_list = [word.strip().replace("…", "") for word in ant_text.split(",")]
    
    return [synonym_list, antonym_list]


def main():
    # Prompt user to choose input file
    Tk().withdraw()
    file_path = askopenfilename()

    # Load the excel file
    xls = pd.ExcelFile(file_path)

    # Get the number of sheets in the Excel file
    sheetnum = len(xls.sheet_names)

    # Create a new workbook
    workbook = Workbook()

    # Get filename and location for output file
    output_filename = asksaveasfilename(defaultextension=".xlsx")



    # Create a dataframe to hold all the data
    final_df = pd.DataFrame(columns=["expression", "expression mods", "definition", "definition in korean", "synonym", "antonym", "passage sentence"])

    # Process each sheet
    for i in range(sheetnum):
        # Load a sheet into a DataFrame by name
        df = xls.parse(xls.sheet_names[i])
        
        for index, row in df.iterrows():
            # Split the columns as per the instructions
            expression_parts = row["expression"].split(' ', 1)
            expression = expression_parts[0]
            expression_mods = expression_parts[1] if len(expression_parts) > 1 else ''

            try : 
                definition_parts = split_lang(row["definition (synonym + antonym)"])
            except:
                definition_parts = split_lang(row[2])

            definition = definition_parts[0]
            if (len(definition_parts) == 1):
                definition_kr = None
                try : 
                    syn_anttt = definition_parts[0].split("syn.)")[1]
                except : 
                    syn_anttt = ''
            else : 
                definition_kr = definition_parts[1]
                if (len(definition_parts)>=3):
                    syn_anttt = definition_parts[2]

            print("definition_parts", definition_parts)


            if (len(definition_parts)>=3):
                synonym, antonym = split_syn_ant(syn_anttt)
                print("synonym : ", synonym)

            else : 
                synonym = None
                antonym = None
            passage_sentence = row[3]
            final_df = final_df._append({"expression": expression, 
                                        "expression mods": expression_mods, 
                                        "definition": definition, 
                                        "definition in korean": definition_kr, 
                                        "synonym": synonym, 
                                        "antonym": antonym, 
                                        "passage sentence": passage_sentence}, ignore_index=True)
    
            
    # Save the DataFrame to an excel file
    final_df.to_excel(output_filename, index=False)

if __name__ == '__main__':
    main()