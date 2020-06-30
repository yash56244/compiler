import os
from flask import render_template, request
from main import app

languages = ['Python', 'C', 'C++', 'Java']

@app.route('/', methods = ['GET', 'POST'])
def compile():
    if request.method == 'POST':
        language1 = dict(request.form.items())
        language = language1['languages']
        if language == "Python":
            open("code.py",'w').write(language1['prog'])
            open("input.file",'w').write(language1['input'])
            os.system("python code.py < input.file 1> output.file 2> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("del code* *.file")
            return render_template("index.html",languages=languages,current_lang=language,prog=language1['prog'],input=language1['input'],remarks=remark,output=outputs)
        elif language == "C":
            open("code.c",'w').write(language1['prog'])
            os.system("gcc code.c -o code 1> output.file 2> remarks.file")
            open("input.file",'w').write(language1['input'])
            os.system("code.exe < input.file 1>> output.file 2>> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("del code* *.file")
            return render_template("index.html",languages=languages,current_lang=language,prog=language1['prog'],input=language1['input'],remarks=remark,output=outputs)
        elif language == "C++":
            open("code.cpp",'w').write(language1['prog'])
            os.system("g++ code.cpp -o code 1> output.file 2> remarks.file")
            open("input.file",'w').write(language1['input'])
            os.system("code.exe < input.file 1>> output.file 2>> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("del code* *.file")
            return render_template("index.html",languages=languages,current_lang=language,prog=language1['prog'],input=language1['input'],remarks=remark,output=outputs)
        elif language == "Java":
            open("code.java",'w').write(language1['prog'])
            open("input.file",'w').write(language1['input'])
            os.system("javac code.java < input.file 1> output.file 2> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("del code* *.file")
<<<<<<< HEAD
            return render_template("index.html",languages=languages,current_lang=language,prog=language1['prog'],input=language1['input'],remarks=remark,output=outputs)
        return render_template('index.html',languages=languages,current_lang='',prog='',input='',remarks='',output='')
    return render_template('index.html',languages=languages,current_lang='',prog='',input='',remarks='',output='')
=======
            return render_template("template.html",languages=languages,current_lang=language,prog=language1['prog'],input=language1['input'],remarks=remark,output=outputs)
        return render_template('template.html',languages=languages,current_lang='',prog='',input='',remarks='',output='')
    return render_template('template.html',languages=languages,current_lang='',prog='',input='',remarks='',output='')
>>>>>>> 6fc9648eb977cc33c9f9975a313ea8fc261cbe6f
