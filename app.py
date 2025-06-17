import streamlit as st
import pandas as pd
import joblib


# # Constants
# MODEL_PATH = "models/model_xgboost.pkl"
# TRAIN_DATA_PATH = "data_student_preprocessed.csv"

# # Load model
# model = joblib.load(MODEL_PATH)

# Constants
MODEL_PATH = "models/model_xgboost.pkl"
ENCODER_PATH = "models/label_encoders.pkl"

# Load model dan encoder
model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODER_PATH)

# Daftar fitur yang digunakan oleh model (subset dari semua fitur input)
categorical_cols = [
    'MothersQualification', 'FathersQualification',
    'MothersOccupation', 'FathersOccupation',
]
numerical_cols = [
    'CurricularUnits1stSemCredited', 'CurricularUnits1stSemEnrolled',
    'CurricularUnits1stSemEvaluations', 'CurricularUnits1stSemApproved',
    'CurricularUnits1stSemGrade', 'CurricularUnits2ndSemCredited',
    'CurricularUnits2ndSemEnrolled', 'CurricularUnits2ndSemEvaluations',
    'CurricularUnits2ndSemApproved', 'CurricularUnits2ndSemGrade'
]

# Hanya fitur yang digunakan oleh model
model_features = categorical_cols + numerical_cols

st.set_page_config(page_title="Prediksi Drop Out", layout="wide")
st.title("🎓 Prediksi Drop Out Mahasiswa - Jaya Jaya Institut")

