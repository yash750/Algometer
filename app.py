import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from utils.check_endpoint import check_algorithm
import mysql.connector
from mysql.connector import Error

# Establishing the connection
connection = mysql.connector.connect(
    host="localhost",
    database="algo_meter",
    user="yash_chundawat",
    password="2628",
    charset="utf8mb4",
    collation="utf8mb4_general_ci",
)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/student")
def upload_form():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return redirect(request.url)

    if file and allowed_file(file.filename):
        cur = connection.cursor()
        name = request.form["name"]
        roll_number = request.form["roll_number"]
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        result = check_algorithm(file_path)
        status = result["status"]
        feedback = result["feedback"]
        insert_query = "INSERT INTO details (name, roll_number, status, other_feedback) VALUES (%s, %s, %s, %s)"
        cur.execute(insert_query, (name, roll_number, status, feedback))
        connection.commit()
        cur.close()

        return render_template("result.html", result=result)
    else:
        flash("Allowed file types are txt")
        return redirect(request.url)


@app.route("/admin")
def admin_page():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT name, roll_number, status, other_feedback FROM details")
    submissions = cursor.fetchall()
    cursor.close()

    return render_template("admin.html", submissions=submissions)


if __name__ == "__main__":
    app.run(debug=True)
    connection.close()
