from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time


search_queries = [
    "machine learning algorithms",
    "5G technology advancements",
    "artificial intelligence applications",
    "quantum computing trends",
    "blockchain security",
    "neural networks in healthcare",
    "autonomous vehicles",
    "IoT applications in smart cities",
    "cybersecurity threats",
    "edge computing innovations",
    "deep learning techniques",
    "data mining in big data",
    "computer vision in robotics",
    "wireless sensor networks",
    "cloud computing architecture",
    "natural language processing",
    "fuzzy logic systems",
    "smart grid technologies",
    "bioinformatics algorithms",
    "signal processing methods",
    "image recognition models",
    "reinforcement learning approaches",
    "power electronics and control",
    "renewable energy systems",
    "satellite communication systems",
    "augmented reality applications",
    "virtual reality in education",
    "human-computer interaction",
    "digital signal processing",
    "microprocessor design",
    "VLSI circuit design",
    "cryptography and network security",
    "embedded systems development",
    "RFID technology",
    "antennas and propagation",
    "software-defined networking",
    "quantum cryptography",
    "machine learning for cybersecurity",
    "speech recognition systems",
    "distributed computing frameworks",
    "sensor fusion techniques",
    "wireless communication protocols",
    "optical fiber communication",
    "artificial neural networks",
    "pattern recognition algorithms",
    "semiconductor devices",
    "bio-inspired computing",
    "swarm intelligence",
    "control systems engineering",
    "automated machine learning (AutoML)",
    "time series analysis in AI",
    "convolutional neural networks (CNNs)",
    "graph neural networks (GNNs)",
    "robot motion planning",
    "smart home automation",
    "computer networks and protocols",
    "intelligent transportation systems",
    "mobile edge computing",
    "energy-efficient computing",
    "big data analytics",
    "high-performance computing",
    "quantum machine learning",
    "3D printing innovations",
    "nanotechnology applications",
    "renewable energy optimization",
    "cyber-physical systems",
    "automated testing in software engineering",
    "cloud-native architecture",
    "5G network slicing",
    "Internet of Everything (IoE)",
    "medical image processing",
    "biometric authentication",
    "AI in healthcare diagnosis",
    "smart agriculture technologies",
    "wearable technology innovations",
    "AI in drug discovery",
    "distributed ledger technology",
    "microservices architecture",
    "self-healing networks",
    "brain-computer interface",
    "augmented reality in manufacturing",
    "predictive maintenance using AI",
    "edge AI in IoT devices",
    "digital twins in industry",
    "autonomous drone technology",
    "low-power VLSI design",
    "cyber resilience strategies",
    "hybrid cloud solutions",
    "data privacy in AI",
    "federated learning models",
    "real-time data analytics",
    "semantic web technologies",
    "cognitive radio networks",
    "cloud security best practices",
    "spiking neural networks",
    "zero-trust architecture",
    "blockchain for supply chain",
    "AI ethics and bias",
    "evolutionary algorithms",
    "unmanned aerial vehicles",
    "neuromorphic computing",
    "digital forensics tools"
]

for each in search_queries:
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    url = "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&" + each
    driver.get(url)
    driver.maximize_window()

    time.sleep(5)

    screenshot_path = "CNN/" + each + ".png"
    driver.save_screenshot(screenshot_path)

    # Define the pixel coordinates (x1, y1, x2, y2) for the cropped area
    x1, y1, x2, y2 = 60, 650, 473, 688

    image = Image.open(screenshot_path)
    cropped_image = image.crop((x1, y1, x2, y2))

    cropped_screenshot_path = "CNN/cropped_screenshot.png"
    cropped_image.save(cropped_screenshot_path)

    print(f"Cropped screenshot saved as {cropped_screenshot_path}")

    driver.quit()