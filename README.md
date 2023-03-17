# team-6-energy-costs

## Project Description

Our objective is to develop a model that can accurately predict energy prices one week in advance. This model will be used to provide users with information on when the best time to buy energy is.

The model will use historical data on energy prices, as well as other relevant factors that may affect prices, such as weather conditions, time of year, and energy feeding volume. We used machine learning algorithms to analyze this data and identify patterns and trends that can be used to make predictions.

To ensure the accuracy of our predictions, we trained the model on a large dataset of historical energy prices and tested it to evaluate its performance. We also fine-tuned the model by adjusting its hyperparameters to achieve the best possible results.

Overall, our model will provide a valuable tool for energy consumers who want to make more informed decisions about their energy usage and expenditures.

## Table of Contents

1. [Project Status](#1-project-status)
2. [Technologies Used](#2-technologies-used)
3. [Setup](#3-setup)
4. [Our Achievements](#4-our-achievements)
5. [Room for Improvement](#5-room-for-improvement)
6. [Our Team](#6-our-team)
7. [Acknowledgements](#7-acknowledgements)

## 1. Project Status

Project is: _in progress_
The project is currently in progress and actively being developed by the team.

## 2. Technologies Used

**Libraries:**

- Numpy
- Pandas
- Matplotlib
- Seaborn
- Statsmodels
- Scikit Learn
- XGBoost

## 3. Setup

To run this project, you need to have installed python3 on your computer([python3](https://www.python.org/downloads/)).
Furthermore, it is helpful to install anaconda ([Anaconda](https://docs.anaconda.com/anaconda/install/index.html)).

- Clone the project

```
git clone git@github.com:M-123-456/team-6-energy-costs.git
```

- Go to the project folder and run

```
conda env create -f ./environment.yml
```

- Or install libraries listed in environment.yml with `pip install`.

## 4. Our Achievements

1. Set goal: Build a simulator to predict the best (cheapest) time to buy energy in the nex week
2. Get datasets with good quality
3. Analyze data to obtain a mental model (ref: [analysis](./analysis.ipynb))
4. Try out several forecasting models to find out the best model for our data and goal
5. Create our model (ref: [model](./DEIN_DATEINAME.ipynb))
6. Search for hyperparameters
7. Finetune our model using covariates

## 5. Room for Improvement

- [ ] Integrate the model into a user-friendly interface that allows users view predicted energy prices for the coming week

## 6. Our Team

This project is developed and maintained by a team of

1. **Giulia Cancian** (Head of Operation)
2. **Rebekka Zawanda** (Head of Communication)
3. **Miki Gerlach**

## 7. Acknowledgements

- This is the project of a data science course at [Techlabs](https://techlabs.org/).
- Many thanks to our mentor **Leonard Kunz** and Techlabs!
