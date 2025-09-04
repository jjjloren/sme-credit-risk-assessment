import pandas as pd
import numpy as np
import random

# Set random seed for reproducible results
np.random.seed(42)
random.seed(42)

print("Starting to create fake business data...")

# Indonesian business types
business_types = [
    "Warung Makan", "Toko Kelontong", "Salon Kecantikan", 
    "Bengkel Motor", "Toko Pakaian", "Jasa Laundry",
    "Kafe", "Toko Elektronik", "Jasa Fotocopy", "Apotek"
]

# Indonesian cities
cities = [
    "Jakarta", "Surabaya", "Bandung", "Medan", "Bekasi",
    "Tangerang", "Depok", "Semarang", "Palembang", "Makassar"
]

# Create 1000 fake businesses
businesses = []

for i in range(1000):
    # Random business info
    business = {
        "business_id": i + 1,
        "business_name": f"Usaha {random.choice(['Berkah', 'Sejahtera', 'Maju', 'Sukses'])} {i+1}",
        "business_type": random.choice(business_types),
        "city": random.choice(cities),
        "owner_age": random.randint(25, 65),
        "years_in_business": random.randint(1, 15),
        "employee_count": random.randint(1, 50),
        
        # Digital presence (some businesses are more digital than others)
        "has_instagram": random.choice([True, False]),
        "instagram_followers": random.randint(0, 10000) if random.choice([True, False]) else 0,
        "has_tokopedia": random.choice([True, False]),
        "tokopedia_rating": round(random.uniform(3.0, 5.0), 1) if random.choice([True, False]) else 0,
        "monthly_digital_payments": random.randint(0, 500),
        
        # Financial info
        "monthly_revenue": random.randint(5000000, 100000000),  # 5 juta to 100 juta rupiah
        "loan_amount_requested": random.randint(10000000, 200000000),  # 10 juta to 200 juta
    }
    
    # Determine if loan should be approved (our target variable)
    # Better digital presence + longer in business = higher chance of approval
    approval_score = 0
    
    if business["years_in_business"] > 3:
        approval_score += 0.3
    if business["has_instagram"] and business["instagram_followers"] > 1000:
        approval_score += 0.2
    if business["has_tokopedia"] and business["tokopedia_rating"] > 4.0:
        approval_score += 0.2
    if business["monthly_digital_payments"] > 100:
        approval_score += 0.1
    if business["monthly_revenue"] > business["loan_amount_requested"] * 0.1:  # Can pay back in 10 months
        approval_score += 0.2
    
    # Add some randomness
    approval_score += random.uniform(-0.1, 0.1)
    
    business["loan_approved"] = approval_score > 0.5
    
    businesses.append(business)

# Convert to DataFrame (like Excel spreadsheet)
df = pd.DataFrame(businesses)

# Save to CSV file
df.to_csv("data/indonesian_sme_data.csv", index=False)

print(f"Created data for {len(businesses)} Indonesian businesses!")
print(f"Loan approval rate: {df['loan_approved'].mean():.1%}")
print("Data saved to: data/indonesian_sme_data.csv")

# Show first few rows
print("\nFirst 5 businesses:")
print(df.head())