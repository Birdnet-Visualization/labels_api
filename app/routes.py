from app import app
from flask import jsonify, request
from app.models import Label

# Ruta para agregar un nuevo label (POST)
@app.route("/add_label", methods=["POST"])
def add_label():
    try:
        label_data = request.get_json()
        label = Label(**label_data)
        label.save()
        return jsonify({"message": "Label agregado exitosamente", "id": str(label.label_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para obtener todos los labels (GET)
@app.route("/get_labels", methods=["GET"])
def get_labels():
    labels = Label.objects.all()
    return jsonify([label.to_dict() for label in labels])

# Ruta para obtener un label por ID (GET)
@app.route("/get_label/<string:label_id>", methods=["GET"])
def get_label(label_id):
    label = Label.objects(id=label_id).first()
    if label:
        return jsonify(label.to_dict())
    else:
        return jsonify({"message": "Label no encontrado"}), 404

# Ruta para eliminar un label por ID (DELETE)
@app.route("/delete_label/<string:label_id>", methods=["DELETE"])
def delete_label(label_id):
    try:
        label = Label.objects(id=label_id).first()
        if label:
            label.delete()
            return jsonify({"message": "Label eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Label no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
