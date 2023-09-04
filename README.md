# New-System-for-Community-Detection

I am currently in the process of developing an innovative community detection system that harnesses a comprehensive suite of community detection algorithms. This system employs a range of techniques, including majority voting and boosting, to amalgamate the results generated by these algorithms, thereby enhancing accuracy and overall effectiveness. This endeavor represents the culmination of my undergraduate studies as it serves as my B.Sc. final project. 

Additionally, I am actively engaged in the task of identifying communities within Stock Markets.

This repository encompasses the following components:

1. Codebase for the development of the combined community detection algorithms system.
2. Presentation materials detailing the development process of the combined community detection algorithms system.
3. Source code for the community detection process specifically tailored to Stock Markets.
4. A final project I designed for a probability and statistics course, focusing on the subject of community detection.

Feel free to reach out if you have any questions or require further information about this project.

## Community Detection Using classic algorithms
You can find the Community Detection codes using classic algorithms in "CD_Classic" folder. In the .py file, there is a system that utilizes the following classic community detection algorithms:
- louvain
- leiden
- hirarchical
- spectral_clustering
- walk_trap
- mcl
- dbscan
- mean_shift
The input consists of the Karate Club dataset, while the output comprises the identified communities generated through the aforementioned algorithms, combined using the majority vote approach.

## Community Detection Using Deep Learning algorithms
Within the repository, you'll find an extensive assortment of code resources thoughtfully organized within the "CD_DL" folder. Our project's approach is intricately designed to build upon the solid foundation laid by the esteemed "CD_Classic" framework, integrating cutting-edge advancements to create a comprehensive suite of community detection algorithms. These algorithms have been meticulously crafted to address a wide array of community detection challenges across various domains and datasets, ensuring the versatility and effectiveness of our community detection system.

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

## Detecting similar stocks by integrating community
In the stock market, certain stocks exhibit similarities in their behavior. For instance, during events like the COVID-19 pandemic in 2020, the stocks of pharmaceutical companies tend to gain increased value. This phenomenon suggests that stocks form interconnected groups or 'communities.' Identifying and categorizing these communities can be instrumental in making more informed investment decisions.
<br>
Community detection algorithms are a powerful tool for identifying and categorizing these communities. These algorithms can be used to construct stock networks based on stock prices and detect dynamic communities within those networks. By analyzing these communities, investors can gain insights into the complex relationships between stocks and improve their investment strategies.
<br>
We have applied community detection algorithms to stock market analysis in various ways. In our study, we used community detection techniques to simplify stock market analysis and selected the Tehran stock exchange for analysis. Another study introduced a methodology for constructing stock networks based on stock prices and detecting dynamic communities. Yet another study explored community detection for the New York stock market and showed the rationality of community detection on the stock market network.
<br>
In the case of Iran's stock market, I am currently engaged in the development of a novel system that uses community detection algorithms for the detection of stock communities. The system is being applied to analyze the dataset from Iran's stock market, and the research paper titled 'Detecting Similar Stocks by Integrating Community Detection Algorithms: A Case Study on the Iran Stock Market' is currently in the preparation stage.
<br>
Overall, community detection algorithms are a valuable tool for stock market analysis. By identifying and categorizing stock communities, investors can gain insights into the complex relationships between stocks and improve their investment strategies. The use of community detection algorithms in stock market analysis is a growing field of research, and there are many opportunities for future studies to explore this topic further

## Presentation
You can find the PowerPoint presentation (as well as its PDF format) in the "PRESENTATION" folder.

## Community Detection Project
While working on this research project, I designed a course project with the same topic, community detection and methods for graph clustering. In "Community-Detection-Project" folder, you'll discover a project centered around the theme of "Graph Clustering Methods". Our approach involves employing community detection algorithms for effective clustering. The primary objective of this project is to showcase the practical applications of probability to students. Alongside this, participants will gain exposure to the realm of recommender systems. Notably, we crafted and executed this project during our tenure as teaching assistants for the probability course at Sharif University of Technology. I had the privilege of leading this group of teaching assistants.
