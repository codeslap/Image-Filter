import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for, send_file, session, send_from_directory
from PIL import Image, ImageFilter, ImageEnhance, UnidentifiedImageError
from flask_session import Session
import threading
import time
import asyncio


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config['UPLOAD_PATH'] = ''



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            ftype = int(request.form.get("select"))
        except ValueError:
            return apology("Please Choose a Filter type", 400)
        global uploaded_file
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        img = uploaded_file.filename
        global newimg
        newimg = "filtered" + img
        try:
            pre = Image.open(uploaded_file)
        except UnidentifiedImageError:
            return apology("Please seelect an image to upload",400)
        print(newimg)
        if ftype == 1:
            pre = Image.open(uploaded_file)
            filtered = pre.filter(ImageFilter.BoxBlur(3))
            filtered.save(newimg)
            filtered.show()
        if ftype == 2:
            pre = Image.open(uploaded_file)
            filtered = pre.filter(ImageFilter.FIND_EDGES)
            filtered.save(newimg)
            filtered.show()
        if ftype == 3:
            pre = Image.open(uploaded_file)
            filtered = pre.convert("L")
            filtered.save(newimg)
            filtered.show()
        if ftype == 4:
            pre = Image.open(uploaded_file)
            width, height = pre.size

            pixels = pre.load() # create the pixel map
            bits = pre.mode
            if bits == 'RGB':
                for py in range(height):
                    for px in range(width):
                        r, g, b = pre.getpixel((px, py))

                        tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                        tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                        tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                        if tr > 255:
                            tr = 255

                        if tg > 255:
                            tg = 255

                        if tb > 255:
                            tb = 255

                        pixels[px, py] = (tr,tg,tb)
            if bits == 'RGBA':
                for py in range(height):
                    for px in range(width):
                        r, g, b, a = pre.getpixel((px, py))

                        tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                        tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                        tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                        if tr > 255:
                            tr = 255

                        if tg > 255:
                            tg = 255

                        if tb > 255:
                            tb = 255

                        pixels[px, py] = (tr,tg,tb)

            pre.save(newimg)
        threading.Thread(target=child, args=()).start()
        return redirect(url_for('download', newimg=newimg))
    else:
        return render_template("index.html")



@app.route('/download/<newimg>')
def download(newimg):
    return send_from_directory(app.config['UPLOAD_PATH'], newimg)

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code
#deletes images
def delete(img):
    os.remove(img)
#timer before deleting files
def child():
    timer = 7
    while timer > 0:
        time.sleep(0.985) # don't sleep for a full second or else you'll be off
        timer -= 1
    delete(newimg)
    delete(uploaded_file.filename)



