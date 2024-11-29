# 🎉 **Live Event Sentiment Analyzer** 🎤

Welcome to the **Live Event Sentiment Analyzer**, an innovative tool designed to track the pulse of live events through the power of **real-time sentiment analysis**. Whether it's a **sports game**, a **concert**, or a **global conference**, this project uses Twitter data to give you insights into the mood of the public, live!

---

## 🚀 **Project Overview**

In the age of instant information, people share their thoughts and opinions about events on social media as they happen. The **Live Event Sentiment Analyzer** connects to the **Twitter API** to fetch real-time tweets related to any event of your choice. These tweets are then analyzed using **Natural Language Processing (NLP)** to classify them as **positive**, **neutral**, or **negative**.

The project provides live **visualizations** to display the overall sentiment, making it an amazing tool for event organizers, social media analysts, or anyone who wants to gauge the real-time public reaction.

---

## 🔧 **Technologies Used**

This project leverages some of the most powerful and easy-to-use tools available in the Python ecosystem:

- **Tweepy**: For interacting with the Twitter API and streaming tweets in real-time.
- **TextBlob**: A simple NLP library to classify sentiment (positive, neutral, negative).
- **Matplotlib**: To create stunning, live sentiment pie charts for easy visualization.
- **Time**: To simulate real-time data collection with pauses between tweet fetches.

---

## 🎯 **How It Works**

1. **Authenticate with Twitter API**: The program uses your **Twitter Developer credentials** to access Twitter’s data.
2. **Stream Tweets**: Using the `tweepy.Cursor` method, we gather real-time tweets containing the event keyword (e.g., #SuperBowl, #ConcertXYZ).
3. **Sentiment Analysis**: Every tweet's content is passed through a **TextBlob** analysis, and a polarity score is calculated to determine whether the sentiment is positive, neutral, or negative.
4. **Real-time Visualization**: A dynamic pie chart visualizes the breakdown of sentiments as new tweets are processed.

---

## 💡 **Features**

- **Real-time Data Collection**: Automatically fetches tweets as they’re posted, ensuring up-to-the-minute analysis.
- **Sentiment Breakdown**: Classifies each tweet as positive, neutral, or negative, providing a clear snapshot of public sentiment.
- **Dynamic Visualization**: The app generates live pie charts to give a visual representation of the sentiments at any given point.
- **Customizable Event Queries**: You can track any event, trend, or hashtag in real-time by simply changing the search query.
- **Python-powered**: All the heavy lifting is done with Python and simple-to-use libraries, making it beginner-friendly while still being powerful.

---

## 🛠 **Setup Instructions**

To get this project up and running on your local machine, follow these steps:

### 1. Clone this repository:
```bash
git clone https://github.com/thomas-legros/live-event-sentiment-analyzer.git
cd live-event-sentiment-analyzer
```

### 2. Install dependencies:
```bash
pip install tweepy textblob matplotlib
```

### 3. Set up Twitter Developer Account:
- Go to [Twitter Developer Portal](https://developer.twitter.com/) and create an app to get your **API Keys** and **Access Tokens**.
- Replace the placeholders for the API credentials in the script with your actual keys:
    ```python
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    ```

### 4. Run the application:
```bash
python sentiment_analyzer.py
```

---

## 📊 **Sample Output**

Once the program is running, you’ll see a live updating sentiment pie chart like this:

As more tweets are collected, the chart dynamically adjusts to show the current public opinion about the event.

---

## 📝 **Future Enhancements**

Here are some ideas to take this project to the next level:
- **Multilingual Support**: Extend the sentiment analysis to multiple languages.
- **Machine Learning Models**: Implement more advanced sentiment classification using ML models like **BERT** or **RoBERTa**.
- **Other Social Media Platforms**: Integrate APIs from other platforms (Instagram, Reddit, etc.) for a more comprehensive view.
- **Historical Analysis**: Track sentiment trends over time for large events, creating a historical view of public opinion.

---

## 🤖 **Contributing**

We welcome contributions! If you have any ideas, improvements, or bugs to report, feel free to fork the repository, create an issue, or submit a pull request. Contributions are always appreciated.

---

## 📱 **Contact**

Created by [Thomas Legros](https://github.com/thomas-legros)  
For any questions or feedback, feel free to open an issue on this repository or email me directly at [tlegros767@insite.4cd.edu](mailto:tlegros767@insite.4cd.edu).

---

## 🎉 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🌍 **Acknowledgments**

- Special thanks to the creators of **Tweepy**, **TextBlob**, and **Matplotlib** for building these awesome libraries.
- Inspired by real-world use cases of sentiment analysis in social media monitoring and event management.

---

Enjoy analyzing live events in real-time with your sentiment analysis tool! 🚀📊
