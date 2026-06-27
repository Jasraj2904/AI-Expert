# ==========================================================
# SENTINEL AI - DISASTER RISK PREDICTION SYSTEM
# GUI VERSION
# PART 1
# ==========================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

import random
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from datetime import datetime

# ==========================================================
# MAIN WINDOW
# ==========================================================

root = tk.Tk()

root.title("🌍 Sentinel AI - Disaster Risk Prediction System")

root.geometry("1200x800")

root.minsize(1000,700)

root.configure(bg="#0B132B")

# ==========================================================
# STYLE
# ==========================================================

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TProgressbar",
    thickness=30
)

style.configure(
    "Blue.TButton",
    font=("Segoe UI",11,"bold"),
    padding=10
)

style.configure(
    "Green.TButton",
    font=("Segoe UI",11,"bold"),
    padding=10
)

style.configure(
    "Red.TButton",
    font=("Segoe UI",11,"bold"),
    padding=10
)

# ==========================================================
# DATASET GENERATION
# ==========================================================

def generate_dataset(records=1500):

    data=[]

    for _ in range(records):

        temperature=random.randint(15,50)
        rainfall=random.randint(0,300)
        humidity=random.randint(20,100)
        wind=random.randint(0,120)

        score=(
            rainfall*0.40+
            humidity*0.25+
            wind*0.25+
            temperature*0.10
        )

        if score<80:
            risk=0

        elif score<140:
            risk=1

        else:
            risk=2

        data.append([
            temperature,
            rainfall,
            humidity,
            wind,
            risk
        ])

    return pd.DataFrame(
        data,
        columns=[
            "Temperature",
            "Rainfall",
            "Humidity",
            "WindSpeed",
            "Risk"
        ]
    )

# ==========================================================
# CREATE DATASET
# ==========================================================

dataset=generate_dataset()

X=dataset[
[
"Temperature",
"Rainfall",
"Humidity",
"WindSpeed"
]
]

y=dataset["Risk"]

# ==========================================================
# SPLIT DATA
# ==========================================================

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================================================
# TRAIN MODEL
# ==========================================================

model=RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

prediction=model.predict(X_test)

accuracy=accuracy_score(
    y_test,
    prediction
)

feature_importance=model.feature_importances_

features=[
    "Temperature",
    "Rainfall",
    "Humidity",
    "Wind Speed"
]

# ==========================================================
# COLORS
# ==========================================================

BG="#0B132B"

CARD="#1C2541"

BLUE="#3A86FF"

GREEN="#06D6A0"

RED="#EF476F"

YELLOW="#FFD166"

WHITE="white"

# ==========================================================
# HEADER
# ==========================================================

header=tk.Frame(
    root,
    bg=BLUE,
    height=90
)

header.pack(fill="x")

title=tk.Label(
    header,
    text="🌍 SENTINEL AI - DISASTER RISK PREDICTION SYSTEM",
    bg=BLUE,
    fg="white",
    font=("Segoe UI",24,"bold")
)

title.pack(pady=10)

subtitle=tk.Label(
    header,
    text="Artificial Intelligence Based Weather Disaster Predictor",
    bg=BLUE,
    fg="white",
    font=("Segoe UI",11)
)

subtitle.pack()

# ==========================================================
# CLOCK
# ==========================================================

clock=tk.Label(
    header,
    bg=BLUE,
    fg="white",
    font=("Consolas",11,"bold")
)

clock.place(relx=0.98,rely=0.1,anchor="ne")

def update_clock():

    current=datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

    clock.config(text=current)

    root.after(
        1000,
        update_clock
    )

update_clock()

# ==========================================================
# MAIN FRAME
# ==========================================================

main=tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# ==========================================================
# LEFT PANEL
# ==========================================================

left=tk.Frame(
    main,
    bg=CARD,
    width=350
)

left.pack(
    side="left",
    fill="y",
    padx=(0,15)
)

left.pack_propagate(False)

# ==========================================================
# RIGHT PANEL
# ==========================================================

right=tk.Frame(
    main,
    bg=CARD
)

right.pack(
    side="right",
    fill="both",
    expand=True
)

# ==========================================================
# INPUT TITLE
# ==========================================================

