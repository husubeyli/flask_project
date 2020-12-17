from flask import render_template, request, redirect, url_for
from main import app
from forms import CommentForm, RegisterForm, LoginForm
from flask_login import login_user, login_required,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import Book, Comment, User




@app.route('/login' , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        post_data= request.data
        form = LoginForm(data=post_data)
        if form.validate:
            user = User.query.filter_by(user_name=form.user_name.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/')
    return render_template('sign_in.html', form = form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        post_data = request.form
        form = RegisterForm(data=post_data)
        if form.validate:
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, username=form.username.data, password=form.password.data)
            user.save()
            return redirect( url_for('get_books') )
    return render_template('sign_up.html', form=form)

@app.route('/')
def get_books():
    book_list = Book.query.all()
    return render_template('index.html', books=book_list)


@app.route('/product')
def show_product():
    products = {
        'book_name': 'İncognito (beyinin gizli həyatı)',
        'price': 12.00,
        'old_price': 15.00,
        'description': 'Tanınmış nevroloq D.İqlmenin 20-dən çox dilə tərcümə edilən və indidən klassik əsərə çevrilən bu kitabı beynin sirli dünyasına təcrübələr, elmi biliklər və tarixi faktlar işığında səyahət edir. Kitab tibbi mövzuda olsa da, müəllif yazarlıq məharətini və zəngin biliyini birləşdirərək elmi faktları sadə və müqayisəli dillə oxucularına təqdim edir. Müəllif əsər boyu sədaqət geni, qumarbazlara çevrilən parkinson xəstələri, gen-mühit əlaqəsi, “yaxşı” və “pis” gen, şüuraltı və qərarvermə mexanizmi, məsuliyyət anlayışı, beynin insan həyatında rolu kimi bir çox mövzulara toxunur. Alim bu mövzuların beyinlə əlaqəsini izah etməklə kifayətlənmir, beyinlə bağlı müxtəlif formullar və modellər irəli sürür. İnsan psixologiyası və davranışlarına neyron və gen prizmasından baxmağı öyrədir. Elmi-populyar dildə yazılmış bu kitab xüsusən müəllimlər, psixoloqlar, valideynlər, həkimlər üçün mühüm bilikləri ehtiva edir.',
        'thumbnail': "../static/images/Inkognito.png",
        'stock': 2,
        'language': 'Azərbaycanca',
        'genre': 'Psixologiya',
        'author': 'David Eagleman'
    } 
    return render_template('products.html', products=products)


@app.route('/book/<int:book_ind>', methods=['GET', 'POST'])
def show_book(book_ind):
    form = CommentForm()
    if request.method == 'POST' and form.validate_on_submit():
        user_name = request.form['user_name']
        comment = request.form['comment']
        comment = Comment(user_name, comment, book_ind)
        comment.save()
    book = Book.query.get(book_ind)
    if not book:
        return 'There is not book from this ID'
    # print(book.comments.all())
    return render_template('book.html', products=book, form=form)


