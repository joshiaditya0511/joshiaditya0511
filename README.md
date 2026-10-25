<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img src="assets/banner-light.svg" alt="Aditya Joshi. Product Manager by day. AI builder by habit." width="100%">
</picture>

<p align="center">
  <a href="https://www.adityajoshi.in"><img alt="Portfolio: adityajoshi.in" src="https://img.shields.io/badge/Portfolio-1f6feb?style=for-the-badge&logo=googlechrome&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/joshiaditya0511"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-1f6feb?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://www.adityajoshi.in/assets/AdityaJoshiResume.pdf"><img alt="Resume (PDF)" src="https://img.shields.io/badge/Resume-1f6feb?style=for-the-badge&logo=readdotcv&logoColor=white"></a>
  <a href="mailto:contact@adityajoshi.in"><img alt="Email: contact@adityajoshi.in" src="https://img.shields.io/badge/Email-1f6feb?style=for-the-badge&logo=maildotru&logoColor=white"></a>
</p>

## Right now: Alyson AI

I'm a product manager at **Revcloud**, though "AI builder" is probably the more honest label. I own the product for [**Alyson AI**](https://alyson.ai), an AI marketing SaaS that tests different versions of landing pages, traffic routing and campaigns on live traffic, and shows which one earns more.

I joined as a data scientist and built the pieces at the center of it: the **traffic router** that sends each visitor to a page by model prediction, audience segment or fixed split, and the **revenue-per-click and conversion-rate models** that predict what each click should be worth. Pages are judged on how far they beat that prediction, so a page that just got luckier traffic doesn't win by accident. In June 2026 I was promoted to product manager.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/alyson-stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/alyson-stats-light.svg">
  <img src="assets/alyson-stats-light.svg" alt="400K+ visits routed by Alyson's router. $175K+ revenue brought in for Revcloud's internal lead generation. Promoted from Data Scientist to Product Manager in June 2026." width="100%">
</picture>

These days that looks like:

- **Specs and delivery.** Writing the product specs and delivery plans, and leading engineers, data scientists, data engineers and a designer from definition to release.
- **Architecture calls.** I designed how Alyson's AI landing page builder deploys pages to customers' own domains, and I review system design across the platform.
- **Still building.** The analytics and reporting layer is mine, hands-on: how far each page beat its prediction, how confident we can be in that, and how traffic was split. I also build SMS campaign audiences end to end.

## Featured projects

All three are open source and live.

### 🏠 Pune Housing Price Prediction

`Machine Learning` `Recommendation Systems` `Web Scraping`

A zero-backend web app that predicts house prices in Pune and recommends similar properties, based on what you're looking for.

<a href="https://www.punehousing.in"><img src="assets/puneprop-predict.png" alt="Pune Housing Price Prediction web app showing the property price predictor form" width="100%"></a>

- Typical prediction lands within **~11% of the actual price** (median APE, R² ≈ 0.93), using LightGBM trained on **30k+ listings** scraped with Selenium.
- Both the price model and the recommender run **in the browser as ONNX models**, so the live site needs no ML backend.
- Also shipped a second architecture: a containerized FastAPI backend on AWS EC2 behind Nginx.

**Stack:** Python · Pandas · Scikit-learn · LightGBM · ONNX · FastAPI · Docker · Astro · React · Vercel

