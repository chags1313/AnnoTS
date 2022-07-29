---
title: 'AnnoTS: a multi-activity annotation tool for inertial measurement unit data'

tags:
  - Annotation
  - Feature Extraction
  - User Interface
  - Human Activity Recognition
  - Machine Learning

authors:
  - name: Cole J. Hagen
    orcid: 0000-0001-7241-8455
    corresponding: true # (This is how to denote the corresponding author)
    affiliation: 1 
  - name: Tessa C. Johnson
    affiliation: 1
  - name: Shivayogi V. Hiremath
    affiliation: 1
affiliations:
 - name: Personal Health Informatics Lab, Temple University, United States
   index: 1

date: 27 July 2022
bibliography: paper.bib
---
# Statement of need
Developing high-quality classification models for human activity recognition often relies on manual annotation of inertial measurement unit data (IMU). For example, applying a machine learning classifier to identify standing, sitting, and laying from three-axis accelerometer recordings requires precise ground truth annotations to correctly delineate subtle differences in acceleration between each activity. Despite the wide availability of annotation software, there is current demand for user-friendly annotation tools that accommodate more than one time-series signal (e.g., x-axis, y-axis, and z-axis accelerometer and gyroscope) and offer customizable labeling options for subsequent training and validation of machine learning models. 

Time-series annotation software must satisfy various user requirements. First, the tool should operate with similar functionality for different data sources (e.g., accelerometer, gyroscope). Also, the tool should support loading of a variety of unique datasets with more than one time-series signals. Further, the tool should take the form of a graphical user interface (GUI) to promote user accessibility, facilitate rapid annotations, and reduce potential errors through visualization of data [@Solsona-Berga:2020]. Finally, the tool should allow users to seamlessly navigate their dataset (using multiple features such as zooming and scrolling) and visualize labeled data overlying time-series signals.

Annotation Tool for Time Series Data (AnnoTS) facilitates manual annotation of large datasets with multiple time-series signals via a user-friendly GUI. Users of AnnoTS can assign custom labels and implement unlimited annotations to segment any span of signal data on a large graphical display. Users can easily implement and edit annotations with manual input (i.e., index of signal data) or a modifiable annotation window. Moveable widgets further allow users to customize their GUI display. All data may be saved to a .csv format with annotations corresponding to time-series signals. The main graphical display provides several export options (e.g., .png, .jpg, .sav) for images of signal data with annotation windows. Furthermore, the AnnoTS repository offers scripts for further time-series analyses such as feature extraction and supervised machine learning.  AnnoTS is currently being used to identify patterns of arm movement from Actigraph IMU data for machine learning classification of upper extremity movements. However, the AnnoTS repository provides users the flexibility to make AnnoTS compatible with other data sources and machine learning applications.

# Summary
Though other annotation tools are available for time-series data [@Solsona-Berga:2020, @Fedjajevs:2020, @Haladjian:2019], there is demand for open-source and standalone annotation software that accommodates multiple data sources. We designed `AnnoTS` as a GUI-based annotation software using several Python libraries (PyQT5, pyqtgraph, and pandas) to annotate IMU data for the application of supervised machine learning. Users can freely access the application as a standalone executable or open-source Python code and customize the tool to support their data annotation needs. Researchers, data scientists, and students will benefit from AnnoTS’s GUI to develop precise reference datasets to train high-quality human recognition algorithms. 

# Features
-	Upload large datasets (tested between 100,000 and 300,000 rows)
-	Label several different annotations (up to 17)
-	Graph multiple time-series signals
-	Graph interactions (zoom, pan, axes customization, data manipulation, export)
-	Customize label names and annotation locations
-	Click and drag unlimited time-locked segmentations
-	Save multiple signals with all time-locked classifications
-	Optional: Extract statistical features and apply supervised machine learning

![Example project using accelerometry data to assess 5 arm activities (e.g., reaching, lifting, etc.) with corresponding color-coded annotations over the course of over 160,000 data points. Customized labels are visible on the left of the GUI. Tools are shown at the bottom of the GUI. The user can use the “Time Tool” (represented by the black line with the black circle cursor) to retrieve information about a specific data point (visible in the middle of the GUI). /label{fig:fig1}](graphicalabstractfig.png)


# Acknowledgements
This work was supported by The Assistant Secretary of Defense for Health Affairs endorsed by the Department of Defense through the Spinal Cord Injury Research Program under Award No. W81XWH-21-1-0637. Opinions, interpretations, conclusions and recommendations are those of the author and are not necessarily endorsed by the Department of Defense.

# References


