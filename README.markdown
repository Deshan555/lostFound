# Lost & Found Project

A robust FastAPI-based system enhanced with image matching capabilities for managing and filtering lost item records. This system integrates MySQL for database management, stores image files on a local VM, and provides a scalable backend with an optional frontend interface.

![Alt text](system.png)

## Project Overview

The Lost & Found Project enables users to:
- Report lost items with details including images, item type, description, date lost, and location.
- Perform image-based matching to identify similar lost items using OpenCV's ORB feature detection.
- Filter and search records based on various criteria (e.g., item type, date range, location).
- Manage records via a RESTful API with MySQL as the backend database.

The system leverages FastAPI, SQLAlchemy, Pydantic, OpenCV, and MySQL, with an optional React-based frontend using TypeScript.

## Project Structure

The project is organized into `backend` and `frontend` directories. Below is the detailed folder structure:

```
lost-and-found/
├── backend/
│   ├── __init__.py                # Marks directory as Python package
│   ├── main.py                    # FastAPI application entry point
│   ├── actions/
│   │   ├── __init__.py            # Marks directory as Python package
│   │   ├── lostRecords_action.py  # Actions related to lost item operations
│   │   └── user_actions.py        # Actions related to user operations
│   ├── auth/
│   │   ├── __init__.py            # Marks directory as Python package
│   │   └── auth.py                # Authentication logic
│   ├── config/
│   │   ├── __init__.py            # Marks directory as Python package
│   │   ├── connectionCheck.py     # Database connection checks
│   │   ├── database.py            # Database configuration
│   │   └── dbinit.py              # Database initialization
│   ├── models/
│   │   ├── __init__.py            # Marks directory as Python package
│   │   ├── document.py            # Model for document-related lost items
│   │   ├── electronics.py         # Model for electronics lost items
│   │   ├── findRecords.py         # Model for record retrieval logic
│   │   ├── jewelry.py             # Model for jewelry lost items
│   │   ├── lostRecords.py         # Core model for lost items
│   │   ├── others.py              # Model for miscellaneous lost items
│   │   ├── pets.py                # Model for pet-related lost items
│   │   ├── policeStationData.py   # Model for police station data
│   │   ├── users.py               # Model for user data
│   │   └── wallet.py              # Model for wallet-related lost items
│   ├── schemas/
│   │   ├── __init__.py            # Marks directory as Python package
│   │   ├── custom_response.py     # Custom response schemas
│   │   ├── documents_schema.py    # Schema for document-related items
│   │   ├── electronics_schema.py  # Schema for electronics items
│   │   ├── jewelry_schema.py      # Schema for jewelry items
│   │   ├── lostRecords_schema.py  # Core schema for lost items
│   │   ├── others_schema.py       # Schema for miscellaneous items
│   │   ├── pets_schema.py         # Schema for pet-related items
│   │   ├── user_schema.py         # Schema for user data
│   │   └── wallets_schema.py      # Schema for wallet-related items
│   ├── services/
│   │   ├── __init__.py            # Marks directory as Python package
│   │   ├── lostRecords.py         # Service layer for lost item operations
│   │   ├── uploads.py             # Service for handling image uploads
│   │   └── user.py                # Service layer for user operations
│   ├── static/
│   │   ├── env                    # Environment configuration
│   │   ├── image.py               # Image handling utilities
│   │   └── image-match.py         # Image matching logic
│   └── requirements.txt           # Python dependencies
├── frontend/
│   ├── package.json               # Node.js dependencies and scripts
│   ├── tsconfig.json              # TypeScript configuration
│   ├── src/
│   │   ├── index.tsx              # Frontend entry point
│   │   ├── components/            # Reusable React components
│   │   ├── pages/                 # Page-specific components
│   │   ├── styles/                # CSS or Tailwind CSS styles
│   │   └── assets/                # Static assets
├── .gitignore                     # Git ignore file
├── README.md                      # Project documentation (this file)
└── docker-compose.yml             # Optional Docker configuration
```

### Directory Descriptions

