import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'os.db')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'os.db')
    SQLALCHEMY_TRACK_MODIFICATIONS =\
        False


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(20), nullable=False)
    test = db.Column(db.String(20), nullable=False)
    # todos = db.relationship('Todo', backref='owner', lazy='dynamic')
    done = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f'User <{self.test}>'


# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, index=True)
#     title = db.Column(db.String(20), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#
#     def __repr__(self):
#         return f'Todo <{self.title}>'


# test 首頁
@app.route("/")
def home():
    return "Hello, World!"


# 新增
@app.route('/users', methods=['POST'])
def create():
    if request.is_json:
        data = request.get_json()
        if 'test' not in data or 'title' not in data:
            return jsonify(
                {
                    'error': '沒test or title',
                    'message': 'sad'
                }
            )
        u = User(
            title=data['title'],
            test=data['test']
        )

        db.session.add(u)
        db.session.commit()
        return {
            'id': u.id,
            'title': u.title,
            'test': u.test,
            'done': u.done
        }
    else:
        return "your input not json"


# 刪除
@app.route('/users/<_id>', methods=['DELETE'])
def delete_user(_id):
    user = User.query.filter_by(id=_id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return {
        'success': 'Data deleted successfully'
    }


# get全部
@app.route('/users/all', methods=['GET'])
def get_users():
    return jsonify([
       {
        '_id': user.id,
        'title': user.title,
        'test': user.test,
        'done': user.done
       }for user in User.query.all()
    ])


# get單一
@app.route('/users/<_id>', methods=['GET'])
def get_user(_id):
    user = User.query.filter_by(id=_id).first_or_404()
    return jsonify({
        'id': user.id,
        'title': user.title,
        'test': user.test,
        'done': user.done
    })


# 修改
@app.route('/users/<_id>', methods=['PUT'])
def update_todo(_id):
    data = request.get_json()
    if 'test' not in data or 'title' not in data:
        return jsonify(
            {
                'error': '沒test or title',
                'message': 'sad'
            }
        )

    user = User.query.filter_by(id=_id).first_or_404()
    user.title = data['title']
    user.test = data['test']
    db.session.commit()
    return jsonify({
            'id': user.id,
            'title': user.title,
            'test': user.test,
            'done': user.done
        })


# done
@app.route('/users/done/<_id>', methods=['PUT'])
def done(_id):
    user = User.query.filter_by(id=_id).first_or_404()
    user.done = True
    db.session.commit()
    return jsonify({
        'id': user.id,
        'title': user.title,
        'test': user.test,
        'done': user.done
    })


# undone
@app.route('/users/undone/<_id>', methods=['PUT'])
def undone(_id):
    user = User.query.filter_by(id=_id).first_or_404()
    user.done = False
    db.session.commit()
    return jsonify({
        'id': user.id,
        'title': user.title,
        'test': user.test,
        'done': user.done
    })


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8090)
