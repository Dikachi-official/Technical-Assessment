# 🧾 Simple Invoicing API — Django REST Framework

This project is a simplified backend API for a small business invoicing tool, built with **Django** and **Django REST Framework (DRF)**.  
It allows you to create customers, generate invoices with multiple line items, and track the status of each invoice (e.g., pending, paid, overdue).

---

## 📦 Features

- ✅ Create and list customers
- ✅ Create invoices with nested line items
- ✅ View invoice details including total amount
- ✅ Update invoice status (e.g., mark as paid)
- ✅ Automatic total calculation for each item and invoice
- ✅ Basic validation (e.g., due date ≥ issue date, no empty invoice items)
- ✅ Sample data and Postman collection included for testing

---

## 🚀 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default, but can be swapped for PostgreSQL)

---

## 🏗 Project Structure



backend-project/
├── api/             # Django app with models, views, serializers
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── invoice_project\_postman\_collection.json  # Postman collection for testing API
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

`

---

## ⚙ Installation & Setup

1. **Clone the repo**

bash
git clone https://github.com/Dikachi-official/Technical-Assessment.git
cd backend-project
`

2. **Create and activate a virtual environment**

bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate


3. **Install dependencies**

bash
pip install -r requirements.txt


4. **Apply migrations**

bash
python manage.py migrate



7. **Run the development server**

bash
python manage.py runserver


Your API will now be live at `http://localhost:8000/`

---

## 🔌 API Endpoints

| Method | Endpoint                     | Description                      |
| ------ | ---------------------------- | -------------------------------- |
| POST   | `/api/customers/`            | Create a new customer            |
| GET    | `/api/customers/`            | List all customers               |
| POST   | `/api/invoices/`             | Create an invoice with items     |
| GET    | `/api/invoices/<id>/`        | Retrieve full invoice with items |
| PATCH  | `/api/invoices/<id>/status/` | Update only the invoice status   |

---

## 📮 Sample Request (Invoice Creation)

**POST** `/api/invoices/`

json
{
  "customer": 1,
  "issue_date": "2025-07-01",
  "due_date": "2025-07-10",
  "status": "pending",
  "items": [
    {
      "description": "Web Design",
      "quantity": 2,
      "unit_price": "150.00"
    },
    {
      "description": "Hosting",
      "quantity": 1,
      "unit_price": "50.00"
    }
  ]
}


---

## 🧪 Testing with Postman

1. Open Postman
2. Click **Import** → Choose `INVOICE PROJECT.postman_collection.json`
3. Use the included requests to:

   * Create a customer
   * Create an invoice
   * View invoice details
   * Update status

---

## ✅ Validation Rules

* `due_date` must not be before `issue_date`
* Each invoice must have **at least one** item
* `quantity` must be a positive integer
* `total` is auto-calculated as `quantity × unit_price`
* `total_amount` for invoice is computed from all its items

---

## 🧪 Optional: Run Unit Tests (if implemented)

bash
python manage.py test


---

## 🛠 Environment Configuration (optional)

You can use environment variables for:

* Switching databases (SQLite → PostgreSQL)
* Secret keys, debug mode, etc.

Add a `.env` file and use `python-decouple` or `django-environ` if needed.

---

## 📤 Deployment Notes

For deploying to production:

* Set `DEBUG = False`
* Use PostgreSQL for performance
* Secure your secret key and apply proper CORS settings

---

## 👤 Author

Made with ❤ by \Dikachi-official
Feel free to fork or suggest improvements!

---

## 📄 License

This project is open source under the [MIT License](LICENSE).


```