from flask import *
import os
app = Flask(__name__)

languages = ['Python', 'C', 'C++', 'Java']

@app.route('/', methods=['POST','GET'])
def compute():
    if request.method == 'POST':
        result = request.form
        result_dict = dict(result.items())
        lang = result_dict['languages']
        if lang == "Python":
            open("code.py",'w').write(result_dict['prog'])
            open("input.file",'w').write(result_dict['input'])
            os.system("python code.py < input.file 1> output.file 2> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("del code* *.file")
            return render_template("template.html",languages=languages,current_lang=lang,prog=result_dict['prog'],input=result_dict['input'],remarks=remark,output=outputs)
        # elif lang == "Java":
            
        elif lang == "C":
            open("code.c",'w').write(result_dict['prog'])
            os.system("gcc code.c -o code 1> output.file 2> remarks.file")
            open("input.file",'w').write(result_dict['input'])
            os.system("code.exe < input.file 1>> output.file 2>> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("del code* *.file")
            return render_template("template.html",languages=languages,current_lang=lang,prog=result_dict['prog'],input=result_dict['input'],remarks=remark,output=outputs)
        elif lang == "C++":
            open("code.cpp",'w').write(result_dict['prog'])
            os.system("g++ code.cpp -o code 1> output.file 2> remarks.file")
            open("input.file",'w').write(result_dict['input'])
            os.system("code.exe < input.file 1>> output.file 2>> remarks.file")
            remark = open("remarks.file",'r').read()
            outputs = open("output.file",'r').read()
            os.system("rm code* *.file")
            return render_template("template.html",languages=languages,current_lang=lang,prog=result_dict['prog'],input=result_dict['input'],remarks=remark,output=outputs)
        else:
            print("You are one kind of a tester")
        return render_template('template.html',languages=languages,current_lang='',prog='',input='',remarks='',output='')
    elif request.method == 'GET':
        return render_template('template.html',languages=languages,current_lang='',prog='',input='',remarks='',output='')
if __name__ == '__main__':
    app.run(debug = False)
