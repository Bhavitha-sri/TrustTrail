\# 🌿 TrustTrail



\### Blockchain-Verified Origin for Every Himalayan Farm \& Artisan Product



TrustTrail is a product-origin verification platform designed to help customers verify the authenticity and origin of Himalayan farm and artisan products such as honey, apples, saffron, and pashmina.



The platform connects \*\*producers and buyers through a transparent digital product journey\*\*, allowing buyers to verify product information using a QR code.



> 🚀 \*\*Hackathon Prototype:\*\* This version demonstrates the core TrustTrail workflow using Python, FastAPI, HTML, CSS, SQLite, and QR-code generation. Blockchain, IPFS, OTP authentication, maps, and real payment integration are planned for the production version.



\---



\## 🎯 Problem



Himalayan farm and artisan products can face problems such as:



\* ❌ Fake or misleading product origins

\* ❌ Lack of transparency for buyers

\* ❌ Difficulty verifying authentic producers

\* ❌ Limited visibility into the product journey

\* ❌ Middlemen reducing producer earnings

\* ❌ Delayed payments to producers



Customers need a simple way to know \*\*where a product came from and whether its origin can be trusted.\*\*



\---



\## 💡 Our Solution



TrustTrail provides a digital verification workflow:



\*\*Producer → Product Batch → QR Code → Buyer Verification → Product Journey → Payment Status\*\*



A producer registers their details and creates a product batch. TrustTrail generates a unique QR code for that batch.



When a buyer scans the QR code, they can view the registered product and producer information and follow the product's verification journey.



\---



\## ✨ Key Features



\### 👨‍🌾 Producer Registration



Producers can register their:



\* Name

\* Phone number

\* Location



\### 📦 Batch Registration



Producers can register product batches with:



\* Product name

\* Quantity

\* Origin

\* Product description



\### 🔲 QR Code Generation



Each registered product batch receives a unique QR code linked to its verification page.



\### 🔍 Product Verification



Buyers can open the QR-linked verification page to view:



\* Producer information

\* Product details

\* Origin

\* Verification status

\* Product journey

\* Payment status



\### 💰 Delivery \& Payment Simulation



The prototype includes a delivery action that changes the batch status to \*\*PAID\*\*, demonstrating the intended producer-payment workflow.



\---



\## 🏗️ System Architecture



```text

&#x20;                   ┌─────────────────────┐

&#x20;                   │       Producer      │

&#x20;                   │    Registration     │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │     FastAPI        │

&#x20;                   │      Backend       │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                   ┌──────────▼──────────┐

&#x20;                   │       SQLite        │

&#x20;                   │      Database       │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │     Batch Record    │

&#x20;                   │   + QR Generation   │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │      QR Code        │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                        Scan / Open

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │   Buyer Verify      │

&#x20;                   │       Page          │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Product Origin \&    │

&#x20;                   │ Journey Information │

&#x20;                   └─────────────────────┘

```



\---



\## 🛠️ Technology Stack



| Technology  | Purpose                |

| ----------- | ---------------------- |

| \*\*Python\*\*  | Backend programming    |

| \*\*FastAPI\*\* | Backend web framework  |

| \*\*Uvicorn\*\* | ASGI server            |

| \*\*SQLite\*\*  | Prototype database     |

| \*\*Jinja2\*\*  | HTML templating        |

| \*\*HTML5\*\*   | Frontend structure     |

| \*\*CSS3\*\*    | User interface styling |

| \*\*QRCode\*\*  | QR-code generation     |

| \*\*Pillow\*\*  | Image processing       |



\---



\## 📁 Project Structure



```text

TrustTrail/

│

├── main.py

├── database.py

├── requirements.txt

├── .gitignore

├── README.md

│

├── templates/

│   ├── index.html

│   ├── producer.html

│   ├── batch.html

│   ├── success.html

│   └── verify.html

│

├── static/

│   └── style.css

│

└── qr\_codes/

```



> Generated QR images and the local SQLite database are excluded from Git using `.gitignore`.



\---



\## ⚙️ Installation \& Setup



\### 1. Clone the repository



```bash

git clone https://github.com/Bhavitha-sri/TrustTrail.git

```



\### 2. Open the project



```bash

cd TrustTrail

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



\*\*Windows PowerShell:\*\*



```powershell

```



