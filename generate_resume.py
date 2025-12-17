import os
from datetime import datetime

# Read data from resume_data.txt
with open("resume_data.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Unpack all 7 fields (including hobbies)
name, email, phone, education, experience, skills, hobbies = lines

# Load the HTML template
with open("templates/resume_template.html", "r") as template_file:
    html_template = template_file.read()

# Replace placeholders in template
html_filled = html_template.replace("{{NAME}}", name)
html_filled = html_filled.replace("{{EMAIL}}", email)
html_filled = html_filled.replace("{{PHONE}}", phone)
html_filled = html_filled.replace("{{EDUCATION}}", education)
html_filled = html_filled.replace("{{EXPERIENCE}}", experience)
html_filled = html_filled.replace("{{SKILLS}}", skills)
html_filled = html_filled.replace("{{HOBBIES}}", hobbies)

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Create timestamp-based filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
html_filename = f"resume_{timestamp}.html"
html_path = os.path.join("output", html_filename)

# Save final HTML resume
with open(html_path, "w", encoding="utf-8") as output_file:
    output_file.write(html_filled)

print(f"✅ HTML Resume generated: {html_path}")

# Optional PDF Export (if pdfkit is installed)
try:
    import pdfkit
    pdf_filename = html_filename.replace(".html", ".pdf")
    pdf_path = os.path.join("output", pdf_filename)
    pdfkit.from_file(html_path, pdf_path)
    print(f"✅ PDF Resume exported: {pdf_path}")
except ImportError:
    print("⚠️ Skipping PDF export (pdfkit not installed)")
