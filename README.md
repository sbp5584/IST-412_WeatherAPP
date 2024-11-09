IST-412 WeatherApp 🌦️
This project is an automated weather data application developed as part of IST-412 coursework. It uses the OpenWeatherMap One Call API to fetch real-time weather data for a specified location (Philadelphia by default) and generates a readable weather report. The application also includes continuous integration (CI) and deployment (CD) through Azure DevOps.

Project Overview
The WeatherApp automates the process of:

Fetching weather data from OpenWeatherMap using API calls.
Parsing the data and generating a detailed weather report.
Securing API keys using environment variables.
Running automated tests and code linting through Azure Pipelines.
Deploying the application to Azure App Services for easy access.
Features
Fetches real-time weather data (temperature, humidity, wind speed, etc.).
Supports error handling for API requests and logging of issues.
Continuous integration using Azure DevOps with automated testing and linting.
Secure management of API keys via Azure DevOps secrets.
Deployed as a web service on Azure App Services.
Technologies Used
Python 3.10
OpenWeatherMap One Call API
Azure DevOps (for CI/CD)
Azure App Service (for deployment)
GitHub (for version control)
flake8 (for code linting)
pytest (for testing)
Setup Instructions
Prerequisites
Python 3.10 installed on your machine.
A valid API key from OpenWeatherMap.
Azure DevOps account and GitHub account.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/sbp5584/IST-412_WeatherAPP.git
cd IST-412_WeatherAPP
Create a virtual environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Environment Variables
Create a .env file in the root directory and add your API key:

bash
Copy code
WEATHER_API_KEY=your_api_key_here
Alternatively, set the API key using environment variables:

bash
Copy code
export WEATHER_API_KEY=your_api_key_here
Running the Application
To fetch the weather data and display the report:

bash
Copy code
python main.py
Testing the Application
To run unit tests with pytest:

bash
Copy code
pytest tests/
To check code quality with flake8:

bash
Copy code
flake8 .
CI/CD Pipeline
The project uses Azure DevOps for continuous integration and deployment. The pipeline includes:

Linting: Ensures code quality using flake8.
Testing: Runs unit tests using pytest.
Deployment: Deploys the application to Azure App Service.
Setting Up the Azure Pipeline
Go to your Azure DevOps project and click on Pipelines > New Pipeline.
Choose the GitHub repository and select the azure-pipelines.yml file.
Run the pipeline to build, test, and deploy the application.
Secrets Management
The API key is stored securely as a secret in Azure DevOps:

Go to Project Settings > Pipelines > Library > + Variable Group.
Add a variable named WEATHER_API_KEY and mark it as secret.
Deployment
The application is deployed to Azure App Service. To access the deployed app, use the following URL:

arduino
Copy code
https://your-app-service-name.azurewebsites.net
Troubleshooting
Error 401 (Unauthorized): Verify that the API key is correct and has access to the One Call API.
Pipeline Failures: Check the Azure Pipeline logs for detailed error messages. Common issues include missing dependencies or API key configuration errors.
Deployment Issues: Ensure that the Azure App Service configuration matches the Python version used in the project.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -m 'Add your message here').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or support, please contact: sbp5584@psu.edu

