from app import app
from flask import jsonify, request
from app.models import Label
from mongoengine.queryset import Q  # Import Q from the queryset module

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

# Ruta para obtener un label por label_id (GET)
@app.route("/get_label/<int:label_id>", methods=["GET"])
def get_label(label_id):
    label = Label.objects(label_id=label_id).first()
    if label:
        return jsonify(label.to_dict())
    else:
        return jsonify({"message": "Label no encontrado"}), 404

@app.route("/get_labels_by_timestamp_range/<int:start_timestamp>/<int:end_timestamp>", methods=["GET"])
def get_labels_by_timestamp_range(start_timestamp, end_timestamp):
    labels = Label.objects.filter(
        start_timestamp__lte=end_timestamp,
        end_timestamp__gte=start_timestamp
    )
    
    labels = list(labels)  # Convertir a lista

    return jsonify([label.to_dict() for label in labels])

# Ruta para obtener un label por label_id (GET)
@app.route("/get_labels_by_timestamp_range/<int:start_timestamp>/<int:end_timestamp>", methods=["GET"])
def get_labels_by_timestamp_range(start_timestamp, end_timestamp):
    labels = Label.objects.filter(
        start_timestamp__lte=end_timestamp,
        end_timestamp__gte=start_timestamp
    )
    labels = list(labels)
    return jsonify([label.to_dict() for label in labels])

# Ruta para eliminar un label por label_id (DELETE)
@app.route("/delete_label/<int:label_id>", methods=["DELETE"])
def delete_label(label_id):
    try:
        label = Label.objects(label_id=label_id).first()
        if label:
            label.delete()
            return jsonify({"message": "Label eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Label no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para obtener un label por ID (GET)
@app.route("/get_label/<string:label_id>", methods=["GET"])
def get_label_by_uid(label_id):
    label = Label.objects(id=label_id).first()
    if label:
        return jsonify(label.to_dict())
    else:
        return jsonify({"message": "Label no encontrado"}), 404

# Ruta para eliminar un label por ID (DELETE)
@app.route("/delete_label/<string:label_id>", methods=["DELETE"])
def delete_label_by_uid(label_id):
    try:
        label = Label.objects(id=label_id).first()
        if label:
            label.delete()
            return jsonify({"message": "Label eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Label no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
