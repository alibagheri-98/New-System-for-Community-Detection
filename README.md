# New-System-for-Community-Detection
I am currently working on creating a system, for identifying communities. This system will use a variety of community detection algorithms, such as majority voting and boosting to combine their results and improve accuracy. It is a part of my project for my B.Sc. Degree.
<br>
In addition to that I am actively involved in the task of finding communities within Stock Markets.
<br>
This repository includes the following components:
1. The codebase for developing the combined community detection algorithms system.
2. Presentation materials that explain how I developed the combined community detection algorithms system.
3. Source code specifically designed for detecting communities in Stock Markets.
4. A final project related to probability and statistics which focuses on community detection.
<br>
If you have any questions or need information, about this project feel free to reach out to me

## Community Detection Using classic algorithms
You'll be able to locate the codes for Community Detection that utilize known algorithms in the "CD_Classic" folder. Inside the .py file you'll find a system that employs classic community detection algorithms, including:
- louvain
- leiden
- hirarchical
- spectral_clustering
- walk_trap
- mcl
- dbscan
- mean_shift
The input data used is the Karate Club dataset and the output consists of identified communities generated through these algorithms. These communities are combined using a majority vote approach.

## Community Detection Using Deep Learning algorithms
Within the repository, you'll find an extensive assortment of code resources thoughtfully organized within the "CD_DL" folder. Our project's approach is intricately designed to build upon the solid foundation laid by the "CD_Classic" folder, integrating cutting-edge advancements to create a comprehensive suite of community detection algorithms. These algorithms have been meticulously crafted to address a wide array of community detection challenges across various domains and datasets, ensuring the versatility and effectiveness of our community detection system.

The "CD_DL" folder serves as a treasure trove of innovative algorithms, each engineered to excel in specific facets of community detection. Here, we provide an exhaustive list of the algorithms contained within this repository, offering a glimpse into the diverse capabilities and functionalities they bring to our community detection system:

**Graph Convolutional Network (GCN)-Based Algorithms:**

1. **GCC (Graph Convolutional Clustering):** A robust algorithm that leverages the power of graph convolutional networks to identify meaningful communities within complex networks.

2. **AGC (Adaptive Graph Convolutional Clustering):** AGC enhances community detection by adapting the graph convolutional clustering process to varying network structures, optimizing accuracy.

3. **G2R (Graph-to-Region):** G2R specializes in delineating community regions within networks, offering a unique perspective on community structures.

4. **AGE (Adaptive Graph Embedding):** AGE employs adaptive graph embedding techniques to uncover hidden community structures within intricate network topologies.

5. **LGNN-GNN (Local Graph Neural Network):** LGNN-GNN employs localized graph neural networks to capture fine-grained community patterns within networks.

6. **NOCD (Node Ordering for Community Detection):** NOCD leverages advanced node ordering strategies to enhance the effectiveness of community detection.

7. **CLARE (Community Detection by Learning Regularities):** CLARE harnesses machine learning principles to identify community regularities and extract meaningful clusters.

8. **RepBin (Representation Binning):** RepBin utilizes representation binning techniques to uncover communities by analyzing the distribution of network node representations.

**Graph Attention Network (GAT)-Based Algorithms:**

1. **HDMI (Hierarchical Deep Mutual Information):** HDMI employs hierarchical deep mutual information to uncover hierarchical community structures within networks.

2. **HeCo (Heterogeneous Community Detection):** HeCo specializes in detecting communities in heterogeneous networks by adapting graph attention networks.

**Autoencoder (AE)-Based Algorithms:**

1. **DANE (Deep Autoencoder Network for Embedding):** DANE utilizes deep autoencoder networks to produce high-quality network embeddings conducive to community detection.

2. **SDCN (Self-Discovered Community Network):** SDCN introduces self-discovery mechanisms to identify communities within networks.

3. **GEC-CSD (Graph Embedding Clustering via Convex Set Decomposition):** GEC-CSD combines graph embedding and convex set decomposition for robust community detection.

4. **DMGC (Deep Multi-Graph Clustering):** DMGC employs deep learning to cluster networks with multiple graphs, accommodating complex network structures.

5. **CDBNE (Community Detection via Binary Node Embedding):** CDBNE leverages binary node embeddings to identify communities efficiently.

