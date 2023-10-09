[![Github commit](https://img.shields.io/github/last-commit/fdjutant/sentiment-analysis-neural-networks/master)](https://github.com/fdjutant/sentiment-analysis-neural-networks)

# Sentiment Analysis using Neural Networks
## Project overview
Determining the sentiment (positive or negative) of tweets about stocks can provide valuable insights for investment decisions. However, manually analyzing a large volume of tweets and adjusting portfolio weights accordingly can be nearly impossible. This project aims to address this challenge by employing neural networks, specifically a mathematical model composed of interconnected linear models forming a network. The model is trained using a labeled dataset of tweets with known sentiments.

In this project, I develop a model capable of generating a sentiment score for stocks based on a given tweet, utilizing a recurrent neural network (RNN). First, The input dataset, which consists of tweets and their corresponding sentiment scores, undergoes pre-processing to prepare it for training. Second, an RNN-based text classifier is built to learn and predict sentiment scores from the processed tweet data. Third, the input dataset is divided into a training dataset and a validation dataset. The training dataset is used to train the model, while the validation dataset is used to compute the validation loss, ensuring the model's accuracy. Finally, the trained neural network model is then employed to make predictions on sentiment scores for stocks based on new tweets.

Throughout this project, the input dataset was obtained from Udacity.

## Project description
### Pre-processing the Tweet corpus
To begin, the input dataset comprising tweets and their corresponding sentiment scores must be divided into features and labels, respectively. The features section, which contains the text of tweets, undergoes a series of cleaning processes using regular expressions (Regex). These processes include the removal of URLs, ticker symbols, punctuation, single characters, and other noise. Following this, tokenization is applied to break down the tweets into individual words. The labels consist of five distinct sentiment scores, ranging from -2 (indicating negative sentiment) to +2 (indicating positive sentiment).

### Bagging Words and Balancing the Dataset Across Sentiments
The words in the dataset are organized into several bags, and their frequency of appearance is counted. Further refinement is carried out to eliminate extremely common and rare words that do not contribute significantly to identifying sentiment patterns.

Another critical consideration is balancing the distribution of the dataset across the five sentiment scores. Half of the dataset typically contains a neutral sentiment score, which can hinder the learning of the network model since the model can achieve a 50% accuracy by simply assigning a value of 0 every time. To address this issue, the dataset with a neutral sentiment score should be reduced from 50% to 20%, resulting in a more uniform distribution across the sentiment scores.

### Building the Neural Network Using RNN
The neural network is constructed with the following components: Embedding layer -> RNN layer -> Dense layer -> Softmax. The use of the softmax distribution is appropriate because there are five sentiment scores as labels.

The input dataset needs to be split into training and validation datasets for both the features and the labels. These datasets are then fed into the model in batches for training.

### Evaluating the Neural Network Model
Once the model is fully trained, the forward pass can be utilized to generate predictions. Given a tweet as input, the model will produce a softmax probability distribution across the five sentiment scores.

## Credits
The project was built as part of a practical course in systematic trading from Udacity: [AI for trading](https://www.udacity.com/course/ai-for-trading--nd880)