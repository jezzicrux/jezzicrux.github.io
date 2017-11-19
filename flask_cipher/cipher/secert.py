## FROM THE CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request

@app.route('/')
def index():
	return render_template('/index.html')

@app.route('/decrypt')
def decrypt():
	return render_template('/decrpyt.html')

@app.route('/uncrypt')
def uncrypt():
	return render_template('/uncrypt.html')

@app.route('/cipher', methods = ['GET', 'POST'])
def secertcode():
	if request.method == 'POST':
		message = request.form['message']
		number = request.form['key']
		code = list(str.lower(message))
		key = int(number)
		if key < 27:
			letters = list('abcdefghijklmnopqrstuvwxyz')
			new_message=code
			for q in range (0,len(code)):
				if new_message[q] in letters:
					i = letters.index(code[q])
					if code[q] == letters[i]:
						new_index=i+key
						new_message[q] = letters[new_index]
					else:
						pass
				else:
					pass
			cipher = "".join(new_message)
			print(cipher)
			return render_template('/cipher.html', decrypt = cipher)
		else:
			warning = "WRONG KEY"
			return render_template('/index.html', key = warning)
	else:
		print('get method')
		return render_template('/index.html')
	return render_template('/cipher.html', decrypt = cipher)
