# Topic 7: Machine Learning
mm_t7 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Machine Learning Paradigms &amp; Mathematical Workflow</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: मशीन लर्निंग (ML) प्रतिमान, एल्गोरिदम एवं जीवन चक्र</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Arthur Samuel &amp; Tom Mitchell • Supervised vs Unsupervised • Ensemble (Random Forest/XGBoost) • Bias-Variance Tradeoff • UP Exam Essentials</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • आर्थर सैमुअल व टॉम मिशेल • सुपरवाइज्ड बनाम अनसुपरवाइज्ड • एन्सेम्बल मेथड्स • बायस-वेरिएंस ट्रेडऑफ • उप्र परीक्षा उपयोगी तथ्य</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-chart-line"></i>
            <span class="lang-en">Machine Learning (ML) Workflow &amp; Paradigms</span>
            <span class="lang-hi">मशीन लर्निंग (ML) जीवन चक्र एवं प्रतिमान</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Foundations, History & ML Life Cycle -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-history" style="color: #059669;"></i>
                    <span class="lang-en">1. ML Foundations &amp; Pipeline</span>
                    <span class="lang-hi">1. ML सैद्धांतिक आधार एवं संपूर्ण जीवन चक्र</span>
                </h4>
                <span class="mindmap-node-tag">Samuel 1959 • Mitchell 1997</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Founders &amp; Pipeline Stages</span>
                        <span class="lang-hi">संस्थापक एवं पाइपलाइन चरण</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Arthur Samuel</strong> (1959, Checkers)</span>
                        <span class="mindmap-chip"><strong>Tom Mitchell</strong> (E, T, P Framework)</span>
                        <span class="mindmap-chip"><strong>Data Cleaning</strong> (Imputation/Outliers)</span>
                        <span class="mindmap-chip"><strong>Feature Scaling</strong> (MinMax/Standard)</span>
                        <span class="mindmap-chip"><strong>Train-Test Split</strong> (80:20 / 70:30)</span>
                        <span class="mindmap-chip"><strong>Hyperparameter Tuning</strong> (GridSearchCV)</span>
                        <span class="mindmap-chip"><strong>MLOps &amp; Drift</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Pioneering Definitions &amp; 6-Step Pipeline</span>
                        <span class="lang-hi">प्रमुख परिभाषाएं एवं 6-चरणीय पाइपलाइन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Arthur Samuel (1959):</strong> Coined the term <em>"Machine Learning"</em> while developing an IBM computer program to play checkers; defined it as "the field of study that gives computers the ability to learn without being explicitly programmed".</span>
                            <span class="lang-hi"><strong>आर्थर सैमुअल (1959):</strong> चेकर्स (शतरंज जैसा खेल) खेलने वाला प्रोग्राम बनाते समय <em>"मशीन लर्निंग"</em> शब्द गढ़ा; परिभाषा दी: "कंप्यूटरों को बिना स्पष्ट प्रोग्रामिंग के स्वतः सीखने की क्षमता प्रदान करना"।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Tom Mitchell's Mathematical Formulation (1997):</strong> A computer program learns from experience $E$ with respect to task $T$ and performance measure $P$, if its performance at task $T$, as measured by $P$, improves with experience $E$.</span>
                            <span class="lang-hi"><strong>टॉम मिशेल का गणितीय सूत्र (1997):</strong> कोई प्रोग्राम कार्य $T$ के संबंध में अनुभव $E$ से सीखता है यदि कार्य $T$ में उसका प्रदर्शन $P$, अनुभव $E$ के साथ बेहतर होता जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>The 6-Step ML Lifecycle:</strong> 1. Problem Formulation &amp; Data Collection -> 2. Data Preprocessing (handling nulls, scaling) -> 3. Feature Engineering (encoding, PCA) -> 4. Model Training -> 5. Hyperparameter Tuning -> 6. Evaluation &amp; Deployment.</span>
                            <span class="lang-hi"><strong>ML का 6-चरणीय जीवन चक्र:</strong> 1. डेटा संग्रह -> 2. डेटा प्रीप्रोसेसिंग (रिक्त मान व आउटलायर हटाना) -> 3. फीचर इंजीनियरिंग -> 4. मॉडल प्रशिक्षण -> 5. हाइपरपैरामीटर ट्यूनिंग -> 6. मूल्यांकन व परिनियोजन (Deployment)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Arthur Samuel coined "Machine Learning" in 1959; Tom Mitchell defined ML formally through E (Experience), T (Task), and P (Performance)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 1959 में आर्थर सैमुअल ने 'मशीन लर्निंग' शब्द गढ़ा; टॉम मिशेल ने इसे E (अनुभव), T (कार्य) व P (प्रदर्शन) द्वारा औपचारिक रूप से परिभाषित किया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Supervised Learning (Regression & Classification) -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tags" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Supervised Learning</span>
                    <span class="lang-hi">2. सुपरवाइज्ड लर्निंग: रिग्रेशन एवं क्लासिफिकेशन</span>
                </h4>
                <span class="mindmap-node-tag">Labeled Data • Regression • SVM</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Supervised Algorithms</span>
                        <span class="lang-hi">प्रमुख सुपरवाइज्ड एल्गोरिदम</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Linear Regression</strong> (Continuous, OLS)</span>
                        <span class="mindmap-chip"><strong>Ridge &amp; Lasso</strong> (L2 / L1 Regularization)</span>
                        <span class="mindmap-chip"><strong>Logistic Regression</strong> (Sigmoid Function)</span>
                        <span class="mindmap-chip"><strong>Decision Trees</strong> (Entropy / Gini)</span>
                        <span class="mindmap-chip"><strong>SVM</strong> (Support Vector Machines, Margin)</span>
                        <span class="mindmap-chip"><strong>KNN</strong> (K-Nearest Neighbors, Lazy Learner)</span>
                        <span class="mindmap-chip"><strong>Naive Bayes</strong> (Bayes Theorem Probability)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Regression vs Classification Mechanics</span>
                        <span class="lang-hi">रिग्रेशन बनाम क्लासिफिकेशन कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Supervised Learning Definition:</strong> Learning algorithm trained on labeled input-output pairs $(X, y)$ to predict outcomes for unseen test data. Divided into <strong>Regression</strong> (continuous output e.g. house price, temperature) and <strong>Classification</strong> (discrete categorical output e.g. spam/not spam, benign/malignant).</span>
                            <span class="lang-hi"><strong>सुपरवाइज्ड लर्निंग परिभाषा:</strong> लेबलयुक्त डेटा $(X, y)$ पर प्रशिक्षित मॉडल। <strong>रिग्रेशन:</strong> सतत संख्यात्मक आउटपुट का अनुमान (उदा. मकान की कीमत, तापमान)। <strong>क्लासिफिकेशन:</strong> असतत श्रेणियों में विभाजन (उदा. स्पैम या नॉन-स्पैम)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Key Classification Algorithms:</strong> <strong>Logistic Regression:</strong> Uses Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ to map real values to probability between 0 and 1. <strong>SVM:</strong> Finds the optimal decision hyperplane that maximizes margin between closest data points (Support Vectors); uses Kernel trick for non-linear boundaries. <strong>Naive Bayes:</strong> Calculates conditional probability assuming feature independence.</span>
                            <span class="lang-hi"><strong>प्रमुख वर्गीकरण एल्गोरिदम:</strong> <strong>लॉजिस्टिक्स रिग्रेशन:</strong> सिग्मॉइड फलन द्वारा 0 और 1 के बीच प्रायिकता देता है। <strong>SVM:</strong> सपोर्ट वेक्टर्स के बीच अधिकतम मार्जिन वाला हाइपरप्लेन खोजता है। <strong>नाइव बेयस:</strong> बेयस प्रमेय पर आधारित प्रायिकता मॉडल।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Logistic Regression is a Classification algorithm (not regression); KNN is called a "Lazy Learner"; Naive Bayes assumes conditional feature independence!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> लॉजिस्टिक्स रिग्रेशन वास्तव में एक क्लासिफिकेशन एल्गोरिदम है; KNN को 'लेज़ी लर्नर' कहा जाता है; नाइव बेयस सभी चरों को स्वतंत्र मानता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Unsupervised Learning (Clustering & Dimensionality) -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-object-group" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Unsupervised Learning</span>
                    <span class="lang-hi">3. अनसुपरवाइज्ड लर्निंग: क्लस्टरिंग एवं डायमेंशनलिटी</span>
                </h4>
                <span class="mindmap-node-tag">Unlabeled • K-Means • PCA</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Clustering &amp; Reduction Techniques</span>
                        <span class="lang-hi">क्लस्टरिंग एवं आयाम न्यूनीकरण तकनीकें</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>K-Means Clustering</strong> (Centroids &amp; Elbow)</span>
                        <span class="mindmap-chip"><strong>Hierarchical Clustering</strong> (Dendrograms)</span>
                        <span class="mindmap-chip"><strong>DBSCAN</strong> (Density Based Spatial)</span>
                        <span class="mindmap-chip"><strong>PCA</strong> (Principal Component Analysis)</span>
                        <span class="mindmap-chip"><strong>t-SNE &amp; UMAP</strong> (Manifold Visualization)</span>
                        <span class="mindmap-chip"><strong>Apriori</strong> (Market Basket Analysis)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Unsupervised Mechanics &amp; Algorithms</span>
                        <span class="lang-hi">अनसुपरवाइज्ड कार्यप्रणाली एवं तकनीक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Unsupervised Learning Definition:</strong> Discovers hidden structures, inherent patterns, or groupings within <strong>unlabeled data</strong> without any predefined target labels or supervisor feedback.</span>
                            <span class="lang-hi"><strong>अनसुपरवाइज्ड लर्निंग:</strong> बिना किसी लेबलयुक्त उत्तर या पर्यवेक्षक के, डेटा में अंतर्निहित पैटर्न, समानताएं और प्राकृतिक समूह (क्लस्टर) खोजना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>K-Means Clustering:</strong> Partitions data into $K$ distinct clusters by minimizing sum of squared distances to cluster centroids. Optimal number of clusters $K$ determined using the <strong>Elbow Method</strong> (inertia plot).</span>
                            <span class="lang-hi"><strong>K-मीन्स क्लस्टरिंग:</strong> डेटा को $K$ समूहों में सेंट्रॉइड्स के आधार पर बांटता है। उपयुक्त $K$ का मान <strong>एल्बो मेथड (Elbow Method)</strong> ग्राफ द्वारा तय होता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Principal Component Analysis (PCA):</strong> Dimensionality reduction technique that transforms large number of correlated variables into a smaller set of orthogonal, uncorrelated variables called <strong>Principal Components</strong>, capturing maximum variance using eigenvectors.</span>
                            <span class="lang-hi"><strong>प्रिंसिपल कंपोनेंट एनालिसिस (PCA):</strong> अत्यधिक चरों (हाई डायमेंशन) को कम चरों में बदलना; आइगेनवेक्टर्स द्वारा अधिकतम विचरण (Variance) को संरक्षित रखता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> K-Means requires specifying K in advance; Elbow Method finds optimal K; PCA is an unsupervised dimensionality reduction method!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> K-मीन्स में K का मान पहले से देना होता है; एल्बो विधि द्वारा श्रेष्ठ K चुना जाता है; PCA आयाम घटाने (डायमेंशनलिटी रिडक्शन) की मुख्य तकनीक है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Ensemble Learning & Reinforcement Learning -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-trophy" style="color: #d97706;"></i>
                    <span class="lang-en">4. Ensemble &amp; Reinforcement Learning</span>
                    <span class="lang-hi">4. एन्सेम्बल मेथड्स एवं रीइन्फोर्समेंट लर्निंग</span>
                </h4>
                <span class="mindmap-node-tag">Bagging • Boosting • Q-Learning</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Ensemble Models &amp; RL Concepts</span>
                        <span class="lang-hi">एन्सेम्बल मॉडल्स एवं RL संकल्पनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Bagging</strong> (Bootstrap Aggregation)</span>
                        <span class="mindmap-chip"><strong>Random Forest</strong> (Leo Breiman, 2001)</span>
                        <span class="mindmap-chip"><strong>Boosting</strong> (Sequential Error Correction)</span>
                        <span class="mindmap-chip"><strong>AdaBoost &amp; XGBoost</strong> (High Performance)</span>
                        <span class="mindmap-chip"><strong>Agent &amp; Environment</strong> (Action, State, Reward)</span>
                        <span class="mindmap-chip"><strong>Markov Decision Process</strong> (MDP)</span>
                        <span class="mindmap-chip"><strong>Q-Learning</strong> (Bellman Equation)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Ensemble Techniques &amp; RL Mechanics</span>
                        <span class="lang-hi">एन्सेम्बल तकनीक एवं RL की कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bagging vs Boosting:</strong> <strong>Bagging (Bootstrap Aggregating):</strong> Trains multiple base learners in parallel on bootstrap sample subsets; reduces variance (e.g. Random Forest). <strong>Boosting:</strong> Trains models sequentially where each new model focuses on instances misclassified by earlier models; reduces bias (e.g. AdaBoost, Gradient Boosting, XGBoost).</span>
                            <span class="lang-hi"><strong>बैगिंग बनाम बूस्टिंग:</strong> <strong>बैगिंग:</strong> स्वतंत्र मॉडल समानांतर में चलाकर वेरिएंस घटाता है (रैंडम फॉरेस्ट)। <strong>बूस्टिंग:</strong> क्रमिक रूप से मॉडल चलाता है जहाँ प्रत्येक अगला मॉडल पिछली गलतियों को सुधारता है; बायस घटाता है (XGBoost, AdaBoost)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Reinforcement Learning (RL):</strong> Trial-and-error learning paradigm where an <strong>Agent</strong> interacts with an <strong>Environment</strong>, performs <strong>Actions</strong> ($A$), observes resulting <strong>States</strong> ($S$), and receives scalar <strong>Rewards</strong> ($R$) to maximize cumulative future reward (Bellman Equation, Q-Learning). Used in AlphaGo and autonomous driving.</span>
                            <span class="lang-hi"><strong>रीइन्फोर्समेंट लर्निंग (RL):</strong> 'प्रयास एवं त्रुटि' आधारित अधिगम; एक <strong>एजेंट</strong> अपने <strong>पर्यावरण</strong> में <strong>कार्य (Action)</strong> करता है, और बदले में <strong>पुरस्कार (Reward)</strong> या दंड प्राप्त कर अपनी रणनीति सुधारता है (Q-लर्निंग)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Random Forest is based on Bagging (parallel trees); XGBoost is based on Boosting (sequential correction); Q-Learning is a Reinforcement Learning algorithm!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> रैंडम फॉरेस्ट 'बैगिंग' पर आधारित है; XGBoost 'बूस्टिंग' पर आधारित है; Q-लर्निंग रीइन्फोर्समेंट लर्निंग का प्रमुख एल्गोरिदम है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Bias-Variance Tradeoff & Evaluation Metrics -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-balance-scale-right" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Bias-Variance &amp; Evaluation Metrics</span>
                    <span class="lang-hi">5. बायस-वेरिएंस ट्रेडऑफ एवं मॉडल मूल्यांकन</span>
                </h4>
                <span class="mindmap-node-tag">Underfitting • Overfitting • F1-Score</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Evaluation Metrics &amp; Curves</span>
                        <span class="lang-hi">मूल्यांकन मानक एवं मैट्रिक्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Confusion Matrix</strong> (TP, TN, FP, FN)</span>
                        <span class="mindmap-chip"><strong>Accuracy</strong> (Overall Correct)</span>
                        <span class="mindmap-chip"><strong>Precision</strong> (TP / TP+FP)</span>
                        <span class="mindmap-chip"><strong>Recall / Sensitivity</strong> (TP / TP+FN)</span>
                        <span class="mindmap-chip"><strong>F1-Score</strong> (Harmonic Mean of P &amp; R)</span>
                        <span class="mindmap-chip"><strong>ROC-AUC</strong> (True vs False Positive)</span>
                        <span class="mindmap-chip"><strong>K-Fold Cross Validation</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Overfitting vs Underfitting Mechanics</span>
                        <span class="lang-hi">ओवरफिटिंग बनाम अंडरफिटिंग कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bias-Variance Tradeoff:</strong> <strong>High Bias (Underfitting):</strong> Model is too simple to capture underlying trend; performs poorly on BOTH training and test data. <strong>High Variance (Overfitting):</strong> Model is overly complex; memorizes training noise; performs exceptionally on training data but fails miserably on unseen test data.</span>
                            <span class="lang-hi"><strong>बायस-वेरिएंस ट्रेडऑफ:</strong> <strong>उच्च बायस (अंडरफिटिंग):</strong> मॉडल इतना सरल है कि डेटा का पैटर्न समझ नहीं पाता (ट्रेनिंग व टेस्ट दोनों में खराब परिणाम)। <strong>उच्च वेरिएंस (ओवरफिटिंग):</strong> मॉडल ट्रेनिंग डेटा को रट लेता है (ट्रेनिंग में 100% सही लेकिन नए डेटा पर पूरी तरह फेल)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Confusion Matrix Metrics:</strong> <strong>Precision:</strong> Measures exactness $\frac{TP}{TP + FP}$ (crucial when false positives are costly, e.g. spam filter). <strong>Recall (Sensitivity):</strong> Measures completeness $\frac{TP}{TP + FN}$ (crucial when false negatives are dangerous, e.g. cancer detection). <strong>F1-Score:</strong> Harmonic mean of Precision and Recall: $\frac{2 \times P \times R}{P + R}$.</span>
                            <span class="lang-hi"><strong>कन्फ्यूजन मैट्रिक्स मानक:</strong> <strong>प्रिसिजन (परिशुद्धता):</strong> $\frac{TP}{TP + FP}$ (स्पैम जांच में उपयोगी)। <strong>रिकॉल (संवेदनशीलता):</strong> $\frac{TP}{TP + FN}$ (कैंसर या बीमारी जांच में अनिवार्य)। <strong>F1-स्कोर:</strong> प्रिसिजन और रिकॉल का हरात्मक माध्य (Harmonic Mean)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Overfitting means high variance and low bias; F1-score is the Harmonic Mean of Precision and Recall; K-Fold Cross Validation prevents overfitting!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ओवरफिटिंग का अर्थ उच्च वेरिएंस व निम्न बायस है; F1-स्कोर प्रिसिजन व रिकॉल का हरात्मक माध्य है; K-फोल्ड क्रॉस वैलिडेशन ओवरफिटिंग रोकता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Tools, Frameworks & Uttar Pradesh Use Cases -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tools" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. ML Frameworks &amp; UP Applications</span>
                    <span class="lang-hi">6. ML टूल्स, फ्रेमवर्क एवं उत्तर प्रदेश अनुप्रयोग</span>
                </h4>
                <span class="mindmap-node-tag">Scikit-Learn • UP Agri • UPPCL</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Libraries &amp; Governance Projects</span>
                        <span class="lang-hi">लाइब्रेरी एवं सरकारी परियोजनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Scikit-Learn</strong> (Core Classical ML)</span>
                        <span class="mindmap-chip"><strong>NumPy &amp; Pandas</strong> (Array &amp; DataFrames)</span>
                        <span class="mindmap-chip"><strong>Matplotlib &amp; Seaborn</strong> (Data Viz)</span>
                        <span class="mindmap-chip"><strong>UP Agriculture ML</strong> (Crop Yield Prediction)</span>
                        <span class="mindmap-chip"><strong>UPPCL Smart Metering</strong> (Theft Detection)</span>
                        <span class="mindmap-chip"><strong>UP Scholarship Portal</strong> (Fraud Prevention)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Real-World Government Applications in UP</span>
                        <span class="lang-hi">उत्तर प्रदेश में वास्तविक सरकारी अनुप्रयोग</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Agricultural Crop Yield &amp; Soil Analytics:</strong> UP Agriculture Department integrates satellite remote sensing with regression ML models to estimate wheat, paddy, and sugarcane yields in advance across 75 districts.</span>
                            <span class="lang-hi"><strong>कृषि उपज एवं मृदा विश्लेषण:</strong> उप्र कृषि विभाग रिमोट सेंसिंग व ML रिग्रेशन मॉडल द्वारा राज्य के 75 जिलों में गेहूं, धान व गन्ने की उपज का अग्रिम सटीक अनुमान लगाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UPPCL Smart Power Loss Detection:</strong> Machine learning anomaly detection algorithms analyze smart electricity meter feeds to detect power theft, bypass tampering, and reduce Aggregate Technical &amp; Commercial (AT&amp;C) losses.</span>
                            <span class="lang-hi"><strong>UPPCL बिजली चोरी रोकथाम:</strong> स्मार्ट मीटरों के डेटा पर ML एनोमली डिटेक्शन मॉडल चलाकर बिजली चोरी व मीटर बाईपास की त्वरित पहचान की जाती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Welfare Fraud Detection:</strong> Machine learning deduplication and verification models prevent duplicate claims in UP scholarship distribution and farmer DBT subsidy schemes.</span>
                            <span class="lang-hi"><strong>कल्याणकारी योजनाओं में फर्जीवाड़ा रोकथाम:</strong> छात्रवृत्ति वितरण एवं किसान सम्मान निधि/सब्सिडी में फर्जी व दोहरे आवेदनों की पहचान हेतु ML सत्यापन का उपयोग।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Scikit-learn is the primary Python library for classical ML algorithms; UPPCL uses ML anomaly detection on smart meter data!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> Scikit-learn शास्त्रीय ML एल्गोरिदम की प्रमुख पायथन लाइब्रेरी है; UPPCL बिजली चोरी रोकने हेतु स्मार्ट मीटरों पर ML का उपयोग करता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
