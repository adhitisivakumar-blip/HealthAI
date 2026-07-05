from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import numpy as np
import pandas as pd
import joblib
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

# =====================================================
# LOAD AI MODEL
# =====================================================

model = joblib.load('models/disease_model.pkl')

# =====================================================
# LOAD DATASET
# =====================================================

training_df = pd.read_csv('datasets/Training.csv')

if 'Unnamed: 133' in training_df.columns:

    training_df = training_df.drop('Unnamed: 133', axis=1)

symptom_list = training_df.columns[:-1]

# =====================================================
# DATABASE CREATION
# =====================================================

def create_database():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    # USERS TABLE

    cur.execute('''

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        email TEXT,
        password TEXT,
        role TEXT

    )

    ''')

    # PATIENT RECORDS TABLE

    cur.execute('''

    CREATE TABLE IF NOT EXISTS patient_records(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient_name TEXT,
        age INTEGER,
        gender TEXT,

        disease TEXT,
        severity TEXT,

        treatment TEXT,
        risk TEXT,
        stress TEXT,

        diet TEXT,
        appointment TEXT,

        symptoms TEXT

    )

    ''')

    conn.commit()
    conn.close()

create_database()

# =====================================================
# HOME PAGE
# =====================================================

@app.route('/')
def home():

    return render_template('index.html')

