## 🚀 **Technologies Used**

- **Python 3.11+**
- **FastAPI** - Modern and fast web framework
- **Uvicorn** - ASGI server for Python applications
- **Pydantic** - Data validation and serialization
- **Unittest** - Python's native testing framework

## 📁 **Project Structure**

```
ebanx_test/
├── src/                      # App Core
│   ├── controllers/            # Business logic
│   │   └── interfaces/           # Interfaces and abstractions
│   ├── models/                 # Data models
│   ├── views/                  # HTTP/API layer
│   │   └── interfaces/           # Interfaces and abstractions
│   ├── tests/                  # Unit tests
│   └── main.py                 # Application entry point
├── requirements.txt          # External Packages
└── README.md
```

## 🔧 **Installation and Setup**

### **1. Clone the repository**

```bash
git clone https://github.com/caiogbriel/ebanx_test.git
cd ebanx_test
```

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

### **3. Run the application**

```bash
fastapi dev src/main.py
```

The API will be available at: `http://localhost:8000`

## 📚 **API Documentation**

After starting the application, access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🧪 **Running Tests**

### **All tests:**

```bash
cd src
python -m unittest -v
```
