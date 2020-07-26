from flask import Flask, render_template, redirect, request
import os
import testing_caption_generator



app = Flask(__name__)


@app.route("/")
def Hello():
    return render_template('index.html')

@app.route('/', methods= ['POST'])
def marks():
    if request.method == 'POST':
        file = request.files["userfile"]
        path = "./static/{}".format(file.filename)
        file.save(path)
        #print(testing_caption_generator.run_all(path))
        caption = testing_caption_generator.run_all(path)
        #print(caption)
        result_dic = {
            'image': path,    
            'caption' : caption }
         

    return render_template("index.html",your_result = result_dic)


if __name__ == "__main__":
    app.run(debug = True) 

