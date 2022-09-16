# Trash classification application

This application uses the dataset as a training set:
[TACO dataset on Kaggle](https://www.kaggle.com/datasets/kneroma/tacotrashdataset?select=meta_df.csv)

# What's The Bin.. L'application qui t'aide à trier tes déchets..

# What is it?
This repository contains :
- a **[Computer vision classification model](#the-model)**, trained to predict the bin category of garbage from the Flagship  of Lille city, our client.
- an **[app](#the-application)** (streamlit) who serves as a graphical interface for the model, and it's an application dedicated to Flagship learners and staff.


# The model
>The model we are using is [Keras](https://keras.io/guides/).
Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result as fast as possible is key to doing good research.

Keras is:

> - Simple -- but not simplistic. Keras reduces developer cognitive load to free you to focus on the parts of the problem that really matter.
> - Flexible -- Keras adopts the principle of progressive disclosure of complexity: simple workflows should be quick and easy, while arbitrarily advanced workflows should be possible via a clear path that builds upon what you've already learned.
> - Powerful -- Keras provides industry-strength performance and scalability: it is used by organizations and companies including NASA, YouTube, and Waymo.

We are using the efficient Convolutional Neural Networks for mobile vision applications **MobileNetV3** .
This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

We also tried other models that we ended up not using, such as:
- Xception
- Resnet32

## Features
The model needs pictures of users's garbage which must be resized to make predictions. It predicts the bin category of garbage object in 9 categories: Battery, Glass, Metal, Cardboard, Paper, Organic, Clothes, Trash and Plastic.


# The application
The application was made using **streamlit** in order to have a simple but good result while **saving development time**.

The **goal** of this application is **to provide easier predictions** to the user following these categories :
- Battery,
- Glass,
- Metal,
- Cardboard, 
- Paper,
- Organic,
- Clothes, 
- Trash 
- Plastic


# Start the application 
> - Use the "docker" branch
> - Install and launch Docker Desktop
> - At the root of the project folder: Build the images with `docker-compose build` then `docker-compose up` to run the apps
> - The application start at this address: http://localhost:8501/ (or "Open app in browser" from Docker Desktop application)

### Main skills:

![Python](https://img.shields.io/badge/-Python-0D1117?style=for-the-badge&logo=python&labelColor=0D1117&textColor=0D1117)&nbsp;

### Tools:

![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-0D1117?style=for-the-badge&logo=visual-studio-code&logoColor=007ACC&labelColor=0D1117)&nbsp;
![Git](https://img.shields.io/badge/-Git-0D1117?style=for-the-badge&logo=git&labelColor=0D1117)&nbsp;
![GitHub](https://img.shields.io/badge/-GitHub-0D1117?style=for-the-badge&logo=github&labelColor=0D1117)&nbsp;
![Windows](https://img.shields.io/badge/-Windows-0D1117?style=for-the-badge&logo=windows&labelColor=0D1117)&nbsp;
![microsoft-office](https://img.shields.io/badge/-microsoft_office-0D1117?style=for-the-badge&logo=microsoft-office&labelColor=0D1117)&nbsp;
![Linux](https://img.shields.io/badge/-linux-0D1117?style=for-the-badge&logo=linux&labelColor=0D1117)&nbsp;
![GoogleColab](https://img.shields.io/badge/-GoogleColab-0D1117?style=for-the-badge&logo=googlecolab&labelColor=0D1117)&nbsp;

### Other Knowledge:

![Markdown](https://img.shields.io/badge/-Markdown-0D1117?style=for-the-badge&logo=markdown&labelColor=0D1117)&nbsp;
