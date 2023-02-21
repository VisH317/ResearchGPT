### Research GPT

**Idea:** an AI system using OpenAI API to help process primary source research documents to make preliminary research easier for research projects

**Features:**
 * Be able to provide information on a specific research topic given a query
 * Provide information on specific research papers given the link

**Steps in pipeline:**
 * First fetch the text given by the query and find the first top matching research documents
 * Extract the text
 * For research paper summary: run a total summary or a summary on each section of the paper
 * For general topic summary: fetch the documents for the query and run a summary on the abstracts and methods

**Technologies Required:**
 * Selenium - for browser automation searching
 * Frontend: Next.js
 * Selenium worker: go
 * OpenAI API: express or fastapi

**OpenAI API Prompts:**
 * Best way to set up as fetching the link, sending the text to OpenAI (chunking if required or separate sections)
 * When checking for general topic: send text and ask for summary in each (bullet point based)
   * Requires some experimentation with the prompts