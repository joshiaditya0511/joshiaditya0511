# Karnataka Assembly Elections: Data Analysis

This project provides a comprehensive analysis of the Karnataka Assembly Elections (2013, 2018, 2023). Through various insights and interactive visualizations, it examines multiple facets of the elections using data from multiple sources. Explore the findings directly on the [website](https://kea.adityajoshi.in).

## Contents
- [Links](#links)
- [Project Overview](#project-overview)
- [Analysis Summary](#analysis-summary)
- [Tools and Tech Used](#tools-and-tech-used)
- [Sources and References](#sources-and-references)
- [Change Log](#change-log)

## Links

- [Project Website](https://kea.adityajoshi.in)
- [LinkedIn](https://www.linkedin.com/in/joshiaditya0511)
- [Personal Website](https://adityajoshi.in)

## Project Overview

This analysis dives deep into the Karnataka Assembly Elections, exploring elements such as vote counts, candidate details, vote margins, and the impact of events like the Bharat Jodo Yatra. All visualizations are interactive to provide an engaging and informative user experience.

## Analysis Summary

### Electoral History (2013–2023)

The three elections tell a story of cyclical swings between the two dominant national parties:

- **2013:** INC won a clear majority (122 seats). BJP and JD(S) each won 40 seats.
- **2018:** BJP surged to 104 seats, overtaking INC (80 seats) despite INC holding a marginally higher popular vote share — pointing to scattered vote distribution.
- **2023:** INC bounced back strongly with 135 seats against BJP's 66, despite only a ~6.2 percentage point lead in vote share — indicating highly efficient vote distribution by INC.

### Impact of the Bharat Jodo Yatra

The Yatra covered 21 assembly constituencies across 511 km in Karnataka over 22 days. In 2018, INC had won only 5 of these 21 constituencies. By 2023, that number rose to 15 (plus 1 allied seat). The INC vote share in Yatra constituencies grew by ~9.78% from 2018 to 2023, compared to ~5.80% in non-Yatra constituencies — suggesting the Yatra had a meaningful, if not conclusively causal, positive impact on INC performance in those areas.

### Emerging Bi-polarity

The combined vote share of BJP and INC has risen consistently across all three elections, squeezing out regional parties and independents. The Effective Number of Parties (ENP) — both by seats and vote share — has declined steadily, pointing toward a consolidating two-party-dominant landscape. JD(S) has shrunk from 40 seats (2013) to just 19 (2023).

### The Paradox of Participation

Despite the consolidation of votes toward the top two parties, the number of contesting parties actually *increased* — from 59 in 2013 to 91 in 2018 and 2023. Simultaneously, independent candidates decreased from 1,157 to 905 over the same period, suggesting candidates prefer party affiliation over running alone, even with smaller parties.

### Party Turnover and Swing Direction

Election cycles show a clear anti-incumbency pattern driven predominantly by INC ↔ BJP swings:
- **2013 → 2018:** 58 constituencies flipped from INC to BJP.
- **2018 → 2023:** 41 constituencies flipped back from BJP to INC.

JD(S) remains a secondary player — losing seats to both major parties in both cycles. Smaller parties and independents have become nearly irrelevant in seat turnover.

### Battleground Constituencies

Six constituencies — Bailhongal, Haliyal, Hosakote, Sringeri, Tumkur City, and Tumkur Rural — recorded winning margins under 5% across all three elections. Key findings:
- The average winning margin across these seats was just **2.725%**, with a minimum of **0.14%**.
- Candidate party-switching did not alter outcomes in some cases (e.g., Bailhongal, Haliyal), suggesting strong local voter loyalty patterns.
- Hosakote demonstrated **party loyalty over candidate loyalty** — when the incumbent switched to BJP and his rival switched to INC, voters followed the INC banner rather than the familiar candidate.

---

## Tools and Tech Used

### Data Gathering:

- **Web Scraping**:
  - `Requests`: Sent GET requests to retrieve webpage content.
  - `BeautifulSoup`: Parsed HTML for relevant data extraction.
  - `Selenium`: Interacted with dynamic pages, ensuring smoother data fetching.
  - `asyncio`: Enhanced performance with asynchronous requests for efficient data retrieval.

- **PDF Extraction**:
  - Processed over 57,000 PDFs to extract voter data for the 2023 elections.
  - `PyPDF2`: Processed PDFs, retaining only essential pages.
  - `pdf2image`: Converted PDF pages to images.
  - `OpenCV`: Detected table borders for precise data extraction.
  - `TesseractOCR`: Extracted text data within table areas.
  - `asyncio` and `multiprocessing`: Enabled asynchronous downloads and parallel processing of PDFs.

### Data Wrangling:

- `Pandas` and `Regular Expressions`: Key tools for data cleaning and organization.
- `OpenAI API`: Used OpenAI Batch API with GPT-4o-mini for segmenting and categorizing education and profession data from candidate details.

### Data Visualization:

- `Plotly`: Main library for crafting interactive visualizations.
- `Flourish Studio`: Created and embedded the Parliamentary Chart as an HTML component.

### Website and Deployment:

- **Frontend**: Built using `HTML`, `Bootstrap`, and `JavaScript` to create a **static** and **responsive** site.
- **Hosting**: Deployed on an `AWS EC2` instance using the free tier, with `NGINX` configured as the web server for efficient delivery.

### Miscellaneous:

- `MapShaper`: Converted Karnataka's assembly boundaries shapefile to GeoJSON and optimized boundaries for faster rendering.

## Sources and References

- **[MyNeta](https://www.myneta.info/)**: Data on candidate assets, liabilities, criminal cases, profession, and education.
- **[NDTV](https://www.ndtv.com/)**: Vote counts for all candidates in the 2023 elections.
- **[OpenCity](https://opencity.in/)**: Detailed results from the 2013 Assembly elections.
- **[ECI (Election Commission of India)](https://eci.gov.in/)**: Detailed results from the 2018 elections.
- **[CEO (Chief Election Officer) of Karnataka](https://ceo.karnataka.gov.in/en)**: Gender distribution data on eligible voters, provided in PDFs.
- **[KGIS (Karnataka Geographic Information System)](https://kgis.ksrsac.in/kgis/)**: Shapefile for assembly constituency boundaries.
- **[MapShaper](https://mapshaper.org/)**: Shapefile conversion to GeoJSON, smoothing boundaries for visualization.
- **[OpenAI](https://openai.com/)**: Used for segmenting and classifying candidate details on education and profession.

## Change Log

- **Transition to a Static Site**: The project originally utilized a dynamic backend with a MySQL database and Streamlit for visualizations. However, due to the stationary nature of the data (i.e., it will not change over time), the database backend was removed. This allowed the project to move to a static site, reducing backend load and enhancing performance.
- **Deployment Update**: The Streamlit-hosted site was replaced with a static site built with HTML, Bootstrap, and JavaScript, hosted on a free-tier AWS EC2 instance using NGINX. This change improves site speed and responsiveness while providing a smoother user experience.