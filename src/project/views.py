from flask import Blueprint, request, jsonify
from project.models import Delivery
from project import db


blueprint = Blueprint('routes', __name__)


@blueprint.route('/')
def index():
    return '<h1>Hello World!</h1>'


@blueprint.route('/deliveries')
def list():
    deliveries = Delivery.query.filter_by(user_id=8).all()

    return jsonify(
        [delivery_to_dict(delivery) for delivery in deliveries]), 200


@blueprint.route('/deliveries', methods=['POST'])
def create():
    data = request.get_json()

    delivery = Delivery(
        description=data.get('description'),
        status='En Curso',
        user_id=8)

    db.session.add(delivery)
    db.session.commit()

    return jsonify(delivery_to_dict(delivery))


def delivery_to_dict(delivery):
    return {
        'id': delivery.id,
        'description': delivery.description,
        'status': delivery.status,
        'creation': delivery.creation
    }
