from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensions import db
from ..util import save_picture
from .forms import PostForm
from .models import Post, EnumPriority
from . import posts_bp


@posts_bp.route('/', methods=["GET"])
def posts_page():
    # form=TodoForm()
    # form.categories.choices = [(c.id, c.name) for c in Category.query.all()] 
    return render_template("posts/posts.html", posts=Post.query.all())
 

@posts_bp.route('/<int:id>', methods=["GET"])
def post_page(id):
    post = Post.query.get_or_404(id)
    if not post.enabled and post.user.id != current_user.id:
        return redirect(url_for("posts.posts_page"))

    return render_template("posts/post.html", post=post)


@posts_bp.route("/new", methods=["GET", "POST"])
@login_required
def add_post():
    form = PostForm()

    if form.validate_on_submit():
        
        new_post = Post(
            title = form.title.data, 
            text = form.text.data,
            image = save_picture(form.image.data, f'{posts_bp.root_path}/static/posts_image') if form.image.data else None,
            type = EnumPriority(int(form.type.data)).name, 
            enabled = form.enabled.data,
            user_id = current_user.id
        )

        try: 
            db.session.add(new_post)
            db.session.commit()
            flash('Post added!', category='success')
            return redirect(url_for("posts.post_page", id=new_post.id))
        except:
            db.session.rollback()
            flash('Error!', category='danger')
        
        return redirect(url_for("posts.add_post"))
    
    return render_template("posts/create_post.html", form=form)


@posts_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
    post = Post.query.get_or_404(id)

    if current_user.id != post.user.id:
        return redirect(url_for("posts.posts_page", id=id))
    
    form = PostForm()

    if form.validate_on_submit():
       
        post.title = form.title.data
        post.text = form.text.data         
        post.type = EnumPriority(int(form.type.data)).name
        post.enabled = form.enabled.data
       
        if form.image.data:
            post.image = save_picture(form.image.data, f'{posts_bp.root_path}/static/posts_image')
       
        try: 
            db.session.commit()
            flash(f'Post({post.id}) updated!', category='success')
            return redirect(url_for("posts.post_page", id=id))
        except:
            db.session.rollback()
            flash('Error!', category='danger')    
        
        return redirect(url_for("posts.update_post", id=id))
    
    form.type.data = str(post.type.value)
    form.enabled.data = post.enabled

    return render_template("posts/update_post.html", form=form, post=post)
 

@posts_bp.route("/delete/<int:id>", methods=["POST"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    
    if current_user.id == post.user.id:
        try: 
            db.session.delete(post)
            db.session.commit()
            flash(f'Post({post.id}) deleted!', category='success')
        except:
            db.session.rollback()
            flash('Error!', category='danger')    

    return redirect(url_for("posts.posts_page"))


# @todo_bp.route('/categories', methods=["GET"])
# def category_page():
#     return render_template("todo/categories.html", categories=Category.query.all(), form=CategoryForm())

# @todo_bp.route("/categories", methods=["POST"])
# def add_category():
#     form=CategoryForm()
    
#     if form.validate_on_submit():
#         new_category = Category(name = form.name.data)
#         try:
#             db.session.add(new_category)
#             db.session.commit()
#             flash(f'Category({new_category.name}) created!', category='success')
#         except:
#             flash('Error!', category='danger')
#             db.session.rollback()
#     else:
#         flash('Invalid form!', category='danger')

#     return redirect(url_for('todo.category_page'))

# @todo_bp.route("/categories/delete/<int:id>", methods=["POST"])
# def delete_category(id):
#     category = Category.query.get_or_404(id)
#     try:
#         db.session.delete(category)
#         db.session.commit()
#         flash(f'Category({category.id}) deleted!', category='success')
#     except:
#         flash('Error!', category='danger')
#         db.session.rollback()
#     return redirect(url_for("todo.category_page"))