**[Live site](https://www.punehousing.in)** · **[Code](https://github.com/joshiaditya0511/pune-house-price-prediction)**

### 🗳️ Karnataka Elections Data Analysis

`Data Analysis` `Web Scraping` `OCR`

An interactive look at the Karnataka Assembly elections: vote counts, candidate details, vote margins, the Bharat Jodo Yatra's effect, and more.

<a href="https://kea.adityajoshi.in"><img src="assets/karnataka-elections-analysis.jpg" alt="Karnataka Elections Analysis site showing a parliamentary seat chart" width="100%"></a>

- Built a pipeline that scraped and processed **57k+ PDFs** (Requests, BeautifulSoup, Selenium, PyPDF2, Tesseract OCR).
- Categorized the extracted data with **OpenAI's Batch API** (GPT-4o-mini) at half the real-time cost.
- Published interactive Plotly.js and Flourish charts on a site hosted on AWS EC2 with NGINX.

**Stack:** Python · Pandas · Selenium · Tesseract · OpenAI Batch API · Plotly.js · AWS EC2 · NGINX

**[Live site](https://kea.adityajoshi.in)** · **[Code](https://github.com/joshiaditya0511/karnataka-election-analysis)**

### 📈 Walmart Sales Analysis and Forecasting

`Time Series` `Data Analysis` `Forecasting`

Time series analysis and forecasting of Walmart's weekly store sales, to uncover patterns, quantify holiday effects and predict future trends.

<a href="https://walmart.adityajoshi.in"><img src="assets/walmart-sales-forecasting.png" alt="Walmart Sales Analysis and Forecasting notebook site with sales charts" width="100%"></a>

- Exploratory analysis of trends, seasonal patterns, holiday effects and anomalies in store-level sales.
- Forecasts future weekly sales with statistical and machine learning models, published as a readable notebook site.

**Stack:** Python · Pandas · Jupyter · Kaggle Walmart dataset

**[Live site](https://walmart.adityajoshi.in)** · **[Code](https://github.com/joshiaditya0511/walmart-sales-forecasting)**

## Notes and resources

Free resources like Khan Academy, NPTEL and MIT OpenCourseWare made a big difference to how I learned, so I share my own notes the same way. I'm a compulsive note taker, and over time they've turned into a library: digital and handwritten notes, Jupyter notebooks, and references to the best external material I found.

<a href="https://github.com/joshiaditya0511/data-science-notes"><img src="assets/notes-preview.gif" alt="Preview of Aditya's data science notes library" width="100%"></a>

| [Machine Learning](https://docs.google.com/document/d/1rMXRlFJ5mDAzik4ipsySVFBUsI54E0NXocDhOct3YNM/edit?usp=sharing) | [Statistics](https://docs.google.com/document/d/1Q2zwoGjBX1Vpa7bEWAOyzZJTJDtmfT8I-YEgkSQCBsQ/edit?usp=sharing) | [Databases & SQL](https://docs.google.com/document/d/1sZOzI4v6-H8X5PJZgeBQFqkwPOBCZhqDPH52HqKDCQI/edit?usp=sharing) | [Python](https://docs.google.com/document/d/1z_m8OYimE4HswM4zOeZxDfJ-jmUXtI8WJpSGKUMU1QY/edit?usp=sharing) |
| :---: | :---: | :---: | :---: |

The full collection, notebooks included, lives in the **[data-science-notes](https://github.com/joshiaditya0511/data-science-notes)** repo.

## How I got here

| When | Role | Where |
| --- | --- | --- |
| Jun 2026 – now | **Product Manager** | Revcloud |
| Aug 2025 – Jun 2026 | **Data Scientist** | Revcloud |
| Aug 2024 – Jul 2025 | **Exec. PG Certification, Data Science & AI** | IIT Roorkee |
| Mar 2024 – Aug 2026 | **Technical Head** (volunteer) | Forengers Foundation, a climate-action NGO in Pune |
| Oct 2023 – Jun 2024 | **Software Engineering Intern** | Oriole Labs |
| 2019 – 2020 | **Brakes design**, BAJA SAE India | Team Kraftwagen |
| 2018 – 2022 | **B.E. Chemical Engineering** | Sinhgad College of Engineering, Pune |

Yes, chemical engineering. In undergrad I designed brake calipers, discs and mounts for an ATV we built from scratch for a national competition. Exhausting, slightly unhinged, and still the best hands-on learning I've had.

## Toolbox

**Product:** `Specs & PRDs` `Roadmapping` `System design` `Cross-functional delivery`

**Data science:** `Python` `Pandas` `Scikit-learn` `LightGBM` `ONNX` `A/B testing` `Statistical inference`

**Data & backend:** `SQL` `Postgres` `SQL Server` `FastAPI` `Docker` `Nginx` `Selenium`

**Cloud:** `AWS SageMaker` `Lambda` `EC2` `RDS` `EventBridge` `Vercel`

**Frontend:** `JavaScript` `React` `Astro` `Plotly.js`

**Workflow:** `Git` `Claude Code`

## Off the clock

Badminton, mostly. Also some mildly embarrassing attempts at wooden staff spinning and (pretend) sword-fighting. Don't ask.

---

<p align="center">
  <a href="https://www.adityajoshi.in">adityajoshi.in</a> ·
  <a href="https://www.linkedin.com/in/joshiaditya0511">LinkedIn</a> ·
  <a href="mailto:contact@adityajoshi.in">contact@adityajoshi.in</a>
  <br>
  <sub>Always happy to talk experiments, ML systems, useful products, or strangely detailed notes.</sub>
</p>
