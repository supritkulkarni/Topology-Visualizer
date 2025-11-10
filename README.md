# Topology Visualizer

A full-stack network topology visualizer built with **Django**, **Django REST Framework**, and **Cytoscape.js**. It models nodes and edges in a graph, exposes RESTful APIs, and renders an interactive frontend for exploring network structures.

---

## Features

- REST API for nodes, edges, and full graph
- Cytoscape.js frontend with dynamic layout
- Node/edge metadata support (e.g. bandwidth, latency, type)
- Seed command for demo data
- Clean project structure with security best practices

---

## Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| Backend      | Django, DRF              |
| Frontend     | Cytoscape.js             |
| Data Model   | PostgreSQL or SQLite     |
| Styling      | CSS                      |
| API Format   | JSON                     |

---

## Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/topology-visualizer.git
cd topology-visualizer/topo_project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Seed demo data
python manage.py seed_topology

# Run server
python manage.py runserver


# Endpoint	Description
/api/nodes/	: List/create/update nodes
/api/edges/ :	List/create/update edges
/api/graph/	: Combined node + edge JSON

Example response from /api/graph/:
{
  "elements": [
    { "data": { "id": "1", "label": "Router-1", "type": "router" } },
    { "data": { "id": "e1", "source": "1", "target": "2", "label": "Router-1 → Switch-1" } }
  ]
}

Visit http://127.0.0.1:8000/ to view the interactive topology diagram.

Nodes styled by type (router, switch, host)

Edges show bandwidth, latency, and direction

Layout auto-adjusts using Cytoscape's cose algorithm

# Project Structure
topo_project/
├── manage.py
├── topo/
│   ├── models.py
│   ├── views_api.py
│   ├── serializers.py
│   ├── api_urls.py
│   ├── urls.py
│   ├── templates/topo/topology.html
│   └── static/topo/topology.js

# Create a .env file or use .env.example:
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost

# Testing
python manage.py test

# Contributing
Pull requests welcome! For major changes, open an issue first to discuss what you’d like to change.

# Contact
Built by https://github.com/supritkulkarni aka n3ur0n
For inquiries or collaboration, feel free to reach out via GitHub.
---

Let me know if you'd like to add:
- Screenshots or GIFs of the live graph
- Deployment instructions (e.g. Heroku, Docker)
- A badge section (build status, license, etc.)


For inquiries or collaboration, feel free to reach out via GitHub.