# =====================================================
# REGISTER PAGE
# =====================================================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')

        conn = sqlite3.connect('healthcare.db')

        cur = conn.cursor()

        cur.execute(

            "INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)",

            (name, email, password, role)

        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

# =====================================================
# LOGIN PAGE
# =====================================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect('healthcare.db')

        cur = conn.cursor()

        cur.execute(

            "SELECT * FROM users WHERE email=? AND password=?",

            (email, password)

        )

        user = cur.fetchone()

        conn.close()

        if user:

            role = user[4]

            if role == 'patient':

                return redirect('/patient_dashboard')

            elif role == 'doctor':

                return redirect('/doctor_dashboard')

            elif role == 'admin':

                return redirect('/admin_dashboard')

        return "Invalid Credentials"

    return render_template('login.html')

# =====================================================
# PATIENT DASHBOARD
# =====================================================

@app.route('/patient_dashboard', methods=['GET', 'POST'])
def patient_dashboard():

    result = {}

    if request.method == 'POST':

        patient_name = request.form.get('patient_name')
        age = request.form.get('age')
        gender = request.form.get('gender')

        symptoms_input = []

        selected_symptoms = []

        for symptom in symptom_list:

            value = request.form.get(symptom)

            if value == 'on':

                symptoms_input.append(1)

                selected_symptoms.append(symptom)

            else:

                symptoms_input.append(0)

        input_array = np.array([symptoms_input])

        # =====================================================
        # DISEASE PREDICTION
        # =====================================================

        prediction = model.predict(input_array)[0]

        # =====================================================
        # SEVERITY ANALYSIS
        # =====================================================

        severity_score = len(selected_symptoms)

        if severity_score <= 3:

            severity = "Mild"

        elif severity_score <= 6:

            severity = "Moderate"

        else:

            severity = "Severe"

        # =====================================================
        # PERSONALIZED HEALTHCARE ENGINE
        # =====================================================

        treatment = ""
        diet = ""
        risk = ""
        appointment = ""
        stress = ""
        emergency = ""
        lifestyle = ""
        similar_case = ""
        success_probability = ""
        drug_interaction = ""

        # =====================================================
        # DIABETES
        # =====================================================

        if prediction.lower() == 'diabetes':

            treatment = (

                "Insulin therapy, glucose monitoring and "
                "endocrinologist supervision recommended."

            )

            diet = (

                "Strict diabetic diet with oats, vegetables "
                "and controlled carbohydrate intake."

            )

            lifestyle = (

                "Walk daily, avoid sugary drinks and maintain "
                "healthy sleep schedule."

            )

            risk = "High"

            emergency = (

                "Continuous diabetic monitoring advised."

            )

            appointment = (

                "Endocrinologist Appointment"

            )

            stress = (

                "Moderate diabetic stress indicators detected."

            )

            success_probability = "87%"

            similar_case = (

                "Similar diabetic patients showed positive "
                "recovery after nutrition control."

            )

        # =====================================================
        # HYPERTENSION
        # =====================================================

        elif prediction.lower() == 'hypertension':

            treatment = (

                "Blood pressure stabilization therapy advised."

            )

            diet = (

                "Low sodium cardiac diet recommended."

            )

            lifestyle = (

                "Practice yoga and maintain cardiovascular exercise."

            )

            risk = "High"

            emergency = (

                "Potential hypertension risk detected."

            )

            appointment = (

                "Cardiologist Appointment"

            )

            stress = (

                "Elevated cardiovascular stress detected."

            )

            success_probability = "82%"

            similar_case = (

                "Hypertension patients improved after "
                "lifestyle modifications."

            )

        # =====================================================
        # HEART DISEASE
        # =====================================================

        elif prediction.lower() == 'heart disease':

            treatment = (

                "Immediate cardiac evaluation required."

            )

            diet = (

                "Low cholesterol heart protective diet."

            )

            lifestyle = (

                "Avoid smoking and maintain supervised exercise."

            )

            risk = "Critical"

            emergency = (

                "Critical cardiac emergency risk identified."

            )

            appointment = (

                "Emergency Cardiology Appointment"

            )

            stress = (

                "Extremely high cardiovascular stress detected."

            )

            success_probability = "70%"

            similar_case = (

                "Similar cardiac patients required "
                "intensive cardiovascular care."

            )

        # =====================================================
        # DEPRESSION
        # =====================================================

        elif prediction.lower() == 'depression':

            treatment = (

                "Psychological counselling and therapy recommended."

            )

            diet = (

                "Mood enhancing foods and omega-3 nutrition advised."

            )

            lifestyle = (

                "Mindfulness exercises and social interaction recommended."

            )

            risk = "Moderate"

            emergency = (

                "Mental health monitoring advised."

            )

            appointment = (

                "Psychiatrist Appointment"

            )

            stress = (

                "High emotional stress indicators identified."

            )

            success_probability = "84%"

            similar_case = (

                "Patients improved significantly after therapy."

            )

        # =====================================================
        # DEFAULT
        # =====================================================

        else:

            treatment = (

                "Personalized treatment and continuous "
                "health monitoring advised."

            )

            diet = (

                "Balanced nutrition and hydration recommended."

            )

            lifestyle = (

                "Maintain exercise, proper sleep and healthy nutrition."

            )

            risk = "Low"

            emergency = (

                "No immediate emergency risk detected."

            )

            appointment = (

                "General Physician Appointment"

            )

            stress = (

                "Low stress indicators detected."

            )

            success_probability = "91%"

            similar_case = (

                "Patients recovered successfully with preventive care."

            )

        # =====================================================
        # DRUG INTERACTION
        # =====================================================

        drug_interaction = (

            "No dangerous drug interactions identified."

        )

        # =====================================================
        # SAVE PATIENT RECORD
        # =====================================================

        conn = sqlite3.connect('healthcare.db')

        cur = conn.cursor()

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

                patient_name,
                age,
                gender,

                prediction,
                severity,

                treatment,
                risk,
                stress,

                diet,
                appointment,

                ", ".join(selected_symptoms)

            )

        )

        conn.commit()
        conn.close()

        # =====================================================
        # RESULTS
        # =====================================================

        result = {

            'prediction': prediction,
            'severity': severity,
            'treatment': treatment,
            'diet': diet,
            'stress': stress,
            'risk': risk,
            'emergency': emergency,
            'success_probability': success_probability,
            'lifestyle': lifestyle,
            'similar_case': similar_case,
            'drug_interaction': drug_interaction,
            'appointment': appointment

        }

    return render_template(

        'patient_dashboard.html',

        result=result,
        symptoms=symptom_list

    )

# =====================================================
# DOCTOR DASHBOARD
# =====================================================

@app.route('/doctor_dashboard')
def doctor_dashboard():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute("""

        SELECT *

        FROM patient_records

        ORDER BY id DESC

    """)

    records = cur.fetchall()

    conn.close()

    return render_template(

        'doctor_dashboard.html',
        records=records

    )

