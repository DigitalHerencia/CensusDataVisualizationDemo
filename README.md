<div align=center>

# US Census CPS Data Visualization


[![Streamlit](https://img.shields.io/badge/Streamlit-0E1E24?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-digitalherencia-black.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/digitalherencia/CensusDataVisualizationDemo) 
[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0)
[![FTP Server](https://img.shields.io/badge/FTP-Server-blue?style=for-the-badge&logo=server&logoColor=white)](ftp://ftp.census.gov)
[![US Census Bureau](https://img.shields.io/badge/US_Census_Bureau-004B87?style=for-the-badge&logo=gov&logoColor=white)](https://www.census.gov)
[![Current Population Survey](https://img.shields.io/badge/Current_Population_Survey-0A0A0A?style=for-the-badge&logo=gov&logoColor=white)](https://www.census.gov/programs-surveys/cps.html)

</div>

## Description

This project visualizes data from the Current Population Survey (CPS) using Streamlit, Altair, and Plotly. The visualizations provide insights into employment status, education level, and age distribution across different demographics in the United States.

## Project Structure

📦scripts  
┣ 📜app.py  
┣ 📜headers.py  
┗ 📜requirements.txt  
📦data  
┗ 📜2024_Basic_CPS_Public_Use_Record_Layout_plus_IO_Code_list.txt  

## Features

- **Age Distribution by Employment Status**
![alt text](data/AgeDistributionbyEmploymentStatus.png)

---

- **Education Level by Sex**
  ![Education Level by Sex](data/EducationLevelbySex.png)

---

- **Employment Status by Age and Sex**
![alt text](data/EmploymentStatusbyAgeandSex.png)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/digitalherencia/CensusDataVisualizationDemo.git
    cd CensusDataVisualizationDemo
    ```

2. **Set up the virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    pip install -r scripts/requirements.txt
    ```

3. **Run the application:**
    ```sh
    streamlit run scripts/app.py
    ```

## Usage

The app fetches the latest CPS data, preprocesses it, and generates interactive visualizations. Open the app in your browser and explore the various charts and graphs to gain insights into the employment and education statistics.

## Visualizations

### 1. Age Distribution by Employment Status
This Plotly box plot shows the distribution of ages for different employment statuses. Hover over the boxes to see detailed statistics.

### 2. Education Level by Sex
This Altair chart shows the education level distribution by sex. Hover over the bars to see details.

### 3. Employment Status by Age and Sex (Heatmap)
This heatmap shows the density of different age groups within each employment status, split by sex.

## License

This project is licensed under the GPLv3.

## Contact

For any inquiries or feedback, please contact [digitalherencia@outlook.com](mailto:digitalherencia@outlook.com).
