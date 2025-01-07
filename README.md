# CNG Streamlit App

This repository contains the code for a **Streamlit application** designed to visualize and analyze geospatial data using **Leaflet**. The app provides interactive features such as filtering and metrics for geospatial data related to a specific dataset.

## Overview

The process begins with **data scraping** and **geocoding** to gather and enrich data, followed by **joining addresses** to the dataset. The data is then converted into a **GeoJSON** format for geospatial analysis. This workflow is executed in a Python notebook and organized in the folder structure for easy use.

The Streamlit app provides an intuitive interface to interact with the geospatial data using **Leaflet** for visualization, along with **filtering buttons** and **metrics** to derive insights. It is designed to be easy to set up and run on your local machine.

## Features

- **Data Scraping**: Collecting data from external sources.
- **Geocoding**: Converting addresses to geographic coordinates.
- **Data Enrichment**: Joining address information to the data.
- **GeoJSON Conversion**: Converting enriched data into GeoJSON format for geospatial analysis.
- **Streamlit App**: A web app built with Streamlit that visualizes the data on a map using Leaflet.
- **Filter Button**: Users can filter the data interactively based on certain criteria.
- **Metrics**: Display key statistics and metrics about the data.
- **CNG Program Information**: An overview of the CNG program and its data.

## Installation

### Prerequisites

Ensure you have Python 3.8+ installed on your machine. You will also need to install the required dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/SammyGIS/cng_streamlit_app.git
cd cng_streamlit_app
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries such as `streamlit`, `geopandas`, `folium`, and others.

### Step 4: Run the Streamlit App

To run the app locally:

```bash
streamlit run app.py
```

This will launch a local server, and the app can be accessed at `http://localhost:8501` in your web browser.

## How to Use

Once the Streamlit app is running, you will be able to interact with the following features:

1. **Map Visualization**: The data will be displayed on a map using **Leaflet**.
2. **Filtering**: Use the filtering options to select specific data points based on your criteria.
3. **Metrics**: The app will display key metrics based on the selected data, such as the number of entries, average values, etc.
4. **Information**: Learn about the CNG program and its relevance to the data.


---

### Project Structure

```
cng_streamlit_app/
├── app.py               # Main Streamlit app file
├── notebook.py          # Jupyter notebook for data processing
├── requirements.txt     # Python dependencies for the project
├── data/                # Folder containing the data 
├── README.md            # Project documentation
```
