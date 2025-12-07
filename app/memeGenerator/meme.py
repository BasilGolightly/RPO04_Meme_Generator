from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
import os 

imagePath = os.path.join("static", "meme.png")
fontPath = os.path.join("static", "impact.ttf")
app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('index.html')
    
@app.route('/postHandler', methods=["POST"]) 
def postHandler():
    if request.method == "POST":
        topText = request.form.get("topText")
        bottomText = request.form.get("bottomText")
        imageRaw =  request.files.get("picture")

        if len(topText) == 0 or len(bottomText) == 0:
            return render_template("index.html")

        # open image and editor
        try:
            imageEdit = Image.open(imageRaw)
            draw = ImageDraw.Draw(imageEdit)
            width, height = imageEdit.size
        except:
            return "Could not open image!"
        
        topFontSize = int((width) / len(topText))
        bottomFontSize = int((width) / len(bottomText))
        
        # get font
        try:
            topFont = ImageFont.truetype(fontPath, topFontSize)
            bottomFont = ImageFont.truetype(fontPath, bottomFontSize)
        except:
            #topFont = ImageFont.load_default
            #bottomFont = ImageFont.truetype("arial.ttf", bottomFontSize)  
            return "Failed to load font!"   
        
        # draw bbox to calculate text width on image
        topBox = draw.textbbox((0, 0), topText, topFont)
        bottomBox = draw.textbbox((0, height), bottomText, bottomFont)
        topTextWidth = topBox[2] - topBox[0]
        bottomTextWidth = bottomBox[2] - bottomBox[0]

        # calculate offset for centered text
        topOffset = (width/2) - (topTextWidth/2)
        bottomOffset = (width/2) - (bottomTextWidth/2)

        # draw black boxes for better text visibility 
        draw.rectangle(((topOffset-topFontSize, 0), (topOffset+topTextWidth+topFontSize, topFontSize*1.25)), "black")
        draw.rectangle(((bottomOffset-bottomFontSize, height-bottomFontSize*1.25), (bottomOffset+bottomTextWidth+bottomFontSize, height)), "black")

        # draw top and bottom text
        draw.text((topOffset, 0), topText, (255, 255, 255), topFont)
        draw.text((bottomOffset,(height-(bottomFontSize+bottomFontSize*0.25))), bottomText, (255, 255, 255), bottomFont)

        # save image
        try:
            imageEdit.save(imagePath)
            return redirect(url_for('static', filename='meme.png'))
        # failed save - write message
        except:
            return "Image could not be saved. Try again"
    else:
        return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)