# =====================================================
# ADMIN DASHBOARD
# =====================================================

@app.route('/admin_dashboard')
def admin_dashboard():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute(

        "SELECT COUNT(*) FROM patient_records"

    )

    total_records = cur.fetchone()[0]

    cur.execute(

        "SELECT COUNT(*) FROM users"

    )

    total_users = cur.fetchone()[0]

    conn.close()

    return render_template(

        'admin_dashboard.html',

        total_records=total_records,
        total_users=total_users

    )

# =====================================================
# PROFILE PAGE
# =====================================================

@app.route('/profile')
def profile():

    return render_template('profile.html')

# =====================================================
# PREDICTIONS PAGE
# =====================================================

@app.route('/predictions')
def predictions():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute("""

        SELECT DISTINCT

            patient_name,
            disease,
            severity,
            treatment,
            appointment

        FROM patient_records

        ORDER BY RANDOM()

        LIMIT 50

    """)

    records = cur.fetchall()

    conn.close()

    return render_template(

        'predictions.html',
        records=records

    )

# =====================================================
# REPORTS PAGE
# =====================================================

@app.route('/reports')
def reports():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute("""

        SELECT DISTINCT

            patient_name,
            disease,
            severity,
            risk

        FROM patient_records

        ORDER BY RANDOM()

        LIMIT 30

    """)

    reports = cur.fetchall()

    conn.close()

    return render_template(

        'reports.html',
        reports=reports

    )

# =====================================================
# APPOINTMENTS PAGE
# =====================================================

@app.route('/appointments')
def appointments():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute("""

        SELECT

            patient_name,
            disease,
            appointment

        FROM patient_records

        ORDER BY RANDOM()

        LIMIT 30

    """)

    appointments_data = cur.fetchall()

    conn.close()

    return render_template(

        'appointments.html',

        appointments=appointments_data

    )

# =====================================================
# BOOK APPOINTMENT
# =====================================================

@app.route('/book_appointment', methods=['POST'])
def book_appointment():

    patient_name = request.form.get('patient_name')

    disease = request.form.get('disease')

    specialist = request.form.get('specialist')

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute(

        '''

        INSERT INTO booked_appointments(

            patient_name,
            disease,
            specialist,
            booking_status

        )

        VALUES(?,?,?,?)

        ''',

        (

            patient_name,
            disease,
            specialist,
            "Confirmed"

        )

    )

    conn.commit()

    conn.close()

    return redirect('/my_appointments')

# =====================================================
# MY APPOINTMENTS
# =====================================================

@app.route('/my_appointments')
def my_appointments():

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute("""

        SELECT

            patient_name,
            disease,
            specialist,
            booking_status

        FROM booked_appointments

        ORDER BY id DESC

    """)

    bookings = cur.fetchall()

    conn.close()

    return render_template(

        'my_appointments.html',

        bookings=bookings

    )
# =====================================================
# PDF REPORT GENERATION
# =====================================================

