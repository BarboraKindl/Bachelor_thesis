import pandas as pd
import csv
from automatize_text_process.columns import columns_csv
import pandas as pd
from sklearn.model_selection import StratifiedKFold


def patient_selection(info, num):
    """
    Function to select data of a single patient from a dictionary containing data
    of multiple patients.

    :param num:
    :param info: Dictionary with patient data, where the key is the patient ID and the value
    are the patient's data.
    whose data we want to obtain. :return: Returns data of a specific patient.
    If the patient with the given ID does not exist, returns None.
    """
    return info.get(num)


def print_patient_dict(patient_dict):
    """
    Function for printing patient data. Each patient is identified by their ID and
    has assigned EEG conclusions.

    :param patient_dict: Dictionary containing patient data. The key is the patient
    ID and the value is a list of EEG conclusions. :return: Does not return anything. The output is
    a printout of the data on the standard output.
    """

    if patient_dict is None or len(patient_dict) == 0:
        print("No patient data available.")
    else:
        for record_id, eeg_conclusions in patient_dict.items():
            print(f"ID: {record_id}")
            if eeg_conclusions:
                for eeg_conclusion in eeg_conclusions:
                    print(f" - {eeg_conclusion}\n")
            else:
                print("No EEG conclusions available for this patient.\n")


def write_to_csv(patient_data):
    """
    Function for writing patient data to a CSV file. The data is converted into
    a tabular format and saved.

    :param patient_data: Dictionary containing patient data. The key is the patient
    ID and the value is a list of EEG conclusions.
    """

    df = pd.DataFrame(
        [(record_id, eeg_conclusion) for record_id, eeg_conclusions in
         patient_data.items() for eeg_conclusion in eeg_conclusions],
        columns=['Record ID', 'Závěr EEG'])
    csv_filename = 'tables_csv/aggregated_data.csv'
    df.to_csv(csv_filename, index=False)


def write_patient_dict_to_txt(patient_dict):
    try:
        with open('aggregated_data.txt', 'w') as file:
            for record_id, eeg_conclusions in patient_dict.items():
                file.write(f"Record ID: {record_id}\n")
                for eeg_conclusion in eeg_conclusions:
                    file.write(f" - {eeg_conclusion}\n\n")
    except IOError as e:
        print(f"Error writing to {file}: {e}")


def create_csv(output_file):
    data = [columns_csv]
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def reduced_csv():
    data = pd.read_csv('tables_csv/BP_Kindlbar_Poskytnuta_veeg_data_18.csv')
    filtered_data = data[data['Závěr EEG'].notna()]
    result_data = filtered_data[['Record ID', 'Závěr EEG']]
    result_data.to_csv('tables_csv/veeg_data.csv', index=False)


if __name__ == "__main__":
    reduced_csv()
