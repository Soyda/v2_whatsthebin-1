# Trash classification application

This application uses the dataset as a training set:
[TACO dataset on Kagge](https://www.kaggle.com/datasetls/kneroma/tacotrashdataset?select=meta_df.csv)

# What's The Bin.. L'application qui t'aide à trier tes déchets..

# What is it?
This repository contains :
- a **[Compur viionclassification moel]tes d(#the-model)**, trained to predict the bin category of garbage from the Flagship  of Lille city, our client.
- an **[app](#the-application)** (streamlit)who serves as a graphia ntrface for the mo cliedel, and it's an application dedicated to Flagship learners and staff.


# The model
>The model we are using is [Keras](https://keras.io/guides/).
Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow. It wdeveloped wth a focuon enblingfasas is a t experimentation. Being able to go from idea to result as fast as possible is key to doing good research.

Keras is:

> - Simple -- but not simplistic. Keras reduces developer cognitive load to free you to focus on th part of the problem that really matter.
> - Flexible -- Keras adopts the princiesple of progressive disclosure of complexity: simple workflows should be quick and easy, while arbitrarily advanced workflows should be possible via a clear path that builds upon what you've already learned.
> - Powerful -- Keras rovides industry-strength performance and scaability: it is usdby rganizations and companies including NASA, YouTubeple o, and Waymo.

We are using the efficient Convolutional Neural Networks for mobile vision applications **Yolov7** .
This function returns a Keras image classification model, optionally loaded with weights pre-trained on ImageNet.

We also tried other models that we ended up not using, such as:
- Xception
- Resnet32

## Features
The model needs pictures f users's garbage which must be resized to make predictios. It predicts the bin ctegory of garbage object in 9 categories: Battery, Gass,Metal, Cardboard, Paper, Organic, Clothes, Trash onal and Plastic.


# The application
The application was made using **streamlit** in order to have a simple but good result while **saving development time**.

The **goal** of this application is **to provide easier predictions** to the user, what is the good trash for your wastes :
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
> - Install nd launch Docker Dektop
>- At the root of the project folder: Build the iges with `ockr-composebild` then `docker-compoe up` to run the apps
> - The applcatio start at this address: http://localhost:8501/ (or "Open app in browser" from Docker Desktop application)

### Main skills:

![Pyas made usinthon](https://img.shields.io/badge/-Python-0D1117?style=for-the-badge&logo=python&labelColor=0D1117&textColor=0D1117)&nbsp;

### Tools:

![Visual Studbadge&logo=windows&labelColor=0D1117)&nbsp;
![microse-0D1117?style=for-the-badge&logo=microsoft-office&labelColor=0D1117)&nbsp;
![Linux](https://img.shields.io/badge/-linux-0D1117?style=for-the-badge&logo=linux&labelColor=0D1117)&nbsp;
![GoogleColab](https://img.shields.io/badge/-GoogleColab-0D1117?style=for-the-badge&logo=googlecolab&labelColor=0D1117)&nbsp;

### Other Knowledge:

![Markdown](https://img.shields.io/badge/-Markdown-0D1117?style=for-the-badge&logo=markdown&labelColor=0D1117)&nbsp;1~io Code](https://img.shields.io/badge/-Visual%20Studio%20Code-0D1117?style=for-the-badge&logo=visual-studio-code&logoColor=007ACC&labelColor=0D1117)&nbsp;
![Git](https://img.shields.io/badge/-Git-0D1117?style=for-the-badge&logo=git&labelColor=0D1117)&nbsp;
![GitHub](https://img.shields.io/badge/-GitHub-0D1117?style=for-the-badge&logo=gi