- **`backend/`**: Contains all backend-related code.
  - **`main.py`**: Initializes the FastAPI app and mounts routers.
  - **`actions/`**: Defines business logic actions.
    - `lostRecords_action.py`: Handles lost item CRUD operations.
    - `user_actions.py`: Manages user-related actions.
  - **`auth/`**: Authentication module.
    - `auth.py`: Implements user authentication logic.
  - **`config/`**: Configuration and database setup.
    - `connectionCheck.py`: Verifies database connectivity.
    - `database.py`: Configures MySQL engine and session.
    - `dbinit.py`: Initializes the database schema.
  - **`models/`**: SQLAlchemy ORM models for various item types and users.
  - **`schemas/`**: Pydantic models for data validation.
  - **`services/`**: Service layer for business logic.
    - `uploads.py`: Manages image uploads to the local VM.
  - **`static/`**: Utilities for environment and image handling.
    - `image-match.py`: Contains image matching logic using OpenCV.
  - **`requirements.txt`**: Lists dependencies (e.g., `fastapi`, `sqlalchemy`, `pydantic`, `opencv-python`, `mysql-connector-python`).

- **`frontend/`**: Optional React-based UI.
  - **`src/`**: Contains frontend source code with components, pages, styles, and assets.

- **`.gitignore`**: Excludes files like `__pycache__` and `node_modules`.
- **`docker-compose.yml`**: (Optional) Defines services for backend and MySQL.

## Data & ORM

- **Database**: MySQL stores lost item records and user data on a local VM.
- **ORM Models** (`models/`): Define tables for various item types (e.g., `lostRecords.py` for core lost items).
- **Session Management** (`config/database.py`): Configures MySQL connection and session factory.

## Endpoints & Models

- **`POST /lost`**: Creates a lost item with an optional image.
- **`POST /lost/custom`**: Filters lost items based on criteria.
- **`POST /lost/match`**: Performs image matching and returns similar items.

## Image Matching

The system includes an image matching feature using OpenCV's ORB algorithm, storing images on a local VM. The `image-match.py` file contains the following function:

```python
import cv2
import os
import json
from pathlib import Path

def feature_matching(query_image_path, folder_path, min_matches=10):
    """
    Perform feature matching between a query image and all images in a folder.
    Returns results as a JSON array with image paths and match counts.
    """
    orb = cv2.ORB_create()
    query_img = cv2.imread(query_image_path, cv2.IMREAD_GRAYSCALE)
    if query_img is None:
        raise ValueError(f"Could not load query image: {query_image_path}")
    query_kp, query_desc = orb.detectAndCompute(query_img, None)
    if query_desc is None:
        raise ValueError("No descriptors found in query image")
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    results = []
    for img_path in Path(folder_path).glob("*.[jp][pn][gf]"):
        img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        kp, desc = orb.detectAndCompute(img, None)
        if desc is None:
            continue
        matches = matcher.knnMatch(query_desc, desc, k=2)
        good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]
        if len(good_matches) >= min_matches:
            results.append({
                "image_path": str(img_path),
                "match_count": len(good_matches)
            })
    return sorted(results, key=lambda x: x["match_count"], reverse=True)

def save_results_to_json(results, output_json_path):
    """
    Save the matching results to a JSON file.
    """
    with open(output_json_path, 'w') as f:
        json.dump(results, f, indent=4)

def main():
    query_image_path = "samples/image.jpeg"
    folder_path = "samples"
    output_json_path = "matching_results.json"
    try:
        results = feature_matching(query_image_path, folder_path)
        save_results_to_json(results, output_json_path)
        print(f"Results saved to {output_json_path}")
        print(json.dumps(results, indent=4))
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/lost-and-found.git
   cd lost-and-found
   ```

2. **Set Up the Backend**:
   - Install Python 3.8+ and create a virtual environment.
   - Install dependencies:
     ```bash
     pip install -r backend/requirements.txt
     ```
   - Configure MySQL on the local VM and update `config/database.py` with credentials.

3. **Set Up the Frontend** (Optional):
   - `cd frontend` and run `npm install`.
   - Start the frontend: `npm start`.

4. **Run the Application**:
   ```bash
   uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```

5. **Access the API**:
   - Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for API documentation.

## Dependencies

- Backend: `fastapi`, `sqlalchemy`, `pydantic`, `opencv-python`, `mysql-connector-python`.
- Frontend: `react`, `typescript`, `axios`.

## Development Notes

- **Image Storage**: Images are stored on a local VM; update `folder_path` in `image-match.py` accordingly.
- **MySQL**: Ensure the database is initialized with `dbinit.py`.
- **Testing**: Use `pytest` for backend and `jest` for frontend.

## Contributing

Fork the repository, create a feature branch, commit changes, and open a pull request.

## License

MIT License.
