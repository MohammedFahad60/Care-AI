import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

class ClinicalDataPreprocessor:
    """
    Handles ETL processes for raw patient data.
    Normalizes vital signs and encodes categorical symptoms.
    """
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoder = OneHotEncoder(handle_unknown='ignore')

    def normalize_vitals(self, vitals_df):
        """
        Standardizes BP, Heart Rate, and Temp using Z-Score normalization.
        Formula: z = (x - u) / s
        """
        columns = ['systolic_bp', 'heart_rate', 'temperature']
        if all(col in vitals_df.columns for col in columns):
            return self.scaler.fit_transform(vitals_df[columns])
        return vitals_df

    def encode_symptoms(self, raw_symptoms):
        """Converts text symptoms into Sparse Matrix for Random Forest"""
        cleaned = [s.lower().strip().replace(" ", "_") for s in raw_symptoms]
        return cleaned