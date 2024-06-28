# InvestIQ

InvestIQ is an AI-powered robo-advisor designed to democratize access to high-quality financial advice. Our platform provides personalized investment advice tailored to your unique profile and needs, offering clear and detailed explanations to enhance your financial literacy.

## Getting Started

Follow the instructions below to run the InvestIQ app locally.

### Prerequisites

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Run Streamlit App Locally

1. **Clone the Repository**

```sh
git clone https://github.com/gplourenco/investiq-app.git
cd investiq-app
```

2. **Set OpenAI Key**

Set the `OPENAI_API_KEY` environment variable using:

 ```sh
export OPENAI_API_KEY=sk-***
```

**OR** set in the `.env` file

3. Start the workspace:

```sh
phi ws up
```

Open [localhost:8501](http://localhost:8501) to view the Streamlit App.

4. Stop the workspace using:

```sh
phi ws down
```
