# AI Crawler Microservice

A FastAPI-based Crawler for fetching data from links.

## Features

- Fetch LinkedIn job data by URL
- Support for different LinkedIn URL formats
- Detailed job information including title, company, description, and more

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your LinkedIn credentials:
   ```
   LINKEDIN_USERNAME=your_linkedin_email
   LINKEDIN_PASSWORD=your_linkedin_password
   GROQ_API_KEY=your_groq_api_key  # Optional, for LLM extraction
   ```
   Note: A `.env.example` file is provided as a template. Copy it to `.env` and add your credentials.
4. Run the API:
   ```
   uvicorn main:app --reload
   ```

## Security

This project uses environment variables to store sensitive information like credentials and API keys. Make sure to:

1. Never commit your `.env` file to version control
2. The `.gitignore` file is configured to exclude sensitive files like:
   - `.env` and other environment files
   - Debug screenshots and HTML files
   - Logs and temporary files
   - Virtual environment directories

If you're forking or cloning this repository, always check that the `.gitignore` file is properly configured before pushing your changes.

## API Endpoints

### GET /

Root endpoint to check if the API is running.

**Example:**
```
curl http://localhost:8000/
```

**Response:**
```json
{
  "message": "LinkedIn Job API is running"
}
```

### POST /jobs

Endpoint to fetch job data by URL.

**Example:**
```
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/jobs/view/4174810714", "skip_login": true}'
```

**Request Parameters:**
- `url` (required): The LinkedIn job URL
- `skip_login` (optional, default: false): If set to true, the API will attempt to dismiss the login modal instead of logging in

**Response:**
```json
{
  "job": {
    "title": "Senior Full Stack Engineer - Climate Tech - Rust & TypeScript",
    "company": "Climatiq",
    "location": null,
    "description": "About the job...",
    "job_id": "4174810714",
    "url": "https://www.linkedin.com/jobs/view/4174810714",
    "salary_range": "Competitive salary and benefits...",
    "employment_type": null,
    "experience_level": null,
    "posted_date": null
  }
}
```

## Supported URL Formats

The API supports various LinkedIn job URL formats:

1. Direct job URL:
   ```
   https://www.linkedin.com/jobs/view/4174810714
   ```

2. Direct job URL with trailing slash:
   ```
   https://www.linkedin.com/jobs/view/4174810714/
   ```

3. Direct job URL with query parameters:
   ```
   https://www.linkedin.com/jobs/view/4174810714?refId=123
   ```

4. Collection URL with currentJobId:
   ```
   https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4174810714
   ```

5. URL with job title and ID:
   ```
   https://www.linkedin.com/jobs/view/senior-software-engineer-at-company-4174810714
   ```

## Testing

Run the test scripts to verify the API functionality:

```
python test_url_extraction.py  # Test job ID extraction
python test_jobs_endpoint.py  # Test the /jobs endpoint
```

## License

MIT
