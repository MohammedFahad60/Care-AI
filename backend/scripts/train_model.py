import os
import joblib 
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 

# --- Configuration Paths ---
# Use the directory of this script as the base path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, 'data', 'training_data.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'model')
MODEL_FILE_PATH = os.path.join(MODEL_DIR, 'model.pkl')

# --- Feature List (Must match app.py and index.html) ---
# Note: 'age' is not included here as it's handled separately as a column
SYMPTOM_FEATURES = [
    'fever', 'cough', 'headache', 'sore_throat', 'runny_nose', 'sneezing',
    'body_ache', 'fatigue', 'chills', 'nausea', 'vomiting', 'diarrhea',
    'shortness_of_breath', 'loss_of_smell', 'loss_of_taste', 'congestion',
    'watery_eyes', 'itchy_eyes', 'joint_pain', 'muscle_pain',
    'abdominal_pain', 'chest_pain', 'dizziness', 'migraine', 'swollen_glands',
    'rash', 'constipation', 'stomach_cramps', 'back_pain', 'neck_pain',
    'appetite_loss', 'weight_loss', 'blurred_vision', 'ringing_in_ears',
    'difficulty_swallowing', 'hoarseness', 'heart_palpitations',
    'blood_in_stool', 'yellow_skin', 'frequent_urination', 'mood_swings',
    'insomnia', 'anxiety', 'dry_skin', 'hives', 'sweating', 'tremors',
    'weakness', 'tingling', 'numbness', 'confusion', 'balance_issues',
    'fainting', 'burning_sensation', 'sensation_of_fullness',
    'swelling_limbs', 'mouth_ulcers', 'bleeding_gums', 'hair_loss',
    'acne', 'sensitivity_to_light', 'difficulty_breathing', 'wheezing',
    'ear_pain', 'eye_redness', 'painful_periods', 'infertility',
    'low_sex_drive', 'excessive_thirst', 'frequent_infections',
    'slow_healing_wounds', 'stomach_acid', 'bloating', 'gas',
    'difficulty_concentrating', 'irritability', 'memory_loss',
    'trembling_hands', 'cold_sensitivity', 'heat_sensitivity',
    'skin_redness', 'bruising_easily', 'nosebleeds', 'chapped_lips',
    'dry_mouth', 'metallic_taste', 'restlessness', 'urgency_to_urinate',
    'muscle_spasms', 'difficulty_moving', 'stiffness', 'tender_joints',
    'poor_circulation', 'cold_feet', 'dry_eyes', 'sun_sensitivity',
    'salty_sweat', 'excessive_gas', 'dark_urine', 'pale_stool',
    'choking_sensation', 'sensation_of_lump', 'difficulty_sleeping',
    'night_sweats', 'burning_when_urinating'
]
DISEASE_TARGETS = list(set([
    "Flu (Influenza)", "Common Cold", "Seasonal Allergies", "Migraine" 
    # Must match the keys in DISEASE_KNOWLEDGE_BASE in app.py
]))


def generate_mock_data():
    """
    Creates a simple mock dataset for initial testing if training_data.csv is missing.
    In a real project, you MUST replace this with high-quality, real data.
    """
    print("WARNING: Generating MOCK data for initial setup. Replace with real data for production.")
    N_SAMPLES = 1000  # Number of simulated patients
    data = {}

    # 1. Create random age data
    data['age'] = np.random.randint(5, 80, N_SAMPLES)

    # 2. Create the symptom columns (mostly 0s, 100+ columns)
    for symptom in SYMPTOM_FEATURES:
        data[symptom] = np.random.randint(0, 2, N_SAMPLES)
    
    # 3. Create a random disease target
    data['disease'] = np.random.choice(DISEASE_TARGETS, N_SAMPLES)

    df = pd.DataFrame(data)
    
    # --- Inject high-confidence patterns for testing ---
    df.loc[0:200, ['fever', 'body_ache', 'chills']] = 1
    df.loc[0:200, 'disease'] = 'Flu (Influenza)'
    
    df.loc[201:400, ['sneezing', 'runny_nose', 'itchy_eyes']] = 1
    df.loc[201:400, 'disease'] = 'Seasonal Allergies'
    
    return df


def load_data():
    """Loads the training data, generating mock data if the file is missing."""
    if not os.path.exists(DATA_FILE_PATH):
        print(f"File not found: {DATA_FILE_PATH}")
        return generate_mock_data()
    
    # If the file exists, load your real training data
    print(f"Loading data from {DATA_FILE_PATH}...")
    try:
        df = pd.read_csv(DATA_FILE_PATH)
        # Ensure all necessary columns are present, fill missing symptom columns with 0
        for col in SYMPTOM_FEATURES:
            if col not in df.columns:
                df[col] = 0
        return df
    except Exception as e:
        print(f"ERROR: Could not read CSV file. Generating mock data instead. Error: {e}")
        return generate_mock_data()


def train_and_save_model():
    """The main function to train and save the model."""
    df = load_data()

    # Define features (X) and target (y)
    # The list of features must be EXACTLY the same as in app.py
    X_features = ['age'] + SYMPTOM_FEATURES
    
    # Check if all required features are in the DataFrame
    missing_features = [col for col in X_features if col not in df.columns]
    if missing_features:
        print(f"CRITICAL ERROR: Missing features in your training data: {missing_features}")
        return

    X = df[X_features]
    y = df['disease']

    # 1. Split data (optional, but good practice)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training Random Forest Classifier...")
    
    # 2. Initialize and Train the Model (Random Forest is great for classification)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 3. Evaluate (optional)
    accuracy = model.score(X_test, y_test)
    print(f"Model Training Complete. Accuracy on test set: {accuracy:.2f}")

    # 4. Save the Model
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_FILE_PATH)
    print(f"Model successfully saved to {MODEL_FILE_PATH}")


if __name__ == '__main__':
    train_and_save_model()