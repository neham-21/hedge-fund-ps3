### **Hedge Fund Risk Modeling \& Semi-Automated Trading System**

**Team Information**



Team Name:Trinity coders

Year: 2nd Year

All-Female Team: Yes



Architecture Overview:



Our Quant Fund webapp follows a modular full-stack architecture designed for portfolio analytics, risk management, and trading signal generation. The system is divided into three major layers: Data Layer, Backend Layer, and Frontend Layer.



The Data Layer contains historical market datasets for equities, oil, gold, bonds, and macroeconomic indicators. These datasets are preprocessed using Python and Pandas to calculate technical indicators such as SMA, RSI, MACD, Bollinger Bands, volatility, and portfolio returns.



The Backend Layer is built using FastAPI and acts as the core analytics engine. It performs signal generation, backtesting, risk analysis, portfolio optimization, and dynamic asset allocation. The backend exposes REST APIs such as /metrics, /signals, /allocations, and /portfolio-history which provide JSON responses to the frontend. The system also computes advanced financial metrics including Sharpe Ratio, Maximum Drawdown, Volatility, and Win Rate.



The Frontend Layer is developed using HTML, CSS, JavaScript, and Chart.js to create an interactive dashboard. It visualizes portfolio performance, trading signals, and asset allocation through charts and tables. The frontend communicates with the backend APIs in real time, enabling dynamic and scalable financial analytics visualization

