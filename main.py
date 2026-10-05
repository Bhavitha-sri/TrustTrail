from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import qrcode
import os

from database import get_connection, create_tables


app = FastAPI(title="TrustTrail")


# Create required folders
os.makedirs("qr_codes", exist_ok=True)
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)


# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# QR code files
app.mount(
    "/qr_codes",
    StaticFiles(directory="qr_codes"),
    name="qr_codes"
)


# HTML templates
templates = Jinja2Templates(directory="templates")


# Create database tables
create_tables()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# --------------------------------------------------
# PRODUCER REGISTRATION PAGE
# --------------------------------------------------

@app.get("/producer", response_class=HTMLResponse)
def producer_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="producer.html",
        context={}
    )


# --------------------------------------------------
# CREATE PRODUCER
# --------------------------------------------------

@app.post("/producer/create")
def create_producer(
    name: str = Form(...),
    phone: str = Form(...),
    location: str = Form(...)
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO producers (name, phone, location)
        VALUES (?, ?, ?)
        """,
        (name, phone, location)
    )

    producer_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return RedirectResponse(
        url=f"/batch?producer_id={producer_id}",
        status_code=303
    )


# --------------------------------------------------
# BATCH REGISTRATION PAGE
# --------------------------------------------------

@app.get("/batch", response_class=HTMLResponse)
def batch_page(
    request: Request,
    producer_id: int
):
    connection = get_connection()

    producer = connection.execute(
        """
        SELECT *
        FROM producers
        WHERE id = ?
        """,
        (producer_id,)
    ).fetchone()

    connection.close()

    return templates.TemplateResponse(
        request=request,
        name="batch.html",
        context={
            "producer": producer
        }
    )


# --------------------------------------------------
# CREATE PRODUCT BATCH
# --------------------------------------------------

@app.post("/batch/create")
def create_batch(
    producer_id: int = Form(...),
    product_name: str = Form(...),
    quantity: str = Form(...),
    origin: str = Form(...),
    description: str = Form("")
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO batches
        (
            producer_id,
            product_name,
            quantity,
            origin,
            description
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            producer_id,
            product_name,
            quantity,
            origin,
            description
        )
    )

    batch_id = cursor.lastrowid

    # QR code will open the verification page
    qr_data = f"http://127.0.0.1:8000/verify/{batch_id}"

    qr = qrcode.make(qr_data)

    qr_filename = f"batch_{batch_id}.png"
    qr_path = os.path.join(
        "qr_codes",
        qr_filename
    )

    qr.save(qr_path)

    # Save QR filename in database
    cursor.execute(
        """
        UPDATE batches
        SET qr_file = ?
        WHERE id = ?
        """,
        (
            qr_filename,
            batch_id
        )
    )

    connection.commit()
    connection.close()

    return RedirectResponse(
        url=f"/batch/success/{batch_id}",
        status_code=303
    )


# --------------------------------------------------
# BATCH SUCCESS PAGE
# --------------------------------------------------

@app.get(
    "/batch/success/{batch_id}",
    response_class=HTMLResponse
)
def batch_success(
    request: Request,
    batch_id: int
):
    connection = get_connection()

    batch = connection.execute(
        """
        SELECT
            batches.*,
            producers.name AS producer_name
        FROM batches
        JOIN producers
            ON batches.producer_id = producers.id
        WHERE batches.id = ?
        """,
        (batch_id,)
    ).fetchone()

    connection.close()

    return templates.TemplateResponse(
        request=request,
        name="success.html",
        context={
            "batch": batch
        }
    )


# --------------------------------------------------
# PRODUCT VERIFICATION PAGE
# --------------------------------------------------

@app.get(
    "/verify/{batch_id}",
    response_class=HTMLResponse
)
def verify_batch(
    request: Request,
    batch_id: int
):
    connection = get_connection()

    batch = connection.execute(
        """
        SELECT
            batches.*,
            producers.name AS producer_name,
            producers.phone AS producer_phone,
            producers.location AS producer_location
        FROM batches
        JOIN producers
            ON batches.producer_id = producers.id
        WHERE batches.id = ?
        """,
        (batch_id,)
    ).fetchone()

    connection.close()

    return templates.TemplateResponse(
        request=request,
        name="verify.html",
        context={
            "batch": batch
        }
    )


# --------------------------------------------------
# SIMULATE DELIVERY AND PAYMENT
# --------------------------------------------------

@app.post("/delivery/{batch_id}")
def mark_delivery(batch_id: int):

    connection = get_connection()

    connection.execute(
        """
        UPDATE batches
        SET status = 'PAID'
        WHERE id = ?
        """,
        (batch_id,)
    )

    connection.commit()
    connection.close()

    return RedirectResponse(
        url=f"/verify/{batch_id}",
        status_code=303
    )