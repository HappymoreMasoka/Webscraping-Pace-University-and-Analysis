Evaluating Pace University Curriculum through Web Scraping and Data Analysis
Author: Happymore Masoka
Repository: GitHub - Webscraping-Pace-University-and-Analysis
Date: May 2025

Abstract
This project explores the curriculum structure of Pace University using web scraping techniques to extract course data directly from the university’s public website. Through data analysis and visualization, the study aims to evaluate the distribution, focus areas, and depth of offerings within academic programs. The goal is to assess the alignment of curriculum content with current academic and industry standards, and provide insights into potential areas of improvement or innovation.

1. Introduction
University curricula play a vital role in shaping students’ academic and professional trajectories. As institutions continuously update their course offerings, it becomes necessary to periodically evaluate whether these offerings meet evolving academic trends and labor market demands. This project uses web scraping and data analysis as tools to extract, organize, and assess the course information provided by Pace University.

2. Objectives
To collect course information from Pace University’s website using web scraping.

To organize the collected data into a structured format suitable for analysis.

To identify patterns in course offerings, such as frequency, focus areas, and department distribution.

To draw conclusions about the curriculum's strengths and potential gaps.

3. Methodology
3.1 Web Scraping
Python’s requests and BeautifulSoup libraries were used to extract HTML data from the university’s course catalog. Each course entry, including the title, code, department, and description, was parsed and stored in a structured format.

3.2 Data Processing
The raw data was cleaned using pandas to remove duplicates, standardize department names, and isolate relevant keywords. The resulting dataset was then saved as a CSV file for reproducibility and further analysis.

3.3 Analysis
Exploratory Data Analysis (EDA) was conducted to identify:

The number of courses per department.

Keyword frequency in course descriptions (e.g., "data", "ethics", "AI").

Undergraduate vs. graduate course ratios.

Credit hour distribution.

Visualization tools such as matplotlib and seaborn were used to generate interpretable graphs.



