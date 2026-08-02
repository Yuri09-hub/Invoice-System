from models import User,Invoice, session
from datetime import datetime
from pydantic import EmailStr


def create_user(name:str,email:EmailStr,session):
    user = session.query(User).filter( User.email == email).first()

    if user:
        return "User already exists"

    user = User(name=name,email=email,created_at=datetime.now())
    session.add(user)
    session.commit()
    return "user created"

def creat_invoice(id:int,price:float,session):
    user = session.query(User).filter( User.id == id ).first()
    if not user:
        return "User does not exist"
    invoice = Invoice(user=user.id,price=price,created_at=datetime.now())
    session.add(invoice)
    session.commit()
    return "Invoice created"

def list_invoice(session):
    invoices = session.query(Invoice).all()

    print(" Nº Fatura       Cliente              Data           Total")
    print("-------------------------------------------------------------------------")

    for invoice in invoices:
        print(
            f"{invoice.id:<15} "
            f"{invoice.user:<20} "
            f"{invoice.created_at}"
            f"{invoice.price:>10} Kz"
        )

def view_invoice(id:int,session):

    invoice = session.query(Invoice).filter( Invoice.id == id).first()
    if not invoice:
        return "Invoice does not exist"

    user = session.query(User).filter( invoice.user==id).first()

    inv = f"""
    ================================
               INVOICE


    Costumer: {user.name}
    Email: {user.email}

    Invoice Nº: {invoice.id}
    Data: {invoice.created_at}

    --------------------------------


    TOTAL:                  {invoice.price} Kz

    Status: Paid

    ================================
    """

    return inv

def view_user(session):
    users = session.query(User).all()

    print("=" * 78)
    print("                           USER LIST")
    print("=" * 78)

    print(
        f"{'ID':<8}"
        f"{'NAME':<25}"
        f"{'EMAIL':<35}"
        f"{'CREATED AT':<15}"
        f"{'STATUS'}"
    )

    print("-" * 78)

    for user in users:
        status = "Active" if user.status else "Inactive"

        print(
            f"{user.id:<8}"
            f"{user.name:<25}"
            f"{user.email:<35}"
            f"{user.created_at.strftime('%d/%m/%Y'):<15}"
            f"{status}"
        )

    print("=" * 78)
