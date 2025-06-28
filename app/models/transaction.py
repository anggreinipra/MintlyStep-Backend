from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as PgEnum
from app import db

class TransactionType(Enum):
    DEBIT = 'DEBIT'
    KREDIT = 'KREDIT'

class CategoryType(Enum):
    MAKAN = 'MAKAN'
    TRANSPORT = 'TRANSPORT'
    BELANJA = 'BELANJA'
    LAINNYA = 'LAINNYA'

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(PgEnum(TransactionType), nullable=False)
    category = db.Column(PgEnum(CategoryType), nullable=False)
    payment_method = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="transactions")
