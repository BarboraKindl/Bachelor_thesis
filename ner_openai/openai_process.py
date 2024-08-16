import openai
import ast
import pandas as pd
import csv

from dotenv import load_dotenv
import os

from automatize_text_process.columns import columns_csv


load_dotenv()
openai.api_key = os.getenv('OPENAI_API')


def openai_chat_completion_response(sentence):
    """
    This function utilizes the OpenAI API to extract named entities from the provided sentence.
    Input:
        sentence: The sentence from which named entities are to be extracted.
    Output:
        Returns the extracted entities in a dictionary format, where the keys correspond to the defined entities.
    """
    definice_entit = (
        "Definice Entit:\n"
        "1. Délka_Monitorování: Délka video/EEG monitorování.\n"
        "2. Přítomnost epileptických záchvatů: Zmínky o 'záchvaty' a 'epileptiformní' aktivitě ukazují na přítomnost epileptických projevů.\n"
        "3. Typy EEG aktivit:'Rytmická' aktivita a obecné zmínky o 'aktivitě' naznačují možnost kategorizace podle charakteristik EEG záznam\n"
        "4. Lokalizace: Slova 'vpravo' a 'vlevo' naznačují, že lokalizace epileptogenních zón může být důležitá pro kategorizaci.\n"
        "5. Specifika: Specifické detaily související se stavem nebo diagnózou, např. možná epileptogenní zóna.\n"
        "6. Aktivita během spánku vs. bdělosti: Rozlišení mezi aktivitou zaznamenanou 've spánku' (zde 'spnku') a 'bdění' (v textu jako 'bdění') může být další relevantní kategorií.\n"
        "7. Lateralita: Indikace laterality (levá/pravá strana) relevantní pro lokalizaci patologických nálezů.\n"
        "8. Typ_aktivity: Typy pozorované mozkové aktivity, identifikované při neurologických vyšetřeních.\n"
        "9. Pacientova reakce: Popisuje reakci nebo chování pacienta během záznamu, například změny v chování nebo motorické reakce.\n"
        "10. Terapie_Redukce: Zda došlo k redukci antiepileptické terapie během monitorování.\n"
        "11. Okcipitální_Rytmus: Přítomnost asymetrie v okcipitálním rytmu.\n"
        "12. Asymetrie_MU_Rytmu: Asymetrie MU rytmu.\n"
        "13. Areální_Diferenciace_Vlevo/Vpravo: Kvalita areální diferenciace na levé/pravé straně.\n"
        "14. FCTP_Oblast_Zpomalení: Přítomnost intermitentního zpomalení nad oblastí FCTP.\n"
        "15. Epileptiformní_Aktivita: Přítomnost epileptiformní aktivity v EEG.\n"
        "16. Maxima_Epileptiformní_Aktivity: Lokalizace maximální epileptiformní aktivity.\n"
        "17. Stav_Spánku: Organizace spánkových stadií v EEG.\n"
        "18. NREM_Epileptiformní_Aktivita: Charakteristika epileptiformní aktivity v NREM spánku.\n"
        "19. REM_Epileptiformní_Aktivita: Charakteristika epileptiformní aktivity v REM spánku.\n"
        "20. Charakter_Záchvatů: Přítomnost a typ záchvatů během monitorování.\n"
        "21. Semiologie: Popis semiologických prvků záchvatů.\n"
        "22. Iktální_EEG: Charakteristika iktálního EEG.\n"
    )
    final_prompt = f"{definice_entit}\n\nVěta pro extrakci: {sentence}.Pokud v některých kategoriích nejsou prezentovány žádné entity, nech je jako None\n"

    system_prompt = "Jsi inteligentní systém pro rozpoznávání pojmenovaných entit (NER). Níže jsou uvedeny definice entit, které potřebuji extrahovat z následující věty, a očekávám výstup ve slovníku, kde klíče budou entity."

    user_prompt = "Jsi si jasný svou rolí?"

    assistant_response = "Jasně, jsem připraven ti pomoci s tvým úkolem NER. Prosím, poskytni mi potřebné informace pro zahájení."
    # Estimated maximum number of tokens the API can handle
    max_tokens = 4096
    if len(final_prompt) > max_tokens:
        raise ValueError(
            "Vstupní text přesahuje limit povolených tokenů pro API.")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": assistant_response},
            {"role": "user", "content": final_prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip(" \n")


def parse_response_to_dict(response):
    """
     Converts a comma-separated string of key-value pairs into a dictionary.
     Each key-value pair should be in the format "key: value".

     :param response: A string containing key-value pairs.
     :return: A dictionary with the keys and values extracted from the input string.
     """
    # Initialize an empty dictionary to store the results
    entity_dict = {}
    # Split the input string into parts using comma as delimiter
    parts = response.split(", ")

    for part in parts:
        try:
            # Split each part into key and value using colon as delimiter
            key, val = part.split(": ")
            # Remove extra spaces and surrounding quotes
            key = key.strip().rstrip()
            val = val.strip("' ")
            # Convert 'None' string to Python's None type
            if val == "None":
                val = None
            # Add the key-value pair to the dictionary
            entity_dict[key] = val
        except ValueError:
            raise ValueError(
                f"Invalid input format: {part}. Expected 'key: value'.")
    return entity_dict


def create_csv(file_output):
    """
    Creates a CSV file with predefined headers related to EEG data recording.

    :param file_output: Path to the output CSV file.
    """
    headers = [
        'Record ID', 'Délka_Monitorování', 'Přítomnost epileptických záchvatů',
        'Typy EEG aktivit', 'Lokalizace', 'Specifika',
        'Aktivita během spánku vs. bdělosti',
        'Lateralita', 'Typ_aktivity', 'Pacientova reakce', 'Terapie_Redukce',
        'Okcipitální_Rytmus', 'Asymetrie_MU_Rytmu',
        'Areální_Diferenciace_Vlevo/Vpravo',
        'FCTP_Oblast_Zpomalení', 'Epileptiformní_Aktivita',
        'Maxima_Epileptiformní_Aktivity',
        'Stav_Spánku', 'NREM_Epileptiformní_Aktivita',
        'REM_Epileptiformní_Aktivita',
        'Charakter_Záchvatů', 'Semiologie', 'Iktální_EEG'
    ]
    try:
        with open(file_output, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    except IOError as e:
        raise IOError(
            f"An error occurred while writing to the file {file_output}: {e}")


def process_records(df, output_file):
    """
    Process records from a DataFrame and write the results to a CSV file.
    
    Parameters:
    - df (pandas.DataFrame): DataFrame containing the EEG data.
    - output_file (str): Path to the output CSV file.

    Returns:
    - float: The success rate of processing records (percentage of successfully
    processed records).
    """
    records_total = 0
    records_successful = 0

    # Open the output CSV file in append mode
    with open(output_file, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        # Process each row in the DataFrame
        for idx, row in df.iterrows():
            id = row['Record ID']
            conclusion = row['Závěr EEG']
            records_total += 1

            try:
                str_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "EEG analysis"},
                              {"role": "user", "content": conclusion}]
                )['choices'][0]['message']['content']

                # Convert the string response to a dictionary
                dict_response = ast.literal_eval(
                    str_response.strip().replace("  ", " ").replace("\n", "")
                )

                # Prepare data row for CSV
                data_row = [id]

                for col in columns_csv:
                    value = dict_response.get(col, '')
                    cleaned_value = ', '.join(value) if isinstance(value,
                                                                   list) else value
                    data_row.append(cleaned_value)

                writer.writerow(data_row)
                records_successful += 1
            except Exception as e:
                print(f"Error processing record {id}: {e}")

    # Calculate success rate
    if records_total > 0:
        success_rate = records_successful / records_total * 100
    else:
        success_rate = 0

    return success_rate
