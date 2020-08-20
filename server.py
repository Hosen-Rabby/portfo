from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv

# @app.route('/')
# def hello_world():
#     return 'Hello, fain'

# @app.route('/<username>/<int:post_id>')
# def hello(username = None, post_id=None):
#     return render_template('index.html', name = username, post_id= post_id)


# @app.route('/blog')
# def blog():
#     return 'Hello, blogmm'

# @app.route('/about')
# def temp():
#     return render_template('index.html')

    



@app.route('/')
def hello_world():
    return 'Hello, fain'

@app.route('/index.html')
def home():
    return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# Write to text file as database

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['u_name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        file = database.write(f'\n{name}, {email}, {subject}, {message}')


# Write to csv file as database

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data['u_name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])



# for dynamic 
@app.route('/<string:pages>')
def pages(pages):
    return render_template(pages)



@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
        	data = request.form.to_dict()
        	write_to_csv(data)
        	return redirect('/thankyou.html')
        except:
            return 'Didn\'t save'
    else:
    	return 'something went wrong!'

    file = open('database.txt', 'wb')