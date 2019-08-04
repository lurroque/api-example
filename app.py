from flask import Flask, request, jsonify, abort
from marshmallow import Schema, fields, validate
from flasgger import swag_from, Swagger
import db


app = Flask(__name__)
Swagger(app)


class PropertySchema(Schema):
    name = fields.String(required=True, validate=validate.Length(3, 120))
    address = fields.String(required=True, validate=validate.Length(3, 120))
    description = fields.String(
        required=True, validate=validate.Length(3, 120)
    )
    status = fields.String(
        required=True, validate=validate.OneOf(["ativo", "inativo"])
    )
    features = fields.String(validate=validate.Length(3, 120))
    type_of = fields.String(
        required=True, validate=validate.OneOf(["apartamento", "casa"])
    )
    purpose = fields.String(
        validate=validate.OneOf(["residencial", "escritorio"])
    )
    real_estate = fields.Integer(required=True)


@app.route("/property", methods=["POST"])
@swag_from("docs/property/property_post.yml")
def register_property():
    registered_prop = request.get_json()
    errors = PropertySchema().validate(registered_prop)
    if errors:
        abort(400, errors)
    id_ = db.create_property(registered_prop)
    registered_prop["id"] = id_
    return registered_prop, 201


@app.route("/property", methods=["GET"])
@swag_from("docs/property/property_get.yml")
def list_properties():
    return jsonify(db.list_properties()), 200


@app.route("/property/<int:identifier>", methods=["DELETE"])
@swag_from("docs/property/property_delete.yml")
def delete(identifier):
    if not db.exist_property(identifier):
        abort(404)
    db.delete_property(identifier)
    return "", 204


@app.route("/property/<int:identifier>", methods=["PUT"])
@swag_from("docs/property/property_put.yml")
def update_property(identifier):
    registered_prop = request.get_json()
    errors = PropertySchema().validate(registered_prop)
    if errors:
        abort(400, errors)
    if not db.exist_property(identifier):
        abort(404)
    db.update_property(registered_prop, identifier)
    return registered_prop


class RealEstateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(3, 120))
    address = fields.String(required=True, validate=validate.Length(3, 120))


@app.route("/real-estate", methods=["POST"])
@swag_from("docs/real_estate/real_estate_post.yml")
def register_real_estate():
    registered_real_estate = request.get_json()
    errors = RealEstateSchema().validate(registered_real_estate)
    if errors:
        abort(400, errors)
    id_ = db.create_real_estate(registered_real_estate)
    registered_real_estate["id"] = id_
    return registered_real_estate, 201


@app.route("/real-estate", methods=["GET"])
@swag_from("docs/real_estate/real_estate_get.yml")
def list_real_estates():
    return jsonify(db.list_real_estates()), 200


@app.route("/real-estate/<int:identifier>", methods=["DELETE"])
@swag_from("docs/real_estate/real_estate_delete.yml")
def delete_real_estate(identifier):
    if not db.exist_real_estate(identifier):
        abort(404)
    db.delete_real_estate(identifier)
    return "", 204


@app.route("/real-estate/<int:identifier>", methods=["PUT"])
@swag_from("docs/real_estate/real_estate_put.yml")
def update_real_estate(identifier):
    registered_real_estate = request.get_json()
    errors = RealEstateSchema().validate(registered_real_estate)
    if errors:
        abort(400, errors)
    if not db.exist_real_estate(identifier):
        abort(404)
    db.update_property(registered_real_estate, identifier)
    return registered_real_estate
