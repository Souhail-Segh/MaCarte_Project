# MaCarte

MaCarte is a Django-based interactive map application that allows users to manage markers and associate photos with them. Users can upload photos for specific markers and view the last uploaded photo in an interactive map interface. The app provides a simple and intuitive way to organize locations and their associated visual content.

---

## Features

- **Marker Management**:
  - Add, delete, and update markers on the map.
  - Store markers with latitude, longitude, and names.

- **Photo Management**:
  - Upload photos and associate them with specific markers.
  - View the last uploaded photo for each marker directly on the map.

- **Dynamic Categories**:
  - Organize photos into categories.
  - Create new categories dynamically during photo upload.

- **Interactive Map**:
  - Display markers with popups showing the last uploaded photo and marker details.
  - Add photo functionality directly from the marker popup.

---

## Installation

Follow these steps to set up and run the MaCarte project locally:

### Prerequisites

- Python 3.10 or higher
- Django 5.1.4
- SQLite (default) or any other database supported by Django
- A virtual environment tool (optional but recommended)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd MaCarte
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://localhost:8000/`, still in local for the moment.

---

## Usage

### 1. Add Markers
- Navigate to the map interface.
- Add markers by specifying the location and name.

### 2. Upload Photos
- Click on a marker to view its popup.
- Use the **Add Picture** button to upload a photo for that marker.
- Fill out the form, select a category, and upload the image.

### 3. View Photos
- Click on a marker to see the last uploaded photo and its details.
- Photos are dynamically fetched and displayed in the marker popup.

---

## Project Structure

```
MaCarte/
|-- gallery/         # App for managing photos and categories
|-- map/             # App for managing markers
|-- MaCarte/         # Project configuration
|-- users/           # User login, logout, registration, ...
|-- static/          # Static files (CSS, JS, etc.)
|-- media/           # Uploaded media files
|-- manage.py        # Django management script
```

---

## API Endpoints

### `/get_markers/`
- **Method**: GET
- **Description**: Fetch all markers along with their details and last uploaded photo.

### `/add/`
- **Method**: GET/POST
- **Description**: Upload a photo and associate it with a marker.

---

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Leaflet.js for map interaction)
- **Database**: SQLite (default, configurable to others)
- **Media Storage**: Local file system (configurable for cloud storage)
- **Cloud Storage**: Integrate cloud storage for photos (AWS S3).

---

## Future Enhancements

- Add more flexibility in filters.
- Add search functionality for markers and photos.
- Add interactive scroll options.
- Implement the website application online (Heroku).

---

## Contribution

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the ALX License. See the `LICENSE` file for details.

---

## Contact

If you have any questions or need assistance, please contact:
- **Developer**: Souhail Segh
- **Email**: [souhail.segh.ds@gmail.com]

Happy mapping, happy souvenirs!

