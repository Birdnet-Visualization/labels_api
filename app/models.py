from mongoengine import Document, FloatField, StringField, IntField

class Label(Document):
    id = IntField(required=True)
    start = FloatField(required=True)
    end = FloatField(required=True)
    scientific_name = StringField(required=True)
    common_name = StringField(required=True)
    confidence = FloatField(required=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "start": self.start,
            "end": self.end,
            "scientific_name": self.scientific_name,
            "common_name": self.common_name,
            "confidence": self.confidence
        }
