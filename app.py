import os
from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template,
    send_from_directory,
    flash,
)
import openpyxl
import csv

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["OUTPUT_FOLDER"] = "output"
app.config["ALLOWED_EXTENSIONS"] = {"xlsx"}
app.secret_key = "supersecretkey"

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

if not os.path.exists(app.config["OUTPUT_FOLDER"]):
    os.makedirs(app.config["OUTPUT_FOLDER"])


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def xlsx_to_csv(xlsx_file):
    workbook = openpyxl.load_workbook(xlsx_file)
    sheet = workbook.active

    csv_content = []
    for row in sheet.iter_rows(values_only=True):
        csv_content.append(row)
    return csv_content


def batch_convert_xlsx_to_csv(input_dir, output_csv_file):
    all_csv_content = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".xlsx"):
            xlsx_file = os.path.join(input_dir, filename)
            csv_content = xlsx_to_csv(xlsx_file)
            all_csv_content.extend(csv_content)
            print(f"Converted {xlsx_file}")

    output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_csv_file)
    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in all_csv_content:
            writer.writerow(row)
    print(f"All files combined into {output_csv_file}")
    return output_path


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "files[]" not in request.files or "output_filename" not in request.form:
            flash("No file part or output filename missing")
            return redirect(request.url)

        files = request.files.getlist("files[]")
        output_filename = request.form["output_filename"]
        if not output_filename.endswith(".csv"):
            output_filename += ".csv"

        for file in files:
            if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        output_path = batch_convert_xlsx_to_csv(
            app.config["UPLOAD_FOLDER"], output_filename
        )

        # Clean up the upload directory after conversion
        for file in os.listdir(app.config["UPLOAD_FOLDER"]):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

        return render_template("result.html", filename=output_filename)

    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/output/<filename>")
def output_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
