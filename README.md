# SIEM-Alert-Normalizer

🚀 **SIEM-Alert-Normalizer** is a clean, scalable **Python project using the Factory Design Pattern** to integrate with **IBM QRadar, Azure Sentinel, and Elastic SIEM**, fetch alerts, and normalize them into a **consistent structure for analysis, enrichment, and automation pipelines**.

It helps security teams:
- Unify alerts from multiple SIEM sources.
- Integrate normalized data into dashboards or ML pipelines.
- Simplify SOC operations with structured, reusable connectors and normalizers.

---

## 📂 Features

✅ Fetch alerts from **QRadar, Sentinel, Elastic** using modular connectors.  
✅ Normalize alerts into **a unified schema** with consistent fields.  
✅ Easily extensible for additional SIEM integrations.  
✅ Clean, readable, and testable architecture using **Factory Design Pattern**.  
✅ Includes unit tests for stability.

---

## 🛠️ Installation

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/alaafawzy/SIEM-Alert-Normalizer.git
cd SIEM-Alert-Normalizer
```

2️⃣ **Create and activate a virtual environment:**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

3️⃣ **Install required libraries:**
```bash
pip install -r requirements.txt
```

---

## 🚦 How to Use

### 1️⃣ Fetch and normalize QRadar alerts
```python
from services.factory.connection_factory import ConnectionFactory
from services.factory.normalization_factory import NormalizationFactory

connector = ConnectionFactory.get_connector(
    "qradar",
    host="https://qradar.example.com",
    token="YOUR_QRADAR_TOKEN"
)
alerts = connector.connect()

for alert in alerts:
    normalizer = NormalizationFactory.get_normalizer("qradar", alert)
    normalized_alert = normalizer.normalize()
    print(normalized_alert)
```

---

### 2️⃣ Fetch and normalize Sentinel alerts
```python
connector = ConnectionFactory.get_connector(
    "sentinel",
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    workspace_id="YOUR_WORKSPACE_ID"
)
alerts = connector.connect()

for alert in alerts:
    normalizer = NormalizationFactory.get_normalizer("sentinel", alert)
    normalized_alert = normalizer.normalize()
    print(normalized_alert)
```

---

### 3️⃣ Fetch and normalize Elastic alerts
```python
connector = ConnectionFactory.get_connector(
    "elastic",
    hosts=["http://localhost:9200"],
    username="elastic",
    password="YOUR_PASSWORD"
)
query = {"query": {"match_all": {}}}
alerts = connector.connect(index="alerts-*", query=query)

for alert in alerts:
    normalizer = NormalizationFactory.get_normalizer("elastic", alert)
    normalized_alert = normalizer.normalize()
    print(normalized_alert)
```

---

## 🪐 Normalized Schema

All SIEM alerts are normalized into:
- `source_type`
- `alert_severity`
- `status`
- `reason`
- `rule`
- `source_ip`
- `destination_ip`
- `user_name`
- `host_name`
- `time_stamp`
- `raw` (original data)

---

## 🧪 Running Tests

Ensure the environment is activated, then:
```bash
python -m pytest tests/
```

---

## 🚩 Extending the Project

To add a new SIEM:
1️⃣ Create a connector under `services/connection/`.  
2️⃣ Create a normalizer under `services/normalization/`.  
3️⃣ Register them in:
   - `services/factory/connection_factory.py`
   - `services/factory/normalization_factory.py`

---

## 🤝 Contributing

✅ Fork the repository.  
✅ Create a feature branch.  
✅ Commit and push your changes.  
✅ Open a pull request.

---

## 📞 Contact

If you need enhancements or integrations with your pipelines, feel free to reach out.