input_title=tk.Label(
    left,
    text="Weather Inputs",
    bg=CARD,
    fg="white",
    font=("Segoe UI",18,"bold")
)

input_title.pack(
    pady=20
)

# ==========================================================
# INPUT LABELS
# ==========================================================

def make_label(text):

    lbl=tk.Label(
        left,
        text=text,
        bg=CARD,
        fg="white",
        anchor="w",
        font=("Segoe UI",11)
    )

    lbl.pack(
        fill="x",
        padx=20,
        pady=(10,2)
    )

# ==========================================================
# INPUT ENTRIES
# ==========================================================

def make_entry():

    entry=tk.Entry(
        left,
        font=("Segoe UI",12),
        relief="flat"
    )

    entry.pack(
        fill="x",
        padx=20,
        ipady=8
    )

    return entry

make_label("🌡 Temperature (°C)")
temp_entry=make_entry()

make_label("🌧 Rainfall (mm)")
rain_entry=make_entry()

make_label("💧 Humidity (%)")
humidity_entry=make_entry()

make_label("🌪 Wind Speed (km/h)")
wind_entry=make_entry()

# ==========================================================
# BUTTON FRAME
# ==========================================================

button_frame=tk.Frame(
    left,
    bg=CARD
)

button_frame.pack(
    pady=25
)
# ==========================================================
# BUTTONS
# ==========================================================

predict_btn = ttk.Button(
    button_frame,
    text="🔍 Predict Risk",
    style="Blue.TButton"
)

predict_btn.grid(row=0, column=0, padx=5, pady=5)

graph_btn = ttk.Button(
    button_frame,
    text="📊 Show Graph",
    style="Green.TButton"
)

graph_btn.grid(row=0, column=1, padx=5, pady=5)

report_btn = ttk.Button(
    button_frame,
    text="💾 Save Report",
    style="Green.TButton"
)

report_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = ttk.Button(
    button_frame,
    text="🗑 Clear",
    style="Red.TButton"
)

clear_btn.grid(row=1, column=1, padx=5, pady=5)

exit_btn = ttk.Button(
    left,
    text="❌ Exit",
    style="Red.TButton",
    command=root.destroy
)

exit_btn.pack(
    fill="x",
    padx=20,
    pady=10
)

# ==========================================================
# RESULT TITLE
# ==========================================================

result_title = tk.Label(
    right,
    text="AI Prediction Dashboard",
    bg=CARD,
    fg="white",
    font=("Segoe UI",22,"bold")
)

result_title.pack(pady=20)

# ==========================================================
# RESULT CARDS
# ==========================================================

cards = tk.Frame(
    right,
    bg=CARD
)

cards.pack(fill="x", padx=20)

# ----------------------------------------------------------

card1 = tk.Frame(
    cards,
    bg="#243B55",
    width=220,
    height=110
)

card1.grid(row=0,column=0,padx=10)

card1.pack_propagate(False)

tk.Label(
    card1,
    text="Risk Level",
    bg="#243B55",
    fg="white",
    font=("Segoe UI",12)
).pack(pady=(10,0))

risk_label=tk.Label(
    card1,
    text="---",
    bg="#243B55",
    fg=GREEN,
    font=("Segoe UI",20,"bold")
)

risk_label.pack()

# ----------------------------------------------------------

card2=tk.Frame(
    cards,
    bg="#243B55",
    width=220,
    height=110
)

card2.grid(row=0,column=1,padx=10)

card2.pack_propagate(False)

tk.Label(
    card2,
    text="Confidence",
    bg="#243B55",
    fg="white",
    font=("Segoe UI",12)
).pack(pady=(10,0))

confidence_label=tk.Label(
    card2,
    text="0%",
    bg="#243B55",
    fg=YELLOW,
    font=("Segoe UI",20,"bold")
)

confidence_label.pack()

# ----------------------------------------------------------

card3=tk.Frame(
    cards,
    bg="#243B55",
    width=220,
    height=110
)

card3.grid(row=0,column=2,padx=10)

card3.pack_propagate(False)

tk.Label(
    card3,
    text="Weather Score",
    bg="#243B55",
    fg="white",
    font=("Segoe UI",12)
).pack(pady=(10,0))

