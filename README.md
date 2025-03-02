# Market Lens 🔍

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green.svg)
![React](https://img.shields.io/badge/React-18+-blue.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A comprehensive, enterprise-grade marketing analytics and budget allocation toolkit that empowers data-driven marketing decisions through advanced analytics, machine learning, and AI-powered insights.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Module Documentation](#module-documentation)
- [Technologies Used](#technologies-used)
- [Usage Examples](#usage-examples)
- [Environment Setup](#environment-setup)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

**Market Lens** is a full-stack marketing analytics platform that combines data science, machine learning, and AI to provide comprehensive insights into marketing performance. The platform addresses critical marketing challenges including:

- **Marketing Channel Effectiveness Analysis** - Identify which channels drive the most value
- **Budget Optimization** - Optimize budget allocation across marketing channels using advanced algorithms
- **E-commerce Data Processing** - Comprehensive analytics for customer, product, and sales data
- **AI-Powered Reporting** - Automated generation of insightful marketing reports
- **Interactive Dashboards** - Real-time visualization of marketing metrics and KPIs

The platform is designed for marketing teams, data analysts, and business stakeholders who need actionable insights to make informed marketing decisions.

## ✨ Key Features

### 🎨 Interactive Web Dashboard
- **Modern React/TypeScript Interface** - Beautiful, responsive dashboard built with shadcn-ui
- **Real-time Data Visualization** - Interactive charts and graphs using Plotly and Recharts
- **Multi-dataset Support** - Upload and analyze multiple datasets simultaneously
- **Authentication System** - Secure user authentication with Supabase
- **Export Capabilities** - Download reports in multiple formats (PDF, Markdown, JSON)

### 📊 Data Analytics Pipeline
- **Customer Analytics** - Univariate and bivariate analysis of customer behavior patterns
- **Product Performance** - Category analysis, pricing optimization, and product hierarchy visualization
- **Revenue Analysis** - Trend analysis, seasonal decomposition, and forecasting
- **Weather Impact** - Correlation analysis between weather patterns and sales performance
- **Marketing Investment ROI** - Channel effectiveness and investment optimization

### 🤖 AI-Powered Report Generation
- **Multi-Agent System** - Coordinated AI agents for specialized analysis:
  - **Exploration Agent** - General data exploration and statistical analysis
  - **SQL Agent** - Database queries and complex data retrieval
  - **ROI Agent** - Return on investment analysis across channels
  - **Budget Agent** - Budget allocation optimization recommendations
  - **KPI Agent** - Key performance indicator evaluation
  - **Market Analysis Agent** - Competitive analysis and market research
- **Automated Report Generation** - Generate comprehensive reports in Markdown and PDF formats
- **Intelligent Insights** - AI-driven recommendations based on data patterns

### 💰 Budget Allocation Optimization
- **Time Series Modeling** - Temporal budget allocation with month-by-month optimization
- **Bi-level Optimization** - Advanced mathematical optimization for consistent allocation strategies
- **Robyn Framework** - Meta's open-source Marketing Mix Modeling (MMM) implementation
- **Constraint Handling** - Respect budget constraints while maximizing ROI

### 📈 Marketing Channel Analysis
- **Machine Learning Models** - Predictive models for channel effectiveness
- **Model Interpretability** - LIME and SHAP explanations for model predictions
- **Statistical Testing** - Hypothesis testing for marketing investment effectiveness
- **Product-Category Impact** - Analyze relationships between channels and product sales

## 🏗️ Project Architecture

```
Market Lens
│
├── Dashboard/              # React/TypeScript Web Application
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/         # Application pages
│   │   ├── contexts/      # React contexts for state management
│   │   └── integrations/  # External service integrations
│   └── public/            # Static assets and data
│
├── Pipeline/              # Data Analytics Framework
│   ├── Customers_*.py     # Customer analysis modules
│   ├── SKU_EDA.py         # Product analysis
│   ├── master_data.py     # Revenue and master data analysis
│   ├── Weather_*.py       # Weather impact analysis
│   ├── Investment_*.py    # Marketing investment analysis
│   └── Feature.py         # Feature engineering
│
├── Report Generation/     # AI-Powered Reporting System
│   ├── agents/            # Specialized AI agents
│   ├── utils/             # Utility functions
│   └── reports/           # Generated reports output
│
├── Budget Allocation/     # Budget Optimization Tools
│   ├── Budget_Allocation_Time_Series.ipynb
│   ├── Budget_Bioptimisation.ipynb
│   └── Robyn.ipynb        # Marketing Mix Modeling
│
├── Analysis/              # Marketing Channel Analysis
│   ├── marketing_channel.ipynb
│   └── Hypothesis_Testing.py
│
├── Channel Allocation/    # Channel Optimization
│   └── Product_Wise_Channel_Allocation.ipynb
│
└── Sales Allocation/      # Sales Performance Analysis
    └── sales.ipynb
```

## 📁 Directory Structure

### Dashboard
Modern web application for visualizing and interacting with marketing data.

**Key Features:**
- React 18+ with TypeScript
- Tailwind CSS for styling
- shadcn-ui component library
- Supabase for authentication and backend
- Vite for fast development and building

**Getting Started:**
```bash
cd Dashboard
npm install
npm run dev
```

### Pipeline
Comprehensive analytics framework for processing e-commerce and marketing data.

**Modules:**
- `Customers_Univariate_EDA.py` - Single-variable customer analysis
- `Customers_Bivariate_EDA.py` - Multi-variable relationship analysis
- `SKU_EDA.py` - Product and category analysis
- `master_data.py` - Revenue trends and master data analysis
- `Weather_Analysis_EDA.py` - Weather impact on sales
- `Investment_EDA.py` - Marketing investment analysis
- `Feature.py` - Feature engineering and derived metrics
- `main.py` - FastAPI web server for interactive analysis

**Output:**
- Interactive Plotly visualizations
- Static PNG images for reports
- Processed datasets with engineered features

### Report Generation
AI-powered system for automated marketing report generation.

**Agent System:**
- **Supervisor Agent** - Coordinates all analysis agents
- **Exploration Agent** - Data exploration and statistical analysis
- **SQL Agent** - Database queries and data retrieval
- **ROI Agent** - Return on investment calculations
- **Budget Agent** - Budget optimization recommendations
- **KPI Agent** - Key performance indicator analysis
- **Market Analysis Agent** - Competitive and market research
- **Compiler Agent** - Compiles all insights into structured reports

**Output Formats:**
- Markdown reports
- PDF documents
- JSON data exports

### Budget Allocation
Advanced budget optimization using multiple mathematical approaches.

**Approaches:**
1. **Time Series Optimization** - Month-by-month budget allocation
2. **Bi-level Optimization** - Constraint-aware allocation strategies
3. **Robyn MMM** - Meta's Marketing Mix Modeling framework

**Features:**
- Constraint handling (budget limits, channel minimums/maximums)
- Temporal effects consideration
- ROI maximization
- Channel effectiveness weighting

### Analysis
Machine learning-based marketing channel effectiveness analysis.

**Capabilities:**
- Channel effectiveness prediction
- Product-category impact analysis
- Model interpretability (LIME, SHAP)
- Statistical hypothesis testing
- Feature importance analysis

### Channel Allocation
Product-wise channel allocation optimization.

**Features:**
- Product-specific channel recommendations
- Allocation strategy optimization
- Performance-based channel selection

### Sales Allocation
Sales performance analysis and optimization.

**Features:**
- Sales trend analysis
- Performance metrics calculation
- Optimization recommendations

## 🚀 Installation

### Prerequisites

- **Python 3.8+** (for backend and analytics)
- **Node.js 18+** (for Dashboard)
- **Poetry** (recommended) or **pip** (for Python dependencies)
- **Git** (for version control)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Himanshusheo/Market-Lens.git
cd Market-Lens
```

### Step 2: Install Python Dependencies

**Using Poetry (Recommended):**
```bash
poetry install
```

**Using pip:**
```bash
pip install -r requirements.txt
```

### Step 3: Install Dashboard Dependencies

```bash
cd Dashboard
npm install
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the `Report Generation` directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

For Dashboard (if using Supabase), create `.env` in the `Dashboard` directory:

```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

## 🎬 Quick Start

### Running the Analytics Pipeline

```bash
# Navigate to Pipeline directory
cd Pipeline

# Start the FastAPI server
python main.py

# Access the web interface at http://localhost:8000
```

### Running the Dashboard

```bash
# Navigate to Dashboard directory
cd Dashboard

# Start the development server
npm run dev

# Access the dashboard at http://localhost:5173
```

### Generating AI Reports

```bash
# Navigate to Report Generation directory
cd "Report Generation"

# Run the report generator
python main.py

# Reports will be generated in the reports/ directory
```

### Running Budget Optimization

```bash
# Open Jupyter notebooks
jupyter notebook "Budget Allocation/Budget_Allocation_Time_Series.ipynb"
```

## 📚 Module Documentation

### Pipeline Module

The Pipeline module provides comprehensive data analytics capabilities:

**Customer Analysis:**
- Order frequency distribution
- GMV (Gross Merchandise Value) analysis
- Payment method preferences
- Geographic distribution (pincode analysis)
- Customer segmentation (RFM analysis)

**Product Analysis:**
- Category and subcategory performance
- Product hierarchy visualization (sunburst charts)
- Price point analysis
- Top-performing products identification

**Revenue Analysis:**
- Time series trend analysis
- Seasonal decomposition
- Holiday impact measurement
- Discount effectiveness
- Channel performance comparison

**Weather Impact:**
- Temperature correlation with sales
- Precipitation effects
- Extreme weather event impact
- Seasonal weather patterns

### Report Generation Module

The AI-powered reporting system uses a multi-agent architecture:

1. **Question Processing** - Each report section has predefined questions
2. **Agent Assignment** - Questions are routed to relevant specialized agents
3. **Parallel Analysis** - Multiple agents analyze simultaneously
4. **Result Compilation** - Compiler agent integrates all insights
5. **Report Formatting** - Structured markdown and PDF generation

**Report Sections:**
- Executive Summary
- Marketing Performance Analysis
- ROI Analysis
- Budget Recommendations
- KPI Evaluation
- Market Analysis
- Implementation Roadmap

### Budget Allocation Module

Three complementary optimization approaches:

**1. Time Series Approach:**
- Considers temporal effects
- Adapts allocations month-by-month
- Accounts for seasonality
- Handles trend changes

**2. Bi-level Optimization:**
- Finds consistent allocation strategies
- Respects budget constraints
- Optimizes for multiple objectives
- Handles complex constraints

**3. Robyn Framework:**
- Meta's open-source MMM implementation
- Attribution modeling
- Channel effectiveness measurement
- Budget response curves

## 🛠️ Technologies Used

### Backend & Analytics
- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **SciPy** - Scientific computing and statistics
- **Scikit-learn** - Machine learning algorithms
- **FastAPI** - Modern web framework for APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database

### Visualization
- **Matplotlib** - Static plotting
- **Seaborn** - Statistical visualizations
- **Plotly** - Interactive visualizations
- **Kaleido** - Static image export

### AI & Machine Learning
- **LangChain** - LLM application framework
- **LangGraph** - Agent orchestration
- **Groq** - High-performance LLM inference
- **LIME** - Model interpretability
- **SHAP** - Model explanation framework
- **RobynPy** - Marketing Mix Modeling

### Frontend
- **React 18+** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **shadcn-ui** - Component library
- **Recharts** - Chart library for React

### Reporting
- **ReportLab** - PDF generation
- **WeasyPrint** - HTML to PDF conversion
- **Markdown** - Report formatting

### Development Tools
- **Poetry** - Dependency management
- **Git** - Version control
- **Jupyter Notebooks** - Interactive analysis

## 💡 Usage Examples

### Example 1: Customer Analysis

```python
from Pipeline.Customers_Univariate_EDA import AnalyticsOrchestrator

# Initialize orchestrator
orchestrator = AnalyticsOrchestrator("path/to/customer_data.csv")

# Run all analyses
results = orchestrator.run_all_analyses()

# Access specific results
gmv_analysis = results['gmv']
payment_analysis = results['payment']

# Save visualizations
orchestrator.save_plots("./output_directory")
```

### Example 2: Budget Optimization

```python
# Using Jupyter Notebook
# Open Budget_Allocation/Budget_Allocation_Time_Series.ipynb

# The notebook includes:
# - Data loading and preprocessing
# - Time series modeling
# - Budget allocation optimization
# - Visualization of results
```

### Example 3: AI Report Generation

```python
from Report_Generation.agents.report_generator import ReportGenerator

# Initialize generator
generator = ReportGenerator()

# Generate report
report = generator.generate_report(
    data_path="path/to/marketing_data.csv",
    output_format="both"  # 'markdown', 'pdf', or 'both'
)

# Report saved to reports/ directory
```

### Example 4: Channel Analysis

```python
# Using Jupyter Notebook
# Open Analysis/marketing_channel.ipynb

# The notebook includes:
# - Data preprocessing
# - Model training
# - Channel effectiveness analysis
# - LIME/SHAP explanations
# - Statistical testing
```

## ⚙️ Environment Setup

### Python Environment

Create a virtual environment:

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using Poetry
poetry shell
```

### API Keys

1. **Groq API Key** (for AI report generation):
   - Sign up at https://console.groq.com
   - Get your API key
   - Add to `Report Generation/.env`

2. **Supabase** (for Dashboard authentication, optional):
   - Create account at https://supabase.com
   - Create a new project
   - Get URL and anon key
   - Add to `Dashboard/.env`

### Database Setup

The Report Generation module uses SQLite by default. To use a different database:

1. Update `Report Generation/utils/data_manager.py`
2. Configure connection string in environment variables

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Commit your changes** (`git commit -m 'Add amazing feature'`)
5. **Push to the branch** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 for Python code
- Use TypeScript for Dashboard code
- Write docstrings for functions and classes
- Add tests for new features
- Update documentation as needed

### Reporting Issues

If you find a bug or have a feature request:

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Meta Robyn** - For the open-source Marketing Mix Modeling framework
- **LangChain** - For the excellent LLM application framework
- **shadcn-ui** - For the beautiful component library
- **Plotly** - For interactive visualization capabilities

## 📞 Contact & Support

- **GitHub Issues**: [Report issues or request features](https://github.com/Himanshusheo/Market-Lens/issues)
- **Repository**: [https://github.com/Himanshusheo/Market-Lens](https://github.com/Himanshusheo/Market-Lens)

---

**Built with ❤️ for data-driven marketing teams**

*Last updated: March 2025*
