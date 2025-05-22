from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    jsonify,
)
# from db_session import create_session
# from models.blog import Poster, ImagePoster, CommentPoster, LikePoster
# from forms.blog import BlogForms, CommentForm
import io

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')


# @blog_bp.route('/create', methods=['GET', 'POST'])
# def create_blog_post():
#     form = BlogForms()
#     if request.method == 'POST':
#         # img_data = request.form.get('blog_imgs')
#         # print("IMGS:", img_data, type(img_data))
#         description = form.description.data
#         session = create_session()
#         blog_post = Poster(description=description, user_id=current_user.id)
#         session.add(blog_post)
#         session.commit()
#         images = request.files.getlist(form.images.name)
#         session = create_session()
#         for image in images:
#             blog_post = max(session.query(Poster).all(), key=lambda s: s.id)
#             if image:
#                 if image.filename != '':
#                     image_data = image.read()
#                     image = ImagePoster(
#                         image=image_data, post_id=blog_post.id
#                     )
#                     image.post_id = blog_post.id
#                     session.add(image)
#         session.commit()
#         # print(session.query(ImagePoster).filter(ImagePoster.post_id == blog_post.id).first())
#         return redirect(url_for('profile.index'))
#
#     return render_template('blog/create.html', form=form)
