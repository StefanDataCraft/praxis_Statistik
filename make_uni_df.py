import pandas as pd

def get_dummied_df():
    uni_df = pd.read_excel(".\data\Fallstudiendaten_Uni.xlsx")
    #uni_df
    # Ausgabe des aktualisierten DataFrames
    #print(uni_df)
    #uni_df["Männlich"] = [x["Geschlecht"]==1 for x in uni_df]
    uni_dummied_df = uni_df
    uni_dummied_df['Männlich'] = 0  # Initialize the new column with 0
    uni_dummied_df['Weiblich'] = 0  # Initialize the new column with 0
    uni_dummied_df['Divers'] = 0  # Initialize the new column with 0
    uni_dummied_df.loc[uni_dummied_df['Geschlecht'] == 1, 'Männlich'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.loc[uni_dummied_df['Geschlecht'] == 2, 'Weiblich'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.loc[uni_dummied_df['Geschlecht'] == 3, 'Divers'] = 1  # Set 'NewColumn' to 1 where the condition is True

    uni_dummied_df['Single'] = 0  # Initialize the new column with 0
    uni_dummied_df['Nicht_zusammen'] = 0  # Initialize the new column with 0
    uni_dummied_df['Zusammen_lebend'] = 0  # Initialize the new column with 0
    uni_dummied_df['Verheiratet'] = 0  # Initialize the new column with 0
    uni_dummied_df['Keine_Angabe'] = 0  # Initialize the new column with 0
    uni_dummied_df.loc[uni_dummied_df['Beziehungsstatus'] == 1, 'Single'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.loc[uni_dummied_df['Beziehungsstatus'] == 2, 'Nicht_zusammen'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.loc[uni_dummied_df['Beziehungsstatus'] == 3, 'Zusammen_lebend'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.loc[uni_dummied_df['Beziehungsstatus'] == 4, 'Verheiratet'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.loc[uni_dummied_df['Beziehungsstatus'] == 5, 'Keine_Angabe'] = 1  # Set 'NewColumn' to 1 where the condition is True
    uni_dummied_df.drop('Beziehungsstatus', axis=1, inplace=True)
    uni_dummied_df.drop('Geschlecht', axis=1, inplace=True)
    return uni_dummied_df