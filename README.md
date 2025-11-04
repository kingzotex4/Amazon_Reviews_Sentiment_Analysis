# Amazon Alexa Reviews Sentiment Analysis 🎤📊

A comprehensive machine learning project that performs sentiment analysis on Amazon Alexa product reviews. This project includes exploratory data analysis, multiple classification models, and a Flask web application for real-time predictions.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)
![ML](https://img.shields.io/badge/ML-XGBoost-orange.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 🎯 Overview

This project analyzes customer sentiment from Amazon Alexa product reviews using Natural Language Processing (NLP) and Machine Learning techniques. The system can classify reviews as either **Positive** or **Negative**, helping businesses understand customer feedback at scale.

The project includes:
- 📊 Comprehensive data exploration and visualization
- 🧹 Text preprocessing with lemmatization and stopword removal
- 🤖 Multiple ML models (Naive Bayes, Random Forest, XGBoost)
- 🌐 Interactive Flask web application
- 📁 Batch prediction support via CSV upload
- 📈 Visual analytics and sentiment distribution

## ✨ Features

- **Single Text Prediction**: Analyze sentiment of individual review texts
- **Bulk Prediction**: Upload CSV files for batch sentiment analysis
- **Visual Analytics**: Automatic pie chart generation showing sentiment distribution
- **Pre-trained Models**: Ready-to-use XGBoost classifier with TF-IDF vectorization
- **REST API**: JSON-based API for integration with other applications
- **Text Preprocessing**: Advanced NLP pipeline with lemmatization and POS tagging
- **Responsive UI**: Clean, user-friendly web interface

## 📁 Project Structure

```
Amazon Alexa Reviews Sentiment Analysis/
│
├── app.py                              # Flask application
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
│
├── Data/
│   ├── amazon_alexa.tsv               # Original dataset
│   ├── predictions.csv                # Sample predictions output
│   └── SentimentBulk.csv              # Bulk prediction sample
│
├── Models/
│   ├── xgboost_model.pkl              # Trained XGBoost classifier
│   └── tfidfVectorizer.pkl            # Fitted TF-IDF vectorizer
│
├── templates/
│   ├── landing.html                   # Landing page
│   └── index.html                     # Prediction interface
│
├── Data Exploration & Modeling.ipynb  # Complete EDA and modeling notebook
│
└── alexa/                             # Python virtual environment
```

## 📊 Dataset

The dataset contains Amazon Alexa product reviews with the following characteristics:

- **Source**: Amazon customer reviews for Alexa devices - ([Kaggle Dataset](https://www.kaggle.com/datasets/sid321axn/amazon-alexa-reviews))
- **Format**: Tab-separated values (TSV)
- **Features**:
  - `rating`: Product rating (1-5 stars)
  - `date`: Review date
  - `variation`: Alexa device variant
  - `verified_reviews`: Customer review text
  - `feedback`: Sentiment label (1 = Positive, 0 = Negative)

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/vineet416/Amazon_Reviews_Sentiment_Analysis.git
cd Amazon_Reviews_Sentiment_Analysis
```

2. **Create a virtual environment** (Optional but recommended)
```bash
conda create -p alexa python=3.12 -y
conda activate alexa/
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLTK data**
```python
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger'); nltk.download('punkt')"
```

## 💻 Usage

### Running the Web Application

1. **Start the Flask server**
```bash
python app.py
```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - You'll see the landing page with options to start predictions

### Single Text Prediction

1. Navigate to the prediction page
2. Enter your review text in the input field
3. Click "Predict Sentiment"
4. View the result (Positive/Negative)

### Bulk Prediction (CSV Upload)

1. Prepare a CSV file with a column named `Sentence` containing reviews
2. Upload the file through the web interface
3. Download the predictions CSV file
4. View the sentiment distribution pie chart

### API Usage

**Endpoint**: `/predict`

**Method**: `POST`

**Request Body** (JSON):
```json
{
  "text": "I love my new Alexa device! It works perfectly."
}
```

**Response**:
```json
{
  "result": "Positive"
}
```

## 📈 Model Performance

The project evaluates multiple machine learning algorithms:

| Model | Accuracy | Description |
|-------|----------|-------------|
| **XGBoost** | ~94-96% | Best performing model (deployed) |
| Random Forest | ~93-95% | Strong ensemble method |
| SVM | ~91-93% | Support Vector Machine with RBF kernel |
| Logistic Regression | ~89-91% | Baseline linear model |

**Key Metrics**:
- Precision: High precision for both classes
- Recall: Balanced recall scores
- F1-Score: Strong F1-scores indicating good overall performance

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.12**: Primary programming language
- **Flask**: Web framework for the application
- **scikit-learn**: Machine learning library
- **XGBoost**: Gradient boosting framework
- **NLTK**: Natural Language Processing

### Data Science Stack
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **WordCloud**: Text visualization

### NLP Preprocessing
- **TF-IDF Vectorization**: Text feature extraction
- **Lemmatization**: Word normalization
- **POS Tagging**: Part-of-speech identification
- **Stopwords Removal**: Noise reduction

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page |
| `/predict` | GET | Prediction interface page |
| `/predict` | POST | Predict sentiment (text or file) |

## 📸 Screenshots

### Landing Page
The home page provides an introduction to the sentiment analysis tool.      
![Landing Page](./Landing_Page.png)

### Prediction Interface
Users can input text or upload CSV files for sentiment analysis.        
![Prediction Interface](./Prediction_Interface.png)

### Results Display
Shows prediction results with visual analytics for bulk predictions.        
![Results Display - Negative](./Results_Display_Negative.png)       

![Results Display - Positive & Batch Analysis](./Results_Display_Positive_&_Batch_Analysis.png)     

## 📝 Key Insights

From the exploratory data analysis:

1. **Class Distribution**: Most reviews are positive, reflecting high customer satisfaction
2. **Text Length**: Review length correlates with sentiment intensity
3. **Rating Correlation**: Strong correlation between star ratings and sentiment
4. **Common Words**: Positive reviews mention "love", "great", "easy"; negative reviews mention "not", "work", "poor"
5. **Device Variations**: Certain Alexa models receive more positive feedback

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Vineet Patel**
- Email: vineetpatel468@gmail.com
- GitHub: [@vineet416](https://github.com/vineet416)
- LinkedIn: [@vineet416](https://www.linkedin.com/in/vineet416/)

## 🙏 Acknowledgments

- Amazon for the Alexa reviews dataset
- scikit-learn and XGBoost communities
- Flask framework developers
- NLTK contributors

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

⭐ If you found this project helpful, please give it a star!