score_label=tk.Label(
    card3,
    text="0 /100",
    bg="#243B55",
    fg=BLUE,
    font=("Segoe UI",20,"bold")
)

score_label.pack()

# ==========================================================
# DISASTER CARD
# ==========================================================

disaster_frame=tk.Frame(
    right,
    bg="#243B55"
)

disaster_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

tk.Label(
    disaster_frame,
    text="Most Probable Disaster",
    bg="#243B55",
    fg="white",
    font=("Segoe UI",15,"bold")
).pack(pady=(10,0))

disaster_label=tk.Label(
    disaster_frame,
    text="Waiting for Prediction...",
    bg="#243B55",
    fg=YELLOW,
    font=("Segoe UI",18,"bold")
)

disaster_label.pack(pady=15)

# ==========================================================
# RISK METER
# ==========================================================

meter_frame=tk.Frame(
    right,
    bg=CARD
)

meter_frame.pack(
    fill="x",
    padx=20
)

tk.Label(
    meter_frame,
    text="Overall Disaster Risk",
    bg=CARD,
    fg="white",
    font=("Segoe UI",14,"bold")
).pack(anchor="w")

progress=ttk.Progressbar(
    meter_frame,
    orient="horizontal",
    length=700,
    mode="determinate",
    maximum=100
)

progress.pack(
    fill="x",
    pady=10
)

meter_value=tk.Label(
    meter_frame,
    text="0%",
    bg=CARD,
    fg="white",
    font=("Segoe UI",11)
)

meter_value.pack(anchor="e")

# ==========================================================
# SAFETY RECOMMENDATIONS
# ==========================================================

recommend_frame=tk.Frame(
    right,
    bg=CARD
)

recommend_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

tk.Label(
    recommend_frame,
    text="Safety Recommendations",
    bg=CARD,
    fg="white",
    font=("Segoe UI",16,"bold")
).pack(anchor="w")

recommend_box=ScrolledText(
    recommend_frame,
    height=10,
    font=("Consolas",11),
    bg="#101820",
    fg="#00FFAA",
    relief="flat"
)

recommend_box.pack(
    fill="both",
    expand=True,
    pady=10
)

recommend_box.insert(
    "end",
    "Waiting for AI prediction..."
)

recommend_box.config(
    state="disabled"
)

# ==========================================================
# STATUS BAR
# ==========================================================

status=tk.Label(
    root,
    text=f"Model Trained Successfully | Accuracy : {accuracy*100:.2f}%",
    bg="#101820",
    fg="white",
    anchor="w",
    padx=15,
    font=("Segoe UI",10)
)

status.pack(
    side="bottom",
    fill="x"
)

# ==========================================================
# VARIABLES
# ==========================================================

current_risk=""
current_confidence=0
current_score=0
current_disaster=""
current_time=""

# ==========================================================
# PLACEHOLDER FUNCTIONS
# (Will be completed in Part 3)
# ==========================================================

def predict():
    pass

def show_graph():
    pass

def save_report():
    pass

def clear_fields():

    temp_entry.delete(0,"end")
    rain_entry.delete(0,"end")
    humidity_entry.delete(0,"end")
    wind_entry.delete(0,"end")

    risk_label.config(text="---",fg=GREEN)
    confidence_label.config(text="0%")
    score_label.config(text="0 /100")
    disaster_label.config(text="Waiting for Prediction...")
    meter_value.config(text="0%")
    progress["value"]=0

    recommend_box.config(state="normal")
    recommend_box.delete("1.0","end")
    recommend_box.insert("end","Waiting for AI prediction...")
    recommend_box.config(state="disabled")

# ==========================================================
# CONNECT BUTTONS
# ==========================================================

predict_btn.config(command=predict)

graph_btn.config(command=show_graph)

report_btn.config(command=save_report)

clear_btn.config(command=clear_fields)# ==========================================================
# PREDICTION FUNCTION
# ==========================================================