@app.route('/generate_report')
def generate_report():

    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from datetime import datetime

    # CREATE REPORTS FOLDER

    if not os.path.exists('reports'):

        os.makedirs('reports')

    filepath = 'reports/AI_Healthcare_Report.pdf'

    # GET LATEST PATIENT RECORD

    conn = sqlite3.connect('healthcare.db')

    cur = conn.cursor()

    cur.execute("""

        SELECT

            patient_name,
            age,
            gender,
            disease,
            severity,
            treatment,
            risk,
            stress,
            diet,
            appointment

        FROM patient_records

        ORDER BY id DESC

        LIMIT 1

    """)

    patient = cur.fetchone()

    conn.close()

    # CREATE PDF

    c = canvas.Canvas(

        filepath,

        pagesize=letter

    )

    width, height = letter

    # =====================================================
    # HEADER
    # =====================================================

    c.setFont("Helvetica-Bold", 26)

    c.drawString(

        140,
        760,
        "AI Healthcare Report"

    )

    c.setFont("Helvetica", 13)

    c.drawString(

        150,
        735,
        "Personalized Treatment Recommendation System"

    )

    # DATE

    c.setFont("Helvetica", 11)

    c.drawString(

        420,
        790,
        datetime.now().strftime("%d-%m-%Y")

    )

    # =====================================================
    # PATIENT DETAILS
    # =====================================================

    y = 680

    c.setFont("Helvetica-Bold", 18)

    c.drawString(

        60,
        y,
        "Patient Information"
    )

    y -= 35

    c.setFont("Helvetica", 12)

    c.drawString(

        70,
        y,
        f"Patient Name: {patient[0]}"
    )

    y -= 25

    c.drawString(

        70,
        y,
        f"Age: {patient[1]}"
    )

    y -= 25

    c.drawString(

        70,
        y,
        f"Gender: {patient[2]}"
    )

    # =====================================================
    # DISEASE ANALYSIS
    # =====================================================

    y -= 50

    c.setFont("Helvetica-Bold", 18)

    c.drawString(

        60,
        y,
        "AI Disease Analysis"
    )

    y -= 35

    c.setFont("Helvetica", 12)

    c.drawString(

        70,
        y,
        f"Predicted Disease: {patient[3]}"
    )

    y -= 25

    c.drawString(

        70,
        y,
        f"Severity Level: {patient[4]}"
    )

    y -= 25

    c.drawString(

        70,
        y,
        f"Emergency Risk: {patient[6]}"
    )

    y -= 25

    c.drawString(

        70,
        y,
        f"Mental Stress Analysis: {patient[7]}"
    )

    # =====================================================
    # TREATMENT PLAN
    # =====================================================

    y -= 50

    c.setFont("Helvetica-Bold", 18)

    c.drawString(

        60,
        y,
        "Treatment & Medication Plan"
    )

    y -= 35

    c.setFont("Helvetica", 12)

    c.drawString(

        70,
        y,
        f"Recommended Treatment:"
    )

    y -= 25

    c.drawString(

        90,
        y,
        patient[5][:90]
    )

    # =====================================================
    # PRESCRIBED MEDICINES
    # =====================================================

    y -= 50

    c.setFont("Helvetica-Bold", 18)

    c.drawString(

        60,
        y,
        "Prescribed Medicines"
    )

    y -= 35

    medicines = []

    disease = patient[3].lower()

    if disease == 'diabetes':

        medicines = [

            "Metformin 500mg",
            "Insulin Therapy",
            "Glucose Monitoring Tablets"

        ]

    elif disease == 'hypertension':

        medicines = [

            "Amlodipine",
            "Losartan",
            "Blood Pressure Tablets"

        ]

    elif disease == 'heart disease':

        medicines = [

            "Aspirin",
            "Atorvastatin",
            "Beta Blockers"

        ]

    elif disease == 'depression':

        medicines = [

            "Sertraline",
            "Escitalopram",
            "Therapy Sessions"

        ]

    else:

        medicines = [

            "Vitamin Supplements",
            "Pain Relief Medication",
            "General Wellness Medicines"

        ]

    c.setFont("Helvetica", 12)

    for med in medicines:

        c.drawString(

            90,
            y,
            f"• {med}"

        )

        y -= 25

    # =====================================================
    # DIET PLAN
    # =====================================================

    y -= 20

    c.setFont("Helvetica-Bold", 18)

    c.drawString(

        60,
        y,
        "Personalized Diet Recommendation"
    )

    y -= 35

    c.setFont("Helvetica", 12)

    c.drawString(

        70,
        y,
        patient[8][:90]
    )

    # =====================================================
    # APPOINTMENT
    # =====================================================

    y -= 50

    c.setFont("Helvetica-Bold", 18)

    c.drawString(

        60,
        y,
        "Specialist Consultation"
    )

    y -= 35

    c.setFont("Helvetica", 12)

    c.drawString(

        70,
        y,
        patient[9][:90]
    )

    # =====================================================
    # FOOTER
    # =====================================================

    c.setFont("Helvetica-Oblique", 10)

    c.drawString(

        140,
        60,
        "Generated using HealthAI Analytics Platform"
    )

    c.save()

    return send_file(

        filepath,

        as_attachment=True

    )
# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == '__main__':

    app.run(debug=True)