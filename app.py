import streamlit as st
import pandas as pd
import geopandas as gpd
import leafmap.foliumap as leafmap

# set constants variables
APP_TITLE = 'NIGERIA CNG Stations Locator App ⛽🌍📍'
FILE_PATH = "cng_locations_ng.geojson"
DEFAULT_CENTER = [9.0820, 8.6753]  # Nigeria's approximate center
DEFAULT_ZOOM = 5


# set page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon='⛽',
    layout='wide',
    initial_sidebar_state="expanded"
)

def load_data(file_path):
    """Load and return the GeoJSON data as GeoDataFrame"""
    try:
        return gpd.read_file(file_path)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None


def filter_data(data:gpd.GeoDataFrame, col_name:str):
    """File GeoDataFrame based on sidebar Selection"""
    # create a sorted unique name
    col_unique_list = [None] + sorted(data[col_name].dropna().unique().tolist())

    # select options
    selection = st.sidebar.selectbox(f"Selct {col_name}", col_unique_list,key=col_name, help=f"Filter stations by {col_name}")

    # filter based on selection
    if selection:
        selected_option = data[data[col_name] == selection]
    else:
        selected_option = data
    
    return selected_option

def get_long_lat(gdf):
    """Get the longitude and latitude from the GeoDataFrame to zoom to the layer"""
    gdf = gdf[['longitude', 'latitude']].astype(float)
    lon, lat = gdf.iloc[0]  # Extracting the first row's longitude and latitude values
    return lon, lat

def create_map(center=None, zoom=DEFAULT_ZOOM, data=None):
    """Create and configure the map"""
    m = leafmap.Map(
        center=center or DEFAULT_CENTER,
        zoom=zoom
    )
    
    m.add_tile_layer(
        url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
        name="Google Satellite",
        attribution="Google",
    )
    m.add_basemap("ROADMAP")
    
    if data is not None:
        m.add_gdf(
            data,
            layer_name="CNG Stations",
            fill_colors='green',
            zoom_to_layer=True
        )
    
    return m
        

def display_statistics(data):
    """Display comprehensive statistics about CNG stations"""
    st.subheader("CNG Station Statistics 📊")
    
    cols = st.columns(3)
    with cols[0]:
        st.metric(
            "Total Active Stations",
            len(data),
            help="Total number of operational CNG stations across Nigeria"
        )
    with cols[1]:
        st.metric(
            "States Coverage",
            data['State'].nunique(),
            help="Number of states with CNG stations"
        )
    with cols[2]:
        st.metric(
            "LGA Coverage",
            data['LGA'].nunique(),
            help="Number of Local Government Areas with CNG stations"
        )

def display_about_section():
    """Display comprehensive information about the application"""
    with st.sidebar.expander("About the Application", expanded=True):
        st.write("""
            # CNG Stations Locator Application 🌍📍

            Welcome to Nigeria's premier Compressed Natural Gas (CNG) station locator application. This comprehensive tool is designed to help drivers, fleet operators, and the general public easily locate CNG fueling stations across Nigeria.

            ## Key Features 🌟

            ### 1. Interactive Mapping System 🗺️
            - Real-time station location visualization
            - Satellite and road map views
            - Zoom and pan capabilities
            - Precise coordinate tracking

            ### 2. Advanced Search Functionality 🔍
            - Filter by State
            - Filter by Local Government Area
            - Filter by Station Name
            - Multi-level filtering support

            ### 3. Detailed Station Information ℹ️
            - Station names and operators
            - Exact location coordinates
            - Operating status
            - Local area information

            ### 4. Live Data Integration 🔄
            - Regular updates from official sources
            - Current operational status
            - Latest station additions

            ## Data Sources and Reliability 📋
            All information is sourced directly from the Presidential CNG Initiative (PCI) 
            database and verified station operators. Data is updated regularly to ensure 
            accuracy and reliability.

            Visit https://pci.gov.ng/conversion-centers for more information.
        """)