def predict():

    global current_risk
    global current_confidence
    global current_score
    global current_disaster
    global current_time

    try:

        temperature = float(temp_entry.get())
        rainfall = float(rain_entry.get())
        humidity = float(humidity_entry.get())
        wind = float(wind_entry.get())

    except:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )

        return

    # ------------------------------------------

    user_data = pd.DataFrame([[
        temperature,
        rainfall,
        humidity,
        wind
    ]], columns=[
        "Temperature",
        "Rainfall",
        "Humidity",
        "WindSpeed"
    ])

    prediction = model.predict(user_data)[0]

    probability = max(
        model.predict_proba(user_data)[0]
    ) * 100

    risk_names = {
        0: "LOW",
        1: "MEDIUM",
        2: "HIGH"
    }

    risk = risk_names[prediction]

    # ======================================================
    # WEATHER SCORE
    # ======================================================

    weather_score = (

        (temperature / 50) * 20 +

        (rainfall / 300) * 35 +

        (humidity / 100) * 20 +

        (wind / 120) * 25

    )

    weather_score = min(weather_score,100)

    # ======================================================
    # DISASTER ESTIMATION
    # ======================================================

    if rainfall > 180 and humidity > 80:

        disaster = "🌊 Flood"

    elif temperature > 42 and humidity < 40:

        disaster = "🔥 Heatwave"

    elif wind > 80:

        disaster = "🌪 Cyclone / Storm"

    elif temperature > 38 and rainfall < 30:

        disaster = "🏜 Drought"

    elif rainfall > 220 and wind > 70:

        disaster = "⛈ Severe Thunderstorm"

    elif temperature < 5:

        disaster = "❄ Cold Wave"

    else:

        disaster = "✅ No Major Disaster Expected"

    # ======================================================
    # STORE VALUES
    # ======================================================

    current_risk = risk

    current_confidence = probability

    current_score = weather_score

    current_disaster = disaster

    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    # ======================================================
    # UPDATE CARDS
    # ======================================================

    risk_label.config(text=risk)

    confidence_label.config(
        text=f"{probability:.2f}%"
    )

    score_label.config(
        text=f"{weather_score:.1f}/100"
    )

    disaster_label.config(
        text=disaster
    )

    progress["value"] = weather_score

    meter_value.config(
        text=f"{weather_score:.1f}%"
    )

    # ======================================================
    # RISK COLORS
    # ======================================================

    if risk == "LOW":

        risk_label.config(
            fg="#00FF99"
        )

    elif risk == "MEDIUM":

        risk_label.config(
            fg="#FFD166"
        )

    else:

        risk_label.config(
            fg="#FF4D6D"
        )

    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    recommend_box.config(
        state="normal"
    )

    recommend_box.delete(
        "1.0",
        "end"
    )

    if risk == "LOW":

        recommend_box.insert(
            "end",
            "🟢 LOW RISK\n\n"
        )

        recommend_box.insert(
            "end",
            "✔ Weather conditions are stable.\n\n"
        )

        recommend_box.insert(
            "end",
            "✔ Continue normal activities.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Stay informed through local weather updates.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Keep emergency contacts available.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Drink plenty of water.\n"
        )

    elif risk == "MEDIUM":

        recommend_box.insert(
            "end",
            "🟡 MEDIUM RISK\n\n"
        )

        recommend_box.insert(
            "end",
            "⚠ Weather conditions may worsen.\n\n"
        )

        recommend_box.insert(
            "end",
            "✔ Prepare an emergency kit.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Avoid unnecessary travel.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Keep phones fully charged.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Follow official forecasts.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Inform family members.\n"
        )

    else:

        recommend_box.insert(
            "end",
            "🔴 HIGH RISK\n\n"
        )

        recommend_box.insert(
            "end",
            "🚨 Severe weather detected.\n\n"
        )

        recommend_box.insert(
            "end",
            "✔ Stay indoors immediately.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Prepare for evacuation if advised.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Charge phones and power banks.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Keep food and drinking water ready.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Follow government alerts.\n"
        )

        recommend_box.insert(
            "end",
            "✔ Avoid rivers and flooded roads.\n"
        )

    recommend_box.insert(
        "end",
        "\n--------------------------------------\n"
    )

    recommend_box.insert(
        "end",
        f"Most Probable Disaster:\n{disaster}"
    )

    recommend_box.config(
        state="disabled"
    )

    # ======================================================
    # SAVE HISTORY
    # ======================================================

    history = (

        f"{current_time} | "

        f"Temp={temperature}°C | "

        f"Rain={rainfall} mm | "

        f"Humidity={humidity}% | "

        f"Wind={wind} km/h | "

        f"Risk={risk} | "

        f"Confidence={probability:.2f}%\n"

    )

    with open(
        "prediction_history.txt",
        "a"
    ) as file:

        file.write(history)

    # ======================================================
    # STATUS BAR
    # ======================================================

    status.config(

        text=f"Prediction Complete | Risk : {risk} | Confidence : {probability:.2f}%"

    )

    # ======================================================
    # SUCCESS MESSAGE
    # ======================================================

    messagebox.showinfo(

        "Prediction Complete",

        f"Predicted Risk Level : {risk}\n\n"

        f"Confidence : {probability:.2f}%"

    )
    # ==========================================================
