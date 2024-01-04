from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'username', 'password', 'your-aurora-endpoint', and 'your-database' with your actual RDS credentials and details.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres_admin:123456789@flaskappdatabase.cluster-crcewgieknm7.us-east-1.rds.amazonaws.com:5432/flaskappdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Routes
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/new_post')
def new_post():
    return render_template('new_post.html')

@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
