from mongoengine import Document, FloatField, StringField, IntField, SequenceField
class Label(Document):
    label_id = SequenceField(required=True)
    start_timestamp = IntField(required=True)
    end_timestamp = IntField(required=True)
    scientific_name = StringField(required=True)
    common_name = StringField(required=True)
    local_name = StringField(required=True)
    confidence = FloatField(required=True)

    meta = {
        'indexes': [
            {'fields': ['start_timestamp', 'scientific_name'], 'unique': True}  # índice único
        ]
    }
    
    @classmethod
    def ensure_indexes(cls):
        super(Label, cls).ensure_indexes()

    def to_dict(self):
        return {
            "label_id": self.label_id,
            "start_timestamp": self.start_timestamp,
            "end_timestamp": self.end_timestamp,
            "scientific_name": self.scientific_name,
            "common_name": self.common_name,
            "local_name": self.local_name,
            "confidence": self.confidence,
        }

Label.ensure_indexes()