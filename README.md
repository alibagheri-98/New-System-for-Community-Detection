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
<b>The abstract of our report:<\b>
<br>
The aim of our research is to analyze the stock market by detecting the community structure using various distance and clustering methods. We utilized Dynamic Time Warping (DTW) as a distance measure due to its ability to capture delays and time shifts and wraps. We also used a modified version of DTW that is not sensitive to singularities which are mostly noises, along with two other distance detection methods. We then constructed four graph based on these distances, where the edges represent similarity. another method used is to represent each stock time series in a low dimensional vector, to do that we extracted the feature vector using auto encoders.
<br>
We applied multiple classical clustering using four graph structural dataset and a voting mechanism between these clustering methods and dataset to obtain a more robust result. Furthermore, we employed deep learning techniques such as convolutional neural networks (CNN) to cluster stocks. We also used graph neural networks (GNN) which is modified for graph structural input. We also used NLP to find the industry, country, etc of stocks as a feature for deep learning algorthims.
<br>
Our results demonstrate that the community structure in the stock market can be identified using DTW and other distance measures. The use of
autoencoders and deep learning techniques in clustering and community detection showed promising results. Ultimately, our research contributes to the
understanding and analysis of the stock market and its structures which can potentially be used in portfolio optimization to inform investment decisions
## Presentation
You can find the PowerPoint presentation (as well as its PDF format) in the "PRESENTATION" folder.

## Community Detection Project
During the course of my research project, I had the opportunity to develop an educational initiative centered around the topic of community detection and graph clustering methods. Inside the "Community-Detection-Project" folder, you'll find a comprehensive project dedicated to exploring the realm of "Graph Clustering Methods." Our approach focuses on utilizing community detection algorithms to facilitate effective clustering of data. The primary goal of this initiative is to introduce students to the practical applications of probability theory while providing them with valuable insights into the world of recommender systems.

This project was conceived and executed during our tenure as teaching assistants at Sharif University of Technology. In this capacity, we had the privilege of leading a group of teaching assistants, collaborating to create a meaningful and educational experience for students. Our shared objective was to not only impart knowledge but also to foster a deeper understanding of probability concepts and their real-world applications.

Within the "Community-Detection-Project" folder, you will uncover the details of this educational endeavor, including instructional materials, project documentation, and resources aimed at enhancing students' comprehension of community detection and graph clustering. Should you have any inquiries or seek further information regarding this educational initiative, please do not hesitate to reach out ([bagheri9877@gmail.com](bagheri9877@gmail.com)). We are dedicated to promoting educational excellence and sharing our experiences in the field of probability and community detection.
