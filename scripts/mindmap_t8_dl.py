# Topic 8: Deep Learning
mm_t8 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Deep Learning Neural Architectures &amp; Optimization</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: डीप लर्निंग (DL) न्यूरल नेटवर्क, अनुकूलन एवं अनुप्रयोग</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Biological to Artificial Neurons • Activations (ReLU/Sigmoid) • Backprop &amp; Adam Optimizer • CNNs (Convolution/Pooling) • RNN &amp; LSTM • Trinetra 2.0</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • जैविक से कृत्रिम न्यूरॉन • एक्टिवेशन फंक्शन्स • बैकप्रोपगेशन व एडम ऑप्टिमाइज़र • CNN (कनवोल्यूशन/पूलिंग) • RNN व LSTM • त्रिनेत्र 2.0 उप्र</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-network-wired"></i>
            <span class="lang-en">Deep Learning (DL) Neural Network Architecture</span>
            <span class="lang-hi">डीप लर्निंग (DL) न्यूरल नेटवर्क वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Biological to Artificial Neurons & Perceptron -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-brain" style="color: #059669;"></i>
                    <span class="lang-en">1. Biological to Artificial Neurons</span>
                    <span class="lang-hi">1. जैविक न्यूरॉन से कृत्रिम न्यूरॉन व परसेप्ट्रॉन</span>
                </h4>
                <span class="mindmap-node-tag">Rosenblatt 1958 • MLP</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Structural Analogies &amp; Pioneers</span>
                        <span class="lang-hi">संरचनात्मक समानताएं एवं वैज्ञानिक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Dendrite -> Inputs</strong> ($x_i$)</span>
                        <span class="mindmap-chip"><strong>Synapse -> Weights</strong> ($w_i$)</span>
                        <span class="mindmap-chip"><strong>Soma -> Summation &amp; Bias</strong> ($\sum w_i x_i + b$)</span>
                        <span class="mindmap-chip"><strong>Axon -> Output</strong> ($y$)</span>
                        <span class="mindmap-chip"><strong>McCulloch-Pitts</strong> (1943 Model)</span>
                        <span class="mindmap-chip"><strong>Rosenblatt Perceptron</strong> (1958)</span>
                        <span class="mindmap-chip"><strong>XOR Problem</strong> (Minsky &amp; Papert 1969)</span>
                        <span class="mindmap-chip"><strong>Multi-Layer Perceptron</strong> (MLP)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Biological Analogy &amp; Perceptron Mechanics</span>
                        <span class="lang-hi">जैविक समानता एवं परसेप्ट्रॉन कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Biological to Artificial Analogy:</strong> Human brain has ~86 billion neurons. <strong>Dendrites</strong> receive incoming electrical signals (Inputs $x_i$). <strong>Synaptic strength</strong> corresponds to connection Weights ($w_i$). <strong>Soma (cell body)</strong> sums weighted inputs with Bias ($\sum w_i x_i + b$). <strong>Axon</strong> fires signal through activation function if threshold exceeded (Output).</span>
                            <span class="lang-hi"><strong>जैविक एवं कृत्रिम न्यूरॉन समानता:</strong> मानव मस्तिष्क में ~86 अरब न्यूरॉन। <strong>डेंड्राइट:</strong> इनपुट ($x_i$)। <strong>सिनैप्स:</strong> कनेक्शन भार/वेट्स ($w_i$)। <strong>सोमा:</strong> वेटेड सम व बायस ($\sum w_i x_i + b$)। <strong>एक्सॉन:</strong> एक्टिवेशन फलन द्वारा प्रेषित आउटपुट।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Perceptron &amp; The XOR Limitation (1969):</strong> Frank Rosenblatt (1958) created the Perceptron (single-layer binary linear classifier). In 1969, Marvin Minsky &amp; Seymour Papert proved mathematically that a single-layer perceptron CANNOT solve linearly inseparable problems like the XOR gate, triggering the 1st AI Winter. Multi-Layer Perceptrons (MLP with hidden layers) solved this.</span>
                            <span class="lang-hi"><strong>परसेप्ट्रॉन एवं XOR समस्या:</strong> फ्रैंक रोसेनब्लैट (1958) ने सिंगल-लेयर परसेप्ट्रॉन बनाया। 1969 में मिंस्की व पेपरट ने सिद्ध किया कि सिंगल लेयर परसेप्ट्रॉन XOR गेट (गैर-रैखिक समस्या) को हल नहीं कर सकता। बाद में मल्टी-लेयर परसेप्ट्रॉन (MLP) ने हिडन लेयर्स जोड़कर इसे हल किया।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Frank Rosenblatt invented the Perceptron in 1958; single-layer perceptrons cannot solve the XOR logic gate; MLPs solve XOR using hidden layers!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 1958 में फ्रैंक रोसेनब्लैट ने परसेप्ट्रॉन बनाया; सिंगल-लेयर परसेप्ट्रॉन XOR गेट को हल नहीं कर सकता; MLP हिडन लेयर्स द्वारा इसे हल करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Activation Functions & Mathematics -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-wave-square" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Activation Functions</span>
                    <span class="lang-hi">2. एक्टिवेशन फंक्शन्स एवं गणितीय आधार</span>
                </h4>
                <span class="mindmap-node-tag">Non-Linearity • ReLU • Softmax</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Activation Functions</span>
                        <span class="lang-hi">प्रमुख एक्टिवेशन फंक्शन्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Sigmoid</strong> (Range 0 to 1)</span>
                        <span class="mindmap-chip"><strong>Tanh</strong> (Range -1 to 1, Zero-Centered)</span>
                        <span class="mindmap-chip"><strong>ReLU</strong> (Max(0, z), Most Popular)</span>
                        <span class="mindmap-chip"><strong>Leaky ReLU</strong> (Max(0.01z, z))</span>
                        <span class="mindmap-chip"><strong>Softmax</strong> (Multiclass Probability)</span>
                        <span class="mindmap-chip"><strong>Vanishing Gradient</strong> Problem</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Function Characteristics &amp; Ranges</span>
                        <span class="lang-hi">फलन की विशेषताएं एवं आउटपुट सीमाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Why Non-Linearity Matters:</strong> Without activation functions, any deep network collapses into a simple linear regression regardless of depth. Activation functions introduce non-linearity, enabling deep networks to learn complex arbitrary patterns (Universal Approximation Theorem).</span>
                            <span class="lang-hi"><strong>गैर-रैखिकता (Non-Linearity) का महत्व:</strong> बिना एक्टिवेशन फलन के, कितने भी गहरे नेटवर्क हों, वे केवल एक साधारण रेखीय समीकरण बन जाते हैं। एक्टिवेशन फलन ही नेटवर्क को जटिल आकृतियां सीखने की शक्ति देते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ReLU (Rectified Linear Unit):</strong> Defined as $f(z) = \max(0, z)$. Range $[0, \infty)$. Computationally ultra-fast; derivative is 1 for $z &gt; 0$, effectively solving the Vanishing Gradient problem that plagues Sigmoid and Tanh in deep hidden layers.</span>
                            <span class="lang-hi"><strong>ReLU (रेक्टिफाइड लीनियर यूनिट):</strong> सूत्र: $f(z) = \max(0, z)$। आउटपुट सीमा: 0 से अनंत। हिडन लेयर्स में सबसे लोकप्रिय; वैनिशिंग ग्रेडिएंट समस्या को समाप्त करता है क्योंकि $z &gt; 0$ पर इसका ढलान 1 रहता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Softmax Function:</strong> Applied at final output layer for multi-class classification. Converts raw output numbers (logits) into a normalized probability distribution where all probabilities sum strictly to 1.</span>
                            <span class="lang-hi"><strong>सॉफ्टमैक्स (Softmax):</strong> मल्टी-क्लास वर्गीकरण की अंतिम परत पर प्रयुक्त। सभी वर्गों के स्कोर को प्रायिकता वितरण में बदलता है, जिनका कुल योग सदैव 1 (100%) होता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sigmoid outputs between 0 and 1; Tanh outputs between -1 and 1; ReLU outputs Max(0, z) and is the most popular hidden layer activation!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सिग्मॉइड का आउटपुट 0 से 1; Tanh का -1 से 1; तथा ReLU का मान Max(0, z) होता है और यह हिडन लेयर्स में सर्वाधिक प्रयुक्त होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Training, Backpropagation & Optimizers -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-sliders-h" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Training &amp; Backpropagation</span>
                    <span class="lang-hi">3. नेटवर्क प्रशिक्षण, बैकप्रोपगेशन एवं ऑप्टिमाइज़र</span>
                </h4>
                <span class="mindmap-node-tag">Chain Rule • Gradient Descent • Adam</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Training Steps &amp; Optimizers</span>
                        <span class="lang-hi">प्रशिक्षण चरण एवं ऑप्टिमाइज़र्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Forward Pass</strong> (Loss Computation)</span>
                        <span class="mindmap-chip"><strong>Loss Function</strong> (MSE / Cross-Entropy)</span>
                        <span class="mindmap-chip"><strong>Backpropagation</strong> (Rumelhart 1986, Chain Rule)</span>
                        <span class="mindmap-chip"><strong>Gradient Descent</strong> (SGD / Mini-Batch)</span>
                        <span class="mindmap-chip"><strong>Adam Optimizer</strong> (Kingma &amp; Ba 2014)</span>
                        <span class="mindmap-chip"><strong>Learning Rate</strong> ($\alpha$ Hyperparameter)</span>
                        <span class="mindmap-chip"><strong>Dropout Regularization</strong> (Srivastava 2014)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Backpropagation Mechanics &amp; Adam Optimizer</span>
                        <span class="lang-hi">बैकप्रोपगेशन कार्यप्रणाली एवं एडम ऑप्टिमाइज़र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Backpropagation (Rumelhart, Hinton &amp; Williams, 1986):</strong> Heart of deep learning training. Uses Calculus <strong>Chain Rule</strong> to propagate errors backward from output layer through hidden layers, calculating partial derivative of loss with respect to every weight ($\frac{\partial L}{\partial w}$) to update weights: $w_{new} = w_{old} - \alpha \frac{\partial L}{\partial w}$.</span>
                            <span class="lang-hi"><strong>बैकप्रोपगेशन (हिंटन आदि, 1986):</strong> डीप लर्निंग प्रशिक्षण का केंद्र। कैलकुलस के <strong>चेन रूल (Chain Rule)</strong> द्वारा त्रुटि को आउटपुट से पीछे की ओर भेजता है और प्रत्येक वेट के प्रति ढलान (Gradient) ज्ञात कर वेट्स अपडेट करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Adam Optimizer (Adaptive Moment Estimation, 2014):</strong> Combines advantages of <strong>Momentum</strong> (accelerating through flat regions using moving average of gradients) and <strong>RMSProp</strong> (adapting learning rates using moving average of squared gradients). Current industry gold standard.</span>
                            <span class="lang-hi"><strong>एडम ऑप्टिमाइज़र (Adam):</strong> मोमेंटम और RMSProp दोनों की खूबियों को जोड़कर प्रत्येक पैरामीटर हेतु अनुकूलित लर्निंग रेट निर्धारित करता है; आधुनिक डीप लर्निंग का सबसे लोकप्रिय ऑप्टिमाइज़र।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dropout Regularization (2014):</strong> Randomly deactivates (drops out) a fraction $p$ (e.g. 20-50%) of neurons during each training step, preventing co-adaptation and effectively fighting overfitting.</span>
                            <span class="lang-hi"><strong>ड्रॉपआउट (Dropout):</strong> प्रशिक्षण के दौरान यादृच्छिक रूप से 20-50% न्यूरॉन्स को अस्थायी रूप से बंद कर देता है, जिससे ओवरफिटिंग पर प्रभावी रोक लगती है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Backpropagation uses the Calculus Chain Rule to update network weights; Adam is an adaptive learning rate optimizer; Dropout prevents overfitting!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बैकप्रोपगेशन चेन रूल द्वारा वेट्स को अपडेट करता है; एडम (Adam) अडेप्टिव लर्निंग रेट ऑप्टिमाइज़र है; ड्रॉपआउट ओवरफिटिंग रोकता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Convolutional Neural Networks (CNNs) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-image" style="color: #d97706;"></i>
                    <span class="lang-en">4. CNNs &amp; Computer Vision</span>
                    <span class="lang-hi">4. कनवोल्यूशनल न्यूरल नेटवर्क (CNN) एवं कंप्यूटर विजन</span>
                </h4>
                <span class="mindmap-node-tag">Filters • Max Pooling • AlexNet</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">CNN Layers &amp; Milestones</span>
                        <span class="lang-hi">CNN की परतें एवं ऐतिहासिक मॉडल</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Convolution Layer</strong> (Kernels/Filters)</span>
                        <span class="mindmap-chip"><strong>Stride &amp; Padding</strong> (Valid vs Same)</span>
                        <span class="mindmap-chip"><strong>Pooling Layer</strong> (Max Pooling, Downsampling)</span>
                        <span class="mindmap-chip"><strong>Fully Connected (FC)</strong> (Final Dense Layer)</span>
                        <span class="mindmap-chip"><strong>LeNet-5</strong> (Yann LeCun, 1998, Check OCR)</span>
                        <span class="mindmap-chip"><strong>AlexNet</strong> (2012, ImageNet Revolution)</span>
                        <span class="mindmap-chip"><strong>ResNet</strong> (Residual Skip Connections)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Layer Mechanics &amp; Visual Feature Extraction</span>
                        <span class="lang-hi">परतों की कार्यप्रणाली एवं छवि फीचर निष्कर्षण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Convolution Layer:</strong> Applies small learnable matrix filters (e.g. $3 \times 3$ kernels) that slide across the image using element-wise dot multiplication to extract spatial features like edges, textures, corners, and object parts.</span>
                            <span class="lang-hi"><strong>कनवोल्यूशन परत:</strong> छोटे फिल्टर्स ($3 \times 3$ कर्नेल) को छवि पर घुमाकर किनारों (Edges), बनावट (Textures) व आकृतियों जैसे दृश्य फीचर्स का निष्कर्षण करती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Pooling Layer (Max Pooling):</strong> Downsamples feature maps by taking maximum value within local window (e.g. $2 \times 2$ window with stride 2); reduces spatial dimensions by 75%, cuts computational parameters, and provides translation invariance.</span>
                            <span class="lang-hi"><strong>पूलिंग परत (मैक्स पूलिंग):</strong> फीचर मैप के आकार को छोटा (डाउनसैंपल) करती है; $2 \times 2$ विंडो में से अधिकतम मान चुनती है; गणना का बोझ घटाती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>AlexNet (2012):</strong> Landmark deep CNN designed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton; won ImageNet Challenge 2012 by reducing error rate from 26% to 15.3% using GPUs, ReLU, and Dropout; ignited modern Deep Learning revolution!</span>
                            <span class="lang-hi"><strong>एलेक्सनेट (AlexNet - 2012):</strong> हिंटन व सुत्स्केवर की टीम द्वारा निर्मित; ImageNet प्रतियोगिता में GPU, ReLU व ड्रॉपआउट का उपयोग कर ऐतिहासिक विजय हासिल की; आधुनिक डीप लर्निंग क्रांति का जनक!</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> CNN is the premier architecture for image and video processing; Max Pooling reduces spatial size; AlexNet (2012) sparked the modern DL explosion!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> इमेज व वीडियो प्रोसेसिंग हेतु CNN प्रमुख आर्किटेक्चर है; मैक्स पूलिंग आकार छोटा करती है; एलेक्सनेट (2012) से आधुनिक डीप लर्निंग की शुरुआत हुई!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Sequential Models: RNN & LSTM -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-stream" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Sequential Models: RNN &amp; LSTM</span>
                    <span class="lang-hi">5. सीक्वेंशियल मॉडल्स: RNN एवं LSTM</span>
                </h4>
                <span class="mindmap-node-tag">Hidden State • Forget Gate • 1997</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Sequential Architectures &amp; Gates</span>
                        <span class="lang-hi">सीक्वेंशियल संरचनाएं एवं गेट्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>RNN</strong> (Recurrent Neural Network)</span>
                        <span class="mindmap-chip"><strong>Hidden State</strong> (Memory Across Time)</span>
                        <span class="mindmap-chip"><strong>Vanishing Gradient</strong> (Long Sequences Fail)</span>
                        <span class="mindmap-chip"><strong>LSTM</strong> (Hochreiter &amp; Schmidhuber 1997)</span>
                        <span class="mindmap-chip"><strong>Forget Gate</strong> (Discards Irrelevant Info)</span>
                        <span class="mindmap-chip"><strong>Input Gate</strong> (Stores New Candidate Info)</span>
                        <span class="mindmap-chip"><strong>Output Gate</strong> (Controls Emitted State)</span>
                        <span class="mindmap-chip"><strong>Cell State</strong> (Long-Term Memory Highway)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Sequential Architecture &amp; LSTM 3-Gate Mechanism</span>
                        <span class="lang-hi">सीक्वेंशियल संरचना एवं LSTM के 3 गेट्स</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Recurrent Neural Networks (RNN):</strong> Designed for sequential and time-series data (speech, text, sensor streams). Passes internal <strong>Hidden State</strong> from one time-step to next. However, standard RNNs suffer from vanishing and exploding gradients, making them unable to retain long-term dependencies.</span>
                            <span class="lang-hi"><strong>आवर्ती न्यूरल नेटवर्क (RNN):</strong> अनुक्रमिक डेटा (टेक्स्ट, भाषण, समय श्रृंखला) हेतु डिजाइन किया गया नेटवर्क; पिछले समय का 'हिडन स्टेट' आगे भेजता है; किंतु लंबे अनुक्रमों में वैनिशिंग ग्रेडिएंट के कारण भूल जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>LSTM (Long Short-Term Memory, 1997):</strong> Invented by Sepp Hochreiter &amp; Jürgen Schmidhuber. Solves the vanishing gradient problem using a constant error carousel (Cell State) regulated by <strong>3 Sigmoid Gates</strong>: <strong>Forget Gate</strong> (what old info to erase), <strong>Input Gate</strong> (what new info to store), and <strong>Output Gate</strong> (what info to output).</span>
                            <span class="lang-hi"><strong>LSTM (लॉन्ग शॉर्ट-टर्म मेमोरी, 1997):</strong> होचराइटर व श्मिटहुबर द्वारा आविष्कृत। सेल स्टेट (दीर्घकालिक मेमोरी) तथा <strong>3 गेट्स</strong> द्वारा पुरानी यादों को सुरक्षित रखता है: <strong>फॉरगेट गेट</strong> (व्यर्थ डेटा हटाना), <strong>इनपुट गेट</strong> (नया डेटा जोड़ना), व <strong>आउटपुट गेट</strong> (परिणाम निकालना)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> LSTM was invented in 1997 by Hochreiter &amp; Schmidhuber to solve RNN vanishing gradients; it uses three gates: Forget Gate, Input Gate, and Output Gate!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> RNN की वैनिशिंग ग्रेडिएंट समस्या मिटाने हेतु 1997 में LSTM बना; इसमें तीन गेट होते हैं: फॉरगेट गेट, इनपुट गेट एवं आउटपुट गेट!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Hardware, Frameworks & Uttar Pradesh Applications -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-server" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Hardware, Frameworks &amp; UP Apps</span>
                    <span class="lang-hi">6. हार्डवेयर, फ्रेमवर्क एवं उप्र में डीप लर्निंग अनुप्रयोग</span>
                </h4>
                <span class="mindmap-node-tag">PyTorch • Trinetra 2.0 • ITMS</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Accelerators &amp; UP Real-World Projects</span>
                        <span class="lang-hi">हार्डवेयर त्वरक एवं उप्र में वास्तविक परियोजनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>NVIDIA GPUs</strong> (CUDA &amp; Tensor Cores)</span>
                        <span class="mindmap-chip"><strong>Google TPU</strong> (Matrix Multiplication)</span>
                        <span class="mindmap-chip"><strong>PyTorch</strong> (Meta) &amp; <strong>TensorFlow</strong> (Google)</span>
                        <span class="mindmap-chip"><strong>Trinetra 2.0</strong> (UP Police Face Recognition)</span>
                        <span class="mindmap-chip"><strong>UP Smart Traffic ITMS</strong> (ANPR Cameras)</span>
                        <span class="mindmap-chip"><strong>Maha Kumbh 2025</strong> (Crowd Density DL)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Hardware Acceleration &amp; UP State Implementations</span>
                        <span class="lang-hi">हार्डवेयर त्वरण एवं उत्तर प्रदेश में क्रियान्वयन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hardware Accelerators:</strong> GPUs (NVIDIA CUDA cores) execute thousands of parallel floating-point matrix multiplications simultaneously, training networks 50-100x faster than CPUs. Google TPUs (Tensor Processing Units) feature systolic array ASICs tailored specifically for matrix dot products.</span>
                            <span class="lang-hi"><strong>हार्डवेयर त्वरक:</strong> GPU (NVIDIA CUDA) समानांतर में हजारों मैट्रिक्स गुणन निष्पादित करते हैं; CPU से 50-100 गुना तेज। गूगल TPU विशेष रूप से न्यूरल नेटवर्क मैट्रिक्स गणना हेतु निर्मित ASIC चिप्स हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Trinetra 2.0 (UP Police):</strong> Advanced deep CNN-based facial recognition platform deployed across Uttar Pradesh police stations, railway terminals, and Kumbh Mela to identify criminals and missing persons in real-time video streams.</span>
                            <span class="lang-hi"><strong>त्रिनेत्र 2.0 (उप्र पुलिस):</strong> गहरे CNN आधारित फेशियल रिकॉग्निशन तकनीक; उप्र के रेलवे स्टेशनों, थानों व महाकुंभ में भीड़ के लाइव कैमरों से अपराधियों व लापता व्यक्तियों की तत्काल पहचान।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ITMS (Integrated Traffic Management System):</strong> Deployed in Lucknow, Kanpur, Prayagraj, Varanasi, Ayodhya using deep learning computer vision for Automatic Number Plate Recognition (ANPR), red-light violations, and speed detection.</span>
                            <span class="lang-hi"><strong>स्मार्ट ट्रैफिक ITMS:</strong> लखनऊ, कानपुर, प्रयागराज, वाराणसी व अयोध्या में डीप लर्निंग ANPR कैमरों द्वारा स्वचालित नंबर प्लेट पहचान, चालान और ट्रैफिक नियंत्रण।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> NVIDIA GPUs accelerate DL training via CUDA; PyTorch and TensorFlow are leading DL frameworks; UP Police uses Trinetra 2.0 for facial recognition!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> NVIDIA GPU में CUDA तकनीक डीप लर्निंग को गति देती है; PyTorch व TensorFlow मुख्य फ्रेमवर्क हैं; उप्र पुलिस 'त्रिनेत्र 2.0' का प्रयोग करती है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
