# CreditAI - SME Credit Risk Assessment Platform

AI-powered loan approval prediction system for Indonesian Small & Medium Enterprises using alternative data sources.

## Project Overview

CreditAI addresses the financing challenges faced by Indonesian SMEs by analyzing non-traditional data sources that conventional banks typically overlook. Rather than relying exclusively on credit history, the system evaluates digital footprints, social media presence, and e-commerce activity to enable more inclusive lending decisions.

### Key Results
- **90.5% prediction accuracy** using Random Forest classification
- **Alternative data integration** from Instagram, Tokopedia, and digital payment platforms
- **Real-time processing** with sub-3-second response times
- **Modern web interface** with professional user experience

## Live Demo

[View Live Application](https://db22dca4-bac4-47c3-9878-7376eb6c5c21-00-2mg9c7r46r60p.sisko.replit.dev/)

## Technology Stack

**Backend & Machine Learning:**
- Python 3.9+
- FastAPI for REST API development
- scikit-learn for machine learning implementation
- Pandas and NumPy for data processing

**Frontend:**
- HTML5, CSS3, and Vanilla JavaScript
- Responsive design with advanced CSS animations
- Space Grotesk typography
- Cross-platform compatibility

**Machine Learning Pipeline:**
- Random Forest Classifier
- Custom feature engineering
- Alternative data source analysis
- Comprehensive model validation

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 90.5% |
| Precision | 89.2% |
| Recall | 91.8% |
| F1-Score | 90.5% |

### Feature Importance Analysis
1. **Years in Business** (42.1%) - Primary business stability indicator
2. **Digital Payment Frequency** (14.1%) - Technology adoption measurement
3. **Revenue-to-Loan Ratio** (9.4%) - Repayment capacity assessment
4. **Digital Presence Score** (8.3%) - Market reach evaluation

## Installation and Setup

```bash
# Clone the repository
git clone https://github.com/jjjloren/sme-credit-risk-assessment.git
cd sme-credit-risk-assessment

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

# Generate synthetic training data
python data/generate_data.py

# Train the machine learning model
python models/train_models.py

# Launch the application
python final_app.py
```

## System Features

### Intelligent Risk Assessment
The system analyzes multiple data sources including social media followers, e-commerce ratings, and digital payment transaction patterns. Custom feature engineering creates meaningful metrics such as digital presence scores and revenue ratios for comprehensive business evaluation.

### Professional User Interface
Built with modern web technologies, the interface provides a clean, responsive experience across all devices. Advanced CSS animations and micro-interactions create an engaging user experience while maintaining professional standards.

### Comprehensive Reporting
Each assessment provides detailed risk analysis with clear recommendations, probability scores, and supporting data visualizations. Results are presented in an easily digestible format suitable for financial decision-making.

## Indonesian Market Context

This project specifically targets the Indonesian SME financing landscape, where approximately 64 million small and medium enterprises face challenges accessing traditional credit. The alternative data approach draws inspiration from successful Indonesian fintech companies like Kredivo and Akulaku, which have demonstrated the effectiveness of non-traditional credit scoring methods in emerging markets.

The training data incorporates common Indonesian business types and reflects local digital adoption patterns, making the model relevant to the domestic market context.

## Technical Implementation

The machine learning pipeline processes 12 distinct features through a Random Forest classifier, combining traditional business metrics with modern digital indicators. Feature engineering creates composite scores that capture business digitization and market presence, providing a more holistic view of creditworthiness than traditional approaches.

The web application implements a FastAPI backend with comprehensive input validation and error handling, ensuring robust performance in production environments. The frontend utilizes modern CSS Grid and Flexbox layouts with careful attention to accessibility and cross-browser compatibility.

## Future Development

**Planned Enhancements:**
- PostgreSQL integration for persistent data storage
- Multi-user authentication with role-based access control
- Comprehensive API documentation using OpenAPI/Swagger
- Integration with real Indonesian financial data sources
- Mobile application development using React Native
- Advanced machine learning techniques including ensemble methods

**Scalability Considerations:**
- Database optimization for high-volume transactions
- API rate limiting and caching strategies
- Microservices architecture for enterprise deployment
- Real-time model updating capabilities

## Development and Contribution

The project follows standard Git workflow practices. Contributors should fork the repository, create feature branches, and submit pull requests for review. Code should maintain the existing quality standards and include appropriate testing coverage.

```bash
# Standard contribution workflow
git checkout -b feature/new-enhancement
git commit -m 'Implement new enhancement'
git push origin feature/new-enhancement
# Submit pull request for review
```

## License and Usage

This project is available under the MIT License, permitting both academic and commercial use with appropriate attribution. See the LICENSE file for complete terms and conditions.

## Contact Information

**Jason Loren**  
Email: jasonloren7031@gmail.com  
LinkedIn: [linkedin.com/in/jasonloren](https://linkedin.com/in/jason-loren)  
GitHub: [@jjjloren](https://github.com/jjjloren)

---

**If you find this project useful, please consider starring the repository.**