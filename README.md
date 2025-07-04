# 💉 COVID-19 Daily Vaccinations Forecast 📈

Welcome to the **COVID-19 Daily Vaccinations Forecast** app!  
This interactive Streamlit dashboard helps you visualize and forecast daily COVID-19 vaccinations for any country in your dataset using a simple, explainable machine learning model.

---

## ✨ Features

- 🌍 **Country selection** from your dataset
- 📅 **Adjustable forecast period** (7–60 days)
- 🧑‍💻 Uses features like total vaccinations, people vaccinated, people fully vaccinated, and day of week
- 📈 **Visualization** of actual vs. forecasted daily vaccinations
- 🔢 **Table of forecasted values**
- 🖼️ **Easy-to-read plots** and data tables
- ⚡ **Fast and lightweight** (no heavy dependencies)

---

## 🚦 How It Works

1. **Data Loading:**  
   The app loads your vaccination dataset and allows you to select a country.

2. **Feature Engineering:**  
   It creates features such as:
   - 📆 Days since the first record
   - 💉 Total vaccinations
   - 👤 People vaccinated
   - 👥 People fully vaccinated
   - 🗓️ Day of the week (to capture weekly trends)

3. **Model Training:**  
   A linear regression model (from scikit-learn) is trained on your data.

4. **Forecasting:**  
   The model predicts daily vaccinations for your chosen forecast period, assuming the last known values for cumulative features remain constant.

5. **Visualization:**  
   The app displays both actual and predicted values on a beautiful line chart and shows the forecasted data in a table.

---

## 🛠️ Requirements

- 🐍 Python 3.7+
- 🐼 pandas
- 🔢 numpy
- 📊 matplotlib
- 🤖 scikit-learn
- 🚦 streamlit

Install all requirements with:
```
pip install streamlit pandas numpy matplotlib scikit-learn
```

---

## 🚀 Usage

1. **Prepare your data:**  
   Place your cleaned `country_vaccinations.csv` file in the project directory.  
   The file should contain at least these columns:
   - 📅 `date`
   - 🌍 `country`
   - 💉 `daily_vaccinations`
   - 💉 `total_vaccinations`
   - 👤 `people_vaccinated`
   - 👥 `people_fully_vaccinated`

2. **Run the app:**
   ```
   streamlit run app.py
   ```

3. **Interact with the app:**  
   - 🌏 Select a country from the dropdown menu.
   - ⏳ Choose the number of days to forecast using the slider.
   - 📈 View the actual and forecasted daily vaccinations on the chart.
   - 🗃️ Explore the forecasted data in the table below the chart.

---

## 📁 File Structure

```
.
├── app.py
├── country_vaccinations.csv
└── README.md
```

---

## 💡 Notes & Tips

- 🧐 The accuracy of the forecast depends on the quality and completeness of your data.
- ⚠️ The model uses only the last known values for cumulative features in the forecast period, which may not reflect real-world changes.
- 🚀 You can further improve the model by adding more features (such as public health interventions, mobility data, or case numbers) if available.
- 📋 To use your own data, ensure it matches the required column names and formats.

---

**Made with ❤️ and Streamlit & scikit-learn — Stay safe and keep