# FEATURE IMPORTANCE GRAPH
# ==========================================================

def show_graph():

    plt.figure(figsize=(8,5))

    plt.bar(features, feature_importance)

    plt.title("Sentinel AI - Feature Importance")

    plt.xlabel("Weather Factors")

    plt.ylabel("Importance")

    plt.tight_layout()

    plt.savefig("feature_importance.png")

    plt.show()


# ==========================================================
# SAVE REPORT
# ==========================================================

def save_report():

    global current_time

    if current_risk == "":

        messagebox.showwarning(
            "No Prediction",
            "Please make a prediction first."
        )

        return

    report = open(
        "Sentinel_AI_Report.txt",
        "w"
    )

    report.write("="*60+"\n")
    report.write("SENTINEL AI DISASTER RISK REPORT\n")
    report.write("="*60+"\n\n")

    report.write(f"Date : {current_time}\n\n")

    report.write("INPUT DATA\n")
    report.write("---------------------------\n")

    report.write(
        f"Temperature : {temp_entry.get()} °C\n"
    )

    report.write(
        f"Rainfall : {rain_entry.get()} mm\n"
    )

    report.write(
        f"Humidity : {humidity_entry.get()} %\n"
    )

    report.write(
        f"Wind Speed : {wind_entry.get()} km/h\n\n"
    )

    report.write("AI RESULTS\n")
    report.write("---------------------------\n")

    report.write(
        f"Risk Level : {current_risk}\n"
    )

    report.write(
        f"Confidence : {current_confidence:.2f}%\n"
    )

    report.write(
        f"Weather Score : {current_score:.1f}/100\n"
    )

    report.write(
        f"Likely Disaster : {current_disaster}\n\n"
    )

    report.write("Generated by Sentinel AI")

    report.close()

    messagebox.showinfo(
        "Saved",
        "Report saved successfully!"
    )


# ==========================================================
# UPDATE BUTTON COMMANDS
# ==========================================================

predict_btn.config(command=predict)

graph_btn.config(command=show_graph)

report_btn.config(command=save_report)

clear_btn.config(command=clear_fields)


# ==========================================================
# WELCOME MESSAGE
# ==========================================================

recommend_box.config(state="normal")

recommend_box.delete("1.0","end")

recommend_box.insert(
    "end",
    "🌍 Welcome to Sentinel AI\n\n"
)

recommend_box.insert(
    "end",
    "Enter the weather information on the left.\n\n"
)

recommend_box.insert(
    "end",
    "Click 'Predict Risk' to let the AI analyze the weather conditions.\n\n"
)

recommend_box.insert(
    "end",
    "The AI will estimate:\n\n"
)

recommend_box.insert(
    "end",
    "• Disaster Risk Level\n"
)

recommend_box.insert(
    "end",
    "• Confidence Percentage\n"
)

recommend_box.insert(
    "end",
    "• Weather Score\n"
)

recommend_box.insert(
    "end",
    "• Most Probable Disaster\n"
)

recommend_box.insert(
    "end",
    "• Safety Recommendations\n"
)

recommend_box.config(state="disabled")


# ==========================================================
# FOOTER
# ==========================================================

footer=tk.Label(

    root,

    text="© 2026 Sentinel AI | Intelligent Disaster Risk Prediction System",

    bg="#111827",

    fg="white",

    font=("Segoe UI",10)

)

footer.pack(fill="x")


# ==========================================================
# START APPLICATION
# ==========================================================

root.mainloop()