def display_conversion_program_info():
    """Display detailed information about the CNG conversion program"""
    # Add a container with custom styling
    with st.container():
        # Create two columns with small gap
        col = st.columns((10, 10), gap='small')
        
        # Left column - About the program
        with col[0]:
            # Add custom CSS styling for the header
            st.markdown("""
                <style>
                .program-header {
                    color: #2E4053;
                    padding: 10px 0;
                    border-bottom: 2px solid #85929E;
                }
                </style>
                """, unsafe_allow_html=True)
            
            st.markdown('<h2 class="program-header">About the program</h2>', unsafe_allow_html=True)
            
            # Program content with enhanced styling
            st.write("""
            ### Conversion Incentive Program 🚗💨

            The Federal Government of Nigeria (FGN) has introduced a **Conversion Incentive Program** to make it easier and more affordable for commercial and ride-share drivers to switch their vehicles to run on **Compressed Natural Gas (CNG)**. This initiative is part of the **Presidential CNG Initiative** aimed at promoting cleaner and more cost-effective fuel options. 🌍♻️

            Here's how it works: 

            😊 **FREE Conversions for Commercial Drivers** 🚕✅  
            Union-registered commercial vehicles in major cities where the program is active can get their vehicles converted to CNG **completely free of charge**, including labor costs.  

            😊 **50% Discount for Ride-Share Drivers** 🚖💸  
            If you're a ride-share driver (e.g., driving for services like Uber or Bolt), you can enjoy a **50% discount** on the cost of converting your vehicle to CNG.

            This program helps drivers save money on fuel, reduces pollution, and supports a greener future for Nigeria. 🌟🌱""")
            
            # Add a visual separator
            st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background: linear-gradient(to right, #f0f2f6, #4e8cff, #f0f2f6);'>", unsafe_allow_html=True)
        
        # Right column - Program Objectives
        with col[1]:
            # Add custom CSS for objectives section
            st.markdown("""
                <style>
                .objectives-header {
                    color: #2E4053;
                    padding: 10px 0;
                    border-bottom: 2px solid #85929E;
                }
                </style>
                """, unsafe_allow_html=True)
            
            st.markdown('<h2 class="objectives-header">Program Objectives 🎯</h2>', unsafe_allow_html=True)
            
            # Objectives content with consistent styling
            st.write("""
                     
            🎯 **Environmental Sustainability** 🏡
            - Reduce carbon emissions
            - Improve air quality in urban areas
            - Support Nigeria's climate change commitments

            🎯 **Economic Benefits** 💸💹
            - Lower fuel costs for drivers
            - Reduce dependency on imported fuel
            - Create new jobs in the CNG sector

            🎯 **Energy Security** ⚡⛽
            - Utilize Nigeria's abundant natural gas resources
            - Reduce pressure on foreign exchange
            - Diversify the transportation fuel mix
                     """)
            
            # Add a call-to-action button
            st.link_button(url="https://pci.gov.ng/cip-program",label="Learn More About CNG Benefits", help="Click to see detailed information about CNG benefits")
            
            # Add a visual separator
            st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background: linear-gradient(to right, #f0f2f6, #4e8cff, #f0f2f6);'>", unsafe_allow_html=True)

    # Add a footnote with data source
    st.caption("Source: Presidential CNG Initiative (PCI) - Official Program Documentation")

def main():
    st.title(APP_TITLE)
    
    # Load data
    data = load_data(FILE_PATH)
    if data is None:
        return
    
    # Sidebar
    st.sidebar.title("Station Filter Options ⬆️⬇️")
    st.sidebar.write("""
        Use these filters to find CNG stations in your area. You can filter by:
        - State
        - Local Government Area (LGA)
        - Station Name
    """)
    
    # Apply filters
    filtered_data = data
    for column in ["State", "LGA", "Name"]:
        filtered_data = filter_data(filtered_data, column)
    
    # Main content
    if not filtered_data.empty:
        display_statistics(filtered_data)
        
        st.markdown("---")
        st.subheader("Interactive Station Map 🗺️")
        
        lon, lat = get_long_lat(filtered_data)
        if lon and lat:
            st.write(f"📍 Selected Station Location: {lon:.4f}°E, {lat:.4f}°N")
            m = create_map([lat, lon], DEFAULT_ZOOM, data)
        else:
            m = create_map(data=data)
        
        m.to_streamlit(height=700)
        st.caption("Data source: Presidential CNG Initiative (PCI) - https://pci.gov.ng/conversion-centers")
    else:
        st.warning("No CNG stations found matching your selected filters. Please try different filter options.")
    
    # Information sections
    st.markdown("---")
    display_conversion_program_info()
    
    col2 = st.columns(2)
    with col2[0]:
        # Images
        st.image(
            "https://pci-gov-ng.b-cdn.net/static/img-optimized/conversion-gas.jpeg",
            caption="CNG Vehicle Conversion Process",
            width=600
        )
    with col2[1]:
        st.image(
            "https://pci-gov-ng.b-cdn.net/static/img-optimized/76661500.webp",
            caption="CNG: A Cleaner Alternative to PMS and Diesel Fuel",
            width=600
        )
    
    # About section in sidebar
    display_about_section()

if __name__ == "__main__":
    main()