with st.form("input_form"):
    st.subheader("📋 Formulir Input Data Mahasiswa")
    input_dict = {}
    col1, col2 = st.columns(2)

    def load_options_from_readme(col_name):
        mapping = {
            'MaritalStatus': [
                ("Belum Menikah", 1), ("Menikah", 2), ("Duda/Janda", 3),
                ("Cerai", 4), ("Fakta Union", 5), ("Pisah Hukum", 6)
            ],
            'ApplicationMode': [
                ("1st phase - general contingent", 1), ("Ordinance No. 612/93", 2),
                ("Special contingent Azores", 5), ("Other higher courses", 7),
                ("Ordinance 854-B/99", 10), ("International student", 15),
                ("Special contingent Madeira", 16), ("2nd phase", 17),
                ("3rd phase", 18), ("Diff Plan", 26), ("Other Institution", 27),
                ("Over 23", 39), ("Transfer", 42), ("Change of course", 43),
                ("Tech spec diploma", 44), ("Change inst/course", 51),
                ("Short cycle", 53), ("Change inst/course Int", 57)
            ],
            'Course': [
                ("Biofuel", 33), ("Multimedia Design", 171), ("Social Service Eve", 8014),
                ("Agronomy", 9003), ("Design", 9070), ("Vet Nursing", 9085),
                ("IT Eng", 9119), ("Equinculture", 9130), ("Management", 9147),
                ("Social Service", 9238), ("Tourism", 9254), ("Nursing", 9500),
                ("Oral Hygiene", 9556), ("Marketing", 9670), ("Journalism", 9773),
                ("Basic Ed", 9853), ("Management Eve", 9991)
            ],
            'DaytimeEveningAttendance': [("Siang", 1), ("Malam", 0)],
            'PreviousQualification': [
                ("Secondary education", 1), ("Bachelor's", 2), ("Degree", 3),
                ("Master's", 4), ("Doctorate", 5), ("Freq HE", 6),
                ("12th not completed", 9), ("11th not completed", 10),
                ("Other 11th", 12), ("10th", 14), ("10th not completed", 15),
                ("Basic 3rd cycle", 19), ("Basic 2nd cycle", 38),
                ("Tech spec", 39), ("Degree 1st cycle", 40),
                ("Prof Tech", 42), ("Master 2nd cycle", 43)
            ],
            'Nationality': [
                ("Portugal", 1), ("German", 2), ("Spanish", 6), ("Italian", 11),
                ("Dutch", 13), ("English", 14), ("Lithuanian", 17), ("Angolan", 21),
                ("Cape Verdean", 22), ("Guinean", 24), ("Mozambican", 25),
                ("Santomean", 26), ("Turkish", 32), ("Brazilian", 41),
                ("Romanian", 62), ("Moldova", 100), ("Mexican", 101),
                ("Ukrainian", 103), ("Russian", 105), ("Cuban", 108),
                ("Colombian", 109)
            ],
            'Displaced': [("Ya", 1), ("Tidak", 0)],
            'EducationalSpecialNeeds': [("Ya", 1), ("Tidak", 0)],
            'Debtor': [("Ya", 1), ("Tidak", 0)],
            'TuitionFeesUpToDate': [("Ya", 1), ("Tidak", 0)],
            'Gender': [("Laki-laki", 1), ("Perempuan", 0)],
            'ScholarshipHolder': [("Ya", 1), ("Tidak", 0)],
            'International': [("Ya", 1), ("Tidak", 0)],
        }
        return mapping.get(col_name, [])

    # Input untuk fitur yang digunakan model
    with col1:
        input_dict['MaritalStatus'] = st.selectbox(
            "Status Pernikahan",
            load_options_from_readme('MaritalStatus'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['ApplicationMode'] = st.selectbox(
            "Jalur Pendaftaran",
            load_options_from_readme('ApplicationMode'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['ApplicationOrder'] = st.slider("Urutan Pilihan (0-9)", 0, 9, 0)
        input_dict['Course'] = st.selectbox(
            "Program Studi",
            load_options_from_readme('Course'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['DaytimeEveningAttendance'] = st.radio(
            "Waktu Kuliah",
            load_options_from_readme('DaytimeEveningAttendance'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['PreviousQualification'] = st.selectbox(
            "Kualifikasi Sebelumnya",
            load_options_from_readme('PreviousQualification'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['PreviousQualificationGrade'] = st.number_input(
            "Nilai Kualifikasi Sebelumnya (0-200)", 0.0, 200.0, 160.0
        )
        input_dict['Nationality'] = st.selectbox(
            "Kewarganegaraan",
            load_options_from_readme('Nationality'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['MothersQualification'] = st.number_input(
            "Kode Pendidikan Ibu (1-44)", 1, 44, 1
        )
        input_dict['FathersQualification'] = st.number_input(
            "Kode Pendidikan Ayah (1-44)", 1, 44, 1
        )
        input_dict['MothersOccupation'] = st.number_input(
            "Kode Pekerjaan Ibu (0-194)", 0, 194, 0
        )
        input_dict['FathersOccupation'] = st.number_input(
            "Kode Pekerjaan Ayah (0-195)", 0, 195, 0
        )

    with col2:
        input_dict['Displaced'] = st.radio(
            "Apakah Terdampak (Displaced)?",
            load_options_from_readme('Displaced'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['EducationalSpecialNeeds'] = st.radio(
            "Kebutuhan Khusus?",
            load_options_from_readme('EducationalSpecialNeeds'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['Debtor'] = st.radio(
            "Memiliki Tunggakan?",
            load_options_from_readme('Debtor'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['TuitionFeesUpToDate'] = st.radio(
            "Bayar Kuliah Lancar?",
            load_options_from_readme('TuitionFeesUpToDate'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['Gender'] = st.radio(
            "Jenis Kelamin",
            load_options_from_readme('Gender'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['ScholarshipHolder'] = st.radio(
            "Penerima Beasiswa?",
            load_options_from_readme('ScholarshipHolder'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['International'] = st.radio(
            "Mahasiswa Internasional?",
            load_options_from_readme('International'),
            format_func=lambda x: x[0]
        )[1]
        input_dict['AgeAtEnrollment'] = st.slider("Usia Saat Masuk", 15, 60, 19)

    st.subheader("📘 Info Akademik dan Ekonomi")
    for k, label, minv, maxv, default in [
        ('CurricularUnits1stSemCredited', "Smt 1 Diakui", 0, 20, 1),
        ('CurricularUnits1stSemEnrolled', "Smt 1 Diambil", 0, 20, 6),
        ('CurricularUnits1stSemEvaluations', "Smt 1 Evaluasi", 0, 20, 6),
        ('CurricularUnits1stSemApproved', "Smt 1 Lulus", 0, 20, 6),
        ('CurricularUnits1stSemGrade', "Nilai Rata-rata Smt 1", 0.0, 20.0, 14.0),
        ('CurricularUnits1stSemWithoutEvaluations', "Smt 1 Tanpa Evaluasi", 0, 20, 0),
        ('CurricularUnits2ndSemCredited', "Smt 2 Diakui", 0, 20, 0),
        ('CurricularUnits2ndSemEnrolled', "Smt 2 Diambil", 0, 20, 6),
        ('CurricularUnits2ndSemEvaluations', "Smt 2 Evaluasi", 0, 20, 6),
        ('CurricularUnits2ndSemApproved', "Smt 2 Lulus", 0, 20, 6),
        ('CurricularUnits2ndSemGrade', "Nilai Rata-rata Smt 2", 0.0, 20.0, 13.67),
        ('CurricularUnits2ndSemWithoutEvaluations', "Smt 2 Tanpa Evaluasi", 0, 20, 0),
        ('UnemploymentRate', "Pengangguran (%)", 0.0, 100.0, 13.9),
        ('InflationRate', "Inflasi (%)", -10.0, 20.0, -0.3),
        ('GDP', "Pertumbuhan GDP (%)", -10.0, 10.0, 0.79),
        ('AdmissionGrade', "Nilai Ujian Masuk", 0.0, 200.0, 150.0)
    ]:
        input_dict[k] = st.number_input(label, min_value=minv, max_value=maxv,
                                        value=default, key=k)

    submitted = st.form_submit_button("🔍 Prediksi Drop Out")

# Prediction
if submitted:
    st.subheader("📊 Hasil Prediksi")
    input_df = pd.DataFrame([input_dict])

    # print("input_df.columns:", input_df.columns.tolist())
    # print("model_features:", model_features)
    # Filter hanya kolom yang dipakai model
    input_df = input_df[model_features].copy()

    # Transformasi kolom kategorikal
    for col in categorical_cols:
        input_df[col] = encoders[col].transform(input_df[col].astype(str))

    # # Baca dataset pelatihan untuk acuan struktur kolom
    # df_train = pd.read_csv(TRAIN_DATA_PATH)
    # df_encoded = pd.get_dummies(df_train[model_features], columns=categorical_cols, drop_first=True)

    # # Encoding input user
    # input_encoded = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)
    # for col in df_encoded.columns:
    #     if col not in input_encoded.columns:
    #         input_encoded[col] = 0
    # input_encoded = input_encoded[df_encoded.columns]

    # Prediksi
    pred_proba = model.predict_proba(input_df)
    pred = model.predict(input_df)
    status = {0: "Tidak Drop Out", 1: "Drop Out"}.get(pred[0], "Unknown")

    st.success(f"✅ Prediksi: {status}")
    st.info(f"Probabilitas Drop Out: {pred_proba[0][1]*100:.2f}%")

# Gaya CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://slidechef.net/wp-content/uploads/2023/10/Free-Simple-White-Background.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
