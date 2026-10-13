# 🔬 Quality Calibration Checker

An interactive Streamlit application demonstrating calibration status verification, dimensional tolerance evaluation, and inspection decision logic using synthetic manufacturing data.

## 🚀 Live Demo

[Launch the Quality Calibration Checker](...)

## 📸 Application Preview

![Quality Calibration Checker](images/Quality%20Calibration.png)


## 🎯 Purpose

This project demonstrates how basic quality inspection rules can be translated into Python decision logic.

Before accepting a dimensional measurement, the application verifies that the measurement instrument has a valid calibration status and that the measured value falls within the specified tolerance limits.

## ⚙️ How It Works

The user selects a measurement instrument and enters:

- Calibration due date
- Nominal dimension
- Tolerance
- Measured value

The application automatically calculates:

- Lower Specification Limit (LSL)
- Upper Specification Limit (USL)
- Calibration status
- Dimensional conformity

## 🔍 Inspection Decision Logic

The application follows three primary decision paths:

**STOP** — Calibration is expired. The measurement should not be used for product acceptance.

**HOLD** — Calibration is valid, but the measurement is outside the specified tolerance limits.

**ACCEPT** — Calibration is valid and the measurement is within specification.

## 🧪 Logic Testing

The application was tested using:

- Measurements exactly at LSL and USL
- Measurements immediately outside specification limits
- Expired calibration dates
- Calibration due on the current date
- Extreme out-of-tolerance measurement values

## 🛠️ Technology

- Python
- Streamlit
- GitHub
- Streamlit Community Cloud

## 📚 Quality Concepts Demonstrated

- Calibration status verification
- Dimensional inspection
- Tolerance evaluation
- LSL and USL calculations
- Nonconforming product decisions
- Measurement validation
- Quality decision logic

## ⚠️ Disclaimer

This application uses synthetic inspection scenarios for educational and portfolio purposes only. It is not a substitute for an organization's approved calibration, inspection, measurement system analysis (MSA), or quality management procedures.
