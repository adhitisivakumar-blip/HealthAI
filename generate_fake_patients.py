import sqlite3
import random

conn = sqlite3.connect('healthcare.db')

cur = conn.cursor()

first_names = [

    "Aarav","Diya","Rahul","Sneha","Arjun",
    "Kavin","Meera","Aditya","Priya","Rohit",
    "Ananya","Vikram","Harini","Sanjay","Nisha",
    "Riya","Karthik","Abhishek","Varun","Pooja",
    "Akash","Neha","Manoj","Keerthi","Surya",
    "Divya","Sathish","Nandhini","Yash","Aishwarya"

]

last_names = [

    "Sharma","Kumar","Reddy","Iyer","Patel",
    "Singh","Verma","Nair","Menon","Kapoor",
    "Das","Joshi","Malhotra","Bhat","Chopra"

]

cities = [

    "Chennai","Bangalore","Mumbai","Delhi",
    "Hyderabad","Pune","Kolkata","Ahmedabad"

]

diseases = [

    "Diabetes",
    "Hypertension",
    "Heart Disease",
    "Allergy",
    "Asthma",
    "Depression",
    "Migraine",
    "Piles",
    "Arthritis",
    "PCOS",
    "Thyroid Disorder"

]

specialists = {

    "Diabetes":
    "Dr. Rajesh Nair - Endocrinologist",

    "Hypertension":
    "Dr. Kavya Sharma - Cardiologist",

    "Heart Disease":
    "Dr. Vikram Patel - Cardiac Surgeon",

    "Allergy":
    "Dr. Neha Kapoor - Allergy Specialist",

    "Asthma":
    "Dr. Arjun Menon - Pulmonologist",

    "Depression":
    "Dr. Priya Iyer - Psychiatrist",

    "Migraine":
    "Dr. Harish Kumar - Neurologist",

    "Piles":
    "Dr. Aditya Verma - Gastroenterologist",

    "Arthritis":
    "Dr. Sneha Das - Orthopedic Specialist",

    "PCOS":
    "Dr. Divya Reddy - Gynecologist",

    "Thyroid Disorder":
    "Dr. Meera Singh - Endocrinologist"

}

treatments = {

    "Diabetes":
    "AI-assisted insulin stabilization and glucose monitoring.",

    "Hypertension":
    "Cardiac pressure management and sodium control therapy.",

    "Heart Disease":
    "Advanced cardiovascular monitoring and cholesterol treatment.",

    "Allergy":
    "Antihistamine therapy and allergen prevention plan.",

    "Asthma":
    "Respiratory inhalation therapy and pulmonary monitoring.",

    "Depression":
    "Mental wellness counselling and behavioral therapy.",

    "Migraine":
    "Neurological pain management and trigger analysis.",

    "Piles":
    "Digestive care and colorectal treatment management.",

    "Arthritis":
    "Joint mobility therapy and inflammation reduction.",

    "PCOS":
    "Hormonal stabilization and gynecological monitoring.",

    "Thyroid Disorder":
    "Hormonal therapy and endocrine balancing."

}

diets = {

    "Diabetes":
    "Low sugar diabetic diet with high fiber intake.",

    "Hypertension":
    "Low sodium heart-protective diet.",

    "Heart Disease":
    "Omega-3 and low cholesterol nutrition.",

    "Allergy":
    "Allergen-free immunity boosting diet.",

    "Asthma":
    "Anti-inflammatory respiratory nutrition.",

    "Depression":
    "Mood-enhancing nutrition with omega-3.",

    "Migraine":
    "Caffeine-controlled neurological diet.",

    "Piles":
    "Fiber-rich digestive support diet.",

    "Arthritis":
    "Joint-support anti-inflammatory diet.",

    "PCOS":
    "Hormonal balance low-carb nutrition.",

    "Thyroid Disorder":
    "Iodine balanced endocrine nutrition."

}

risks = [

    "Low",
    "Moderate",
    "High",
    "Critical"

]

severities = [

    "Mild",
    "Moderate",
    "Severe"

]

genders = [

    "Male",
    "Female"

]

times = [

    "9:00 AM",
    "10:30 AM",
    "12:00 PM",
    "2:00 PM",
    "4:30 PM",
    "6:00 PM"

]

hospitals = [

    "Apollo Hospital",
    "Fortis Healthcare",
    "AIIMS",
    "Global Hospitals",
    "Manipal Hospital"

]

for i in range(300):

    full_name = (

        random.choice(first_names)
        + " " +
        random.choice(last_names)

    )

    disease = random.choice(diseases)

    severity = random.choice(severities)

    risk = random.choice(risks)

    age = random.randint(18,80)

    gender = random.choice(genders)

    city = random.choice(cities)

    hospital = random.choice(hospitals)

    appointment = (

        specialists[disease]
        + " | "
        + hospital
        + " | "
        + random.choice(times)

    )

    stress = random.choice([

        "Low Stress",
        "Moderate Stress",
        "High Stress"

    ])

    symptoms = (

        "fatigue, fever, body pain, dizziness"

    )

    cur.execute(

        '''

        INSERT INTO patient_records(

            patient_name,
            age,
            gender,
            disease,
            severity,
            treatment,
            risk,
            stress,
            diet,
            appointment,
            symptoms

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?)

        ''',

        (

            full_name + " (" + city + ")",

            age,
            gender,

            disease,
            severity,

            treatments[disease],

            risk,

            stress,

            diets[disease],

            appointment,

            symptoms

        )

    )

conn.commit()

conn.close()

print("300 Advanced Fake Patients Added Successfully")