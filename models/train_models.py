import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("Starting AI model training")

# Load our fake business data
print("Loading business data...")
df = pd.read_csv("data/indonesian_sme_data.csv")

print(f"Loaded {len(df)} businesses")

# Prepare the data for AI
print("Preparing data for AI...")

# Convert True/False to 1/0 for the AI to understand
df['has_instagram_num'] = df['has_instagram'].astype(int)
df['has_tokopedia_num'] = df['has_tokopedia'].astype(int)

# Create new features (these help the AI make better decisions)
df['revenue_to_loan_ratio'] = df['monthly_revenue'] / df['loan_amount_requested']
df['digital_presence_score'] = (
    df['has_instagram_num'] * 0.3 + 
    df['has_tokopedia_num'] * 0.3 + 
    (df['instagram_followers'] > 1000).astype(int) * 0.2 +
    (df['tokopedia_rating'] > 4.0).astype(int) * 0.2
)

# Select features (inputs) for our AI model
features = [
    'owner_age', 
    'years_in_business', 
    'employee_count',
    'has_instagram_num',
    'instagram_followers',
    'has_tokopedia_num', 
    'tokopedia_rating',
    'monthly_digital_payments',
    'monthly_revenue',
    'loan_amount_requested',
    'revenue_to_loan_ratio',
    'digital_presence_score'
]

# X = inputs (business information), y = output (loan approval decision)
X = df[features]
y = df['loan_approved']

print(f"Using {len(features)} features to predict loan approval")

# Split data: 80% for training AI, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} businesses")
print(f"Testing on {len(X_test)} businesses")

# Create and train the AI model
print("Training AI model")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test how well our AI performs
print("Testing AI performance")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"AI Accuracy: {accuracy:.1%}")
print(f"   This means the AI is correct {accuracy:.1%} of the time!")

# Show which features are most important for loan decisions
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nMost important factors for loan approval:")
for idx, row in feature_importance.head().iterrows():
    print(f"   {row['feature']}: {row['importance']:.1%}")

# Save the trained model
print("Saving AI model")
joblib.dump(model, 'models/loan_prediction_model.pkl')
joblib.dump(features, 'models/feature_names.pkl')

print("AI model training complete!")
print("Model saved as: models/loan_prediction_model.pkl")