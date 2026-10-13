import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Quality Calibration Checker",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Quality Calibration Checker")
st.caption(
    "Interactive educational tool for calibration status, "
    "measurement validation, and tolerance evaluation."
)

st.info(
    "This application uses synthetic inspection scenarios for "
    "educational and portfolio purposes."
)

# -----------------------------
# Inspection Setup
# -----------------------------

st.subheader("Inspection Setup")

col1, col2 = st.columns(2)

with col1:
    instrument = st.selectbox(
        "Measurement Instrument",
        [
            "Digital Caliper",
            "Outside Micrometer",
            "Height Gauge",
            "Bore Gauge"
        ]
    )

    calibration_due = st.date_input(
        "Calibration Due Date",
        value=date(2026, 12, 15)
    )

with col2:
    nominal = st.number_input(
        "Nominal Dimension (mm)",
        value=25.000,
        format="%.3f"
    )

    tolerance = st.number_input(
        "Tolerance ± (mm)",
        min_value=0.001,
        value=0.050,
        format="%.3f"
    )

    measurement = st.number_input(
        "Measured Value (mm)",
        value=25.000,
        format="%.3f"
    )

# -----------------------------
# Calculate Limits
# -----------------------------

lsl = nominal - tolerance
usl = nominal + tolerance

st.divider()

st.subheader("Inspection Results")

metric1, metric2, metric3 = st.columns(3)

metric1.metric("LSL", f"{lsl:.3f} mm")
metric2.metric("Measured", f"{measurement:.3f} mm")
metric3.metric("USL", f"{usl:.3f} mm")

# -----------------------------
# Calibration Status
# -----------------------------

today = date.today()
calibration_valid = calibration_due >= today
dimension_valid = lsl <= measurement <= usl

if not calibration_valid:
    st.error("🔴 CALIBRATION EXPIRED")
    st.warning(
        "Measurement not valid for product acceptance. "
        "Calibration status must be verified before this instrument "
        "is used for product disposition."
    )

elif not dimension_valid:
    st.error("🔴 NONCONFORMING — HOLD FOR REVIEW")
    st.write(
        "The measurement is outside the specified tolerance limits."
    )

else:
    st.success("🟢 ACCEPTABLE — Measurement Within Specification")
    st.write(
        "Calibration status is current and the measurement falls "
        "within the specified tolerance limits."
    )

st.divider()

st.caption(
    "Educational simulation only. This application is not a substitute "
    "for an organization's approved calibration, inspection, MSA, "
    "or quality management procedures."
)
