## PuneProp Predict — Project Summary

**What it is:** A machine learning-powered web app that predicts residential property prices in Pune, India, and recommends similar listings based on user-defined features.

**Data:** Over 30,000 property listings scraped from MagicBricks.com using Selenium, targeting an internal API endpoint discovered via browser dev tools.

**Core ML:**
- A **LightGBM model** for price prediction (R² ≈ 0.93, Median APE ≈ 11%), trained after rigorous feature selection using SHAP, permutation importance, and multiple model-based scoring methods.
- A **content-based recommendation system** using Scikit-learn's `NearestNeighbors` (Euclidean distance) to find similar properties from the dataset.

**Architecture evolution:**
- Started with a decoupled **FastAPI backend on AWS EC2** serving prediction and recommendation endpoints, with an Astro.js + React frontend on Vercel.
- Currently runs entirely **client-side** — models were converted to **ONNX format** and run directly in the browser, eliminating the backend entirely. Feature weighting for recommendations is handled in JavaScript.

**Tech Stack:** Python, LightGBM, Scikit-learn, ONNX, FastAPI, Astro.js, React, Docker, AWS EC2, Vercel.

**Planned improvements** include scraping automation, tiered prediction models, amenity-based features, ANN-based vector search, an insights page with locality analytics, and general UI/SEO polish.