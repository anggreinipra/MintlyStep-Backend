from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.transaction import Transaction, TransactionType, CategoryType
from app.models.user import User
from datetime import datetime

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")

# Get all transactions for current user
@transactions_bp.route("/", methods=["GET"])
@jwt_required()
def get_transactions():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    transactions = Transaction.query.filter_by(user_id=user.id).all()
    result = []
    for tx in transactions:
        result.append({
            "id": tx.id,
            "description": tx.description,
            "amount": tx.amount,
            "type": tx.transaction_type.value,
            "category": tx.category.value,
            "payment_method": tx.payment_method,
            "date": tx.date.isoformat()
        })

    return jsonify(result), 200

# Create transaction
@transactions_bp.route("/", methods=["POST"])
@jwt_required()
def create_transaction():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    try:
        new_tx = Transaction(
            user_id=user.id,
            description=data["description"],
            amount=data["amount"],
            transaction_type=TransactionType[data["transaction_type"]],
            category=CategoryType[data["category"]],
            payment_method=data["payment_method"],
            date=datetime.fromisoformat(data["date"])
        )
        db.session.add(new_tx)
        db.session.commit()
        return jsonify({"msg": "Transaction created!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Delete transaction
@transactions_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_transaction(id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    tx = Transaction.query.filter_by(id=id, user_id=user.id).first()
    if not tx:
        return jsonify({"msg": "Transaction not found"}), 404

    db.session.delete(tx)
    db.session.commit()
    return jsonify({"msg": "Transaction deleted"}), 200