6. **One2Multi (One-to-Many Community Detection):** One2Multi focuses on discovering multiple community structures within networks, allowing for diverse community perspectives.

7. **TGA/TVGA (Topology-Aware Graph Autoencoder):** TGA/TVGA incorporates topology-aware graph autoencoders for improved community detection.

8. **sE-Autoencoder (Sparse Eigenvector Autoencoder):** sE-Autoencoder employs sparse eigenvector autoencoders to enhance community detection in sparse networks.

This exhaustive collection of algorithms within the "CD_DL" folder showcases the depth and breadth of our commitment to advancing the field of community detection. These algorithms, each with its unique strengths, collectively contribute to the versatility and effectiveness of our community detection system, enabling us to tackle diverse challenges across a wide range of network scenarios.

## Detecting Similar Stocks by Integrating Community Detection Algorithms
In the stock market, certain stocks exhibit similarities in their behavior. For instance, during events like the COVID-19 pandemic in 2020, the stocks of pharmaceutical companies tend to gain increased value. This phenomenon suggests that stocks form interconnected groups or 'communities.' Identifying and categorizing these communities can be instrumental in making more informed investment decisions.
<br>
Community detection algorithms are a powerful tool for identifying and categorizing these communities. These algorithms can be used to construct stock networks based on stock prices and detect dynamic communities within those networks. By analyzing these communities, investors can gain insights into the complex relationships between stocks and improve their investment strategies.
<br>
We have applied community detection algorithms to stock market analysis in various ways. In our study, we used community detection techniques to simplify stock market analysis and selected the Tehran stock exchange for analysis. Another study introduced a methodology for constructing stock networks based on stock prices and detecting dynamic communities. Yet another study explored community detection for the New York stock market and showed the rationality of community detection on the stock market network.
<br>
We have developed a novel system that uses community detection algorithms for the detection of stock communities. The system is being applied to analyze the dataset from all of the stocks in the world, and the research paper titled 'Detecting similar stocks using community detection algorithms' is currently in the submission stage. A report of some of our results is shown in "Stock-Community-Detection.pdf".
<br>
Overall, community detection algorithms are a valuable tool for stock market analysis. By identifying and categorizing stock communities, investors can gain insights into the complex relationships between stocks and improve their investment strategies. The use of community detection algorithms in stock market analysis is a growing field of research, and there are many opportunities for future studies to explore this topic further
<br>
![image](https://github.com/alibagheri-98/New-System-for-Community-Detection/assets/112773855/b4f9582a-bb81-432a-b8b0-d27c2d34e23d)

<b>The abstract of our report:</b>
<br>
The aim of our research is to analyze the stock market by detecting the community structure using various distance and clustering methods. We utilized Dynamic Time Warping (DTW) as a distance measure due to its ability to capture delays and time shifts and wraps. We also used a modified version of DTW that is not sensitive to singularities which are mostly noises, along with two other distance detection methods. We then constructed four graph based on these distances, where the edges represent similarity. another method used is to represent each stock time series in a low dimensional vector, to do that we extracted the feature vector using auto encoders.
<br>
We applied multiple classical clustering using four graph structural dataset and a voting mechanism between these clustering methods and dataset to obtain a more robust result. Furthermore, we employed deep learning techniques such as convolutional neural networks (CNN) to cluster stocks. We also used graph neural networks (GNN) which is modified for graph structural input. We also used NLP to find the industry, country, etc of stocks as a feature for deep learning algorthims.
<br>
Our results demonstrate that the community structure in the stock market can be identified using DTW and other distance measures. The use of
autoencoders and deep learning techniques in clustering and community detection showed promising results. Ultimately, our research contributes to the
understanding and analysis of the stock market and its structures which can potentially be used in portfolio optimization to inform investment decisions.
<br>
Some of the results of clusterings:
![Cluster71](https://github.com/alibagheri-98/New-System-for-Community-Detection/assets/112773855/979cf45e-4f53-4508-85e8-686d4abd9105)
![Cluster173](https://github.com/alibagheri-98/New-System-for-Community-Detection/assets/112773855/317e7fa9-520a-4b33-b3a4-de7d2ee1099f)
![Cluster264](https://github.com/alibagheri-98/New-System-for-Community-Detection/assets/112773855/939bd5e9-2dae-46cc-b00d-44e975ebefda)

## Presentation
You can find the PowerPoint presentation (as well as its PDF format) in the "PRESENTATION" folder.

## Community Detection Project
During the course of my research project, I had the opportunity to develop an educational initiative centered around the topic of community detection and graph clustering methods. Inside the "Community-Detection-Project" folder, you'll find a comprehensive project dedicated to exploring the realm of "Graph Clustering Methods." Our approach focuses on utilizing community detection algorithms to facilitate effective clustering of data. The primary goal of this initiative is to introduce students to the practical applications of probability theory while providing them with valuable insights into the world of recommender systems.

This project was conceived and executed during our tenure as teaching assistants at Sharif University of Technology. In this capacity, we had the privilege of leading a group of teaching assistants, collaborating to create a meaningful and educational experience for students. Our shared objective was to not only impart knowledge but also to foster a deeper understanding of probability concepts and their real-world applications.

Within the "Community-Detection-Project" folder, you will uncover the details of this educational endeavor, including instructional materials, project documentation, and resources aimed at enhancing students' comprehension of community detection and graph clustering. Should you have any inquiries or seek further information regarding this educational initiative, please do not hesitate to reach out ([bagheri9877@gmail.com](bagheri9877@gmail.com)). We are dedicated to promoting educational excellence and sharing our experiences in the field of probability and community detection.





























## A project to optimize advertisment in social medias 
###  The main goal of the project
"The primary objective of our project is to optimize advertising algorithms for enhanced advertising across various social media platforms. We are currently working on the entire project with the aim of achieving this goal.
Our main focus is to showcase our advertisements to a wide audience in need of our product, all while adhering to a predetermined budget. We refer to this group as our 'target audience.' The size of this target audience is influenced by several factors, including the channel's subscriber count, the engagement rate of subscribers with channel posts, and the willingness of these subscribers to purchase our product."
### What is the engagment rate?
When we mention the "engagement rate,"we are referring to the cumulative reactions, comments, and views a post receives within different timeframes and on various days of the week in a specific channel or page.
### Predicting advertisment prices
"We have developed a model that predicts advertisement prices for channels or pages based on various features, such as the number of subscribers, engagement rate, and the community label associated with that channel or page. The purpose of creating this model is to estimate the advertisement prices for a given channel based on its specific characteristics.
Subsequently, we compare this estimated price to the actual price offered by the owner of the channel or page. If the offered price exceeds our estimate, it suggests that the channel's pricing is not competitive. However, if the offered price falls below our estimate by a certain threshold, we consider adding that channel to our list of potential advertising targets. The specific threshold is determined by the budget at our disposal."
### Predicting engagment rate 
"We've developed a neural network model capable of predicting the engagement rate of posts within a channel using specific data from both the post and the channel. This data includes the number of subscribers to the channel, the channel's community label, the time at which the post was published, and various other features. Detailed information regarding this process can be found in "result1.pdf" located within the repository.
The primary motivation for this development is to streamline the calculation of the engagement rate for posts in a channel, a task that is both time-consuming and computationally expensive when done on a daily basis. By collecting data from the channel, we can use our model to predict the engagement rate of future posts, thereby saving time and computational resources. It's important to note that we will periodically update our dataset after a specified interval."
### Desire of subscribers
"The subsequent tasks involve two key objectives: first, identifying the most suitable community label that aligns with our product, and second, identifying the related communities corresponding to that community label.
The first task is relatively straightforward. For instance, the most relevant label for clothing products is, unsurprisingly, 'clothing.' However, the second task is more challenging because a clothing product could potentially be advertised on a channel with a 'shoes' community label, but it would not be appropriate to advertise it on a channel primarily focused on political content.
In the case of Telegram, achieving this second objective necessitates employing natural language processing (NLP) techniques to assess the content and community labels. On other platforms like Instagram, a different approach can be taken by monitoring the degree of overlap in followers between various pages with different community labels."
### The final task
"The ultimate task is to select the optimal set from the available list, taking into account their prices, subscriber counts, engagement rates, and community labels. To accomplish this, we have created a neural network designed to evaluate and test the output for all potential sets."
### The results
"Our system has undergone rigorous testing and is adaptable to a range of usage scenarios. We've successfully attracted numerous customers and generated 50 million Tomans in revenue from this project. While our current system has been trained for Telegram, we are in the process of developing a new system for Instagram and another platform, referred to as 'X'."
