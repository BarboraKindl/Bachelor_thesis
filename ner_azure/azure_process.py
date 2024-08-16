import pandas as pd
import os
import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def save_data_to_csv(all_data, output_csv):
    """
    Saves data to a CSV file. If the file already exists, the data is appended to the end.
    If the file does not exist, a new one is created.

    Args:
    all_data (list of dict): List of dictionaries with data to be saved.
    output_csv (str): Path to the output CSV file.
    """
    df = pd.DataFrame(all_data)
    file_exists = os.path.exists(output_csv)
    try:
        df.to_csv(output_csv, mode='a', index=False, header=not file_exists)
    except FileNotFoundError as e:
        print(f"Error writing to file: {e}")

    print(
        f"Data has been appended to {output_csv}"
        f"from patient with id {id}")


def save_data(data, id_patient):
    """
    Saves data to a CSV file specific to the given patient.

    Args:
    data (list of dict): Data to be saved.
    id_patient (int): Patient identifier to be used in the file name.
    """
    df = pd.DataFrame(data)
    output_csv = f"patient_health_data_{id_patient}.csv"
    df.to_csv(output_csv, index=False)
    print(f"Data has been saved to {output_csv}")


def analyze_health_data(client, documents, patient_ids, eeg_dates,
                        language="en"):
    """
    Analyzes health data using Azure Text Analytics for healthcare.
    The analysis results are stored in a CSV file.

    Args:
    client (TextAnalyticsClient): Client for Azure Text Analytics.
    documents (list): List of documents to analyze.
    patient_ids (list): List of patient identifiers.
    eeg_dates (list): List of EEG record dates.
    
    language (str, optional): Language of the documents. Default is 'en' (English).
    """
    global patient_id
    combined_data = []
    try:
        poller = client.begin_analyze_healthcare_entities(documents,
                                                          language=language)
        results = poller.result()
    except Exception as e:
        print(f"Error processing healthcare entities: {e}")
        return

    for doc, patient_id, eeg_date in zip(results, patient_ids, eeg_dates):
        if not doc.is_error:
            for entity in doc.entities:
                entity_data = {
                    "Patient ID": patient_id,
                    "EEG Date": eeg_date,
                    "Entity": entity.text,
                    "Normalized Text": entity.normalized_text,
                    "Category": entity.category,
                    "Subcategory": entity.subcategory,
                    "Offset": entity.offset,
                    "Confidence Score": entity.confidence_score
                }

                if entity.assertion is not None:
                    entity_data.update({
                        "Conditionality": entity.assertion.conditionality,
                        "Certainty": entity.assertion.certainty,
                        "Association": entity.assertion.association
                    })
                combined_data.append(entity_data)

    path = "tables_csv/azure_csv/"
    save_data_to_csv(combined_data, path + "combined_health_data.csv")
