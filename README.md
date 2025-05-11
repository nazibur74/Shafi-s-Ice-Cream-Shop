# 🍨 Shafi's Ice Cream Shop  
**Author**: Nazibur Rahman
**Institution**: Daffodil International University

**Shafi's Ice Cream Shop** is a **Django-based demo project** that functions as a basic for small ice cream businesses.

---

## 💻 Tech Stack

- **Backend**: Django (Python)  
- **Database**: SQLite  
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript  
- **Authentication**: Django Auth System  
- **Templating**: Django Templates

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/shafi-icecream-shop.git
cd shafi-icecream-shop

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Start development server
python manage.py runserver
````

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📊 Future Enhancements

* 📦 Barcode scanning support
* 📈 Graph-based sales analytics (using Chart.js or Plotly)
* 📧 Email alerts for low stock
* 🔒 Role-based permission levels (admin/cashier)
