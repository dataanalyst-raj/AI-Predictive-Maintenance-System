from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf(
    machine_type,
    air_temp,
    process_temp,
    rot_speed,
    torque,
    tool_wear,
    temp_difference,
    prediction,
    confidence,
    shap_features
):
    filename = "Prediction_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # ---------------------------------
    # Title
    # ---------------------------------

    story.append(
        Paragraph("<b><font size=18>AI Predictive Maintenance Report</font></b>", styles["Title"])
    )

    story.append(
        Paragraph(
            f"<b>Date :</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------------------------
    # Machine Information
    # ---------------------------------

    story.append(Paragraph("<b>Machine Information</b>", styles["Heading2"]))

    story.append(Paragraph(f"Machine Type : {machine_type}", styles["Normal"]))
    story.append(Paragraph(f"Air Temperature : {air_temp} K", styles["Normal"]))
    story.append(Paragraph(f"Process Temperature : {process_temp} K", styles["Normal"]))
    story.append(Paragraph(f"Rotational Speed : {rot_speed} rpm", styles["Normal"]))
    story.append(Paragraph(f"Torque : {torque} Nm", styles["Normal"]))
    story.append(Paragraph(f"Tool Wear : {tool_wear} min", styles["Normal"]))
    story.append(Paragraph(f"Temperature Difference : {temp_difference:.2f} K", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------------------------
    # Prediction
    # ---------------------------------

    story.append(Paragraph("<b>Prediction Result</b>", styles["Heading2"]))

    story.append(Paragraph(f"Machine Status : <b>{prediction}</b>", styles["Normal"]))
    story.append(Paragraph(f"Confidence : {confidence:.2f} %", styles["Normal"]))

    if prediction == "Healthy":
        risk = "LOW"
    else:
        risk = "HIGH"

    story.append(Paragraph(f"Overall Risk : {risk}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------------------------
    # SHAP Explanation
    # ---------------------------------

    story.append(Paragraph("<b>Top AI Factors (SHAP)</b>", styles["Heading2"]))

    for feature in shap_features:
        story.append(
            Paragraph(f"• {feature}", styles["Normal"])
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    # ---------------------------------
    # Recommendation
    # ---------------------------------

    story.append(Paragraph("<b>Recommendation</b>", styles["Heading2"]))

    if prediction == "Healthy":

        story.append(
            Paragraph(
                "Machine is operating normally. Continue routine preventive maintenance.",
                styles["Normal"]
            )
        )

    else:

        story.append(
            Paragraph(
                "Potential machine failure detected. Schedule maintenance inspection immediately.",
                styles["Normal"]
            )
        )

    doc.build(story)

    return filename
